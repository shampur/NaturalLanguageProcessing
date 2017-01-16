__author__ = 'charanshampur'
import json
import sys

"""
print sys.path
sys.path.append("/Users/charanshampur/Library/Python/2.7/lib/python/site-packages/nltk")
sys.path.append("/Users/charanshampur/nltk_data")
sys.path.append("/usr/share/nltk_data")
sys.path.append("/usr/local/share/nltk_data")
sys.path.append("/usr/lib/nltk_data")
sys.path.append("/usr/local/lib/nltk_data")
#sys.path.append("/usr/share/nltk_data   ")
"""
import nltk
nltk.data.path.append("/Users/charanshampur/Library/Python/2.7/lib/python/site-packages/nltk")
nltk.data.path.append("/Users/charanshampur/nltk_data")
nltk.data.path.append("/usr/share/nltk_data")
nltk.data.path.append("/usr/local/share/nltk_data")
nltk.data.path.append("/usr/lib/nltk_data")
nltk.data.path.append("/usr/local/lib/nltk_data")
from nltk.corpus import stopwords
cachedStopWords = set(stopwords.words("english"))
junkCharac = set(['+','@','$','%','^','&','*','(',')','_','=','}','{','|',';','"','?','\'','>','<','~','`',',','\\','/','#',':',']','[','.','!','-'])
actorFile = open("NLP/actorCompleteCharFile.txt","r")
actorJson = json.load(actorFile)
vocabFile = open("NLP/vocab2.txt","r")
vocab=json.load(vocabFile)
#tagger = nltk.UnigramTagger(nltk.corpus.brown.tagged_sents())

summaryFile=open("NLP/summary.txt","r")
testingFile=open("NLP/testGenre.txt","w")
finalActorsGenre={"action":0,"thriller":0,"comedy":0,"drama":0,"horror":0,"fiction":0}
wordsVisited=set()
wordsList=[]
actorList=set()
for summary in summaryFile:
    tokens = nltk.word_tokenize(summary)
    wordsVisited.clear()
    wordsList=[]
    actorList.clear()
    for i in range(0,len(tokens)):
        tok1=tokens[i].lower()
        if not (i==len(tokens)-1):
            tok2=tokens[i+1].lower()
        bigramWord=tok1+" "+tok2
        unigramWord=tok1
        if unigramWord in actorJson and unigramWord not in actorList:
            actorList.add(unigramWord)
            actorGenre=actorJson[unigramWord]
            for genre in actorGenre:
                finalActorsGenre[genre]+=actorGenre[genre]
            continue
        if bigramWord in actorJson and bigramWord not in actorList:
            actorList.add(bigramWord)
            actorGenre=actorJson[bigramWord]
            for genre in actorGenre:
                finalActorsGenre[genre]+=actorGenre[genre]
            continue
        if unigramWord not in vocab:
            continue
        if unigramWord in wordsVisited:
            continue
        if unigramWord in cachedStopWords:
            continue
        wordCount=1.0
        for j in range(i+1,len(tokens)):
            newWord=tokens[j].lower()
            if unigramWord==newWord:
                wordCount+=1.0
        wordsVisited.add(unigramWord)
        stringRep=str(vocab[unigramWord])+':'+str(wordCount)
        wordsList.append(stringRep)

    sortedWordList=sorted(wordsList,key=lambda x: int(x.split(':')[0]))
    stringBuild=" "+' '.join(sortedWordList)
    actorGenreString=" 1:"+str(float(finalActorsGenre["action"]))+" 2:"+str(float(finalActorsGenre["thriller"]))+" 3:"+str(float(finalActorsGenre["comedy"]))+" 4:"+str(float(finalActorsGenre["drama"]))+" 5:"+str(float(finalActorsGenre["horror"]))+" 6:"+str(float(finalActorsGenre["fiction"]))
    finalStringBuild="1"+actorGenreString+stringBuild
    testingFile.write(finalStringBuild+'\n')
print "success"











