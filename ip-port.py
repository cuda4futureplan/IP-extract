

with open('telnet-Zoomeye_20220420203902.txt') as fh:
    fstring = fh.readlines()

for line in fstring:
    [host,port]=line.split(":")
    #print ([host,port])
    print (host)
    print (port[:-1])
    open(port[:-1]+".txt","a+").write(f"{host} ")
