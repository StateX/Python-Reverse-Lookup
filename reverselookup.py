import socket

def reverselookup():
    result = open("result.txt","w")
    for item in open('asset.txt'):
        try:
            addr1 = socket.gethostbyaddr(item)
            name = (item, addr1)
            print (name)
            result.write(str(name))
        except:
            print (item, "Not found")
            noname = (item, "Not found")
            result.write(str(noname))

if __name__ == "__main__":
    print ("Checking")
    reverselookup()
