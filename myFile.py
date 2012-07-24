file = open('test.txt');
file.write('hello world!');
file.close();

with open('test.txt') as myFile:
	myFile.write('myFile');