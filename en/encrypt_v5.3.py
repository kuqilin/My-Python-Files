from colorama import Fore, init
import webbrowser
init()


#判断偶数
def is_even(n):
    '''检验number是否为偶数，是返回True，否返回False'''
    return n % 2 == 0

#加密函数
def en(msg):
    '''如果msg长度不是偶数，就在后面加x'''
    if not is_even(len(msg)):
        msg = msg + 'x'
    msg = list(msg)
    for i in range(0,len(msg),2):
        msg[i],msg[i+1] = msg[i+1],msg[i]
    en_msg = ''.join(reversed(msg))
    return en_msg

def de(msg):
    msg = list(msg)
    for i in range(0,len(msg),2):
        msg[i],msg[i+1] = msg[i+1],msg[i]
    de_msg = ''.join(reversed(msg))
    return de_msg


mode = input(Fore.GREEN + '请选择：\n0.退出\n1.加密\n2.解密\n3.查看作者\n>>>')

if mode == '0':
    sb = input('键入Enter以退出...')
    if sb == '\n':
        exit()
elif mode == '1':
    message = input('请输入待加密文本：')
    en_message = en(message)
    while True :
        print('加密后的文本是：%s'%en_message)
        sb = input('请输入exit后退出\n>>>')
        if sb == 'exit' :
            exit()
elif mode == '2':
    message = input('请输入待解密文本：')
    de_message = de(message)
    while True:
        print('加密后的文本是：%s'%de_message)
        sb = input('请输入exit后退出\n>>>')
        if sb == 'exit':
            exit()
elif mode == '3':
    webbrowser.open('https://space.bilibili.com/699667237')
    webbrowser.open('https://space.bilibili.com/473385387')
    print('作者是：bilibili苦麒麟\nuid:699667237')
    print('友情链接：bilibili什么是鸡你太美\nuid:473385387')
else :
    while True:
        print(Fore.RED + '傻逼，退出重进吧！没看清楚输入1或2吗？')
    
