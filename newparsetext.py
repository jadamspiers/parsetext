# updated and now sexy




logs = open('logs.txt','r')
data = ''
with open('logs.txt') as f:
    for line in f:
        data = data + line

result = open('output.txt','w')


def newsourceData():
    for item in data.split('\n'):
        if 'OnStarted' in item or 'ARTaskDone' in item:
            if 'destIp' in item:
                startDate=getDate(item)
                destip=item.split('destIp = ')[1]
                result.write(startDate+'\t'+destip+'\n')
            elif 'srcVol' in item:
                srcvol=item.split('srcVol = ')[1]
                code=item.split('AsyncRepTask-')[1][:6]
                result.write(srcvol+'\t'+code+'\n')
            elif 'ARTaskPass' in item:
                result.write('Success\n\n')
        if 'ARTaskFail: status' in item:
            status=item.split('detail = ')[1]
            result.write(startDate+'\t'+status+'\n\n')
        if 'AsyncRepDestTask-' in item or 'ARD_TaskPass' in item:
            if 'ARD_STATE_STARTED' in item:
                startDate=getDate(item)
                code=item.split('AsyncRepDestTask-')[1][:6]
                result.write(startDate+'\t'+code+'\n')






def getDate(line):
    return line[7:17]



newsourceData()
