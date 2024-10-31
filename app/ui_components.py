import streamlit as st
from ai_chat import generate_subtasks

def task_input(task_manager):
  new_task = st.text_input("Add a new task!")

  if st.button("Add Task"):
    if new_task.strip():
      error = task_manager.add_task(new_task)
      if (error):
        st.error(error)
      else:
        subtasks = generate_subtasks(new_task)
        # subtasks = ["asdfasdfasdfa", "werwerwerwer", "43534534543"]
        index = task_manager.get_task_index(new_task)
        task_manager.add_subtasks_to_task(index, subtasks)
        st.rerun()
    else:
      st.error("Task cannot be empty!")

def task_component(task_manager, task_index, task):
  cols = st.columns([0.2, 4, 1, 1])

  if f"task_completed_{task_index}" not in st.session_state:
    st.session_state[f"task_completed_{task_index}"] = task.completed
  
  label = f"~~{task.description}~~" if task.completed else task.description

  is_completed = cols[0].checkbox(label, value=task.completed, key=f"checkbox_task_{task_index}", label_visibility="collapsed")

  cols[1].markdown(label)

  if is_completed != task.completed:
    task.toggle_completed()
    st.rerun()

  if cols[2].button("Edit", key=f"edit_task_{task_index}"):
    st.session_state["edit_task_index"] = task_index

  if cols[3].button("Delete", key=f"delete_task_{task_index}"):
    task_manager.delete_task(task_index)
    st.session_state["edit_task_index"] = -1
    st.session_state["edit_subtask_index"] = -1
    st.rerun()

def subtask_component(task_manager, task_index, subtask_index, subtask):
  cols = st.columns([0.25, 0.2, 3.75, 1, 1])

  if f"subtask_completed_{subtask_index}" not in st.session_state:
    st.session_state[f"subtask_completed_{subtask_index}"] = subtask.completed
  
  label = f"~~{subtask.description}~~" if subtask.completed else subtask.description

  is_completed = cols[1].checkbox(label, value=subtask.completed, key=f"checkbox_task_{task_index}_subtask_{subtask_index}", label_visibility="collapsed")

  cols[2].markdown(label)

  if is_completed != subtask.completed:
    subtask.toggle_completed()
    st.rerun()

  if cols[3].button("Edit", key=f"edit_task_{task_index}_subtask_{subtask_index}"):
    st.session_state["edit_task_index"] = task_index
    st.session_state["edit_subtask_index"] = subtask_index

  if cols[4].button("Delete", key=f"delete_task_{task_index}_subtask_{subtask_index}"):
    task_manager.delete_subtask(task_index, subtask_index)
    st.session_state["edit_task_index"] = -1
    st.session_state["edit_subtask_index"] = -1
    st.rerun()

def edit_task_component(task_manager, task_index, task):
  new_task_input = st.text_input(f"Edit task {task.description}", value=task.description, key=f"edit_task_{task_index}_input")

  if st.button("Save Changes", key=f"save_changes_task_{task_index}"):
    error = task_manager.edit_task(task_index, new_task_input)
    if (error):
      st.error(error)
    else:
      st.session_state["edit_task_index"] = -1
      st.session_state["edit_subtask_index"] = -1
      st.rerun()

def edit_subtask_component(task_manager, task_index, subtask_index, subtask):
  new_subtask_input = st.text_input(f"Edit subtask {subtask.description}", value=subtask.description, key=f"edit_task_{task_index}_subtask_{subtask_index}_input")

  if st.button("Save Changes", key=f"save_changes_subtask_{subtask_index}"):
    task_manager.edit_subtask(task_index, subtask_index, new_subtask_input)
    st.session_state["edit_task_index"] = -1
    st.session_state["edit_subtask_index"] = -1
    st.rerun()