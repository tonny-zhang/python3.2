#path_config = [
#	['abc/js-ource23/','abc/js'],
#	['abc/js-s','abc/js']
#	,123,
#	'abc'];
#print('123'+path_config);
#current_path = '123abc/js-source1/modules/';
#for arr in path_config:
#	print(type(arr));
#	if current_path.startswith(arr[0]):
#		print('command '+current_path+'  '+current_path.replace(arr[0],arr[1]));
#		break;
#	else:
#		print(arr[1]);
print(len('abc'));
import json
print(json.dumps([[1,2],[4,5]]));
print(','.join(['a','b','cc']));
import os
def _formatPath (uri):
	return uri.replace('\\','/');


_file_name = _formatPath('D:/GC/test/abc/p_product_list.js');
_path = os.path.dirname(_file_name)+'/';

#compress.js config
_nodeCommand = _formatPath('node E:/nodejsSite/uglifyJS_compress/compress.js ');

_compressInfo = 'no compress';
#path must be composed by slash (/),not by (\)
#site config
_siteJsPath = [_formatPath('D:/GC/test/'),
				[_formatPath('D:/GC/test/'),_formatPath('D:/GC/test-min/')]
			  ];
print(_path);
for _jsPathConfig in _siteJsPath:
	_checkPath = _jsPathConfig[0] if type(_jsPathConfig) == type([]) else _jsPathConfig;
	print(_checkPath);
	if(_path.startswith(_checkPath)):
		_compressInfo = 'compress with uglify';
		_nodeCommand = _nodeCommand + _file_name+' ';
		_nodeCommand += _file_name.replace(_jsPathConfig[0],_jsPathConfig[1]) if (type(_jsPathConfig) == type([]) and len(_jsPathConfig) > 1) else '';
		os.popen(_nodeCommand);
		break;

#if(_path.startswith(_siteJsPath)):
#	_compressInfo = 'compress with uglify';
#	os.popen(_nodeCommand+_file_name);

#uglifyInfo.txt at base path of Sublime Text
file_info = open('D:/sorft/sublime/uglifyInfo.txt', 'w')
file_info.write('nodeCommand: '+_nodeCommand+'\n');
file_info.write(_compressInfo+'\n');
file_info.write('currentPath: '+_path+'\n');
file_info.write('checkPath: '+_checkPath+'\n');
file_info.write('_siteJsPath: '+(json.dumps(_siteJsPath))+'\n');
file_info.close();

