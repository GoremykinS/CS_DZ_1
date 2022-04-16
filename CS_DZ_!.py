# 1 ========================================================

development = 'разработка'
print(development)
print(type(development))

development_uni = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
print(type(development_uni))
print(development_uni)
print('----------------------------------------')

socket = 'сокет'
print(socket)
print(type(socket))
socket_uni = '\u0441\u043e\u043a\u0435\u0442'
print(type(socket_uni))
print(socket_uni)
print('----------------------------------------')


decorator = 'декоратор'
print(decorator)
print(type(decorator))

decorator_uni = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
print(type(decorator_uni))
print(decorator_uni)


# 2 ========================================================
list=[]
elem =''
while elem != 'stop':
        elem = str(input('введите слова, который нобходимо записать в байтовом типе.'
                         ' Как исчерпаете свою фантазию напишите stop: ', ))
        if elem != 'stop':
            list.append(elem)
for i in list:
    i_list = f'b"{i}"'
    i_b = eval(i_list)
    print(i_b,type(i_b))




# 3 ========================================================

list=[]
elem =''
while elem != 'stop':
    elem = str(input(':', ))
    if elem != 'stop':
       list.append(elem)
       print(list)

for i in list:
    i_list = f'b"{i}"'
    error=0
    try:
        i_b = eval(i_list)
    except SyntaxError:
        print(i, 'невозможно записать в байтовом типе')
        error=1
    if error == 0:
        print(i_b,type(i_b))



# 4 ===========================================================

list_str=[]
list_bytes =[]
elem =''
while elem != 'stop':
        elem = str(input('введите слова,как исчерпаете свою фантазию напишите stop: ', ))
        if elem != 'stop':
            list_str.append(elem)
            print(list_str)
print('encode ----------------------------------------------------')
for i in list_str:
    elem_bytes = i.encode('utf-8')
    print(elem_bytes, type(elem_bytes))
    list_bytes.append(elem_bytes)
print('decode ----------------------------------------------------')
for i in list_bytes:
    elem_str = i.decode('utf-8')
    print(elem_str, type(elem_str))

# 5 ==========================================================

import chardet   # необходима предварительная инсталляция: pip install chardet
import subprocess
import platform


param = '-n' if platform.system().lower() == 'windows' else '-c'
print('youtube.com---------------------------')
args = ['ping', param, '2', 'youtube.com']
process = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in process.stdout:
    result = chardet.detect(line)
    print('result = ', result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))
print('googl.com----------------------------')
args = ['ping', param, '2', 'googl.com']
process = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in process.stdout:
    result = chardet.detect(line)
    print('result = ', result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))


# 6 ==========================================================

from chardet import detect


f = open('file.txt', 'w', encoding='utf-8')
f.write('сетевое программирование'+ '\n' + 'сокет' + '\n' + 'декоратор')
f.close()


with open('file.txt', 'rb') as f:
    content = f.read()
encoding = detect(content)['encoding']
print('encoding: ', encoding)



with open('file.txt', encoding=encoding) as f_n:
    for el_str in f_n:
        print(el_str, end='')
    print()








