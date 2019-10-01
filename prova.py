'''set1={"a","b","c"}
set2={1,2,3}

set3=set1.union(set2)
print(set3)'''

'''def saluto(nome):
	print("Ciao"+nome+"!")

nome=input("Come ti chiami?")
saluto(nome)
'''

'''def sommatoria(nome,*elementi):
	print("Lista: ",nome)
	print("Numero elementi: ",len(elementi))
	somma=sum(elementi)
	print("Somma: ", somma)


sommatoria("X",1,1,2,3,5,8,13,21)'''

'''def printList(L):
	if L:
		print (L[0])
		printList(L[1:])

4
S=["saa","dsds","ds"]
printList(S)'''



'''def fattoriale(n):
	if n==1:
		return 1
	else: 
		return n - fattoriale(n-1)

print(fattoriale(4))'''
'''import time
def countdown(N):
	if N == 0:
		return 0
	else:
		print(N)
		time.sleep(0.02)
		return  countdown(N-1) 


a=int(input("Numero: "))
print(countdown(a))'''

'''def pali(s):
	t=len(s)
	if (t==0) or (t==1):
		print("palindroma")
		return 
	elif s[0]!=s[t-1]:
		print(" no  palindroma")
		return 
	elif s[0]==s[t-1]:
		return pali(s[0+1:t-1])


a=str(input("dammi la stringa: "))

pali(a.replace(" ", ""))'''


'''def numeri(a,b,c):
	if a >= b and a >= c:
		return a
	if b >= a and b >= c:
		return b
	if c >= a and c >= b:
		return c
	

a=int(input("n1 "))
b=int(input("n2 "))
c=int(input("n3 "))'''


'''lista=[[1,2,3],[13,11,9],[11,15,13],[1,1,1],[0,0,0]]

for y in range(0,len(lista)):
	
	#for x in lista[y]:
		#print(x)
		#print(lista[y][x])
		print("il numero più grande è",numeri(lista[y][0],lista[y][1],lista[y][2]))'''


'''def voc(a):
	vocale_set = {'a','e','i','o','u','A','E','I','U','O'}
	if a in vocale_set:
		return print("è una vocale")
	else:
		return print("non è una vocale")
	

s=input("inserisci")
voc(s)'''

'''def ariocontra(s):
	s2=""
	l=len(s)
	for x in range(l-1,-1,-1):
		s2=s2+s[x]
	return print(s2)
	#return s[::-1]



z=input("inserisci: ")

ariocontra(z)'''
def crip(s):
	cifrario = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
            'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
            'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
            'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
            'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
            'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
            'W':'J', 'X':'K', 'Y':'L', 'Z':'M',' ':' '}
	s2=""
	l=len(s)
	for x in range(0,l,):
		if (s[x]) in cifrario:
			s1=(cifrario[s[x]])
			s2=s2 +s1		
	return s2	


x = input("inserisci parola: ")
x.replace(" ","")
print("Parola Criptata: ",crip(x))