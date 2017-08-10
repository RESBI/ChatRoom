import socket,time,random,_thread,getre


def ding(conn):
    while 1:
        time.sleep(30)
        conn.send("'Server:Keep online.....'".encode(encoding='utf-8'))


def Check(conn,addr,Username):
    while 1:
        f = open("./Temps/temp.txt","r")
        a = f.read()
        f.close

        f = open("./Temps/%s.txt" % Username,"r")
        b = f.read()
        f.close()
        
        if a in b:
            pass
        else:
            f = open("./Temps/%s.txt" % Username,"w+")
            f.write(a)
            f.close()
            conn.send(a.encode(encoding='utf-8'))


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


def ChildThread(ip,port,Username):
    try:
        S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        S.bind((ip,port))
        S.listen(5)

    except:
        print("Something error")


    conn,addr = S.accept()

    print(addr)

    conn.settimeout(16384)

    _thread.start_new_thread(Logs,(conn,addr,Username,))  #Save to log.

    _thread.start_new_thread(Check,(conn,addr,Username,))  #Check if some information recv.

    _thread.start_new_thread(ding,(conn,))  #Keep online.

    f = open("./Temps/temp.txt","w+")
    f.write("["+str(time.time())+"]"+Username+":"+"Join the server!")
    f.close()

    while 1:
        pass


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

                newport = int(random.random() * 10000)

                _thread.start_new_thread(ChildThread,(ip,newport,Username))

                conn.send(str(newport).encode(encoding='utf-8'))

                print("["+str(time.time())+"]"+"{"+str(addr)+"}"+Username+"--port:"+str(newport))

                conn.close()

                break

        print("%s||%s was join the server!\033[4;31;40m" % (str(addr),Username))
        log = open("log.txt","at")
        log.write("["+str(time.time())+"]"+"{"+str(addr)+"}"+"User:"+Username+":"+"Join the server!"+"\n")
        log.close()

        f = open("./Temps/%s.txt" % Username,"w+")
        f.close()


ip = "0.0.0.0"
port = int(input("Input a port for listen:"))
GiveNewPort(ip,port)

