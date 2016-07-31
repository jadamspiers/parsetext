# open files
logs = open('logs.txt','r')


data=""
with open('logs.txt') as f:
    for line in f:
        data = data + line



result = open('output.txt','w')


# strip date
def getDate(line):
    return line[1:30]

# find line containing text
def sepSource():
    temp=""
    for item in data.split('\n'):
        if 'AsyncRepTask' in item:
            temp = temp+item+'\n'
    return temp

def sepDest():
    for item in data.split('\n'):
        if 'AsyncRepDestTask' in item:
            result.write(item+'\n')




print(sepSource())

logs.close()
result.close()

