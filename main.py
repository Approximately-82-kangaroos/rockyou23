import requests
import time

if (__name__ == "__main__"):
    urlList = []

    filefile = open("files.txt", "r")
    for line in filefile:
        urlList.append(line.strip())
    
    passwordList = ["password"]

    for url in urlList:
        r = requests.get(url, allow_redirects = True)
        open("temp.txt", "w").write(r.content.decode("latin-1"))
        tempFile = open("temp.txt", "r")
        time1 = time.time()
        time2 = time.time()
        for line in tempFile:
            line = line.strip()
            if (line not in passwordList):
                passwordList.append(line)
                if (len(passwordList) % 10000 == 0):
                    print(f"{len(passwordList)}\t{10000/(time.time() - time1)}\t{len(passwordList)/(time.time() - time2)}")
                    time1 = time.time()
            else:
                print(f"Skipped {line}")
        print(len(passwordList))
    
    passwordFile = open("rockyou23.txt", "a")
    for i in passwordList:
        passwordFile.write(f"{i}\n")

