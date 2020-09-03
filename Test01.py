n=int(input('enter number of students:'))
s={}
for i in range(n):
 name=input('Enter name of student:')
 marks=int(input('enter marks of students:'))
 s[name]=marks
print( 'Name \t\t\t\t Marks')
for k,v in s.items():
 print('{}  \t\t\t {}'.format(k,v))