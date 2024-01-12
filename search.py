import searchdata
import count
import sort
import math
import os

def search(phrase, boost):
    words = phrase.split(" ")
    words = sort.merge_sort(words)
    qis = {}
    dis = {}
    urls = []
    searchVector= []
    docVector = []
    cosineSims = {}
    order = []
    compleQ = {}
    
    x = words
    for word in x:
        if searchdata.get_idf(word) <= 0:
            y = words.index(word)
            x.pop(y)
    
    words = x

    for word in words:
        if word in compleQ:
            continue
        numOfWord = count.count(words, word)
        qi = math.log(1 + ((numOfWord) / len(words)), 2) * searchdata.get_idf(word)
        qis[word] = qi
        searchVector.append(qi)
        compleQ[word] = 0

    compleD = {}
    cosineSimsTosort = []

    files = os.listdir("seeds")
    for file in files:
        filein = open(os.path.join("seeds", file), "r")
        url = filein.readline()
        urls.append(url)
        filein.close()

        docVector = []
        compleD = {}
        for word in words:
            if word in compleD:
                continue
            docTfIdf = searchdata.get_tf_idf(url, word)
            docVector.append(docTfIdf)
            compleD[word] = 0
        dis[url] = docVector
        
        nume = 0
        ldenom = 0
        rdenom = 0
        dnom = 0

        for index in range(len(searchVector)):
            nume += searchVector[index] * docVector[index]
            ldenom += searchVector[index] ** 2
            rdenom += docVector[index] ** 2
        dnom += math.sqrt(ldenom) * math.sqrt(rdenom)
        if dnom == 0:
            cosineSims[url] = 0
            continue
        cosineSim = nume / dnom
        if boost == True:
            cosineSims[url] = cosineSim * searchdata.get_page_rank(url)    
        else:
            cosineSims[url] = cosineSim     
    
    rever = {}
    dup = {}

    for url in cosineSims:
        cosineSimsTosort.append(cosineSims[url])
        if cosineSims[url] in rever:
            if dup.get(cosineSims[url]) == None:
                dup[cosineSims[url]] = [url]
            else:
                dup[cosineSims[url]].append(url)
        else:
            rever[cosineSims[url]] = url


    sortedCos1 = sort.merge_sort(cosineSimsTosort)

    returnVal = []
    returnDict = {}

    used = {}
    for i in range(10):
        cosineSimx = sortedCos1[len(sortedCos1) - 1 - i]
        returnDict = {}
        if rever[cosineSimx] in used:
            returnDict["url"] = dup[cosineSimx][0]
            returnDict["title"] = searchdata.getTitle(dup[cosineSimx][0]).strip(".txt")
            returnDict["score"] = cosineSimx
            returnVal.append(returnDict)
            dup[cosineSimx].pop(0)
        else:
            returnDict["url"] = rever[cosineSimx]
            used[rever[cosineSimx]] = 0
            returnDict["title"] = searchdata.getTitle(returnDict["url"]).strip(".txt")
            returnDict["score"] = cosineSimx
            returnVal.append(returnDict)
    
    return returnVal 
    
print(search("peach papaya", True)) 