import json
from tkinter import *

GlobalPack = {}

def SaveInfo():
    GlobalPack["Class"] = BipE.get()
    GlobalPack["category"] = ipcategory.get()
    GlobalPack["yn"] = verdict.get()
    GlobalPack["Reason"] = reasonE.get()
    GlobalPack["nsubnets"] = NsubnetworksE.get()
    GlobalPack["nhosts"] = NhostsE.get()
    GlobalPack["range"] = RangeE.get()
    GlobalPack["networkids"] = NetworkIDsE.get()
    GlobalPack["broadcastids"] = BroadcastIDsE.get()

    file = open("save.json","a")
    file.write(json.dumps(GlobalPack))
    file.close()


def display(info):
    ip.delete(0, END)
    ip.insert(0, ".".join([str(i) for i in info["IP"]]))

    Bip.delete(0,END)
    Bip.insert(0, ".".join([str(i) for i in info["BIP"]]))

    mask.delete(0, END)
    mask.insert(0, ".".join([str(i) for i in info["MASK"]]))

    maskE.delete(0,END)
    maskE.insert(0, ".".join([str(i) for i in info["BMASK"]]))

    Network.delete(0, END)
    Network.insert(0, ".".join([str(i) for i in info["NID"]]))

    BNetwork.delete(0, END)
    BNetwork.insert(0, ".".join([str(i) for i in info["BNID"]]))


def Reset():
    display({"IP": [], "BIP": [], "NID": [], "BNID": [], "MASK": [], "BMASK": [], "class": ""})


def IsValid(ip):
    if len(ip) != 4:
        return False
    else:
        for i in ip:
            if i > 255 or i < 0:
                return False
        return True


def DefaultMask():
    i = ip.get()
    IP = list(map(int, i.split(".")))
    if IsValid(IP):
        if IP[0] >= 0 and IP[0] <= 127:
            mask.delete(0, END)
            mask.insert(0, "255.0.0.0")
        elif IP[0] >= 128 and IP[0] <= 191:
            mask.delete(0, END)
            mask.insert(0, "255.255.0.0")
        elif IP[0] >= 192 and IP[0] <= 223:
            mask.delete(0, END)
            mask.insert(0, "255.255.255.0")
        else:
            mask.delete(0, END)
            mask.insert(0, "255.255.255.255")


def Read():
    i = ip.get()
    m = mask.get()
    Class = ""
    NID = []
    BIP = []
    BM = []
    BNID = []
    try:
        IP = list(map(int, i.split(".")))
        MASK = []
        if m != "":
            MASK = list(map(int, m.split(".")))
        else:
            # CLASS
            if IP[0] >= 0 and IP[0] <= 127:
                Class = "A"
                MASK = [255, 0, 0, 0]
            elif IP[0] >= 128 and IP[0] <= 191:
                Class = "B"
                MASK = [255, 255, 0, 0]
            elif IP[0] >= 192 and IP[0] <= 223:
                Class = "C"
                MASK = [255, 255, 255, 0]
            elif IP[0] >= 224 and IP[0] <= 239:
                Class = "D"
                MASK = [255, 255, 255, 255]
            else:
                Class = "E"
                MASK = [255, 255, 255, 255]

        if IsValid(IP):
            # Calculate Network ID
            for i in range(4):
                T = IP[i] & MASK[i]
                NID.append(T)
            # Binary Conversions
            for j in IP:
                b = bin(j)[2:]
                if len(b) != 8:
                    b = "0" * (8 - len(b)) + b
                BIP.append(b)
            for j in MASK:
                b = bin(j)[2:]
                if len(b) != 8:
                    b = "0" * (8 - len(b)) + b
                BM.append(b)
            for j in NID:
                b = bin(j)[2:]
                if len(b) != 8:
                    b = "0" * (8 - len(b)) + b
                BNID.append(b)

            pack = {"IP": IP, "BIP": BIP, "NID": NID, "BNID": BNID, "MASK": MASK, "BMASK": BM, "class": Class}
            global GlobalPack
            GlobalPack = pack
            print(pack)
            display(pack)

        else:
            raise IndexError
    except:
        print("Invalid")


root = Tk()
root.geometry("1200x500")
root.title("Internet Protocol")

# IP Information
IpI = Label(root, text="- IP Information -")
IpI.place(x=20, y=20)

lip = Label(root, text="IP Address :  ")
lip.place(x=50, y=60)
ip = Entry(root, width=30, justify="center")
ip.place(x=140, y=60)
B1 = Button(root, text="Reset", width=25, command=Reset)
B1.place(x=360, y=55)

subnetmask = Label(root, text="Subnet Mask :  ")
subnetmask.place(x=50, y=110)
mask = Entry(root, width=30, justify='center')
mask.place(x=140, y=110)
B2 = Button(root, text="Default Mask", width=25, command=DefaultMask)
B2.place(x=360, y=105)

NetworkID = Label(root, text="Network ID :  ")
NetworkID.place(x=50, y=150)
Network = Entry(root, width=30, justify='center')
Network.place(x=140, y=150)
B3 = Button(root, text="Compute Now", width=25, command=Read)
B3.place(x=360, y=145)

# Binary Information
BIpI = Label(root, text="- Binary Information -")
BIpI.place(x=20, y=200)

BipAddress = Label(root, text="IP Address :  ")
BipAddress.place(x=50, y=255)
Bip = Entry(root, width=70, justify='center')
Bip.place(x=140, y=255)

Bmask = Label(root, text="Mask :  ")
Bmask.place(x=60, y=295)
maskE = Entry(root, width=70, justify='center')
maskE.place(x=140, y=295)

BNetworkID = Label(root, text="Network ID :  ")
BNetworkID.place(x=50, y=335)
BNetwork = Entry(root, width=70, justify='center')
BNetwork.place(x=140, y=335)

Save = Button(root, bg="Green", text="Save", height=5, width=38,command=SaveInfo)
Save.place(x=30, y=390)

Close = Button(root, bg="Red", text="Close", height=5, width=38, command=root.destroy)
Close.place(x=330, y=390)

##################################################################
# Network information
networkI = Label(root, text="- Network Information -")
networkI.place(x=620, y=20)

ipAddressclass = Label(root, text="IP Address Class :  ")
ipAddressclass.place(x=650, y=45)
BipE = Entry(root, width=5, justify='center')
BipE.place(x=850, y=45)

AddressType = Label(root, text="Address Type : ")
AddressType.place(x=650, y=85)
ipcategory = Entry(root, width=30, justify='center')
ipcategory.place(x=800, y=85)

goodip = Label(root, text="Good IP to host : ")
goodip.place(x=650, y=150)
verdict = Entry(root, width=5, justify='center')
verdict.place(x=800, y=150)
YN = Label(root, text="YES/NO")
YN.place(x=790, y=130)
reason = Label(root, text="Reason")
reason.place(x=950, y=130)
reasonE = Entry(root, width=30, justify='center')
reasonE.place(x=890, y=150)

# Subnetting Information
subnettingI = Label(root, text="- Subnetting Information -")
subnettingI.place(x=620, y=200)

Nsubnetworks = Label(root, text="# of Subnetworks : ")
Nsubnetworks.place(x=800, y=230)
NsubnetworksE = Entry(root, width=8, justify='center')
NsubnetworksE.place(x=950, y=230)

Nhosts = Label(root, text="# of Hosts : ")
Nhosts.place(x=820, y=260)
NhostsE = Entry(root, width=8, justify='center')
NhostsE.place(x=950, y=260)

Range = Label(root, text="Range : ")
Range.place(x=840, y=290)
RangeE = Entry(root, width=8, justify='center')
RangeE.place(x=950, y=290)

NetworkIDs = Label(root, text="Network ID's : ")
NetworkIDs.place(x=780, y=350)
NetworkIDsE = Entry(root, width=20, justify='center')
NetworkIDsE.place(x=870, y=350)

BroadcastIDs = Label(root, text="Broadcast ID's")
BroadcastIDs.place(x=780, y=400)
BroadcastIDsE = Entry(root, text="Broadcast ID's : ", justify='center')
BroadcastIDsE.place(x=870, y=400)

root.mainloop()
