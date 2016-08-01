# open files
logs = open('logs.txt','r')


data=""
with open('logs.txt') as f:
    for line in f:
        data = data + line



result = open('output.txt','w')


# strip date
def getDate(line):
    return line[1:30]+' '

def getStatus(line):
    return line.split('AsyncRepTask-')[1][:6]

def getTCode(line):
    return

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


def sourceData(val):
    srcLog=sepSource()
    for item in srcLog.split('\n'):
        if 'destIp' in item and val == 'destIp':
            return getDate(item)+item.split('= ')[1]
        if 'srcVol' in item and val == 'srcVol':
            return getStatus(item)


print(sourceData('destIp'))
print(sourceData('srcVol'))


logs.close()
result.close()

