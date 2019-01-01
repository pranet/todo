# python3 -m unittest discover .
import unittest
from models import Data, TaskStatus
class DataTest(unittest.TestCase):
    
    def setUp(self):
        self.data = Data()

    def test_add_tasks(self):
       self.data.addTask('test')
       self.assertEqual(self.data.task_list[0].id, 1)
       self.assertEqual(self.data.task_list[0].description, 'test')
       self.assertEqual(self.data.task_list[0].status, TaskStatus.PENDING)

    def test_add_multiple_tasks(self):
        for i in range(1, 10):
            self.data.addTask(str(i))
        for i in range(1, 10):
            self.assertEqual(self.data.task_list[i - 1].id, i)
            self.assertEqual(self.data.task_list[i - 1].description, str(i))
            self.assertEqual(self.data.task_list[i - 1].status, TaskStatus.PENDING)

    def test_mark_test_done(self):
        for i in range(1, 10):
            self.data.addTask(str(i))
        self.data.markTaskDone(2)
        for i in range(1, 10):
            self.assertEqual(self.data.task_list[i - 1].id, i)
            self.assertEqual(self.data.task_list[i - 1].description, str(i))
            self.assertEqual(self.data.task_list[i - 1].status, TaskStatus.DONE if i == 2 else TaskStatus.PENDING)

    def test_mark_test_undone(self):
        for i in range(1, 3):
            self.data.addTask(str(i))
        self.data.markTaskDone(1)
        self.data.markTaskDone(2)
        for i in range(1, 3):
            self.assertEqual(self.data.task_list[i - 1].id, i)
            self.assertEqual(self.data.task_list[i - 1].description, str(i))
            self.assertEqual(self.data.task_list[i - 1].status, TaskStatus.DONE)

        self.data.markTaskPending(2)
        for i in range(1, 3):
            self.assertEqual(self.data.task_list[i - 1].id, i)
            self.assertEqual(self.data.task_list[i - 1].description, str(i))
            self.assertEqual(self.data.task_list[i - 1].status, TaskStatus.PENDING if i != 1 else TaskStatus.DONE)

    def test_remove_task(self):
        for i in range(1, 10):
            self.data.addTask(str(i))
        self.data.removeTask(5)
        
        self.assertEqual(len(self.data.task_list), 8)
        for i in range(1, 9):
            if i < 5:
                self.assertEqual(self.data.task_list[i - 1].id, i)
                self.assertEqual(self.data.task_list[i - 1].description, str(i))
                self.assertEqual(self.data.task_list[i - 1].status, TaskStatus.PENDING)
            if i >= 5:
                pass
                self.assertEqual(self.data.task_list[i - 1].id, i + 1)
                self.assertEqual(self.data.task_list[i - 1].description, str(i + 1))
                self.assertEqual(self.data.task_list[i - 1].status, TaskStatus.PENDING)

    def test_update_description(self):
        for i in range(1, 10):
            self.data.addTask(str(i))
        self.data.updateTaskDescription(5, 'updated')        
        for i in range(1, 10):
            self.assertEqual(self.data.task_list[i - 1].id, i)
            self.assertEqual(self.data.task_list[i - 1].description, 'updated' if i == 5 else str(i))
            self.assertEqual(self.data.task_list[i - 1].status, TaskStatus.PENDING)
            
