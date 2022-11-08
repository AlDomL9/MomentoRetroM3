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

#____________________________________Main______________________________________
if __name__ == "__main__":
    # Create solver 1
    solver1 = Task1(datasetPath = "./Datasets/task1_dataset.txt")
    # Solve task 1
    print("Solving task 1:")
    solver1.solve()