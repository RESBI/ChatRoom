#By Resbi

import socket,os,_thread,time
import CodeBeta as CB

def ding(S,key):
    while 1:
        time.sleep(30)
        S.send(CB.enc("'Keep online.....'",key).encode(encoding='utf-8'))

        #Recv data from server.

def Sent(S,key):
    while 1:
        print("-" * 10)
        a = str(input())
        if a == "":
            pass
        else:
            S.send(CB.enc(a,key).encode('utf-8'))

        #Client to server with the new port.
def client(serverip,serverport,Username):
    #Key is the newport.

    S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Connecting to newport....")
    S.connect((serverip, serverport))

    key = str(serverport)

    print("Successful login with %s!" % Username)

    _thread.start_new_thread(Sent,(S,key))
    _thread.start_new_thread(ding,(S,key))

    #Recv.
    while 1:
        Receive = S.recv(1024)

        if Receive:
            ReceiveDecoded = CB.dec(Receive.decode('utf-8'),key)
            if not "Keep online....." in ReceiveDecoded:
                print("|====|"+ReceiveDecoded)
                print("-" * 10)
                #print("-" * 10)

        #Get a new port from server.
def GetPort(serverip,serverport,Username):
    S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    S.connect((serverip, serverport))
    #Send your username.
    S.send(("'%s'" % Username).encode(encoding='UTF-8'))

    print("Getting a new port...")

    newPort = S.recv(1024)
    x = newPort.decode("UTF-8")
    newPort = int(x)
    print("Get a new port : %s" % newPort)

    S.close()
    client(serverip,int(newPort),Username)


serverip = str(input("Input the server Ipaddress:"))
serverport = int(input("Input the server port:"))
Username = str(input("Enter your name:"))
GetPort(serverip,serverport,Username)
