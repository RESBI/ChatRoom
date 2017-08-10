#By Resbi

import socket,os,_thread,getre

        #Recv data from server.
def Recvi(S):
    while 1:
        Receive = S.recv(1024)
        if Receive:
#            print(str(Receive))
#            [a] = getre.get(r'b"(.+)"',str(Receive))
#            if "ClEaR-yOuR-sCrEeN" in a:
#                os.system("clear")
#                os.system("cls")
#                pass
            print("|====|"+Receive.decode('utf-8'))
            print("-" * 10)

        #Send data to server.
def Sent(S):
    while 1:
        print("-" * 10)
        a = str(input())
        if a == "":
            S.send(a.encode(encoding='utf-8'))
            exit()
        if a == "exit":
            S.send("exit".encode(encoding='utf-8'))
            exit()
        else:
            S.send(a.encode(encoding='utf-8'))

        #Client to server with new port.
def client(serverip,serverport,Username):

    S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Connecting to newport....")
    S.connect((serverip, serverport))

    print("Successful login with %s!" % Username)

    _thread.start_new_thread(Sent,(S,))

    _thread.start_new_thread(Recvi,(S,))

    while 1:
        pass

        #Get a new port from server.
def GetPort(serverip,serverport,Username):

    S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    S.connect((serverip, serverport))

#    S.send("Client!".encode(encoding='utf-8'))
    S.send(("'%s'" % Username).encode(encoding='UTF-8'))

    print("Getting a new port...")

    newPort = S.recv(1024)
    x = ""

    print(str(newPort))
    newPort = str("%s\'" % newPort)
    for i in range(len(newPort) - 4):
        x = x + str(newPort[i + 2])

    newPort = int(x)

    print("Get a new port : %s" % newPort)

    S.close()

    client(serverip,int(newPort),Username)


serverip = str(input("Input the server Ipaddress:"))
serverport = int(input("Input the server port:"))
Username = str(input("Enter your name:"))
GetPort(serverip,serverport,Username)
