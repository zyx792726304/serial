#使用串口调试助手发送的数据格式为x,y 必须为2个数据（经纬度），且逗号为英文逗号


#导入串口模块和正则表达式
import serial
import re
from tkinter import *

#串口读取数据操作函数
def serialmain(var):
  #打开串口COM3，如果需要更改串口，直接更改第一个参数。9600为波特率
  ser = serial.Serial(var,9600)
  #主循环，循环读取串口数据
  while(1):
    file = open('data.txt','a')
    data = str(ser.readline())
    save = re.findall(r'\d*\.?\d*\,{1}\d*\.?\d*',data)
    for i in save:
      file.write(i)
      file.write('\r\n')
    file.close()
    print(save)

#回调确认所有传入参数函数
def mainback(variable,var,variable1,var1):
  if (variable!=var):
    var = variable
  if (variable1!=var1):
    var1 = variable1
  return var,var1
  
root = Tk()
root.title('Lora串口调试助手')
#串口选择
variable = StringVar()
var = StringVar()
variable.set('COM3')#下拉窗口的默认COM口
var.set('COM3')#程序中传递对比的值


#波特率选择
variable1 = IntVar()
var1 = IntVar()
variable1.set(9600)#下拉窗口的默认波特率
var1.set(9600)#程序中传递对比的值


#下拉窗口
commenu = OptionMenu(root,variable,'COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9','COM10')
commenu.grid(row=1,column=0,sticky=W,padx=10,pady=5)
baudmenu = OptionMenu(root,variable1,300,600,1200,2400,4800,9600,19200,38400,43000,56000,57600,115200)
baudmenu.grid(row=2,column=0,sticky=W,padx=10,pady=5)


#确认按钮
okbutton = Button(root,text='确定激活',command=mainback(variable.get(),var.get(),variable1.get(),var1.get()))
okbutton.grid(row=1,column=1,sticky=E,padx=10,pady=10)

#信息显示
textmsg = StringVar()
textmsg.set('请在选择好串口之后点击激活串口，\n然后关闭此页面！')
label = Label(root,textvariable=textmsg,justify=LEFT)
label.grid(row=3,column=0)

mainloop()

cominfo=''
baudinfo=1
cominfo,baudinfo=mainback(variable.get(),var.get(),variable1.get(),var1.get())
var.set(cominfo)
var1.set(baudinfo)
print('当前串口为:'+var.get())
print('当前波特率为:'+str(var1.get()))
serialmain(var.get())




