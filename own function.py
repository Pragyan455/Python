def intro(name):
    print('Hello '+ name )
    print('how are you doing')

print('enter total number contestants ')
no=input()
for i in range(int(no)):
    print('please enter your name')
    n=input()
    intro(n)
    
