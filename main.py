import requests
import math

if (__name__ == "__main__"):
    urlList = []

    filefile = open("files.txt", "r")
    for line in filefile:
        urlList.append(line.strip())
    
    passwordList = set()

    for url in urlList:
        if (url[:1] == "#"):
            continue
        print(url)
        if (url[:4] == "http"):
            r = requests.get(url)
            open("temp.txt", "w").write(r.content.decode("latin-1"))
            tempFile = open("temp.txt", "r")
        else:
            tempFile = open(url, "r")
        for line in tempFile:
            line = line.strip()
            passwordList.add(line)
        print(len(passwordList))
        tempFile.close()
    
    passwordFile = open("hurricane.txt", "w")
    passwordFile.write("")
    passwordFile.close()
    passwordFile = open("hurricane.txt", "a")
    for i in passwordList:
        passwordFile.write(f"{i}\n")

