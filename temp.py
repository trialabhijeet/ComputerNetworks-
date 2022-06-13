import os
import re
import xlwt
import socket
import xlsxwriter
import subprocess
from tkinter import *
from scapy.all import *
from xlwt import *

# ip_list = [f"{i}.{j}.{k}.{l}" for i in range(f[0],s[0]+1) for j in range(f[1],s[1]+1) for k in range(f[2],s[2]+1) for l in range(f[3],s[3]+1)]

ip_list = ["127.0.0.1","8.8.8.8"]


def Range():
    global ip_list

    f = [int(i) for i in fip.get().split(".")]
    s = [int(i) for i in lip.get().split(".")]

    L = [f"{i}.{j}.{k}.{l}" for i in range(f[0],s[0]+1) for j in range(f[1],s[1]+1) for k in range(f[2],s[2]+1) for l in range(f[3],s[3]+1)]

    ip_list = L.copy()

    calculate()

def calculate():

    wb = Workbook()
    sheet = wb.add_sheet('Sheet 1')

    sheet.write(0, 0, "  IP ADDRESS")
    sheet.write(0, 1, "  STATE")
    sheet.write(0, 2, "  MAC ADDRESS")
    sheet.write(0, 3, "  HOST NAME")

    for i in range(len(ip_list)):
        empty = ""
        res = subprocess.getoutput("ping -n 1 " + ip_list[i])
        empty += res
        need = re.compile(r'TTL=')
        time = need.search(empty)
        try:
            if time.group() == "TTL=":
                state = "Alive"
                hostname = socket.gethostbyaddr(ip_list[i])[0]
                mac = getmacbyip(ip_list[i])

                sheet.write(i+1, 0, ip_list[i])
                sheet.write(i+1, 1,state)
                sheet.write(i+1, 2, mac)
                sheet.write(i+1, 3, hostname)
                print("Alive")
        except:
            sheet.write(i+1, 0, "Dead")
            sheet.write(i+1, 1, "--")
            sheet.write(i+1, 2, "--")
            sheet.write(i+1, 3, "--")
            print("Down")

    wb.save('Scan.xls')


    rfile = (r'C:\Users\abhijeet\Desktop\CN\Scan.xls')
    os.startfile(rfile)

    


root = Tk()

root.geometry("600x400")
root.title("Network Scanner")

lfip = Label(root, text="Initial Address  :  ",font=("Arial", 15))
lfip.place(x=70, y=60)
fip = Entry(root, width=40, justify="center")
fip.place(x=240, y=65)

llip = Label(root, text="Last Address  :  ",font=("Arial", 15))
llip.place(x=70, y=160)
lip = Entry(root, width=40, justify="center")
lip.place(x=240, y=165)

B = Button(root, text="Scan Network",bg="Green",font=("Arial", 15), width=25,command=Range)
B.place(x=180, y=265)

root.mainloop()