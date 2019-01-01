from enum import Enum

class TaskStatus(Enum):
    PENDING = 'PENDING'
    DONE = 'DONE'

class Task(object):

    def __init__(self, id, description, status):
        self.id = id
        self.description = description
        self.status = status

class Data(object):
    
    def __init__(self):
        self.task_list = []

    def addTask(self, description):
        ret = 0
        for task in self.task_list:
            ret = max(ret, task.id)
        self.task_list.append(Task(ret + 1, description, TaskStatus.PENDING))
        
    def markTaskDone(self, id):
        for task in self.task_list:
            if task.id == id:
                task.status = TaskStatus.DONE
                break

    def markTaskPending(self, id):
        for task in self.task_list:
            if task.id == id:
                task.status = TaskStatus.PENDING
                break

    def removeTask(self, id):
        self.task_list = [task for task in self.task_list if task.id != id]

    def updateTaskDescription(self, id, description):
        for task in self.task_list:
            if task.id == id:
                task.description = description
                break
