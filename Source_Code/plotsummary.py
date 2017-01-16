import json
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import PorterStemmer

junkCharac = set(['+','@','$','%','^','&','*','(',')','_','=','}','{','|',';','"','?','\'','>','<','~','`',',','\\','/','#',':',']','[','.','!','-','\'s','``','\'\'','...','n\'t','\'ll','\'ve'])
cachedStopWords = set(stopwords.words("english"))

#f = open('NLP/plotTest.txt', 'r')
f = open('NLP/plot_summaries.txt', 'r')
f1 = open('NLP/vocab2.txt','w')
count=1
vocabList=set()
vocabJson={}
stemmer = PorterStemmer(ignore_stopwords=False)
for line in f:
    try:
        tokens = nltk.word_tokenize(line)
    except:
        continue
    for i in range(1,len(tokens)):
        token=tokens[i].lower()
        """
        try:
            token=stemmer.stem(token)
        except:
            continue
        """
        if token not in junkCharac and not token.isdigit():
            if token not in vocabJson:
                if token not in cachedStopWords:
                    vocabJson[token]=count+6
                    print count
                    count+=1

jsonarray = json.dumps(vocabJson,indent=4)
f1.write(jsonarray)