from mySha import *
import des
import hashlib
def DesEncoded(M,Key,Mode,ivString,debug=False):
	if Mode=="ECB":
		return des.desEncoded_ECB(M,Key,debug)
	elif Mode=="CFB":
		return des.desEncoded_Flush(M,Key,ivString,"CFB",debug)
	elif Mode=="OFB":
		return des.desEncoded_Flush(M,Key,ivString,"OFB",debug)
	else:
		return "Wrong Mode!"

def DesDecoded(C,Key,Mode,ivString,debug=False):
	if Mode=="ECB":
		return des.desDecoded_ECB(C,Key,debug)
	elif Mode=="CFB":
		return des.desDecoded_Flush(C,Key,ivString,"CFB",debug)
	elif Mode=="OFB":
		return des.desDecoded_Flush(C,Key,ivString,"OFB",debug)
	else:
		return "Wrong Mode!"

def desEcb():
	print("<=====================>")
	M=input("请输入要加密的数据")
	print("ECB 加密数据 ",M,"默认密钥01234567")
	# M="computeert"
	key="01234567"
	C1=DesEncoded(M,key,"ECB","",True)
	print("密文",hex(int(C1,2)).split("0x")[1])
	M1=DesDecoded(C1,key,"ECB","",True)
	print("解密得到",M1)	
def desCfb():
	print("<=====================>")
	M=input("请输入要加密的数据")
	print("CFB 加密数据 ",M," IV='qwerghui' 默认密钥 01234567")
	# M="zlbqsaldfe"
	key="01234567"
	C1=DesEncoded(M,key,"CFB","qwertyui",True)
	print("密文",hex(int(C1,2)).split("0x")[1])
	M1=DesDecoded(C1,key,"CFB","qwertyui",True)
	print("解密得到",M1)
def desOfb():
	print("<=====================>")
	M=input("请输入要加密的数据")
	print("OFB 加密数据 ",M," IV='qwerghui' 默认密钥01234567")
	# M="SADhhhhaaaaaFGHJK"
	key="01234567"
	C1=DesEncoded(M,key,"OFB","qwertyui",True)
	print("密文",hex(int(C1,2)).split("0x")[1])
	M1=DesDecoded(C1,key,"OFB","qwertyui",True)
	print("解密得到",M1)
def desEcb_3():
	print("<=====================>")
	print("3Des is time consuming,please wait...")
	print("3des ECB 加密数据 computer")
	M="computer"
	key1="01234567"
	key2="12345678"
	key3="23456789"
	C1=DesEncoded(M,key1,"ECB","")
	C2=DesEncoded(C1,key2,"ECB","")
	C3=DesEncoded(C2,key3,"ECB","")
	M3=DesDecoded(C3,key3,"ECB","")
	M2=DesDecoded(M3,key2,"ECB","")
	M1=DesDecoded(M2,key1,"ECB","")
	print("解密得到",M1)
def desCfb_3():
	print("<=====================>")
	print("3Des is time consuming,please wait...")
	print("3des CFB 加密数据 zlbqldfe IV='qwertyui'")
	M="zlbqldfe"
	key1="01234567"
	key2="12345678"
	key3="23456789"
	C1=DesEncoded(M,key1,"CFB","qwertyui")
	C2=DesEncoded(C1,key2,"CFB","qwertyui")
	C3=DesEncoded(C2,key3,"CFB","qwertyui")
	M3=DesDecoded(C3,key3,"CFB","qwertyui")
	M2=DesDecoded(M3,key2,"CFB","qwertyui")
	M1=DesDecoded(M2,key1,"CFB","qwertyui")
	print("解密得到",M1)
def desOfb_3():
	print("<=====================>")
	print("3Des is time consuming,please wait...")
	print("3des OFB 加密数据 SADFGHJK IV='qwertyui'")
	M="SADFGHJK"
	key1="01234567"
	key2="12345678"
	key3="23456789"
	C1=DesEncoded(M,key1,"OFB","qwertyui")
	C2=DesEncoded(C1,key2,"OFB","qwertyui")
	C3=DesEncoded(C2,key3,"OFB","qwertyui")
	M3=DesDecoded(C3,key3,"OFB","qwertyui")
	M2=DesDecoded(M3,key2,"OFB","qwertyui")
	M1=DesDecoded(M2,key1,"OFB","qwertyui")
	print("解密得到",M1)
def sha_1():
	print("<==================Sha-1 Block========================>")

	ascii=[]
	M=[]#总块
	H=["67452301","EFCDAB89","98BADCFE","10325476","C3D2E1F0"]
	string=input("Please input data:")
	for i in range(0,string.__len__()):
		ascii.append(hex(ord(string[i])).split("0x")[1])
	# m_num表示最终有几个块
	m_num=8*ascii.__len__()
	m_num=m_num//448
	m_num=m_num+1
	# print("m_num:",m_num)

	for x in range(0,m_num):
		M.append(PadMessage_09(string,m_num,x))
		for i in range(16,80):
			M[x].append("")
		print("处理第",x+1,"分组")
		SHADataExtend_09(M[x])

		print("扩充结果：")
		for i in range(1,81):
			print(M[x][i-1],end="   ")
			if i%5==0:
				print()
	for pos in range(0,M.__len__()):
		functoDeal512Bit(H,M[pos])
		print("计算第",pos+1,"分组后H为",H)
	print("与自带sha-1的算法结果比较")
	print("计算SHA-1结果为 ",end="")
	for pos in range(0,5):
		print(H[pos],end="")
	print()
	print("自带SHA-1结果为",hashlib.sha1(string.encode("utf8")).hexdigest())

while 1:
	print("<==========Menu===========>")
	print("1、des-ecb")
	print("2、des-ofb")
	print("3、des-cfb")
	print("4、3des-ecb")
	print("5、3des-ofb")
	print("6、3des-cfb")
	print("7、sha-1")
	option=input("Please input your choice：")
	option=int(option,10)
	if option==1:
		desEcb()
		input("Input anything to continue...")
	elif option==2:
		desOfb()
		input("Input anything to continue...")
	elif option==3:
		desCfb()
		input("Input anything to continue...")
	elif option==4:
		desEcb_3()
		input("Input anything to continue...")
	elif option==5:
		desOfb_3()
		input("Input anything to continue...")
	elif option==6:
		desCfb_3()
		input("Input anything to continue...")
	elif option==7:
		sha_1()
		input("Input anything to continue...")
	else:
		print("wrong input!")




