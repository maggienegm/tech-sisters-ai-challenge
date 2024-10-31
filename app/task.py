class Task:
  def __init__(self, task: str):
    self.description: str = task
    self.subtasks: list = []
    self.completed: bool = False

  def get_num_of_subtasks(self):
    return len(self.subtasks)
  
  def add_subtask(self, subtask: str):
    new_subtask = Task(subtask)
    self.subtasks.append(new_subtask)

  def edit_subtask(self, index: int, new_subtask: str):
    self.subtasks[index].description = new_subtask
  
  def delete_subtask(self, index: int):
    self.subtasks.pop(index)

  def toggle_completed(self):
    self.completed = not self.completed

  def toggle_subtask_completion(self, index: int):
    self.subtasks[index].completed = not self.subtasks[index].completed
