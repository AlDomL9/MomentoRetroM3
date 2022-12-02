"""

Implementation of model trainer.

Classes:
    Trainer

Author:
    Alejandro Domínguez Lugo
    A01378028

Date:
    10/11/2022

"""
#_________________________________Libraries____________________________________
from flair.data import Corpus
from flair.embeddings import WordEmbeddings, StackedEmbeddings, FlairEmbeddings
from flair.datasets import ColumnCorpus
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer
from flair.visual.training_curves import Plotter

#__________________________________Classes_____________________________________
class Trainer:
    """
    Class to train a ner model.

    ...

    Attributes
    ----------
    epochs : int, optional
        Epochs to train (default is 10)
    
    corpus : Corpus
        Corpus including train, test and dev datasets
        
    tagger : SequenceTagger
        Sequence tagger
        

    Methods
    -------
    train(verbose = False):
        Trains the ner model
    
    plot_results()
        Plots training loss
        
    """
    
    def __init__(self, epochs = 5, percent_examples_to_train = 1.0, data_folder =  "../Datasets/DatasetsTask2"):
        """
        Construct attributes for the class.

        Parameters
        ----------
            epochs : int, optional
                Epochs to train model. (default : 5)
                
            percent_examples_to_train : float, optional
                Percent of corpus to use for training. (default : 1.0. Value 
                                                         from 0.01 -> 1.0)
                
            data_folder : str, optional
                Path to datasets
        
        Returns
        -------
            None
        """
        self.epochs = epochs
        
        # Prepare tag type as ner
        tagType = "ner"
        
        # Columns in dataset
        columns = {0: "text", 1: tagType}
        
        # Generate embeddings
        embedding_types = [WordEmbeddings('glove'),
                           FlairEmbeddings('news-forward-fast'),
                           FlairEmbeddings('news-backward-fast')]
        embeddings = StackedEmbeddings(embeddings=embedding_types)
        
        # Create corpus
        self.corpus: Corpus = ColumnCorpus(data_folder = data_folder, 
                                           column_format = columns,
                                           train_file='train',
                                           test_file='test',
                                           dev_file='dev')
        
        # Reduce corpus 
        self.corpus.downsample(percent_examples_to_train)
        
        # Generate tag dictionary
        tagDictionary = self.corpus.make_label_dictionary(label_type=tagType)
        
        # Create tagger
        self.tagger = SequenceTagger(hidden_size=5,
                                     embeddings=embeddings,
                                     tag_dictionary=tagDictionary,
                                     tag_type=tagType)
        
    def train(self):
        """
        Train the ner model.

        Parameters
        ----------
            None
            
        Returns
        -------
            None
        """
        # Create trainer
        trainer = ModelTrainer(self.tagger, self.corpus)

        # Train
        trainer.train('resources/taggers/ner-english',
                      train_with_dev=False,
                      max_epochs = self.epochs)
        
    def plot_results(self):
        """
        Plot training results.

        Parameters
        ----------
            None

        Returns
        -------
            None            
        """
        # Plot
        plotter = Plotter()
        plotter.plot_training_curves('./resources/taggers/ner-english/loss.tsv')
        
#____________________________________Main______________________________________
if __name__ == "__main__":
    # Create trainer
    trainer = Trainer(epochs = 2, percent_examples_to_train=0.1)
    # Train
    trainer.train()
    # Show results
    trainer.plot_results()
    
    
#__________________________________Citation____________________________________
"""
@inproceedings{akbik2018coling,
  title={Contextual String Embeddings for Sequence Labeling},
  author={Akbik, Alan and Blythe, Duncan and Vollgraf, Roland},
  booktitle = {{COLING} 2018, 27th International Conference on Computational Linguistics},
  pages     = {1638--1649},
  year      = {2018}
}
"""