import sys
num=int(sys.argv[1])


if (num<0 or num>9999):
	print("alguno de los números no son enteros o positivos, inténtalo nuevamente")
	print("ejemplo de uso del script", "escribir_linear.py ","[primerEntero 9999]" "")
elif len(sys.argv)==2:
	numChar=str(num)
	sizeNum=len(numChar)
	for i in range(sizeNum):
		print("{:04d}".format(int(numChar[sizeNum-1-i])*10**i))
		

else:
	print("falta uno o los dos argumentos ")
	print("ejemplo de uso del script", "escribir_linear.py ","[9999]""")
