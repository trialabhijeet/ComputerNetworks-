import ipaddress
from tkinter import *


def Display(info):
    ip.delete(0, END)
    ip.insert(0, ".".join(info["ip"]))

    ip2.delete(0, END)
    ip2.insert(0, info["l"])

    Binarytext.delete(1.0, "end")
    Binarytext.insert(1.0, " ".join(info["bip"]))

    Binarytext1.delete(1.0, "end")
    Binarytext1.insert(1.0, info["bl"])

    c.delete(1.0, "end")
    c.insert(1.0, info["class"])

    c1.delete(1.0, "end")
    c1.insert(1.0, info["no127"])

    c2.delete(1.0, "end")
    c2.insert(1.0, info["lhn"])


def IsValid(ip):
    if len(ip) != 4:
        return False
    else:
        for i in ip:
            if i > 255 or i < 0:
                return False
        return True


def ReadIP():
    t = ip.get()
    IP = []
    BIP = []
    L = -1
    BL = 0
    Class = "-"
    NO127 = "-"
    LHN = "-"
    try:
        IP = list(map(int, t.split(".")))
        if IsValid(IP):
            L = IP[0] * pow(2, 24) + IP[1] * pow(2, 16) + IP[2] * pow(2, 8) + IP[3]
            N = [IP[0] * pow(2, 24), IP[1] * pow(2, 16), IP[2] * pow(2, 8), IP[3]]
            BL = bin(L)[2:]
            BL = "0" * (32 - len(BL)) + BL
            for j in IP:
                b = bin(j)[2:]
                if len(b) != 8:
                    b = "0" * (8 - len(b)) + b
                BIP.append(b)

            # CLASS
            if IP[0] >= 0 and IP[0] <= 127:
                Class = "A"
                NO127 = str(IP[0])
                LHN = str(sum(N[1:]))
            elif IP[0] >= 128 and IP[0] <= 191:
                Class = "B"
                NO127 = str(IP[0] + IP[1])
                LHN = str(sum(N[2:]))
            elif IP[0] >= 192 and IP[0] <= 223:
                Class = "C"
                NO127 = str(IP[0] + IP[1] + IP[2])
                LHN = str(sum(N[3:]))
            elif IP[0] >= 224 and IP[0] <= 239:
                Class = "D"
            else:
                Class = "E"

            pack = {"ip": [str(i) for i in IP], "bip": [str(i) for i in BIP], "l": L, "bl": BL, "class": Class,
                    "no127": NO127, "lhn": LHN}
            print(pack)
            Display(pack)
        else:
            raise IndexError
    except:
        print("Invalid")


def ReadLong():
    t = str(ipaddress.ip_address(int(ip2.get())))
    IP = []
    BIP = []
    L = -1
    BL = 0
    Class = "-"
    NO127 = "-"
    LHN = "-"
    try:
        IP = list(map(int, t.split(".")))
        if IsValid(IP):
            L = IP[0] * pow(2, 24) + IP[1] * pow(2, 16) + IP[2] * pow(2, 8) + IP[3]
            N = [IP[0] * pow(2, 24), IP[1] * pow(2, 16), IP[2] * pow(2, 8), IP[3]]
            BL = bin(L)[2:]
            BL = "0" * (32 - len(BL)) + BL
            for j in IP:
                b = bin(j)[2:]
                if len(b) != 8:
                    b = "0" * (8 - len(b)) + b
                BIP.append(b)

            # CLASS
            if IP[0] >= 0 and IP[0] <= 127:
                Class = "A"
                NO127 = str(IP[0])
                LHN = str(sum(N[1:]))
            elif IP[0] >= 128 and IP[0] <= 191:
                Class = "B"
                NO127 = str(IP[0] + IP[1])
                LHN = str(sum(N[2:]))
            elif IP[0] >= 192 and IP[0] <= 223:
                Class = "C"
                NO127 = str(IP[0] + IP[1] + IP[2])
                LHN = str(sum(N[3:]))
            elif IP[0] >= 224 and IP[0] <= 239:
                Class = "D"
            else:
                Class = "E"

            pack = {"ip": [str(i) for i in IP], "bip": [str(i) for i in BIP], "l": L, "bl": BL, "class": Class,
                    "no127": NO127, "lhn": LHN}
            print(pack)
            Display(pack)
        else:
            raise IndexError
    except:
        print("Invalid")


root = Tk()
root.geometry("1000x400")
root.title("Internet Protocol")

# IP Information
IpI = Label(root, text="- IP Information -")
IpI.place(x=10, y=10)

lip = Label(root, text="seperated by dots ( . )")
lip.place(x=15, y=65)
ip = Entry(root, width=30 ,justify='center')
ip.place(x=13, y=50)
B1 = Button(root, text="Dot IP Address To Long", command=ReadIP)
B1.place(x=290, y=45)

lip2 = Label(root, text="seperated by commas ( , )")
lip2.place(x=15, y=130)
ip2 = Entry(root, width=30,justify='center')
ip2.place(x=13, y=110)
B2 = Button(root, text="Long to Dot IP Address", command=ReadLong)
B2.place(x=290, y=105)

# Network Information
NI = Label(root, text="- Network Information -")
NI.place(x=10, y=180)

c = Text(height=1.4, width=3)
c.place(x=45, y=215)
lc = Label(root, text="Network Class")
lc.place(x=15, y=245)

c1 = Text(height=1, width=10)
c1.place(x=115, y=215)
lc1 = Label(root, text="Network \nof/127")
lc1.place(x=135, y=245)

c2 = Text(height=1, width=15)
c2.place(x=275, y=215)
lc2 = Label(root, text="Local Host Number\n of 16,277,215")
lc2.place(x=275, y=245)

####################################################################################
# Binary
Bi = Label(root, text="- IP Information -")
Bi.place(x=550, y=10)

DIP = Label(root, text="- Dot IP -")
DIP.place(x=720, y=30)
Binarytext = Text(height=1, width=50)
Binarytext.place(x=550, y=60)
DIP1 = Label(root, text="MSByte                   To                   LSByte")
DIP1.place(x=650, y=90)

LIP = Label(root, text="- Long IP -")
LIP.place(x=720, y=130)
Binarytext1 = Text(height=1, width=50)
Binarytext1.place(x=550, y=160)
DIP1 = Label(root, text="MSByte                   To                   LSByte")
DIP1.place(x=650, y=190)

Close = Button(root, bg="red", text="Close", height=5, width=60, command=root.destroy)
Close.place(x=550, y=250)

root.mainloop()
