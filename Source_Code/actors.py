__author__ = 'charanshampur'
import json
actorsFile = open("/Users/charanshampur/movie_genre_nlp/MovieSummaries/character.metadata.tsv","r")
movieFile = open("/Users/charanshampur/movie_genre_nlp/MovieSummaries/movie.metadata.tsv","r")
movieGenreFile = open("./NLP/movieGenreFile.txt","w")
movieActorFile=open("./NLP/movieActorFile.txt","w")
actorMovieFile=open("./NLP/actorMovieFile.txt","w")
actorCompleteCharFile=open("./NLP/actorCompleteCharFile.txt","w")
movieCompleteCharFile=open("./NLP/movieCompleteCharFile.txt","w")

movieGenreList=["action","thriller","adventure","comedy","drama","romance","horror","fiction"]
movieDict={}
movieActorsDict={}
actorDetails=[]
actorDict={}
for actor in actorsFile:
    #The below code gets {actor1:[movie1,movie2,movie3], actor2:[movie1,movie2]}
    actorDetails=actor.split('\t')
    actorName=actorDetails[8]
    if actorName=='':
        continue
    if actorName.lower() not in actorDict:
        actorMovieList=[actorDetails[0]]
        actorDict[actorName.lower()]=actorMovieList
    else:
        actorDict[actorName.lower()].append(actorDetails[0])
    movieName=actorDetails[0]
    # The below code gets {movieID1:[actor1,actor2], movieID2:[actor1,actor2,actor3]}
    if movieName not in movieActorsDict:
        actorList=[actorName.lower()]
        movieActorsDict[movieName]=actorList
    else:
        movieActorsDict[movieName].append(actorName.lower())

jsonarray = json.dumps(actorDict,indent=4)
actorMovieFile.write(jsonarray)
jsonarray = json.dumps(movieActorsDict,indent=4)
movieActorFile.write(jsonarray)

for movie in movieFile:
    #The below code gets {movieID1:[name,genre], movieID2:[name,genre]}
    movieDetails = movie.split('\t')
    if movieDetails[0] not in movieDict:
        movieName = movieDetails[2]
        inputGenre=eval(movieDetails[8])
        genreFound=False
        for k,v in inputGenre.items():
            for i in range(0,len(movieGenreList)):
                if (v.lower().find(movieGenreList[i]) > -1):
                    genreFound=True
                    if (i==2):
                        movieGenre=movieGenreList[i-1]
                    elif (i==5):
                        movieGenre=movieGenreList[i-1]
                    else:
                        movieGenre=movieGenreList[i]
                    break;
            if genreFound:
                break
        if not genreFound:
            #continue
            movieGenre="drama"
        movieDict[movieDetails[0]]=[movieName,movieGenre]
    else:
        continue
jsonarray = json.dumps(movieDict,indent=4)
movieGenreFile.write(jsonarray)

actorCompleteChar={}
actorGenre={}
for actor in actorDict:
    #this code gets {actor1:{action:0,thriller:2,comedy:30...}, actor2:{action:0,thriller:2,comedy:30...}}
    actorMovies=actorDict[actor]
    actorGenreDict={"action":0,"thriller":0,"comedy":0,"drama":0,"horror":0,"fiction":0}
    for movie in actorMovies:
        try:
            actor_movie_genre=movieDict[movie][1]
        except:
            continue
        actorGenreDict[actor_movie_genre]+=1
    #actorGenreTuple=list(actorGenreString.items())
    actorCompleteChar[actor]=dict(actorGenreDict)

jsonarray = json.dumps(actorCompleteChar,indent=4)
actorCompleteCharFile.write(jsonarray)

#reference # The below code gets
# {movieID1:[actor1,actor2], movieID2:[actor1,actor2,actor3]}
movieCompleteCharacter={}
for movie in movieActorsDict:
    actorList=movieActorsDict[movie]
    actorGenreDict={"action":0,"thriller":0,"comedy":0,"drama":0,"horror":0,"fiction":0}
    for actor in actorList:
        actorKind=actorCompleteChar[actor]
        for key in actorGenreDict:
            actorGenreDict[key]+=actorKind[key]
    actorGenreDict["genre"]=movieDict[movie][1]
    movieCompleteCharacter[movie] = dict(actorGenreDict)

jsonarray = json.dumps(movieCompleteCharacter,indent=4)
movieCompleteCharFile.write(jsonarray)
























