import random
import time
#global variable
zeroNum=0#记录补0个数
keysRecord=[]#记录每组子秘钥
#主要变换函数
def F_func(rightPart,presentKey):
	"F函数"
	E_box=[
	32,1,2,3,4,5,
	4,5,6,7,8,9,
	8,9,10,11,12,13,
	12,13,14,15,16,17,
	16,17,18,19,20,21,
	20,21,22,23,24,25,
	24,25,26,27,28,29,
	28,29,30,31,32,1
	]
	S_box1=[
	[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
	[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
	[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
	[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
	]

	S_box2=[
	[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
	[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
	[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
	[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
	]
	S_box3=[
	[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
	[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
	[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
	[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
	]
	S_box4=[
	[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
	[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
	[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
	[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
	]
	S_box5=[
	[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
	[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
	[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
	[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
	]
	S_box6=[
	[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
	[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
	[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
	[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
	]
	S_box7=[
	[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
	[13,0,11,7,4,9,1,10,10,3,5,12,2,15,8,6],
	[1,4,11,13,12,3,7,14,14,15,6,8,0,5,9,2],
	[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
	]
	S_box8=[
	[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
	[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
	[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
	[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
	]
	Sbox_List=[S_box1,S_box2,S_box3,S_box4,S_box5,S_box6,S_box7,S_box8]
	P_box=[
	16,7,20,21,
	29,12,28,17,
	1,15,23,26,
	5,18,31,10,
	2,8,24,14,
	32,27,3,9,
	19,13,30,6,
	22,11,4,25
	]
	after_E=""
	print("======E盒拓展 start ======")
	print("输入：",hex(int(rightPart,2)))
	for x in range(0,48):
		after_E+=rightPart[E_box[x]-1]
	print("输出：",hex(int(after_E,2)))
	print("======E盒拓展 end ======\n")
	xor_1=int(after_E,2)
	xor_2=int(presentKey,2)
	rst_xor=str(bin(xor_1^xor_2).split("0b")[1])
	print("======S盒压缩 start ======")
	print("输入：",hex(int(rst_xor,2)))
	while rst_xor.__len__()<48:
		rst_xor="0"+rst_xor
	dataBySbox=[
	rst_xor[0:6],rst_xor[6:12],
	rst_xor[12:18],rst_xor[18:24],
	rst_xor[24:30],rst_xor[30:36],
	rst_xor[36:42],rst_xor[42:48]
	]
	Line=""
	Column=""
	for x in range(0,8):
		Line=dataBySbox[x][0]+dataBySbox[x][5]
		Line=int(Line,2)
		Column=dataBySbox[x][1:5]
		Column=int(Column,2)
		dataBySbox[x]=(Sbox_List[x])[Line][Column]#十进制值
	for x in range(0,8):
		dataBySbox[x]=str(bin(dataBySbox[x]).split("0b")[1])
		while dataBySbox[x].__len__()<4:
			dataBySbox[x]="0"+dataBySbox[x]
	#到目前为止Sbox压缩完成 数据在dataBySbox里
	after_Sbox=""
	for x in range(0,8):
		after_Sbox+=dataBySbox[x]
	print("输出：",hex(int(after_Sbox,2)))
	print("======S盒压缩 end ======\n")

	print("======P盒置换 start ======")
	print("输入：",hex(int(after_Sbox,2)))
	after_P=""
	for x in range(0,32):
		after_P+=after_Sbox[P_box[x]-1]
	print("输出：",hex(int(after_P,2)))
	print("======P盒置换 end ======\n")
	return after_P

def init_Ip(m):
	"初始IP置换"
	ipTable=[
	58,50,42,34,26,18,10,2,
	60,52,44,36,28,20,12,4,
	62,54,46,38,30,22,14,6,
	64,56,48,40,32,24,16,8,
	57,49,41,33,25,17,9,1,
	59,51,43,35,27,19,11,3,
	61,53,45,37,29,21,13,5,
	63,55,47,39,31,23,15,7
	]
	fin=""
	if m.__len__()!=64:
		print("输入信息m长度有误。errorPos:init_Ip()")
		return 
	else:
		for x in range(0,64):
			fin+=m[ipTable[x]-1]
	print("======IP初始置换 start ======")
	print("输入：",hex(int(m)),"\n结果：",hex(int(fin)))
	print("======IP初始置换 end ======\n")

	return fin
	
def inv_Ip(m):
	invIpTable=[
	40,8,48,16,56,24,64,32,
	39,7,47,15,55,23,63,31,
	38,6,46,14,54,22,62,30,
	37,5,45,13,53,21,61,29,
	36,4,44,12,52,20,60,28,
	35,3,43,11,51,19,59,27,
	34,2,42,10,50,18,58,26,
	33,1,41,9,49,17,57,25
	]
	fin=""
	for x in range (0,64):
		fin+=m[invIpTable[x]-1]
	print("======IP逆置换 start ======")
	print("输入：",hex(int(m,2)),"\n结果：",hex(int(fin,2)))
	print("======IP逆置换 end ======\n")
	return fin

def PC1(initKey):
	dealtKey=""
	PC1_Table=[
	57,49,41,33,25,17,9,
	1,58,50,42,34,26,18,
	10,2,59,51,43,35,27,
	19,11,3,60,52,44,36,
	63,55,47,39,31,33,15,
	7,62,54,46,38,30,22,
	14,6,61,53,45,37,29,
	21,13,5,28,20,12,4
	]
	for x in range(0,56):
		dealtKey+=initKey[PC1_Table[x]-1]
	print("======PC1 start ======")
	print("输入：",hex(int(initKey,2)),"\n结果：",hex(int(dealtKey,2)))
	print("======PC1 end ======\n")
	return dealtKey

def PC2(key):
	dealtKey=""
	PC2_Table=[
	14,17,11,24,1,5,
	3,28,15,6,21,10,
	23,19,12,4,26,8,
	16,7,27,20,13,2,
	41,52,31,37,47,55,
	30,40,51,45,33,48,
	44,49,39,56,34,53,
	46,42,50,36,29,32
	]
	for x in range(0,48):
		dealtKey+=key[PC2_Table[x]-1]
	print("======PC2 start ======")
	print("输入：",hex(int(key,2)),"\n结果：",hex(int(dealtKey,2)))
	print("======PC2 end ======\n")
	return dealtKey
#tools
def stringToAscii(string):
	"返回字符串用二进制ascii码的表示值"
	Rst=""
	for x in range(0,string.__len__()):
		Rst+=complete8bits(bin(ord(string[x])).split("0b")[1])
	print("======stringToAscii start ======")
	print("输入：",string,"\n输出：",Rst)
	print("======stringToAscii end ======\n")
	
	return Rst

def AsciiToString(m):
	Message=""
	for x in range(0,m.__len__()//8):
		Message+=chr(int(m[x*8:(x+1)*8],2))
	print("======AsciiToString start ======")
	print("输入：",m,"\n输出：",Message)
	print("======AsciiToString end ======\n")
	return Message

def ivInit(ivString):
	IV=""
	randomWord=[]
	for i in range(0,ivString.__len__()):
		randomWord.append(stringToAscii(ivString[i]))
	IV="".join(randomWord)
	
	return randomWord

def complete8bits(string):
	"补全为8位二进制数"
	while string.__len__()<8:
		string="0"+string
	return string
#KeyMode
def keyMode_ECB(seed):
	"ECB模式  固定秘钥加密 返回所有子秘钥的组"
	global keysRecord
	singlePart=[]
	for  x in range(1,17):
		if x==1:
			keyNow=keyGenernate(seed,x).split(",")[0]#本轮秘钥48bit
			keyNow_=keyGenernate(seed,x).split(",")[1]#本轮秘钥在PC2之前的值56bit
		else:	
			keyNow=keyGenernate(keyNow_,x).split(",")[0]
			keyNow_=keyGenernate(keyNow_,x).split(",")[1]
		singlePart.append(keyNow)
	keysRecord.append(singlePart)
	return singlePart

def keyMode_OFB(IV,O):
	"OFB模式 O(OUTPUT)用来更新IV值"
	for x in range(1,IV.__len__()):
		IV[x-1]=IV[x]
		if x==IV.__len__()-1:
			IV[x]=O

def keyMode_CFB(IV,C):
	"CFB模式  C(CIPHERTEXT)用来更新IV值"
	for x in range(1,IV.__len__()):
		IV[x-1]=IV[x]
		if x==IV.__len__()-1:
			IV[x]=C
	

def keyGenernate(KeySeed,roundTime):
	"子秘钥生成算法  每次调用时传入当前参与到F函数中的秘钥以及目前进行到的轮次"
	# 第一次传入的时候不是2进制ascii码，以后传入的都是二进制值不必调用stringToAscii()
	bitToShift=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
	if roundTime==1:
		seed=stringToAscii(KeySeed)
		seed=PC1(seed)
	else :
		seed=KeySeed
	key_L=seed[0:28]
	key_R=seed[28:56]
	key_L=key_L[bitToShift[roundTime-1]:]+key_L[:bitToShift[roundTime-1]]
	key_R=key_R[bitToShift[roundTime-1]:]+key_R[:bitToShift[roundTime-1]]
	key=key_L+key_R
	key=PC2(key)
	return key+","+key_L+key_R
#core Function
def desEncoded_ECB(M,keySeed,debug=False):
	"输入message  秘钥给出密文  K暂定为模式函数名（指定密码工作模式）"
	global zeroNum
	global keysRecord
	block_M=[]#加密前存放明文分组，加密后用密文替代该位置的明文分组
	M_ascii=stringToAscii(M)
	block_num=M_ascii.__len__()//64#取整

	if keySeed.__len__()!=8:
		print("秘钥长度有误，加密终止")
		return
	if M_ascii.__len__()/64>block_num:#有余数的话取整除法与带小数除法值不等
		block_num+=1#确定分组数

	for x in range(0,block_num):
		#每64bit分一组 进行分组工作
		block_M.append(M_ascii[64*x:64*(x+1)])
	if debug:
		print("明文分组后：",block_M)

	if block_M[block_num-1].__len__()<64:
		#开始补0
		zeroNum=0#指示补了多少个0
		while block_M[block_num-1].__len__()<56:
			block_M[block_num-1]+="0"
			zeroNum+=1
		zeroNum=bin(zeroNum).split("0b")[1]
		while zeroNum.__len__()<8:
			zeroNum="0"+zeroNum
		block_M[block_num-1]+=zeroNum
		zeroNum=int(zeroNum,2)
	#以上不足64位补0 最后8位指示补了多少个0
	else:
		#不需要补0的话就加一个64bit的“0”字串跟在后面
		block_M.append("0000000000000000000000000000000000000000000000000000000000000000")
		if debug:
			print("无需填充，补64bit'0'作为标识")
		zeroNum=0
	#encode core operation
	if debug:
		print("填充后分组：",block_M)

	for block_pos in range(0,block_num):
		binMesToDeal=init_Ip(block_M[block_pos])#每一轮中待处理的二进制字符串 
		keyNowPart=keyMode_ECB(keySeed)#每一分组都要实现自己的秘钥 目前分组所用的所有秘钥

		if debug:
			print("输入秘钥为：",keySeed)
		for roundTime in range(1,17):
			L=binMesToDeal[0:32]
			R=binMesToDeal[32:64]
			keyNow=keyNowPart[roundTime-1]

			if debug:
				print("目前为第",block_pos+1,"分组","第",roundTime,"轮")
				print("目前使用的子秘钥为：",hex(int(keyNow,2)).split("0x")[1])

			newL=R
			rst_F=F_func(R,keyNow)
			rst_F=int(rst_F,2)
			L=int(L,2)
			rst_xor_LF=L^rst_F
			rst_xor_LF=bin(rst_xor_LF).split("0b")[1]
			while rst_xor_LF.__len__()<32:
				rst_xor_LF="0"+rst_xor_LF
			#将异或结果补全到32位二进制字符串
			newR=rst_xor_LF
			binMesToDeal=newL+newR

			if debug:
				print("本轮运算结果为：",hex(int(binMesToDeal,2)).split("0x")[1])
			
		#16轮结束
		L=binMesToDeal[0:32]
		R=binMesToDeal[32:64]
		binMesToDeal=R+L
		block_M[block_pos]=inv_Ip(binMesToDeal)
		if debug:
			print("分组",block_pos+1,"处理结束")
		#一整个分组加密结束
	C=""
	for x in range(0,block_M.__len__()):
		C+=block_M[x]
	return C

def desDecoded_ECB(C,keySeed,debug=False):
	"输入密文字符串  秘钥还原message K为模式函数名"
	global zeroNum
	if C.__len__()/64!=C.__len__()//64:
		print("密文输入长度有误！")
		return
	#确定分组数
	block_C=[]
	block_num=C.__len__()//64

	if debug:
		print("输入密文为：",hex(int(C,2)).split("0x")[1])

	#构造分组
	for x in range(0,block_num):
		block_C.append(C[x*64:(x+1)*64])
	for block_pos in range(0,block_num):
		binCToDeal=init_Ip(block_C[block_pos])
		keyNowPart=keyMode_ECB(keySeed)#每一分组都要实现自己的秘钥 目前分组所用的所有秘钥
		if block_C[block_pos]=="0000000000000000000000000000000000000000000000000000000000000000":
			if debug:
				print("该分组为无填充标识分组，不做处理，直接丢弃")
			break
		for roundTime in range(1,17):
			L=binCToDeal[0:32]
			R=binCToDeal[32:64]
			keyNow=keyNowPart[16-roundTime]

			if debug:
				print("目前为第",block_pos+1,"分组","第",roundTime,"轮")
				print("目前使用的子秘钥为：",hex(int(keyNow,2)).split("0x")[1])

			newL=R
			rst_F=F_func(R,keyNow)
			rst_F=int(rst_F,2)
			L=int(L,2)
			rst_xor_LF=L^rst_F
			rst_xor_LF=bin(rst_xor_LF).split("0b")[1]
			while rst_xor_LF.__len__()<32:
				rst_xor_LF="0"+rst_xor_LF
			#将异或结果补全到32位二进制字符串
			newR=rst_xor_LF
			binCToDeal=newL+newR
			
			if debug:
				print("本轮运算结果为：",hex(int(binCToDeal,2)).split("0x")[1])

		#16轮结束
		L=binCToDeal[0:32]
		R=binCToDeal[32:64]
		binCToDeal=R+L
		block_C[block_pos]=inv_Ip(binCToDeal)
		if debug:
			print("分组",block_pos+1,"处理结束")
	if debug:
		print("处理填充位")

	if block_C[block_C.__len__()-1]=="0000000000000000000000000000000000000000000000000000000000000000":
		del block_C[block_C.__len__()-1]
		zeroNum=0
		if debug:
			print("丢弃全0标识位")
	else:
		binLenth=(block_C[block_C.__len__()-1])[56:64]
		zeroNum=int(binLenth,2)
	if zeroNum!=0:
		block_C[block_C.__len__()-1]=(block_C[block_C.__len__()-1])[0:56-zeroNum]
		if debug:
			print("丢弃填充位")
	block=""
	for x in range(0,block_C.__len__()):
		block+=block_C[x]
	block_C=block
	codedM=""
	for x in range(0,block_C.__len__()):
		codedM+=block_C[x]
	return AsciiToString(codedM)

def desEncoded_Flush(M,Key,ivString,Mode,debug=False):
	#输入秘钥加密IV IV取出高8位加密一个字节
	IV=ivInit(ivString)
	M_ascii=stringToAscii(M)
	C=""
	for x in range(0,M.__len__()):
		ivS="".join(IV)
		encodedIV=desEncoded_ECB(ivS,Key)
		rst_xor=int(encodedIV[0:8],2)^int(M_ascii[x*8:(x+1)*8],2)
		rst_xor=bin(rst_xor).split("0b")[1]
		while rst_xor.__len__()<8:
			rst_xor="0"+rst_xor
		C+=rst_xor
		if debug:
			print("当前加密第",x+1,"个字节，该字节加密结果为",rst_xor)
		if Mode=="CFB":	
			keyMode_CFB(IV,rst_xor)
			if debug:
				print("反馈内容为",rst_xor)
				print("反馈后IV结果为",IV)
		elif Mode=="OFB":
			keyMode_OFB(IV,encodedIV[0:8])
			if debug:
				print("反馈内容为",encodedIV[0:8])
				print("反馈后IV结果为",IV)
	return C
def desDecoded_Flush(C,Key,ivString,Mode,debug=False):
	IV=ivInit(ivString)
	M=""
	cList=[]
	for x in range(0,C.__len__()//8):
		cList.append(C[x*8:(x+1)*8])
	for x in range(0,cList.__len__()):
		ivS="".join(IV)
		encodedIV=desEncoded_ECB(ivS,Key)
		rst_xor=int(encodedIV[0:8],2)^int(cList[x],2)
		rst_xor=bin(rst_xor).split("0b")[1]
		while rst_xor.__len__()<8:
			rst_xor="0"+rst_xor
		M+=rst_xor
		if debug:
			print("当前解密第",x+1,"个字节，该字节解密结果为",rst_xor)
		if Mode=="CFB":	
			keyMode_CFB(IV,cList[x])
			if debug:
				print("反馈内容为",cList[x])
				print("反馈后IV结果为",IV)
		elif Mode=="OFB":
			keyMode_OFB(IV,encodedIV[0:8])
			if debug:
				print("反馈内容为",encodedIV[0:8])
				print("反馈后IV结果为",IV)
	return AsciiToString(M)

#消息第一个字符的ascii10进制值作为随机数种子

#思路：每组加密前算出所有的子秘钥 zeroNum,keysRecord作为全局变量 加密解密时需要引用
#独立成模块做包导入其他文件


if __name__ == '__main__':
	mes=input("Please input your messages：")
	print("ECB 加密数据 ",mes,"默认密钥01234567")
	key="01234567"
	print("...开始加密过程")
	time.sleep(3)
	C=desEncoded_ECB(mes,key,False)
	print("密文",hex(int(C,2)).split("0x")[1])
	print("...开始解密过程")
	time.sleep(3)
	M=desDecoded_ECB(C,key,False)
	print("解密得到：",M)
