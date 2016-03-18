import zlib
with open('2.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')
    
S = zlib.compress(data)
with open("temp.zlib", "wb") as myfile:
    myfile.write(S)