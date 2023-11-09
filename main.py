import requests
import time
import math

if (__name__ == "__main__"):
    urlList = []

    filefile = open("files.txt", "r")
    for line in filefile:
        urlList.append(line.strip())
    
    passwordList = set()

    time2 = time.time()
    for url in urlList:
        r = requests.get(url)
        open("temp.txt", "w").write(r.content.decode("latin-1"))
        tempFile = open("temp.txt", "r")
        time1 = time.time()
        for line in tempFile:
            line = line.strip()
            passwordList.add(line)
        print(len(passwordList))
    
    passwordFile = open("rockyou23.txt", "a")
    for i in passwordList:
        passwordFile.write(f"{i}\n")

