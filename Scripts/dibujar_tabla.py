import sys

num1=int(sys.argv[1])
num2=int(sys.argv[2])

if (num1>9 or num1<1 or num2<1 or num2>9):
	print("alguno de los números no son enteros o positivos, inténtalo nuevamente")
	print("ejemplo de uso del script", "escribir_linear.py ","[primerEntero 1-9]", "[segundoEntero 1 -9]""")
elif len(sys.argv)==3:
	for i in range(num1):
		print()
		for h in range(num2):
			print("*",end='')

else:
	print("falta uno o los dos argumentos ")
	print("ejemplo de uso del script", "escribir_linear.py ","primerEntero", "segundoEntero""")
