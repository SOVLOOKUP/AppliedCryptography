def prepare(text, key):
    text = "".join(text.split())  # to remove white spaces
    alphabetAndKey = key + list("abcdefghiklmnonpqrstuvwxyz")
    # create a 1d matrix that contains the key and alphabets
    # with no redundant letters
    oneDmatrix = []
    for x in alphabetAndKey:
        if x not in oneDmatrix:
            if x == "i" or x == "j":
                x = "i"
            oneDmatrix.append(x)
    #print(oneDmatrix)

    # transform to two dimensional matrix, with each row 5 elements
    n = 5
    # global twoDmatrix
    twoDmatrix = [oneDmatrix[i:i + 5] for i in range(0, len(oneDmatrix), n)]
    #print(twoDmatrix)

    # separate the plaintext into blocks of size 2:
    n = 2
    # global plain
    plain = []
    i = 0
    while (i < len(text)):
        if i + 1 == len(text):
            plain.append([text[i], 'x'])
            i += 1
        elif text[i] == text[i + 1]:
            plain.append([text[i], 'x'])
            i += 1
        else:
            plain.append(list(text[i:i + n]))
            i += 2
    #print(plain)
    print(twoDmatrix)
    return twoDmatrix, plain

def playfair(operation:str):
    key = list(input("Enter you key: "))
    result = ""
    if operation == '加密':
        text = input("Enter your PlainText: ").strip()
        text = "".join(text.split())  # to remove white spaces
        # create the matrix and split the plain text into blocks
        twoDmatrix, plain = prepare(text, key) # creates two global variables: twoDmatrix, and plain
        # encipher the text
        for i in range(len(plain)):
            for j in range(len(twoDmatrix)):
                if twoDmatrix[j].count(plain[i][0]) == 1:
                    row1 = j
                    col1 = twoDmatrix[j].index(plain[i][0])
                if twoDmatrix[j].count(plain[i][1]) == 1:
                    row2 = j
                    col2 = twoDmatrix[j].index(plain[i][1])
            if row1 == row2: # shift left
                result += twoDmatrix[row1][(col1+1)%5] + twoDmatrix[row2][(col2+1)%5]
            elif col1 == col2: # shift down
                result += twoDmatrix[(row1+1)%5][col1] + twoDmatrix[(row2+1)%5][col2]
            else:
                result += twoDmatrix[row1][col2] + twoDmatrix[row2][col1]
    elif operation == '解密':
        text = input("Enter your CipherText: ").strip()
        twoDmatrix, plain = prepare(text, key)
        # decipher the text
        for i in range(len(plain)):
            for j in range(len(twoDmatrix)):
                if twoDmatrix[j].count(plain[i][0]) == 1:
                    row1 = j
                    col1 = twoDmatrix[j].index(plain[i][0])
                if twoDmatrix[j].count(plain[i][1]) == 1:
                    row2 = j
                    col2 = twoDmatrix[j].index(plain[i][1])
            if row1 == row2: # shift right
                result += twoDmatrix[row1][col1-1] + twoDmatrix[row2][col2-1]
            elif col1 == col2: # shift up
                result += twoDmatrix[row1-1][col1] + twoDmatrix[row2-1][col2]
            else:
                result += twoDmatrix[row1][col2] + twoDmatrix[row2][col1]
    else:
        print("Invalid input")
    print(result)


class Vigenere:

    def __init__(self, key: str):
        self.key = key
        self.ASCII = 'abcdefghijklmnopqrstuvwxyz'
        self.keylen = len(
            key
        )

    def encode(self, plaintext: str) -> str:
        plaintext = plaintext.replace(" ", "")
        keylen, ptlen = self.keylen, len(plaintext)

        ciphertext, i = '', 0

        while i < ptlen:

            j = i % keylen

            k = self.ASCII.index(self.key[j])

            m = self.ASCII.index(plaintext[i])

            ciphertext += self.ASCII[(m+k) % 26]

            i += 1

        return ciphertext

    def decode(self, ciphertext: str) -> str:
        ciphertext = ciphertext.replace(" ", "")
        keylen, ctlen = self.keylen, len(ciphertext)

        plaintext, i = '', 0

        while i < ctlen:

            j = i % keylen

            k = self.ASCII.index(self.key[j])

            m = self.ASCII.index(ciphertext[i])

            if m < k:

                m += 26

            plaintext += self.ASCII[m-k]

            i += 1

        return plaintext

def askWithKey() -> str:
    return input("你的密钥🔐️是？")

def default(operator:str, encode , decode):
    if operator == "加密":
        a = encode(input("需要加密的字符串:"))
        print("\033[1;32m加密结果:\033[0m")
        print(a)
    elif operator == "解密":
        a = decode(input("需要解密的字符串:"))
        print("\033[1;32m解密结果:\033[0m")
        print(a)

def playfairFunc(operator:str):
    playfair(operator)

def vigenereFunc(operator:str):
    v = Vigenere(askWithKey())
    default(operator, v.encode, v.decode)

CipherDict = {
    "playfair":playfairFunc,
    "vigenere":vigenereFunc
    }

OperatorList = ["加密","解密"]

def main():
    for k in CipherDict.keys():
        print(k)
    
    name = input("\033[1;34m请选择以上⬆️加密算法的一种：️\033[0m")

    for k in CipherDict.keys():
        if k.startswith(name):
            print(f"\033[1;34m你选择的是： \033[1;32m{k}\033[0m \033[1;34m算法\033[0m")
            i = 0
            for o in OperatorList:
                print(i,o)
                i += 1
            index = input("\033[1;34m请选择以上⬆️操作的一种,输入序号：️\033[0m")
            CipherDict[k](OperatorList[int(index)])
            return
    
    print("\033[1;31m输入不合法！\n\033[0m")
    main()

main()

