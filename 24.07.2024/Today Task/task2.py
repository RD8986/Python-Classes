import os

data=os.getcwd()
print("Current Working directory: ",data)

directorydata=os.listdir(os.path.join(data+'\StandardLibrary'))

print(directorydata)