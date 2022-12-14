print('Digite dois numero:')
x = int(input('primeiro numero: '))
y = int(input('Segundo numero: '))

while x != y:
   if x < y:
     print('Crescente')
   else:
     print('Decrescente')

   print('Digite outros dois numero:')
   x = int(input())
   y = int(input())
