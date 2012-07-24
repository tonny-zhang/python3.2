import os

_command = os.popen('node E:/nodejsSite/uglifyJS_compress/compress.js D:/GC/test/p_product_list.js D:/GC/test-min/p_product_list.js');
for _line in _command.readlines():
	print(_line);
	if ~_line.find('error'):
		print('error');
		break
	else:
		print('no');