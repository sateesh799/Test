Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='22-08-2020'
>>> l=s.split('-')
>>> print(l)
['22', '08', '2020']
>>> l=['one','two','three','four']
>>> s.join(l)
'one22-08-2020two22-08-2020three22-08-2020four'
>>> a=['one','two','three','four']
>>> j=a.join()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    j=a.join()
AttributeError: 'list' object has no attribute 'join'
>>> j=join(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    j=join(a)
NameError: name 'join' is not defined
>>> j=j.join(l)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    j=j.join(l)
NameError: name 'j' is not defined
>>> j=.join()
SyntaxError: invalid syntax
>>> j=.join(a)
SyntaxError: invalid syntax
>>> a=['one','two','three','four']
>>> j=' '.join(a)
>>> print(j)
one two three four
>>> l=','.join(a)
>>> print(l)
one,two,three,four
>>> m=l.join(a)
>>> print(m)
oneone,two,three,fourtwoone,two,three,fourthreeone,two,three,fourfour
>>> oneone,two,three,fourtwoone,two,three,fourthreeone,two,three,fourfour
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    oneone,two,three,fourtwoone,two,three,fourthreeone,two,three,fourfour
NameError: name 'oneone' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 877888
877888
>>> 877888877888
877888877888
>>> 
>>> 
>>> 
>>> 
>>> 
>>> x=[1,2,3,4]
>>> y=x.join(a)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    y=x.join(a)
AttributeError: 'list' object has no attribute 'join'
>>> x=['1','2','3','4']
>>> y=x.join(a)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    y=x.join(a)
AttributeError: 'list' object has no attribute 'join'
>>> l='1,2,3,4'
>>> y=l.join(a)
>>> print(y)
one1,2,3,4two1,2,3,4three1,2,3,4four
>>> x=['1','2','3','4']
>>> y='-'.join(x)
>>> print(y)
1-2-3-4
>>> s='Learning python Is Very easy'
>>> l=s.lower(s)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    l=s.lower(s)
TypeError: lower() takes no arguments (1 given)
>>>  l=s.lower()
 
SyntaxError: unexpected indent
>>> l=sloewr()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    l=sloewr()
NameError: name 'sloewr' is not defined
>>> l=s.lower()
>>> print(l)
learning python is very easy
>>> s='Learning python Is Very easy'
>>> l=s.lower()
>>> print(l)
learning python is very easy
>>> u=s.upper()
>>> print(u)
LEARNING PYTHON IS VERY EASY
>>> a='I am On Way to the tour'
>>> b=a.swap()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    b=a.swap()
AttributeError: 'str' object has no attribute 'swap'
>>> b=a.swapcase()
>>> print(b)
i AM oN wAY TO THE TOUR
>>> c=a.title()
>>> print(C)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print(C)
NameError: name 'C' is not defined
>>> s.prit(c)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    s.prit(c)
AttributeError: 'str' object has no attribute 'prit'
>>> print(c)
I Am On Way To The Tour
>>> a='I am On Way to the tour'
>>> d=a.captalize()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    d=a.captalize()
AttributeError: 'str' object has no attribute 'captalize'
>>> d=a.capitalize()
>>> print(d)
I am on way to the tour
>>> 