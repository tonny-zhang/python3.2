# encoding: UTF-8
import re

# 将正则表达式编译成Pattern对象
#pattern = re.compile(r'\[ \*\*\* error \*\*\* \]( \[message:"(.+?)"(,line:(\d+))?(,col:(\d+))?\])?')
pattern = re.compile(r'\[message:"(.+?)"(,line:(\d+))?(,col:(\d+))?\]')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
str = '[ *** error *** ] [message:"Unexpected token: punc ())",line:31,col:2] D:/GC/test/p_product_list.js'
#match = pattern.search(str);

if (pattern.search(str)):
    # 使用Match获得分组信息
    print match.group(),match.group(1);
else:
	print('no');

### 输出 ###
# hello