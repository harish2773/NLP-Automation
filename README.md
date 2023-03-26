# NLP Automation
Natural Language Processing (NLP) is the ability of a machine to read, write, understand and derive meaning from a human language.
Steps in pre-processing of data in NLP 
* Tokenization
* Stemming
* Lemmatization
* Part-of-speech (POS) tagging
* Named entity recognition
* Chunking

All these parts are done in pre processing of the data using nlp. We will either use NLTK or Spacy libraries in NLP to achieve the pre processing of data.

Natural language Toolkit (NLTK): NLTK is a complete toolkit for all NLP techniques.

SpaCy: SpaCy is an open-source NLP library which is used for Data Extraction, Data Analysis, Sentiment Analysis, and Text Summarization

## Text Preprocessing
### Converting to lowercase

Lower casing: Converting a word to lower case (NLP -> nlp). Words like Book and book mean the same but when not converted to the lower case those two are represented as two different words in the vector space model (resulting in more dimensions).

### Removal of Punctuations

We need to carefully choose the list of punctuation which we are going to discard based on the use case. For example, Python’s string module contains the following list of punctuation.

### Removal of stopwords

Stop word removal is one of the most commonly used preprocessing steps across different NLP applications. The idea is simply removing the words that occur commonly across all the documents in the corpus. 

### Removal of frequent words

### Removal of Rare words

### Removal of Special Characters

### Stemming

Stemming is the process of reducing a word to its stem that affixes to suffixes and prefixes or to the roots of words known as "lemmas".

### Lemmatization

Lemmatization is a text normalization technique used in Natural Language Processing (NLP), that switches any kind of a word to its base root mode. Lemmatization is responsible for grouping different inflected forms of words into the root form, having the same meaning.

## Loading the pretrained model BERT(Bidirectional Encoder Representations from Transformers)

About bert-base-multilingual-uncased-sentiment:

This a bert-base-multilingual-uncased model finetuned for sentiment analysis on product reviews in six languages: English, Dutch, German, French, Spanish and Italian. It predicts the sentiment of the review as a number of stars (between 1 and 5).

This model is intended for direct use as a sentiment analysis model for product reviews in any of the six languages above, or for further finetuning on related sentiment analysis tasks.

## Loading the pretrained model GPT3( Third-Generation Generative Pre-trained Transformer)

About GPT-3:

GPT-3, or the third-generation Generative Pre-trained Transformer, is a neural network machine learning model trained using internet data to generate any type of text.

GPT-3 is the largest neural network ever produced.
GPT-3 is better than any prior model for producing text that is convincing enough to seem like a human could have written it.

## Loading the pretrained model CodeBERT

CodeBERT is extension of BERT model developed by Microsoft.
This model can be used for multiple downstream tasks using programming language and natural language, such as suggesting developer a code for particular task, aiding developers for code translations and many more.
