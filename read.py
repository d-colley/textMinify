import zlib

with open("temp.zlib", "rb") as myfile:
    S = myfile.read()
T = zlib.decompress(S)

print T

with open('new2.txt', 'w') as myFile:
    myFile.write(T)