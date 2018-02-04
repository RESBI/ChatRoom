import socket,time,random,_thread,getre
global temp_message

def ding(conn):
    while 1:
        time.sleep(30)
        conn.send("'Server:Keep online.....'".encode(encoding='utf-8'))

def check(conn,addr,Username):
    global temp_message
    tt = ""
    while 1:
        """
        f = open("./Temps/temp.txt","r")
        a = f.read()
        f.close

        f = open("./Temps/%s.txt" % Username,"r")
        b = f.read()
        f.close()
        
        if not(a in b):
            f = open("./Temps/%s.txt" % Username,"w+")
            f.write(a)
            f.close()
            conn.send(a.encode(encoding='utf-8'))
        """
        if tt != temp_message:
            conn.send(temp_message.encode(encoding='utf-8'))
            tt = temp_message

"""
def Logs(conn,addr,Username):
    while 1:
        Receive = conn.recv(1024)
        
        log = open("log.txt","at")
        log.write("["+str(time.time())+"]"+"{"+str(addr)+"}"+Username+":"+str(Receive)+"\n")
        log.close()
     
        f = open("./Temps/temp.txt","w+")
        f.write("["+str(time.time())+"]"+Username+":"+str(Receive))
        f.close()

        print("["+str(time.time())+"]"+"{"+str(addr)+"}"+Username+":"+str(Receive))
"""

def ChildThread(ip,port,Username,old):
    global temp_message
    S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        S.bind((ip,port))
    except:
        print("Something error in port:" + str(port) + "let's try again.")
        newport = random.randint(2000,3000)
        ChildThread,(ip,newport,Username,old)
    S.listen(5)
    old.send(str(port).encode(encoding='utf-8'))
    old.close()
    conn,addr = S.accept()

    print(addr)

    conn.settimeout(16384)
    """
    f = open("./Temps/temp.txt","w+")
    f.write("["+str(time.time())+"]"+Username+":"+"Join the server!")
    f.close()
    """
    temp_message = "["+str(time.time())+"]"+Username+":"+"Join the server!"

#    _thread.start_new_thread(Logs,(conn,addr,Username,))  #Save to log.

    _thread.start_new_thread(check,(conn,addr,Username,))  #Check if some information recv.

    _thread.start_new_thread(ding,(conn,))  #Keep online.


    while 1:
        Receive = conn.recv(1024)
        if Receive:
            log = open("log.txt","at")
            log.write("["+str(time.time())+"]"+"{"+str(addr)+"}"+Username+":"+str(Receive)+"\n")
            log.close()
            """    
            f = open("./Temps/temp.txt","w+")
            f.write("["+str(time.time())+"]"+Username+":"+str(Receive))
            f.close()
            """
            temp_message = "["+str(time.time())+"]"+Username+":"+Receive.decode("UTF-8")
            print(temp_message)

def GiveNewPort(ip,port):
    while 1:
        S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        S.bind((ip,port))
        S.listen(5)
        conn,addr = S.accept()

        conn.settimeout(65536)

        while 1:

            Receive = conn.recv(1024)
    
            if Receive:
                [Username] = getre.get(r'b"(.+)"',str(Receive))

                print("%s||%s was join the server!" % (str(addr),Username))
                log = open("log.txt","at")
                log.write("["+str(time.time())+"]"+"{"+str(addr)+"}"+"User:"+Username+":"+"Join the server!"+"\n")
                log.close()
                """
                f = open("./Temps/%s.txt" % Username,"w+")
                f.close()
                """
				
                newport = random.randint(2000,3000)

                _thread.start_new_thread(ChildThread,(ip,newport,Username,conn))

#                conn.send(str(newport).encode(encoding='utf-8'))

                print("["+str(time.time())+"]"+"{"+str(addr)+"}"+Username)    #+"--port:"+str(newport))

                break
        S.close()


ip = "0.0.0.0"
port = int(input("Input a port for listen:"))
GiveNewPort(ip,port)
