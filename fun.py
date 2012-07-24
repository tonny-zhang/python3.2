#this is first function in python
def hello (name):
	'function hello'
	print('your name is: '+ name);

hello('test');
print(hello.__doc__);

from math import sqrt
for i in range(99,80,-1):
	root = sqrt(i);
	if root == int(root):
		print(i,root);
		break
else:
	print('not find it');

int_test = 1;
if 1 == int_test:
	print('equals 1');
elif 2 == int_test:
	pass;
else:
	print('equals other');

int_test = 1,
print(int_test);

class Person:
	def _formatPath (uri):
		return uri.replace('\\','/');
	def say ():
		print(_formatPath('d:\ybc\c/test'));

p = new Person();
p.say();



