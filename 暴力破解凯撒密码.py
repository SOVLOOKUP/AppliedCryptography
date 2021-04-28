messgae = 'merkwqeikdycudtqqd'
messgae = messgae.upper()
nums = range(1,27)
mode = 'decrypt'    #模式是加密而非解密（decrypt）
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    #常量要大写
translated = ''
for key in nums:
    translated =''    
    for symbol in messgae:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)    #find()返回的是该字符在字符串中的位置
            if mode == 'encrypt':#判断当前是加密还是解密过程
                num = num+key
            elif mode == 'decrypt':
                num = num-key
            if num > len(LETTERS):#当处理后的数字脱离26个字母的数字范围后的处理
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]#空字符串一个个加上翻译后得到的字符
        else:
            #如果要翻译的字符不在26个大写字母的范围内
            translated =translated + symbol
    print(key ,translated.lower())
