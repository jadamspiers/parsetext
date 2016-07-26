def printOnce(string):
    lines_seen = set()
    output = open('output.txt','w')
    for line in open('logs.txt','r'):
        line = line.split(']').pop()
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()



data = ""
count = 0

with open('logs.txt') as f:
	for line in f:
		data = data + line

fo = open('output.txt','wb')

for item in data.split('\n'):
    if 'destIp' in item:
        fo.write(item+'\n')
    if 'srcVol = MAIN-NexGen-Infrastructure-' in item:
        fo.write(item+'\n')




