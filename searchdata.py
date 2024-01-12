import os
import sort
import searchHelper as search
import crawler
import math

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

title = ""

def get_outgoing_links(URL):
    global title
    title = ""
    if os.path.isdir("seeds"):
        files = os.listdir("seeds")
        for file in files:
            filein = open(os.path.join("seeds", file), "r")
            seed = filein.read().strip()
            if seed == URL:
                title = file
                filein.close()
                break
            filein.close()
        
        if title == "":
            return None
    
    if os.path.isdir("urlsOut"):
        files = sort.merge_sort(os.listdir("urlsOut"))
        toOpen = search.binarySearchString(files, title)
        filein = open(os.path.join("urlsOut", files[toOpen]), "r")
        urls = []
        for line in filein:
            if urls != "" and line.startswith("http"):
                urls.append(line.strip())
        return urls

def get_incoming_links(URL):
    name = crawler.getTitle(URL)
    if name == None:
        return None
    if os.path.isdir("urlsIn"):
        files = sort.merge_sort(os.listdir("urlsIn"))
        toOpen = search.binarySearchString(files, name)
        filein = open(os.path.join("urlsIn", files[toOpen]), "r")
        urls = []
        for line in filein:
            if urls != "":
                urls.append(line.strip())
        return urls


def get_page_rank(URL): #URL is the query?
    title = getTitle(URL)
    if title == None:
        return -1

    if os.path.isdir("pageRank"):
        files = os.listdir("pageRank")
        files = sort.merge_sort(files)
        toOpen = search.binarySearchString(files, title)
        filein = open(os.path.join("pageRank", files[toOpen]), "r")
        pageRank = filein.readline()
        return float(pageRank)


def get_idf(word):
    if os.path.isdir("idf"):
        files = os.listdir("idf")
        files = sort.merge_sort(files)
        present = search.binarySearchString(files, word + ".txt")
        if present == -1:
            return 0
        else:
            filein = open(os.path.join("idf", word + ".txt"), "r")
            idf = filein.read().strip()
            filein.close()
            return float(idf)


def get_tf(URL, word):

    name = crawler.getTitle(URL)
    tf = 0

    if os.path.isdir("termFreqs"):
        files = sort.merge_sort(os.listdir("termFreqs"))
        if name == None:
            return 0
        toOpen = search.binarySearchString(files, name)
        filein = open(os.path.join("termFreqs", files[toOpen]), "r")
        for line in filein:
            line = line.strip()
            if line.startswith(word):
                tf = line[len(word):]
                return float(tf)

    return 0

def get_tf_idf(URL, word):
    tfIdf = math.log(1 + get_tf(URL, word),2) * get_idf(word)
    return float(tfIdf)