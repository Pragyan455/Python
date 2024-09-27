import random
a={'Top-L':' ','Top-M':' ','Top-R':' ','Mid-L':' ','Mid-M':' ','Mid-R':' ','Low-L':' ','Low-M':' ','Low-R':' ',}
def board():
    print(a['Top-L'] +'|'+ a['Top-M']+'|'+a['Top-R'])
    print('-----')
    print(a['Mid-L'] +'|'+ a['Mid-M']+'|'+a['Mid-R'])
    print('-----')
    print(a['Low-L'] +'|'+ a['Low-M']+'|'+a['Low-R'])
def user():
    print('Congratulations!!!, You Won')
def ai():
    print('Computer won try again next time')

for i in range (5):
    
    board()
  
    if a['Top-L']=='x' and a['Top-M']=='x' and a['Top-R']=='x':
         user()
         break
    elif a['Top-L']=='O' and a['Top-M']=='O' and a['Top-R']=='O':
         ai()
         break
    elif a['Mid-L']=='x' and a['Mid-M']=='x' and a['Mid-R']=='x':
         user()
         break
    elif a['Mid-L']=='O' and a['Mid-M']=='O' and a['Mid-R']=='O':
         ai()
         break
    elif a['Low-L']=='x' and a['Low-M']=='x' and a['Low-R']=='x':
         user()
         break
    elif a['Low-L']=='O' and a['Low-M']=='O' and a['Low-R']=='O':
         ai()
         break
    elif a['Top-L']=='x' and a['Mid-M']=='x' and a['Low-R']=='x':
         user()
         break
    elif a['Top-L']=='O' and a['Mid-M']=='O' and a['Low-R']=='O':
         ai()
         break
    elif a['Low-L']=='x' and a['Mid-M']=='x' and a['Top-R']=='x':
         user()
         break
    elif a['Low-L']=='O' and a['Mid-M']=='O' and a['Top-R']=='O':
         ai()
         break
    elif a['Top-L']=='x' and a['Mid-L']=='x' and a['Low-L']=='x':
         user()
         break
    elif a['Top-L']=='O' and a['Mid-L']=='O' and a['Low-L']=='O':
         ai()
         break
    elif a['Top-M']=='x' and a['Mid-M']=='x' and a['Low-M']=='x':
         user()
         break
    elif a['Top-M']=='O' and a['Mid-M']=='O' and a['Low-M']=='O':
         ai()
         break
    elif a['Top-R']=='x' and a['Mid-R']=='x' and a['Low-R']=='x':
         user()
         break
    elif a['Top-R']=='O' and a['Mid-R']=='O' and a['Low-R']=='O':
         ai()
         break   
   
        
    while True:
     comp=random.randint(1,9)
     if comp==1 and a['Top-L']==' ':
        a['Top-L']='O'
        break
     elif comp==2 and a['Top-M']==' ':
        a['Top-M']='O'
        break
     elif comp==3 and a['Top-R']==' ':
        a['Top-R']='O'
        break
     elif comp==4 and a['Mid-L']==' ':
        a['Mid-L']='O'
        break
     elif comp==5 and a['Mid-M']==' ':
        a['Mid-M']='O'
        break
     elif comp==6 and a['Mid-R']==' ':
        a['Mid-R']='O'
        break
     elif comp==7 and a['Low-L']==' ':
        a['Low-L']='O'
        break
     elif comp==8 and a['Low-M']==' ':
        a['Low-M']='O'
        break
     elif comp==9 and a['Low-R']==' ':
        a['Low-R']='O'
        break
     continue
    board()
    
    print('please enter your move;Top-L;Top-M;Top-R;Mid-L;Mid-M;Mid-R;Low-L;Low-M;Low-R;')
    m=input()
    a[m]='x'

    
    

    print()
     
     

