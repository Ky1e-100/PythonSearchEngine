import webdev as wd
import queue1 as q #queue with dictionary search -- realized later that i forgot to use it and am too lazy to remove it
import osOperations as op #modified os demo file for directories and files
import os
import math
import sort
import searchHelper as search
import matmult

def getTitle(URL):
    title = ""
    if os.path.isdir("seeds"):
        files = os.listdir("seeds")
        for file in files:
            filein = open(os.path.join("seeds", file), "r")
            seed = filein.read().strip()
            if seed == URL:
                title = file
                filein.close()
                return title
            filein.close()
        
        if title == "":
            return None

def crawl(seed):
    op.delete_directory("urlsOut")
    op.delete_directory("wordFreqs")
    op.delete_directory("seeds")
    op.delete_directory("urlsIn")
    op.delete_directory("termFreqs")
    op.delete_directory("totalOut")
    op.delete_directory("totalWordInDoc")
    op.delete_directory("total")
    op.delete_directory("idf")
    op.delete_directory("pageRank")
    count = 1

    queue = [seed]
    finished = [seed]
    inLinks = {}
    addedInLink = {}
    dict = {}
    totalWordDocs = {}
    totalWordDocsLinks = {} #Used links
    id = {}
    idCount = 0
    seedId = {}
    adjMatrix = []
    actualId = {}

    while len(queue) > 0:
        info = wd.read_url(seed)
        seedId[seed] = idCount

    # Find the title
        titStart = info.find("<title>") + 7
        titEnd = info.find("</title>")
        title = info[titStart:titEnd]

        id[title + ".txt"] = idCount
        actualId[idCount] = title + ".txt"

    # Link URLs to Title
        if op.check_directory("seeds") == False:
            op.create_directory("seeds")
        op.create_file("seeds", (title + ".txt"), seed)

    # Get body paragraphs
        bodys = []
        tempBod = info
        bod = tempBod.find("<p>")
        while True:
            if bod == -1:
                break
            bodStart = bod + 3
            bodEnd = tempBod.find("</p>")
            bodys.append(tempBod[bodStart:bodEnd])
            tempBod = tempBod[bodEnd +4:]
            bod = tempBod.find("<p>")
            
    #Get word frequency
        wordFreq = {}
        for body in bodys:
            words = body.strip().split("\n")
            for word in words:
                if word not in wordFreq:
                    wordFreq[word] = 1
                else:
                    wordFreq[word] += 1

    # Total word frequency
        for word in wordFreq:
            if word in totalWordDocs: #added
                if totalWordDocsLinks.get(word) == None: #added and no seed added
                    totalWordDocs[word] += 1
                    totalWordDocsLinks[word].append(seed)
                else: #added seed added
                    if seed in totalWordDocsLinks[word]:
                        continue
                    else:
                        totalWordDocs[word] += 1
                        totalWordDocsLinks[word].append(seed)
            else:
                totalWordDocs[word] = 1
                if totalWordDocsLinks.get(word) == None:
                    totalWordDocsLinks[word] = []
                totalWordDocsLinks[word].append(seed)
                        
    #Store word Freq in the info file
        content = ""
        totalWords = 0
        for key in wordFreq:
            content += key + " " + str(wordFreq[key]) + "\n"
            totalWords += wordFreq[key]
        content += str(totalWords)                              #COME BACK TO THIS
        if op.check_directory("wordFreqs") == False:
            op.create_directory("wordFreqs")
        op.create_file("wordFreqs", (title + ".txt"), content)

    #Store term freq
        content = ""
        for word in wordFreq:
            termFreq = wordFreq[word] / totalWords
            content += word + " " + str(termFreq) + "\n"

        if op.check_directory("termFreqs") == False:
            op.create_directory("termFreqs")
        op.create_file("termFreqs", (title + ".txt"), content)

    # Get links on THIS webpage
        urls = []
        temp = info
        urlBeg = temp.find("href=\"")
        while True:
            if urlBeg == -1:
                break
            urlStart = urlBeg + 6
            temp = temp[urlStart:]
            urlEnd = temp.find("\"")
            url = temp[:urlEnd]
            urls.append(url)
            temp = temp[urlEnd:]
            urlBeg = temp.find("href=\"")

    #Queue for urls

        content = ""
        tempSeed = seed[:seed.rfind("/")]
        totalOut = 0
        for url in urls:
            if url in finished:
                continue
            elif str(url).startswith("http://"):
                url = link
                q.addend(queue, dict, link)
                content += link + "\n" #for outgoing files
                totalOut += 1
                if inLinks.get(link) == None:
                    inLinks[link] = [seed]
                elif seed in inLinks[link]:
                    continue
                else:
                    inLinks[link].append(seed)
            elif not str(url).startswith("http://"):
                url = url[1:]
                link = tempSeed + url
                content += link + "\n" #outgoing files
                q.addend(queue, dict, link)   
                totalOut += 1        
                if inLinks.get(link) == None:
                    inLinks[link] = [seed]
                elif seed in inLinks[link]:
                    continue
                else:
                    inLinks[link].append(seed)
        content += str(totalOut)        
        
    #Add outgoingUrls to a file
        if op.check_directory("urlsOut") == False:
            op.create_directory("urlsOut") 
        op.create_file("urlsOut", (title + ".txt"), content)

    #add totalOutgoingUrls to a file MIGHT NOT NEED
        if op.check_directory("totalOut") == False:
            op.create_directory("totalOut") 
        op.create_file("totalOut", (title + ".txt"), str(totalOut))

    #Repeat until all links are visited
        for item in queue:
            if item in finished:
                queue.remove(item)
        
        if len(queue) == 0:
            break
        elif queue[0] == "":
            queue.pop[0]
            continue
            
        elif queue[0] in finished:
            queue.pop(0)
            continue

        seed = queue[0]
        finished.append(seed)
        count += 1
        idCount += 1
        queue.pop(0)
    # LAST FILE
        info = wd.read_url(seed)
        seedId[seed] = idCount

    # Find the title
        titStart = info.find("<title>") + 7
        titEnd = info.find("</title>")
        title = info[titStart:titEnd]

        id[title + ".txt"] = idCount
        actualId[idCount] = title + ".txt"

    # Link URLs to Title
        if op.check_directory("seeds") == False:
            op.create_directory("seeds")
        op.create_file("seeds", (title + ".txt"), seed)

    # Get body paragraphs
        bodys = []
        tempBod = info
        bod = tempBod.find("<p>")
        while True:
            if bod == -1:
                break
            bodStart = bod + 3
            bodEnd = tempBod.find("</p>")
            bodys.append(tempBod[bodStart:bodEnd])
            tempBod = tempBod[bodEnd +4:]
            bod = tempBod.find("<p>")
            
    #Get word frequency
        wordFreq = {}
        for body in bodys:
            words = body.strip().split("\n")
            for word in words:
                if word not in wordFreq:
                    wordFreq[word] = 1
                else:
                    wordFreq[word] += 1

    # Total word frequency
        for word in wordFreq:
            if word in totalWordDocs: #added
                if totalWordDocsLinks.get(word) == None: #added and no seed added
                    totalWordDocs[word] += 1
                    totalWordDocsLinks[word].append(seed)
                else: #added seed added
                    if seed in totalWordDocsLinks[word]:
                        continue
                    else:
                        totalWordDocs[word] += 1
                        totalWordDocsLinks[word].append(seed)
            else:
                totalWordDocs[word] = 1
                if totalWordDocsLinks.get(word) == None:
                    totalWordDocsLinks[word] = []
                totalWordDocsLinks[word].append(seed)
                        
    #Store word Freq in the info file
        content = ""
        totalWords = 0
        for key in wordFreq:
            content += key + " " + str(wordFreq[key]) + "\n"
            totalWords += wordFreq[key]
        content += str(totalWords)                              #COME BACK TO THIS
        if op.check_directory("wordFreqs") == False:
            op.create_directory("wordFreqs")
        op.create_file("wordFreqs", (title + ".txt"), content)

    #Store term freq
        content = ""
        for word in wordFreq:
            termFreq = wordFreq[word] / totalWords
            content += word + " " + str(termFreq) + "\n"

        if op.check_directory("termFreqs") == False:
            op.create_directory("termFreqs")
        op.create_file("termFreqs", (title + ".txt"), content)

    # Get links on THIS webpage
        urls = []
        temp = info
        urlBeg = temp.find("href=\"")
        while True:
            if urlBeg == -1:
                break
            urlStart = urlBeg + 6
            temp = temp[urlStart:]
            urlEnd = temp.find("\"")
            url = temp[:urlEnd]
            urls.append(url)
            temp = temp[urlEnd:]
            urlBeg = temp.find("href=\"")

    #Queue for urls

        content = ""
        tempSeed = seed[:seed.rfind("/")]
        totalOut = 0
        for url in urls:
            if url in finished:
                continue
            elif str(url).startswith("http://"):
                url = link
                q.addend(queue, dict, link)
                content += link + "\n" #for outgoing files
                totalOut += 1
                if inLinks.get(link) == None:
                    inLinks[link] = [seed]
                elif seed in inLinks[link]:
                    continue
                else:
                    inLinks[link].append(seed)
            elif not str(url).startswith("http://"):
                url = url[1:]
                link = tempSeed + url
                content += link + "\n" #outgoing files
                q.addend(queue, dict, link)   
                totalOut += 1        
                if inLinks.get(link) == None:
                    inLinks[link] = [seed]
                elif seed in inLinks[link]:
                    continue
                else:
                    inLinks[link].append(seed)
        content += str(totalOut)        
        
    #Add outgoingUrls to a file
        if op.check_directory("urlsOut") == False:
            op.create_directory("urlsOut") 
        op.create_file("urlsOut", (title + ".txt"), content)

    #add totalOutgoingUrls to a file MIGHT NOT NEED
        if op.check_directory("totalOut") == False:
            op.create_directory("totalOut") 
        op.create_file("totalOut", (title + ".txt"), str(totalOut))



#add inboundUrls to a file
    if op.check_directory("urlsIn") == False:
        op.create_directory("urlsIn")
    for seed in inLinks:
        name = getTitle(seed)
        if name == None:
            continue
        op.create_file("urlsIn", name, "")
        fileout = open(os.path.join("urlsIn", name), "a")
        for inboundLink in inLinks[seed]:
            fileout.write(inboundLink + "\n")
        fileout.close()
    
#add total amount of a Word in all the documents 
    if op.check_directory("totalWordInDoc") == False:
        op.create_directory("totalWordInDoc")
    
    for word in totalWordDocs:
        op.create_file("totalWordInDoc", word + ".txt", str(totalWordDocs[word]))

#Total num of docs
    if op.check_directory("total") == False:
        op.create_directory("total")
        op.create_file("total", "total.txt", str(count))
   

# Calculate idf values
    if op.check_directory("idf") == False:
        op.create_directory("idf")
    for word in totalWordDocs:
        idf = math.log(count / (1 + totalWordDocs[word]), 2)
        op.create_file("idf", word + ".txt", str(idf))

# Matrix Stuff
    for row in range(count):
        rowValue = []
        for col in range(count):
            rowValue.append(0)
        adjMatrix.append(rowValue)

    files1 = os.listdir("urlsOut")

    for file in files1: #adjacency matrix
        filein = open(os.path.join("urlsOut", file), "r")
        fileId = id[file]
        for line in filein:
            if line.startswith("http"):
                line = line.strip()
                lineID = seedId[line]
            adjMatrix[fileId][lineID] = 1

        filein.close()
    

    for row in range(len(adjMatrix)): #initial transition divide rows bt # of ones
        oneCount = 0
        for col in range(len(adjMatrix[row])) :
            if adjMatrix[row][col] == 1:
                oneCount += 1
        for col in range(len(adjMatrix[row])):
            adjMatrix[row][col] = adjMatrix[row][col] / oneCount

    #Scaled adjancency matrix 1 - alpha * adjencency
    a = 0.1

    adjMatrix = matmult.mult_scalar(adjMatrix, (1-a))

    #add alpha/n to each entry
    for row in range(len(adjMatrix)): #initial transition divide rows bt # of ones
        for col in range(len(adjMatrix[row])) :
            adjMatrix[row][col] += (a / count)
    
   #multiplication vector stuff
    
    initVector = []
    for i in range(len(files1)):
        initVector.append(1 / len(files1))

    result0 = matmult.multiply(initVector, adjMatrix)
    result1 = matmult.multiply(result0, adjMatrix)
    
    temp = []
    eD = math.dist(result0, result1)

    target = 0.0001

    while eD > target:
        temp = matmult.multiply(result1, adjMatrix) #when it ends temp is the final page rank
        eD = math.dist(result1, temp)
        result1 = temp

    pageRank = temp

#   add it to a file
    if op.check_directory("pageRank") == False:
        op.create_directory("pageRank")
    
    for id in range(len(pageRank)):
        op.create_file("pageRank", actualId[id], str(pageRank[id]))

    print("finished crawl")
    return count
    

crawl("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html")