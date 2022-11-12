"""

Implementation of solution to task 3.

Classes:
    Task3

Author:
    Alejandro Domínguez Lugo
    A01378028

Date:
    10/11/2022

"""
#_________________________________Libraries____________________________________
from translate import Translator
from googletrans import Translator as googTrans
from nltk.translate.bleu_score import corpus_bleu
import os

#__________________________________Classes_____________________________________
class Task3():
    """
    Class to solve task 3.

    ...

    Attributes
    ----------
    datasetPath : str
        Path to dataset and reference
    
    corpus : lst
        List of strings that compose the corpus
        
    reference : lst
        List of strings that compose the reference
        
    myMemory : Translator
        Translator with My Memory as source
        
    google : Translator
        Translator with Google Translate as source

    Methods
    -------
    solve(verbose = False):
        Loads corpus, translates it with both translators, prepares 
        translations for a bleu test, runs the test and shows the result.
        
    test(verbose = True):
        Loads small sample corpus, makes translations and runs bleu test.
        
    """
    
    def __init__(self, dataset_path = "../Datasets/DatasetsTask3"):
        """
        Construct attributes for the class.

        Parameters
        ----------
            datasetPath : str, optional
                 Path to dataset and reference.
        
        Returns
        -------
            None
        """
        self.datasetPath = dataset_path
        self.corpus = None
        self.reference = None
        self.myMemory = Translator(to_lang = "en", from_lang = "es")
        self.google = googTrans()
        
        
    def __create_corpus(self, file_name, verbose = False):
        """
        Create corpus.

        Parameters
        ----------
        file_name : str
            Name of corpus file
            
        verbose : bool, optional
            More info to be displayed (default is False)

        Returns
        -------
        corpus : lst
            List of strings that compose the corpus
        
        """
        # Build path
        filePath = os.path.join(self.datasetPath, file_name)
        
        # Open file and build corpus
        file = open(filePath, 'r')
        corpus = file.readlines()
        for i in range(len(corpus)):
            corpus[i] = corpus[i].replace("\n", "")
        file.close()
        
        if verbose:
            print("Corpus built from file:", filePath, "with", 
                  str(len(corpus)), "lines.")
        
        return corpus
        
    def __create_reference(self, file_name, verbose = False):
        """
        Create reference.

        Parameters
        ----------
        file_name : str
            Name of reference file
            
        verbose : bool, optional
            More info to be displayed (default is False)

        Returns
        -------
        reference : lst
            List of strings that compose reference.
        
        """
        # Build path
        filePath = os.path.join(self.datasetPath, file_name)
        
        # Open file and build reference
        file = open(filePath, 'r')
        reference = file.readlines()
        for i in range(len(reference)):
            reference[i] = reference[i].replace("\n", "")
        file.close()
        
        if verbose:
            print("Reference built from file:", filePath, "with", 
                  str(len(reference)), "lines.")
            
        return reference
        
    def __translate_corpus(self, corpus, translator, google = False, 
                           verbose = False):
        """
        Make translation for a given corpus with a given translator.
        
        Parameters
        ----------
        corpus : lst
            List of strings that compose the corpus.
            
        translator : Translator
            Translator object to be used for translation.
            
        google : bool, optional
            Identifier for google translator since it works different. 
            (default = False)
            
        verbose : bool, optional
            More info to be displayed (default is False)

        Returns
        -------
        translation : lst
            List of strings that compose the translation.
        
        """
        # For each line in corpus translate and add to translation
        translation = []
        for line in corpus:
            if google:
                translation.append(translator.translate(line).text)
            else:
                translation.append(translator.translate(line))
                
        if verbose:
            print("Translated", str(len(corpus)), 
                  "lines from spanish to english")
            
        return translation

    def __prepare_translation_for_bleu(self, translation, verbose = False):
        """
        Transform translation to bleu test format.

        Parameters
        ----------
        translation : lst
            List of strings that compose the translation
            
        verbose : bool, optional
            More info to be displayed (default is False)

        Returns
        -------
        bleuReady = lst
            List of lists of words that compose the reference.
            Format:
                [["Some", "translated", "sentence"], ["Another", "sentence"]]
        
        """
        # For each line in translation split and add to list
        bleuReady = []
        for line in translation:    
            bleuReady.append(line.split())
            
        if verbose:
            print("Prepared translation for bleu test splitting into", 
                  str(len(bleuReady)), "parts")
            
        return bleuReady
    
    def __prepare_reference_for_bleu(self, reference, verbose = False):
        """
        Transform reference to bleu test format.

        Parameters
        ----------
        reference : lst
            List of strings that compose the reference
            
        verbose : bool, optional
            More info to be displayed (default is False)

        Returns
        -------
        bleuReady = lst
            List of lists of lists of words that compose the reference.
            Format:
                [[["Some", "reference", "sentence"]], 
                 [["Another", "sentence"]]]
        
        """
        # For each line split and add to list inside another list
        bleuReady = []
        for line in reference:    
            bleuReady.append([line.split()])
            
        if verbose:
            print("Prepared reference for bleu test splitting into", 
                  str(len(bleuReady)), "parts")
            
        return bleuReady
    
    def __run_bleu_test(self, ref, hyp, verbose = False):
        """
        Run bleu test.

        Parameters
        ----------
        ref : lst
            List of lists of lists of words that compose the reference
        
        hyp : lst
            List of lists of words that compose the hypothesis
            
        verbose : bool, optional
            More info to be displayed (default is False)

        Returns
        -------
        bleu_score : float
            Result of bleu score.
        
        """
        if verbose:
            print("Running BLEU test")
        
        # Run test
        return corpus_bleu(ref, hyp)
        
    def __show_results(self, scores, translators_names):
        """
        Show bleu test results.

        Parameters
        ----------
        scores : touple
            Bleu scores of each translation
        
        translators_names : touple
            Names of each translator

        Returns
        -------
        None
        
        """
        # For each translator show results
        for i in range(len(scores)):
            print(translators_names[i], "score:", str(scores[i]))
    
    def solve(self, verbose = False):
        """
        Solve task 3.

        Parameters
        ----------
        verbose : bool, optional
            More info to be displayed (default is False)

        Returns
        -------
        None
        
        """
        # Build corpus
        corpus = self.__create_corpus(file_name = "es.txt", verbose = verbose)
        
        # Build reference
        reference = self.__create_reference(file_name = "en.txt", 
                                            verbose = verbose)
        
        # Make translations
        myMindTranslation = self.__translate_corpus(corpus = corpus, 
                                                    translator = self.myMemory,
                                                    verbose = verbose)
        googleTranslation = self.__translate_corpus(corpus = corpus, 
                                                    translator = self.google, 
                                                    google = True,  
                                                    verbose = verbose)
        
        # Transform to bleu test format
        myMindBleuReady = self.__prepare_translation_for_bleu(translation = myMindTranslation, 
                                                              verbose = verbose)
        googleBleuReady = self.__prepare_translation_for_bleu(translation = googleTranslation, 
                                                              verbose = verbose)
        referenceBleuReady = self.__prepare_reference_for_bleu(reference = reference, 
                                                               verbose = verbose)
        
        # Calculate scores
        myMindScore = self.__run_bleu_test(ref = referenceBleuReady, 
                                           hyp = myMindBleuReady, 
                                           verbose = verbose)
        googleScore = self.__run_bleu_test(ref = referenceBleuReady, 
                                           hyp = googleBleuReady, 
                                           verbose = verbose)
        
        # Show scores
        self.__show_results(scores = (myMindScore, googleScore), 
                            translators_names = ("My Mind", 
                                                 "Google Translate"))
        
    def test(self, verbose = True):
        """
        Test class.

        Parameters
        ----------
        verbose : bool, optional
            More info to be displayed (default is True)

        Returns
        -------
        None
        
        """
        # Save original path ans prepare test path
        aux = self.datasetPath
        self.datasetPath = "../Tests"
        
        # Build corpus
        corpus = self.__create_corpus(file_name = "test_task3.txt", 
                                      verbose = verbose)
        
        # Build reference
        reference = self.__create_reference(file_name = "reference_task3.txt", 
                                            verbose = verbose)
        
        # Make translations
        myMindTranslation = self.__translate_corpus(corpus = corpus, 
                                                    translator = self.myMemory,
                                                    verbose = verbose)
        googleTranslation = self.__translate_corpus(corpus = corpus, 
                                                    translator = self.google, 
                                                    google = True,  
                                                    verbose = verbose)
        
        # Transform to bleu test format
        myMindBleuReady = self.__prepare_translation_for_bleu(translation = myMindTranslation, 
                                                              verbose = verbose)
        googleBleuReady = self.__prepare_translation_for_bleu(translation = googleTranslation, 
                                                              verbose = verbose)
        referenceBleuReady = self.__prepare_reference_for_bleu(reference = reference, 
                                                               verbose = verbose)
        
        # Calculate scores
        myMindScore = self.__run_bleu_test(ref = referenceBleuReady, 
                                           hyp = myMindBleuReady, 
                                           verbose = verbose)
        googleScore = self.__run_bleu_test(ref = referenceBleuReady, 
                                           hyp = googleBleuReady, 
                                           verbose = verbose)
        
        # Show scores
        self.__show_results(scores = (myMindScore, googleScore), 
                            translators_names = ("My Mind", 
                                                 "Google Translate"))
        
        # Prepare dataset path
        self.datasetPath = aux

if __name__ == "__main__":
    # Build solver
    solver3 = Task3()
    
    # Run test
    solver3.test()