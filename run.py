"""
Implementation of solution to tasks 1-3.

Author:
    Alejandro Domínguez Lugo
    A01378028

Date:
    10/11/2022

"""

#_________________________________Libraries____________________________________
import sys

#______________________________Load solutions__________________________________
sys.path.insert(1, './Task1')
from task1 import Task1

sys.path.insert(2, 'Task2')
from task2 import Task2

sys.path.insert(3, 'Task3')
from task3 import Task3

#____________________________________Main______________________________________
if __name__ == "__main__":
    # Create solver 1
    print("Task 1")
    solver1 = Task1(dataset_path = "./Datasets/task1_dataset.txt")
    # Solve task 1
    print("Solving task 1:")
    solver1.solve()
    print("Task 1 solved")
    
    # Create solver 2 
    print("Task 2")
    solver2 = Task2(epochs = 5, percent_examples_to_train = 1.0, 
                    dataset_path = "./Datasets/DatasetsTask2")
    # Solve task 2
    print("Solving task 2:")
    solver2.solve()
    print("Task 2 solved")
    
    # Create solver 3
    print("Task 3")
    solver3 = Task3(dataset_path = "./Datasets/DatasetsTask3")
    # Solve task 3
    solver3.solve()
    print("Task 3 solved")
    