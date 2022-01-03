# TRIANGLES
print('Square')
num=int(input('entre range:'))
for row in range(num): #directly, print('* '*num)
    for col in range(num):
        print('* ',end='')
    print()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('Right Triangle on LHS')
a=int(input('entre range:'))
for row in range(1,a+1): # if I put 0 or a in range then first no. would be 0 and it won't work
    print('* '*row) #i times the print of star 1 in 1st line then 2 in 2nd line
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('Pyramid')
b=int(input('entre range:'))
for row in range(1,b+1):
    print(' '*(b-row)+'* '*row) # same but we use space for LHS (b-i) is formula 'coz if b=5 then 5-i (in first line) would be b-i=5-1=4 col block & then 5th would be *
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('Right Triangle from RHS')
c=int(input('entre range:'))
for row in range(1,c+1): # gaps change the above code from pyramid to RHS
    print('  '*(c-row)+'* '*row) # same but we use space for LHS (c-i) is formula 'coz if c=5 then 5-i (in first line) would be c-i=5-1=4 col block & then 5th would be *
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('Diamond')
d=int(input('entre range:'))
for i in range(1,d+1): #upper part of diamond
    print(' '*(d-i)+'* '*i)
for i in range(d-1,0,-1): #reverse triangle so reverse range,but from d-1 so 2 lines don't look same
    print(' '*(d-i)+'* '*i) #lower part of diamond
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('Reverse Right Triangle on LHS')
e=int(input('entre range:'))
for i in range(e,0,-1): #reverse range
    print(''*(e-1)+'* '*i) #1 in triangle or print('*'*i)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('Reverse Pyramid')
f=int(input('entre range:'))
for i in range(f,0,-1): #reverse range 
    print(' '*(f-i)+'* '*i) #i in pyramid
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('Reverse Triangle on RHS')
g=int(input('entre range:'))
for i in range(g,0,-1): #reverse range 
    print('  '*(g-i)+'* '*i) #i in pyramid and adding one more space in space
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('Arrow pointing RIGHT')
h=int(input('entre range:'))
for i in range(1,h+1): #upper part of arrow
    print('* '*i)
for i in range(h-1,0,-1): #reverse triangle so reverse range,but from h-1 so 2 lines don't look same
    print('* '*i) #lower part of arrow
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('Arrow pointing LEFT')
j=int(input('entre range:'))
for i in range(1,j+1): #upper part of arrow
    print('  '*(j-i)+'* '*i)
for i in range(j-1,0,-1): #reverse triangle so reverse range,but from j-1 so 2 lines don't look same
    print('  '*(j-i)+'* '*i) #lower part of arrow
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('Number Triangle')
n=int(input('entre a value:'))
for row in range (1,n+1):
    for col in range(1,row+1):
        print(col,end=' ')
    print()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('Number Triangle ,but with each no. of line no. of no. are printed as no.')
n=int(input('entre a value:'))
for row in range (1,n+1):
    for col in range (1,row+1):
        print(row,end=' ')
    print()
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('Number Pyramid')
n=int(input('entre no. of rows'))
for i in range(1,n+1):
    for j in range(1,num-i+1):
        print(' ',end='')
    for j in range(i,0,-1):
        print(j,end='')
    for j in range(2,i+1):
        print(j,end='')
    print('')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('reverse no. triangle')
n=int(input('entre a value:'))
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(col,end=' ')
    print()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('reverse no. tianlgle with no. in lines')
n=int(input('entre a value:'))
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(row,end=' ')
    print()
