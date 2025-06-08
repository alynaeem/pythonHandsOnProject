from Task import Task


class TaskManager:

    def __init__(self):
        self.tasks = []

    def addTask(self, title):
        task = Task(title)
        self.tasks.append(task)

    def viewTasks(self):
        if not self.tasks:
            print("No tasks found")
        for i, task in enumerate(self.tasks):
            status = "✅" if task.done else "❌"
            print(f"{i}. {task.title}: {status}")
    def markTaskDone(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].markDone()
            print(f"Task {index} done")
        else:
            print(f"Task {index} not found")

    def deleteTask(self, index):
        if 0 <= index < len(self.tasks):
            deletedTask = self.tasks.pop(index)
            print(f"Task {index} deleted")
        else:
            print(f"Task {index} not found")

