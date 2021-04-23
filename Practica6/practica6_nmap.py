import nmap

nm = nmap.PortScanner()
ip = input("IP: ")
nm.scan(hosts = ip, arguments = "--top-ports 1000 -sV --version-intensity 3")
print("Protocolos: {}".format(nm[ip].all_protocols()))
print("Estado: {}".format(nm[ip].state()))

for puerto in nm[ip]["tcp"].keys():
    print("--------------")
    print("Puerto: " ,puerto)
    for data in nm[ip]["tcp"][puerto]:
        print(data + " : " + nm[ip]["tcp"][puerto][data])


    
