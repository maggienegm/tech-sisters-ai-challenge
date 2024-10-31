from task import Task

class TaskManager:
  def __init__(self):
    self.tasks: list = []

  def add_task(self, task: str):
    if task in (t.description for t in self.tasks):
      return "Task already exists. Try adding a new task!"
    new_task = Task(task)
    self.tasks.append(new_task)

  def add_subtasks_to_task(self, task_index: int, subtasks: list):
    for subtask in subtasks:
      if subtask not in (st.description for st in self.tasks[task_index].subtasks):
        self.tasks[task_index].add_subtask(subtask)

  def edit_task(self, task_index: int, new_task: str):
    if new_task in (t.description for t in self.tasks):
      return "This task already exists. Try entering another task description!"
    if 0 <= task_index < len(self.tasks):
      task = self.tasks[task_index]
      task.description = new_task

  def edit_subtask(self, task_index: int, subtask_index: int, new_subtask: str):
    if 0 <= task_index < len(self.tasks) and 0 <= subtask_index < self.tasks[task_index].get_num_of_subtasks():
      self.tasks[task_index].edit_subtask(subtask_index, new_subtask)

  def delete_task(self, task_index: int):
    if 0 <= task_index < len(self.tasks):
      self.tasks.pop(task_index)

  def delete_subtask(self, task_index: int, subtask_index: int):
    if 0 <= task_index < len(self.tasks) and 0 <= subtask_index < self.tasks[task_index].get_num_of_subtasks():
      self.tasks[task_index].delete_subtask(subtask_index)

  def get_task_index(self, task_description: str):
    for i, task in enumerate(self.tasks):
      if task_description == task.description:
        return i
    return -1

  def toggle_subtask_completion(self, task_index: int, subtask_index: int):
    if 0 <= task_index < len(self.tasks) and 0 <= subtask_index < self.tasks[task_index].get_num_of_subtasks():
      self.tasks[task_index].toggle_subtask_completion(subtask_index)