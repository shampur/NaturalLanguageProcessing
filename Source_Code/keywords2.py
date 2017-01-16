# This script is used to generate the feature set from the plot summary and the corresponding POS tags, it is associated with corresponding movie ID

import json
import nltk
from nltk.stem.snowball import PorterStemmer
from nltk.corpus import stopwords
cachedStopWords = set(stopwords.words("english"))
stemmer = PorterStemmer(ignore_stopwords=False)
#Open vocab file
f=open('NLP/vocab2.txt','r')

#Open movie plot summary file
#f1=open('NLP/plotTest.txt','r')
f1=open('NLP/plot_summaries.txt','r')
trainingFile=open("NLP/finalTrainFile2.txt","w")
movieCompleteCharFile=open("NLP/movieCompleteCharFile.txt","r")
actorRating=json.load(movieCompleteCharFile)

#Empty dictionary to write the vocabulary from vocab.txt
vocab = {}

#Write into vocab dictionary
vocab=json.load(f)

#Create the indexes for POS tags(Noun, Verb, Adj) from the last index in vocab file
vocab_size = len(vocab)
Noun_index = vocab_size+1
Verb_index = vocab_size+2
Adj_index = vocab_size+3

#list of speical characters, punctuations etc.
junkCharac = set(['+','@','$','%','^','&','*','(',')','_','=','}','{','|',';','"','?','\'','>','<','~','`',',','\\','/','#',':',']','[','.','!','-'])

#Dictionary of most common POS tags for Noun, Verb and Adj
#POS_taglist = {'1':'NN','2':'NNP','3':'NNS','4':'NNPS','5':'VB','6':'VBG','7':'VBZ','8':'VBD','9':'VBN','10':'VBP','11':'JJ','12':'JJS','13':'JJR'}
#POS_taglistNew = {'NN':1,'NNP':2,'NNS':3,'NNPS':4,'VB':5,'VBG':6,'VBZ':7,'VBD':8,'VBN':9,'VBP':10,'JJ':11,'JJS':12,'JJR':13}
pos_nouns=set(["NN","NNP","NNS","NNPS"])
pos_verbs=set(["VB","VBG","VBZ","VBD","VBN","VBP"])
pos_adjective=set(["JJ","JJS","JJR"])
#Empty dict to hold all the features of all the movies
#movieGenreList=["action","thriller","adventure","comedy","drama","romance","horror","fiction"]
genre={"action":1,"thriller":2,"comedy":3,"drama":4,"horror":5,"fiction":6}
#Read from plot_summaries.txt
wordsVisited=set()
lineCount=1
for line in f1:
    #Parts of Speech tag - feature creation
    #try:
    try:
        tokens = nltk.word_tokenize(line)
    except:
        continue
    movieId=tokens[0]
        #tagged = nltk.pos_tag(tokens)
    #tagged=nltk.pos_tag(tokens)
    #except:
        #continue
    #count starting from 1.0 to avoid divide by zero error
    Noun = 1.0
    Verb = 1.0
    Adj = 1.0
    #Consider each of the tags and get only the Nouns, Verbs and Adjectives
    #for tag in tagged:
    wordsVisited.clear()
    stringBuild=''
    #for i in range(1,len(tagged)):
    for i in range(1,len(tokens)):
        #word=tagged[i][0].lower()
        try:
            word=tokens[i].lower()
            #word=stemmer.stem(word)
        except:
            continue
        #posTagWord=tagged[i][1]
        if word in cachedStopWords:
            continue
        if word in junkCharac:
            continue
        if word not in vocab:
            continue
        """
        if posTagWord in pos_nouns:
            Noun+=1
        if posTagWord in pos_verbs:
            Verb+=1
        if posTagWord in pos_adjective:
            Adj+=1
        """
        if word in wordsVisited:
            continue
        wordCount=1.0
        #for j in range(i+1,len(tagged)):
        for j in range(i+1,len(tokens)):
            #newWord=tagged[j][0]
            try:
                newWord=tokens[j].lower()
                #newWord=stemmer.stem(newWord)
            except:
                continue
            if word==newWord:
                wordCount+=1.0
        wordsVisited.add(word)
        if word in vocab:
            stringBuild+=" "+str(vocab[word])+":"+str(wordCount)
    """
    total_postags = Noun+Verb+Adj
    Noun = float(Noun/total_postags)
    Verb = float(Verb/total_postags)
    Adj = float(Adj/total_postags)
    stringBuild+=" "+str(Noun_index)+":"+str(Noun)
    stringBuild+=" "+str(Verb_index)+":"+str(Verb)
    stringBuild+=" "+str(Adj_index)+":"+str(Adj)
    """
    if movieId in actorRating:
        actorGenre=actorRating[movieId]
        #movieGenreList=["action","thriller","adventure","comedy","drama","romance","horror","fiction"]
        actorGenreString=" 1:"+str(float(actorGenre["action"]))+" 2:"+str(float(actorGenre["thriller"]))+" 3:"+str(float(actorGenre["comedy"]))+" 4:"+str(float(actorGenre["drama"]))+" 5:"+str(float(actorGenre["horror"]))+" 6:"+str(float(actorGenre["fiction"]))
    #finalString=movieId+" "+actorGenre["genre"]+actorGenreString+stringBuild
    finalString=str(genre[actorGenre["genre"]])+actorGenreString+stringBuild
    print lineCount
    lineCount+=1
    trainingFile.write(finalString+"\n")