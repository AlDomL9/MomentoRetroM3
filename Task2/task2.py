"""

Implementation of solution to task 2.

Classes:
    Task2

Author:
    Alejandro Domínguez Lugo
    A01378028

Date:
    10/11/2022

"""

#_______________________________Load trainer___________________________________
from trainer import Trainer

#__________________________________Classes_____________________________________
class Task2 ():
    """
    Class to solve task 2.

    ...

    Attributes
    ----------
    datFolder : str
        Path to datasets

    Methods
    -------
    solve(verbose = False):
        Trains ner model and shows results for training
    
    test():
        Trains a ner model with reduced corpus and with less epochs and shows
        results for training.
        
    """
    
    def __init__(self, epochs = 5, percent_examples_to_train = 1.0, 
                 dataset_path = "../Datasets/DatasetsTask2"):
        """
        Construct attributes for the class.

        Parameters
        ----------
            epochs : int, optional
                Epochs to train. (default : 5)
                
            percent_examples_to_train: float optional
                Percet of corpus to use in training. (default : 1.0. Values 
                                                      from 0.01 -> 1.0)
                
            data_folder : str, optional
                Path to data folder
        
        Returns
        -------
            None
        """
        self.dataFolder = dataset_path
        self.trainer = Trainer(epochs = epochs, 
                               percent_examples_to_train = percent_examples_to_train, 
                               data_folder = self.dataFolder)
    
    def solve(self, verbose = False):
        """
        Train model and show results.

        Parameters
        ----------
        verbose : bool, optional
            More info to be displayed (default is False)

        Returns
        -------
            None
        
        """
        # Train
        self.trainer.train()
        
        if verbose:
            print("Model trained")
            print("Showing results")
            
        # Show results
        self.trainer.plot_results()
        
    def test(self):
        """
        Test implementation with a reduced corpus to 10% and training only 2 epochs of model.

        Parameters
        ----------
            None

        Returns
        -------
            None
        
        """
        # Create test Trainer
        testTrainer = Trainer(epochs = 2, 
                              percent_examples_to_train = 0.1, 
                              data_folder = self.dataFolder)
        # Train
        testTrainer.train()
        # Show results
        testTrainer.plot_results()
        
#____________________________________Main______________________________________
if __name__ == "__main__":
    # Create solver
    solver2 = Task2()
    # Run test
    solver2.test()