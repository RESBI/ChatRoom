maxBit = 20
def getOrdList(content):
    ordList = []
    for tl in content:
        ordList += [ord(tl)]
    return ordList
    
def getChrList(content):
    chrList = []
    for tl in content:
        chrList += [chr(tl)]
    return chrList

def getBin(content):
    Bin = []
    for l in content:
        Bin += [bin(l).replace("0b","").zfill(maxBit)]
    return Bin

def getNum(content):
    Num = []
    for l in content:
        Num += [int(l,2)]
    return Num

def Xor(one,keys):
    result = []
    count = 0
    for b in range(len(one)):
        rt = []
        for a in range(len(one[b])):
            r = int(one[b][a]) ^ int(keys[0][count])
            rt += [r]
            count += 1
        result += [rt]
    return result

def peip(msg,key):
    result = ""
    while len(result) < len(msg):
        result += key
    return result

def link(content):
    result = ""
    for l in content:
        result += l
    return [result]

def lk2(content):
    result = []
    for l in range(len(content)):
        rt = ""
        for ll in range(0,len(content[l])):
            rt += str(content[l][ll])
        result += [rt.zfill(maxBit)]
    return result

def code(msg,key):
        #Get ord list.
    msgOrd = getOrdList(msg)
    keyOrd = getOrdList(key)
        #Get binary list.
    msgBin = getBin(msgOrd)
    keyBin = getBin(keyOrd)
        #Get longkey.
    LK = peip(link(msgBin)[0],link(keyBin)[0])
        #Link up.
    LKlink = link(LK)
        #Crypto.
    Xor_result = Xor(msgBin,LKlink)
    lkResult = lk2(Xor_result)
        #Get coded num.
    encodeNums = getNum(lkResult)
        #Get coded chr.
    encodeChrs = getChrList(encodeNums)
    return encodeChrs

def enc(msg,key):
    return link(code(msg,key))[0]

def dec(msg,key):
    return link(code(msg,key))[0]

