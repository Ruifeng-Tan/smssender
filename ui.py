from PyQt5 import QtWidgets
from form import Ui_Form # 导入ui文件转换后的py文件
import xlrd
import sys
import pandas as pd
user_dic = {}
sms_list = []
#将槽函数都写在mywindow里



class mywindow(QtWidgets.QWidget, Ui_Form):
    def  __init__ (self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonclicked)

    def buttonclicked(self):
        excel_path = self.lineEdit.text()
        txt_path = self.lineEdit_2.text()

        data = xlrd.open_workbook(excel_path, encoding_override='utf-8')
        table = data.sheets()[0]#选定表
        nrows = table.nrows#获取行号
    
        for i in range(0, nrows):
            alldata = table.row_values(i)#循环输出excel表中每一行，即所有数据
            name_column = int(self.comboBox.currentText())-1
            tele_column = int(self.comboBox_2.currentText())-1


            name = str(alldata[name_column])        
            telephonenumber = str(int(alldata[tele_column]))

            user_dic[name] = telephonenumber

        with open(txt_path,'w') as file_object:
            file_object.write('#-*-coding:utf8;-*-'+'\n'
            +'#qpy:3'+'\n'+
            '#qpy:console'+'\n'+
            'from sl4a import *'+'\n'+
            's = Android().smsSend'+'\n'
            )

            sms_txt = self.lineEdit_3.text()
                
            sms_single_maxnum = 70
            if len(sms_txt)%70 == 0:
                run_times = int(len(sms_txt)/70)
            else:
                run_times = int( (len(sms_txt)/70)+1 )

            j = 1
            for i in range(0,run_times):
                sms_list.append(sms_txt[i*sms_single_maxnum:j*sms_single_maxnum])
                j += 1

            for name_needed , num in user_dic.items():
                file_object.write('s'+'('+"'" + num + "'" + "," + "'"+"你好!"+name_needed+"'"+ ")"+"\n")
                for i in range(0,run_times):
                    file_object.write('s'+'('+"'" + num + "'" + "," + "'"+sms_list[i]+"'"+ ")"+"\n")
                    i += 1


                       
if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    ui = mywindow()    
    ui.show()
    sys.exit(app.exec_())

'''          ##开发者:不合格的WHU程序员雨墨##         '''