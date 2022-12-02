"""

Implementation of solution to task 1.

Classes:
    Task1

Author:
    Alejandro Domínguez Lugo
    A01378028

Date:
    10/11/2022

"""

#_________________________________Libraries____________________________________
from transformers import pipeline
import string

class Task1():
    """
    Class to solve task 1.

    ...

    Attributes
    ----------
    datasetPath : str
        Path to test dataset
    
    sentiment_pipeline = pipeline
        Model

    Methods
    -------
    solve(verbose = False):
        Generates inference for each line in the test dataset
        
    """
    
    def __init__(self, dataset_path = "../Datasets/task1_dataset.txt"):
        """
        Construct attributes for the class.

        Parameters
        ----------
            datasetPath : str, optional
                Path to test dataset
            
        """
        self.datasetPath = dataset_path
        
        # Load model from hugging face
        self.sentiment_pipeline = pipeline(model = "distilbert-base-uncased-finetuned-sst-2-english")
    
    def __extract_lines(self, verbose = False):
        """
        Extract lines from the given file.

        Parameters
        ----------
        verbose : bool, optional
            More info to be displayed (default is False)

        Returns
        -------
        lines : list
            List of lines from the file
        
        """
        # Open file
        with open(self.datasetPath, 'r') as file: 
            lines = file.readlines()
            if verbose:
                  print("Lines extracted from: '", self.datasetPath, "'")
            return lines
        
        if verbose: print("Lines extracted from: '", self.datasetPath, "'")
        
        return lines

    def __infer(self, lines,  verbose = False):
        """
        Make inferences for each line.

        Parameters
        ----------
        lines: list
            List of lines to be analyzed
        
        verbose : bool, optional
            More info to be displayed (default is False)

        Returns
        -------
        inferences : list
            Predictions for each line
        
        """
        inferences = []
        
        # For each line predict and extract label
        for line in lines: 
            data = line.translate(str.maketrans('', '', string.punctuation))
            inference = self.sentiment_pipeline(data)
            inferences.append(inference[0]["label"])
        
        if verbose: print("Number of inferences made:", str(len(inferences)))
        
        return inferences
    
    def solve(self, verbose = False):
        """
        Make and show predictions for each line in the given text.

        Parameters
        ----------
        verbose : bool, optional
            More info to be displayed (default is False)

        Returns
        -------
        inferences : list
            Predictions for each line
        
        """
        # Extract lines from text
        if verbose: print("Extracting lines")
        lines = self.__extract_lines(verbose = verbose)
        
        # Make inferences
        if verbose: print("Making inferences")
        inferences = self.__infer(lines = lines, verbose = verbose)
        
        # Show results
        if verbose: print("Results:")
        for inference in inferences:
            print(inference)
            
        return inferences
    
    def test(self, verbose = True):
        """
        Test implementation with a controlled dataset.

        Parameters
        ----------
        verbose : bool, optional
            More info to be displayed (default is True)

        Returns
        -------
        None
        
        """
        # Expected results
        expected = ["POSITIVE", "NEGATIVE", "NEGATIVE", "POSITIVE", "POSITIVE"]
        
        # Save task 1 dataset path load test path
        aux = self.datasetPath
        self.datasetPath = "../Tests/test_task1.txt"
        if verbose: print("Testing text in: ", self.datasetPath)
        
        # Solve
        solutions = self.solve(verbose = verbose)
        
        # Check results
        if solutions == expected:
            print("Test passed")
        
        else:
            print("Test not passed")
            print("Got: ")
            print(solutions)
            print("Expected: ")
            print(expected)
            
        self.datasetPath = aux
        
        
        
if __name__ == "__main__":
    # Create solver
    solver1 = Task1()
    # Show results
    solver1.test(verbose = True)
    


