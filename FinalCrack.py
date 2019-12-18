import collections
import argparse 

maxKeyLen = 10
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
letters = LETTERS.upper()
englishLetterFreq = {'e': 12.02, 't': 9.10, 'a': 8.12,
                     'o': 7.68, 'i': 7.31, 'n': 6.95, 's': 6.28, 'h': 6.02, 'r': 5.92, 'd': 4.32,
                     'l': 3.98, 'u': 2.88, 'c': 2.71, 'm': 2.61, 'f': 2.30, 'y': 2.11, 'w': 2.09,
                     'g': 2.03, 'p': 1.82, 'b': 1.49, 'v': 1.11, 'k': 0.69, 'x': 0.17,
                     'q': 0.11, 'j':0.10 , 'z': 0.07}


def translateMessage(key, message, mode):
    translated = [] # stores the encrypted/decrypted message string
    keyRound = 0
    keyIndex = 0
    key = key.upper()
    for symbol in message: # loop through each character in message
        num = letters.find(symbol.upper())
        if num != -1: # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += letters.find(key[keyIndex]) + keyRound 
            elif mode == 'decrypt':
                num -= letters.find(key[keyIndex]) + keyRound
            num %= len(letters)
            if symbol.isupper():
                translated.append(letters[num])
            elif symbol.islower():
                translated.append(letters[num].lower())

            keyIndex += 1 
            if keyIndex == len(key):
                keyIndex = 0
                keyRound += 1
        else:
            translated.append(symbol)

    return ''.join(translated)
        
def ioc(string):
    counter = collections.Counter(string)
    s = sum(n*(n-1) for n in counter.values())
    tot = sum(counter.values())
    ioc = s /(float) (tot*(tot-1))
    return ioc

def minIOC(translated):
    value = []
    for i in range(0,10):
        value.append(ioc(translated[i]))
    return value.index(max(value))

def checkFreq(string):
    counter = collections.Counter(string)
    dic = dict(counter)
    tot =  sum(counter.values())
    tot = float(tot)
    newList = {k: v / tot *100 for k, v in dic.items()}
    d3 = {key: abs(englishLetterFreq[key] - newList.get(key, 0)) \
          for key in englishLetterFreq.keys()}
    return sum(d3.values())

def checkfirst(string,start,stride):
    somestr = ["" for f in range(26)] 
    freqErr = [0]*26
    for j in range(0,len(LETTERS)):
        stringNew = string
        for i in range(start,len(string),stride):
            stringNew = stringNew[:i] + LETTERS[(LETTERS.find(stringNew[i])-j)%26] \
            + stringNew[i + 1:]
        freqErr[j] = checkFreq(stringNew)
        somestr[j] += stringNew
    idx = freqErr.index(min(freqErr))
    stringOut = somestr[idx]
    return stringOut,idx


def printKey(translated):
    transfCipherIdx = minIOC(translated)
    transfCipherIdx = int(transfCipherIdx)
    keyLen = maxKeyLen - transfCipherIdx #minIOC()
    key = ""
    start = 0
    strr = translated[transfCipherIdx]
    for i in range(keyLen):
        strr,idx = checkfirst(strr,start+i,keyLen)
        key += LETTERS[idx]
    return (key)

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

'''
key = "aaaaaaaaa"
with open("plaintext", "rb") as myfile:
    myMessage = myfile.read().decode("utf-8")
    
encrypted = translateMessage(key, myMessage, 'encrypt')
'''
#########################################################################################
#   print(encrypted)

def main(command_line = None):

    parser = argparse.ArgumentParser()
    #parser.add_argument("--m", "mode", help="specify the mode e/d (encrypt/decrypt)")
    subparsers = parser.add_subparsers(title='command', dest='command', help="mode help")

    encrypt_parser = subparsers.add_parser('encrypt' , help='encrypt help')
    encrypt_parser.add_argument("filepath", help="specify path of the plaintext file")
    encrypt_parser.add_argument("key", help="key to use for encryption")

    decrypt_parser = subparsers.add_parser('crack',help="crack help")
    decrypt_parser.add_argument("filepath", help="specify path of the ciphertext file")
    
    args = parser.parse_args(command_line)
   
    myMode = args.command # set to 'encrypt' or 'decrypt'
    if myMode == 'encrypt':
        key = args.key
        with open(args.filepath, "r") as myfile:
            myMessage = myfile.read().replace('\n', '')
        print(len(myMessage))
        translated = encryptMessage(key, myMessage).replace(" ", "")
        output = 'ciphertext'
        fop = open(output,'w')
        fop.write(translated)
        fop.close()

    elif myMode == 'crack':
        with open("ciphertext", "r") as myfile:
            encrypted = myfile.read().replace('\n', '')
        translated = ["" for f in range(10)]    
        txt = ""
        inTxt = encrypted
        for c in inTxt:
            if(c.isalpha()):
                txt += c
        txt = txt.lower()
        x = 0
        for i in range(10,0,-1):
            cnt = 0
            j = 0
            for c in txt:
                num = LETTERS.find(c)
                num = (num - j)%26
                translated[x] +=  LETTERS[num]
                cnt += 1
                if(cnt == i):
                    j += 1
                    cnt = 0
            x += 1
        key = printKey(translated)
        print("Key could be " + key.upper() +"\n")
        fop = open('output-plaintext','w')
        fop.write(translateMessage(key,encrypted,'decrypt'))
        fop.close()


#print(translateMessage(key,encrypted,'decrypt'))
if __name__ == '__main__':

    main()
