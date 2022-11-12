# Momento_de_Retroalimentacion_Modulo_3_NLP
## Task 1
Implemented using model: distilbert-base-uncased-finetuned-sst-2-english

Created by: Hugging Face

Dataset saved in path: /Datasets/task1_dataset.txt

Tets dataset saved in path: /Tests/test_task1.txt

The test was prepared with five lines expressing positive and negative emotions.

## Task 2
Implemented using model: flair/ner-english-fast

Created by: Flair

Dataset folder in path: /Datasets/DatasetsTask2

The test was run with 2 epochs in training and 10% of the original corpus 

Results with 5 epochs and full corpus:

https://drive.google.com/file/d/1m_98pYCGuWnGKUe6pezcxyOS5C26bZhe/view?usp=share_link

Citation required by model developer:

@inproceedings{akbik2018coling,

  title={Contextual String Embeddings for Sequence Labeling},

  author={Akbik, Alan and Blythe, Duncan and Vollgraf, Roland},

  booktitle = {{COLING} 2018, 27th International Conference on Computational Linguistics},

  pages     = {1638--1649},

  year      = {2018}

}

## Task 3
Implemented using translators: py-translate and Google Translate API (No APi Keys requiered, although use is limited. However the solver should run just fine for two or three runs)

Datasets saved in path: /Datasets/DatasetsTask3

Test datasets saved in path: /Tests

The test was prepared using a three-lines text and its translated reference.