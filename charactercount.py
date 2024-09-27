import pprint
print('enter a sentence')
st=input()
count={}
for i in st.ucase:
    count.setdefault(i,0)
    count[i]=count[i]+1

print('total no of letters used in the sentence is ')
pprint.pprint(count)
    
