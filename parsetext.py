import os



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

def getTCode(line,dest):
    if dest == 'source' and line:
        return line.split('AsyncRepTask-')[1][:6]
    elif dest == 'target' and line:
        return line.split('AsyncRepDestTask-')[1][:6]

def getStatus(line):
    return line.split('detail = ')[1]

# find line containing text
def sepSource():
    temp=""
    for item in data.split('\n'):
        if 'AsyncRepTask' in item:
            temp = temp+item+'\n'
    return temp

def sepDest():
    temp=""
    for item in data.split('\n'):
        if 'AsyncRepDestTask' in item:
            temp = temp+item+'\n'
    return temp

def newHeader(kind):
    if kind == 'src':
        result.write('\n\n***SOURCE***\n\n\n')
    elif kind == 'targ':
        result.write('\n\n***TARGET***\n\n\n')


def sourceData(val):
    newLog=''
    srcLog=sepSource()
    for item in srcLog.split('\n'):
        if 'destIp' in item and val == 'destIp':
            newLog='destIp:     '+getDate(item)+item.split('= ')[1]+'\n'
            result.write(newLog)
        if 'srcVol' in item and val == 'srcVol':
            newLog='srcVol:     '+item.split('srcVol = ')[1]+getTCode(item,'source')+'\n'
            result.write(newLog)
        if 'detail =' in item and val == 'status':
            newLog='Status:     '+getDate(item)+getStatus(item)+'\n'
            result.write(newLog)

def targetData(val):
    newLog=''
    targLog=sepDest()
    for item in targLog.split('\n'):
        if 'AsyncRepDestTask-' in item and val == 'tcode':
            newLog='task code:      '+getDate(item)+getTCode(item,'target')+'\n'
            result.write(newLog)
        if 'detail =' in item and val == 'status':
            newLog='Status:     '+getDate(item)+getStatus(item)+'\n'
            result.write(newLog)


newHeader('src')
sourceData('destIp')
sourceData('srcVol')
sourceData('status')

newHeader('targ')
targetData('status')

logs.close()
result.close()

