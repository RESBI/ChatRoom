import socket,time,random,_thread,getre

import CodeBeta as CB

global temp_message

def ding(conn,key):
    while 1:
        time.sleep(30)
        conn.send(CB.enc("'Server:Keep online.....'",key).encode(encoding='utf-8'))

def check(conn,addr,Username,key):
    global temp_message
    tt = ""
    while 1:
        if tt != temp_message:
            conn.send(CB.enc(temp_message,key).encode(encoding='utf-8'))
            tt = temp_message

def ChildThread(ip,port,Username,old):
    global temp_message
    S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def client(ip, port):
        try:
            S.bind((ip,port))
        except:
            print("Something error in port:" + str(port) + "let's try again.")
            newport = random.randint(2000,3000)
            client(ip,newport)
    client(ip,port)

    S.listen(5)
    old.send(str(port).encode(encoding='utf-8'))
    old.close()
    conn,addr = S.accept()

    print(addr)

    conn.settimeout(16384)
    temp_message = "["+str(time.time())+"]"+Username+":"+"Join the server!"

#    _thread.start_new_thread(Logs,(conn,addr,Username,))  #Save to log.
    _thread.start_new_thread(check,(conn,addr,Username,str(port),))  #Check if some information recv.
    _thread.start_new_thread(ding,(conn,str(port),))  #Keep online.

    while 1:
        Receive = conn.recv(1024)
        if Receive:
            log = open("log.txt","at")
            log.write("["+str(time.time())+"]"+"{"+str(addr)+"}"+Username+":"+CB.dec(Receive.decode("UTF-8"),str(port))+"\n")
            log.close()
            temp_message = "["+str(time.time())+"]"+Username+":"+CB.dec(Receive.decode("UTF-8"),str(port))
            print(temp_message)

def GiveNewPort(ip,port):
    while 1:
        S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        S.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        S.bind((ip,port))
        S.listen(5)
        conn,addr = S.accept()

        conn.settimeout(65536)

        while 1:

            Receive = conn.recv(1024)
    
            if Receive:
                Username = Receive.decode("UTF-8")

                print("%s||%s was join the server!" % (str(addr),Username))
                log = open("log.txt","at")
                log.write("["+str(time.time())+"]"+"{"+str(addr)+"}"+"User:"+Username+":"+"Join the server!"+"\n")
                log.close()
				
                newport = random.randint(2000,3000)
                _thread.start_new_thread(ChildThread,(ip,newport,Username,conn))
                print("["+str(time.time())+"]"+"{"+str(addr)+"}"+Username)    #+"--port:"+str(newport))
                time.sleep(2)
                S.close()
                break

ip = "0.0.0.0"
port = int(input("Input a port for listen:"))
GiveNewPort(ip,port)
