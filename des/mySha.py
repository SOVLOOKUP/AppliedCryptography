def PadMessage_09(string,m_num,pos):
	"数据填充函数"
	ascii=[]
	hexInfo=[]
	hexNum=hex(string.__len__()*8)[2:]
	while hexNum.__len__()<16:
		hexNum="0"+hexNum
	for i in range(0,string.__len__()):
		ascii.append(hex(ord(string[i])).split("0x")[1])
	
	ascii.append("80")
	for i in range(ascii.__len__(),64*m_num-8):
		ascii.append("00")
	for i in range(0,ascii.__len__(),4):
		hexInfo.append(ascii[i]+ascii[i+1]+ascii[i+2]+ascii[i+3])
	hexInfo.append(hexNum[0:8])
	hexInfo.append(hexNum[8:16])
	return hexInfo[pos*16:(pos+1)*16]
	
def SHADataExtend_09(w):
	"SHA拓展80函数"
	for i in range(16,80):
		num_1=int(w[i-3],16)
		num_2=int(w[i-8],16)
		num_3=int(w[i-14],16)
		num_4=int(w[i-16],16)
		temp=num_1^num_2^num_3^num_4
		tempStr=bin(temp).split("0b")[1]
		while tempStr.__len__()<32:
			tempStr="0"+tempStr
		tempStr=tempStr[1:]+tempStr[0]
		w[i]=hex(int(tempStr,2)).split("0x")[1]
		while  w[i].__len__()<8:
			w[i]="0"+w[i]
		
	return

def functoDeal512Bit(H,M_x):
	"处理512bit分块函数 M_x表示当前参与的某个512bit的分组，list类型"

	A=int(H[0],16)
	B=int(H[1],16)
	C=int(H[2],16)
	D=int(H[3],16)
	E=int(H[4],16)
	K=[int("5A827999",16),int("6ED9EBA1",16),int("8F1BBCDC",16),int("CA62C1D6",16)]
	def f1(B,C,D):
		"0-19轮"
		return (B&C)|((~B)&D)
	def f2(B,C,D):
		"20-39轮"
		return (B^C^D)
	def f3(B,C,D):
		"40-59轮"
		return ((B&C)|(B&D)|(C&D))
	def f4(B,C,D):
		"60-79轮"
		return (B^C^D)
	T=0
	mod232=int(4294967296)

	for t in range(0,20):
		A_rotl5=bin(A).split("0b")[1]
		while len(A_rotl5)<32:
			A_rotl5="0"+A_rotl5
		for time in range(0,5):
			A_rotl5=A_rotl5[1:]+A_rotl5[0]
		A_rotl5=int(A_rotl5,2)
		T=A_rotl5+f1(B, C, D)+E+int(M_x[t],16)+K[0]
		E=D
		D=C
		B_rotl30=bin(B).split("0b")[1]
		while len(B_rotl30)<32:
			B_rotl30="0"+B_rotl30
		for time in range(0,30):
			B_rotl30=B_rotl30[1:]+B_rotl30[0]
		B_rotl30=int(B_rotl30,2)
		C=B_rotl30
		B=A
		A=T&0xffffffff
		
	for t in range(20,40):
		
		A_rotl5=bin(A).split("0b")[1]
		while len(A_rotl5)<32:
			A_rotl5="0"+A_rotl5
		for time in range(0,5):
			A_rotl5=A_rotl5[1:]+A_rotl5[0]
		A_rotl5=int(A_rotl5,2)
		T=A_rotl5+f2(B, C, D)+E+int(M_x[t],16)+K[1]
		E=D
		D=C
		B_rotl30=bin(B).split("0b")[1]
		while len(B_rotl30)<32:
			B_rotl30="0"+B_rotl30
		for time in range(0,30):
			B_rotl30=B_rotl30[1:]+B_rotl30[0]
		B_rotl30=int(B_rotl30,2)
		C=B_rotl30
		B=A
		A=T&0xffffffff

	for t in range(40,60):
		
		A_rotl5=bin(A).split("0b")[1]
		while len(A_rotl5)<32:
			A_rotl5="0"+A_rotl5
		for time in range(0,5):
			A_rotl5=A_rotl5[1:]+A_rotl5[0]
		A_rotl5=int(A_rotl5,2)
		T=A_rotl5+f3(B, C, D)+E+int(M_x[t],16)+K[2]
		# T=T%mod232
		E=D
		D=C
		B_rotl30=bin(B).split("0b")[1]
		while len(B_rotl30)<32:
			B_rotl30="0"+B_rotl30
		for time in range(0,30):
			B_rotl30=B_rotl30[1:]+B_rotl30[0]
		B_rotl30=int(B_rotl30,2)
		C=B_rotl30
		B=A
		A=T&0xffffffff

	for t in range(60,80):
		
		A_rotl5=bin(A).split("0b")[1]
		while len(A_rotl5)<32:
			A_rotl5="0"+A_rotl5
		for time in range(0,5):
			A_rotl5=A_rotl5[1:]+A_rotl5[0]
		A_rotl5=int(A_rotl5,2)
		T=A_rotl5+f4(B, C, D)+E+int(M_x[t],16)+K[3]
		E=D
		D=C
		B_rotl30=bin(B).split("0b")[1]
		while len(B_rotl30)<32:
			B_rotl30="0"+B_rotl30
		for time in range(0,30):
			B_rotl30=B_rotl30[1:]+B_rotl30[0]
		B_rotl30=int(B_rotl30,2)
		C=B_rotl30
		B=A
		A=T&0xffffffff
	
	H[0]=str(hex((A+int(H[0],16))%mod232).split("0x")[1])
	H[1]=str(hex((B+int(H[1],16))%mod232).split("0x")[1])
	H[2]=str(hex((C+int(H[2],16))%mod232).split("0x")[1])
	H[3]=str(hex((D+int(H[3],16))%mod232).split("0x")[1])
	H[4]=str(hex((E+int(H[4],16))%mod232).split("0x")[1])


# if __name__ == '__main__':
		
	# 测试数据
	# string="abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"
	# string="2fsdfsddfsdfsdfretheroituerioturioesdjahjkgkjgjkgkjgkjiugijgjkgzkjvgsk;jvhsdkjhgak;jgjsf;015123009"
	# string="abc"
	# string=input("Please input data:")
	# string=input("请输入要获取摘要的内容：")
	# ascii=[]
	# M=[]#总块
	# H=["67452301","EFCDAB89","98BADCFE","10325476","C3D2E1F0"]


	# for i in range(0,string.__len__()):
	# 	ascii.append(hex(ord(string[i])).split("0x")[1])
	# # m_num表示最终有几个块
	# m_num=8*ascii.__len__()
	# m_num=m_num//448
	# m_num=m_num+1
	# print("m_num:",m_num)

	# for x in range(0,m_num):
	# 	M.append(PadMessage_09(string,m_num,x))
	# 	for i in range(16,80):
	# 		M[x].append("")
	# 	SHADataExtend_09(M[x])

	# for pos in range(0,M.__len__()):
	# 	functoDeal512Bit(H,M[pos])
	# print("与自带sha-1的算法结果比较")
	# for pos in range(0,5):
	# 	print(H[pos],end="")
	# print()
	# print(hashlib.sha1(string.encode("utf8")).hexdigest())