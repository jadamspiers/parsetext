import collections
orderedDict = collections.OrderedDict()

from collections import OrderedDict

# sort dictionary by date

mydict = {'2016-06-07': 'last',
          '2016-06-05': 'first',
          '2016-06-06': 'mid'}

def sortDict(item):
    return sorted(item)

def spitResults(item):
    holder=''
    item = sorted(item)
    for date in item:
        print (date+'\t'+item[date]+'\n')


def spitResults(item):
    item = collections.OrderedDict()
    for k, v in item.items():
        print k, v

print OrderedDict(sorted(mydict.items(), key=lambda t: t[0]))
