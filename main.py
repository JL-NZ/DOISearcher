import time
import os

# store start time
StartTime = time.time()

# open files as text files
ArticleList = open("AllArticles.ris", "r", encoding="utf-8")
TargetList = open("TargetArticles.ris", "r", encoding="utf-8")

# compile a list of DOI to search for
TargetDOIArray = []
for line in TargetList:
    if line.startswith("DO"):
        TargetDOIArray.append(line[5:])

# search the full list of articles for each of our target DOI
FoundArticles = []
NumArticlesFound = 0
for line in ArticleList:
    if line.startswith("DO"):
        for doi in TargetDOIArray:
            if doi in line:
                NumArticlesFound += 1
                FoundArticles.append(doi)

# evaluate the time the program took to execute
EndTime = time.time()
ElapsedTime = EndTime - StartTime

# console output
print ("Search Queries: " + str(len(TargetDOIArray)))
print ("Articles Found: " + str(NumArticlesFound))
print ("Elapsed Time: " + str(ElapsedTime))

# delete previous created files if they exist
if os.path.exists("FoundArticles.txt"):
    os.remove("FoundArticles.txt")
if os.path.exists("MissingArticles.txt"):
    os.remove("MissingArticles.txt")

# create files
FoundArticlesFile = open("FoundArticles.txt", "w")
for Article in FoundArticles:
    FoundArticlesFile.write(Article)

MissingArticlesFile = open("MissingArticles.txt", "w")
for Article in TargetDOIArray:
    if Article not in FoundArticles:
        MissingArticlesFile.write(Article)

# cleanup
ArticleList.close()
TargetList.close()
FoundArticlesFile.close()
MissingArticlesFile.close()