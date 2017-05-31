import os

for i in range(6):
    str = "result is %s" % i
    print(str)



filePath = "H:\pythondownload\contract\\test\cc.txt"

fileDir = os.path.dirname(filePath)
print(fileDir)

if not os.path.exists(fileDir):
    os.makedirs(fileDir)