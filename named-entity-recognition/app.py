import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('punkt') 
nltk.download('words')
nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab')

sent = 'Rohan was born on 14 July 2001 he is trying to learn ml algorithms' 
words = nltk.word_tokenize(sent)
tagged = nltk.pos_tag(words)
print(tagged)
chunked = nltk.ne_chunk(tagged)
print(chunked)

