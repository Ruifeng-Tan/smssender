import xlrd
#请给你的python 装上xlrd工具
inpath = r'C:\Users\Lenovo\Desktop\test.xlsx'#excel文件所在路径
outpath= r'C:\Users\Lenovo\Desktop\test.txt' #txt文件所在路径
user_dic = {}

def extract(path):
    
    data = xlrd.open_workbook(path, encoding_override='utf-8')
    table = data.sheets()[0]#选定表
    nrows = table.nrows#获取行号
    
    for i in range(1, nrows):
        alldata = table.row_values(i)#循环输出excel表中每一行，即所有数据
        name = str(alldata[0])          #取出列表中的第一列数据
        telephonenumber = str(int(alldata[1]))#取出表中第二列数据

        user_dic[name] = telephonenumber

      
extract(inpath)

with open(outpath,'w') as file_object:
    file_object.write('#-*-coding:utf8;-*-'+'\n'
    +'#qpy:3'+'\n'+
    '#qpy:console'+'\n'+
    'from sl4a import *'+'\n'+
    's = Android().smsSend'+'\n'
    )
    
    for name_needed , num in user_dic.items():
        file_object.write('s'+'('+"'"+num+"'"+","+"'你好!"+name_needed+",内容'"+')'+'\n')



