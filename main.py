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
            if (len(passwordList) % 10000 == 0):
                time3 = time.time() - time2
                if (time3 >= 3600):
                    print(f"{len(passwordList)}\t{10000/(time.time() - time1)}\t{math.floor(time3/3600)} hours {math.floor((time3 % 3600) / 60)} minutes {time3 % 60} seconds")
                elif (time3 >= 60):
                    print(f"{len(passwordList)}\t{10000/(time.time() - time1)}\t{math.floor(time3/60)} minutes {time3 % 60} seconds")
                else:
                    print(f"{len(passwordList)}\t{10000/(time.time() - time1)}\t{time3} seconds")
                time1 = time.time()
        print(len(passwordList))
    
    passwordFile = open("rockyou23.txt", "a")
    for i in passwordList:
        passwordFile.write(f"{i}\n")

