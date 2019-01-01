#!/opt/homebrew/bin/python3
import argparse
import json
from argparse import ArgumentParser
from enum import Enum
from models import Data, TaskStatus
from pprint import pprint
import os
import pickle

class Operation(Enum):
    add = 'add'
    done = 'done'
    remove = 'remove'
    show = 'show'
    sync = 'sync'
    undo = 'undo'
    update = 'update'

    def __str__(self):
        return self.name

# create a parser object 
parser = ArgumentParser(description = "A todo program")
parser.add_argument("operation", help = "Operation", type=Operation, choices=list(Operation))  
parser.add_argument("--desc", help = "Description of the new task")  
parser.add_argument("--id", help = "ID of a task", type=int)  

args = parser.parse_args()

def processAdd():
    description = args.desc.strip('\n')
    if not description:
        print('Please specify description using --desc')
        return
    data.addTask(description)

def processRemove():
    id = args.id
    if not id:
        print('Please specify id to remove using --id')
        return
    data.removeTask(id)

def processUpdate():
    id = args.id
    description = args.desc
    if not id:
        print('Please specify id to remove using --id')
        return
    if not description:
        print('Please specify description using --desc')
        return  
    data.updateTaskDescription(id, description)

def processDone():
    id = args.id
    if not id:
        print('Please specify id to remove using --id')
        return
    data.markTaskDone(id)

def processUndo():
    id = args.id
    if not id:
        print('Please specify id to remove using --id')
        return
    data.markTaskPending(id)

def processShow():
    finished_tasks = [task for task in data.task_list if task.status == TaskStatus.DONE]
    pending_tasks = [task for task in data.task_list if task.status == TaskStatus.PENDING]
    
    print('********************************')
    print('*           PENDING            *')
    print('********************************')

    for task in pending_tasks:
        print('{}.\t {}'.format(task.id, task.description))
    
    print('\n')
    print('********************************')
    print('*             DONE             *')
    print('********************************')
    for task in finished_tasks:
        print('{}.\t {}'.format(task.id, task.description))

def processSync():
    raise NotImplementedError('Operation {} is not yet supported'.format(Operation.sync))

def fetchData(filename):
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
    except FileNotFoundError:
        data = Data()
    return data

def writeData(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

directory = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(directory, 'data.json')
data = fetchData(filename)    

if args.operation == Operation.add:
    processAdd()
elif args.operation == Operation.done:
    processDone()
elif args.operation == Operation.remove:
    processRemove()
elif args.operation == Operation.update:
    processUpdate()
elif args.operation == Operation.undo:
    processUndo()
elif args.operation == Operation.sync:
    processSync()
elif args.operation == Operation.show:
    processShow()
else:
    raise NotImplementedError('Operation {} is not yet supported'.format(args.operation))

writeData(data, filename)
