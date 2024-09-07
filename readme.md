## Journey so far with ml-for-nlp: /n
### 1)  Tokenization:
 it is used for transfering a big paragraph (corpus) into a list of sentences (documents) and sentences into list of words/n
we use different methods in the nltk library to perform these tokenization algorithms like nltk.sent_tokenize nltk.words_tokenize/n
### 2) Afte Tokenization we apply Stemming or for better results Lemmatization./n
Stemming provides the stem word like for eating it is eat so on and so forth but this technique does not give the best results so we use Lemmatization/n
Lemmatization provide us better results we import it from nltk.stem (lemmatizer) and it has a method lemmatizer.lemmatize it also has a pos tag/n
### 3) The pos tag in lemmatizer: 
it basically is for more better results like if the word in noun or adverb if we provide pos tag as well the results will be more accurate/n
### 4) Stop words:
 we can apply stop words as well these are just a list of words which does not play an important role so we just remove them we can also create our own list of stop words we import stop words from nltk.corpus /n
 