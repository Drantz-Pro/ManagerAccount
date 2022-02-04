from io import open
import sys

def processData(arr):
    data = []
    id = 0

    for d in arr:
        account = d.split('|')
        account.append(str(id))
        data.append(account)
        id+=1
    return data

def spaces (arr):
    u = []
    p = []
    w = []
    id = 2
    for x in arr:
        u.append(len(x[0]))
        p.append(len(x[1]))
        w.append(len(x[2]))
        if len(x[-1]) > 2:
            id = len(x[-1])
    return [max(u),max(p),max(w),id]

def processTable (data , size):
    account = []
    accountStorage = []
    for x in data:
        account = []
        if len(x[0]) < size[0]:
            account.append(x[0]+ " " *(size[0]-len(x[0])))
        else:
            account.append(x[0])
        if len(x[1]) < size[1]:
            account.append(x[1]+ " " *(size[1]-len(x[1])))
        else:
            account.append(x[1])
        if len(x[2]) < size[2]:
            account.append(x[2]+ " " *(size[2]-len(x[2])))
        else:
            account.append(x[2])
        if len(x[-1]) < size[-1]:
            account.append(x[-1]+ " " *(size[-1]-len(x[-1])))
        else:
            account.append(x[-1])
        accountStorage.append(account)
    return accountStorage

def getAccount():
    file = open('accounts', 'r', encoding='UTF-8')

    info = file.read().split(';')

    info.pop()

    data = processData(info)

    sizeWord = spaces(data)

    tableData = processTable(data,sizeWord)

    for x in tableData:
        print(f"| {x[-1]} | {x[0]} | {x[1]} | {x[2]} |")


    file.close


sys.modules[__name__] = getAccount