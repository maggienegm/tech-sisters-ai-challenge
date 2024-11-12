import streamlit as st
import ui_components as ui
from task_manager import TaskManager

if "task_manager" not in st.session_state:
   st.session_state.task_manager = TaskManager()

task_manager = st.session_state.task_manager

if "edit_task_index" not in st.session_state:
    st.session_state["edit_task_index"] = -1

if "edit_subtask_index" not in st.session_state:
    st.session_state["edit_subtask_index"] = -1

# Initialize the session state for storing messages in ai_chat module
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🌱 Tiny Tasks")
st.subheader("_Turn Big Tasks into Tiny Tasks with the Power of Generative AI_")

ui.task_input(task_manager)

st.header("To-do List")

if task_manager.tasks:
  for i, task in enumerate(task_manager.tasks):
    ui.task_component(task_manager, i, task)
    for j, subtask in enumerate(task.subtasks):
       ui.subtask_component(task_manager, i, j, subtask)

if st.session_state["edit_task_index"] != -1 and st.session_state["edit_subtask_index"] == -1:
   index = st.session_state["edit_task_index"]
   task_to_edit = task_manager.tasks[index]
   ui.edit_task_component(task_manager, index, task_to_edit)

if st.session_state["edit_subtask_index"] != -1 and st.session_state["edit_task_index"] != -1:
   task_index = st.session_state["edit_task_index"]
   subtask_index = st.session_state["edit_subtask_index"]
   subtask_to_edit = task_manager.tasks[task_index].subtasks[subtask_index]
   ui.edit_subtask_component(task_manager, task_index, subtask_index, subtask_to_edit)

if not task_manager.tasks:
    st.info("No tasks in your to-do list!")