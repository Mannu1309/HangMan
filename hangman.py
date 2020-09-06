

'''H A N G M A N'''

    
wor='MANISH'
l=len(wor)
G=[]
for i in range(l):
    if wor[i]==' ':
        G.append(' ')
    else:
        G.append('-')
    
print('The Word(s) is/are :-\n'+str(G))
print('Point to be noted : You only get '+ str(2*l) +' tries')

for i in range(2*l):
    print('\nThis is your '+str(i+1)+' Try')
    x=input('Guess the Letter : '); str(x)
    if wor.find(x)!=-1:
        print('You Guessed it Right')
       # G[wor.find(x)]=wor[wor.find(x)]
        for i in range(l):
            if wor[i]==x:
                G[i]=wor[i] 
        print(G)
    else:
        print('SORRY! Its Wrong')
    if i==((2*l)-1):
        print('\nYour Chances are over')
        print('\nYOU LOST!!!')
    
    if '-' not in G:
        print('\n***CONGRATULATIONS! YOU WON***')
        break
    
    
    
