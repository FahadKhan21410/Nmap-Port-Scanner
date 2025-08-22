import nmap

scanner = nmap.PortScanner()

print("PortScanner Utilizing Nmap(Should be used for ethical purposes")
print("-------------------------------------------------------------------")

ipAddr = input("Please enter the target ip address: ").strip()
type(ipAddr)

response = input("\nWhat type of scan you want to perform:\n"
                 "1)SYN Scan\n"                              #(Tells if ports are closed or not)
                 "2)UDP Scan\n"  #UDP --> Online Ports
                 "3)Comprehensive Scan\n"                     #UDP scans, OS detection, version detection, script scanning, and potentially vulnerability scanning
                 "4)FIN Scan\n"                               #(To see how the target responds)
                 "Enter Your Choice (1/2/3/4): ")

print(f"Your selected response: {response} ")

try:
    if response == '1':
        print("[Initiating SYN Scan]")
        scanner.scan(ipAddr,'1-1024','-v -sS')
    elif response == '2':
        print("[Initiating UDP Scan]")
        scanner.scan(ipAddr,'1-1024','-v -sU')
    elif response == '3':
        print("[Initiating Comprehensive Scan]")
        scanner.scan(ipAddr,'1-1024','-v -sV -sC -sS -O')
    elif response == '4':
        print("[Initiating FIN Scan]")
        scanner.scan(ipAddr,'1-1024','-v -sF')

    #Printing All The Required Info

    print("\nScan Info: ", scanner.scaninfo())
    print("Ip State: ", scanner[ipAddr].state())
    print("All Protocols: ",scanner[ipAddr].all_protocols())

    #Open Ports

    if 'tcp' in scanner[ipAddr]:
        print("[Open Tcp Ports]",scanner[ipAddr]['tcp'].keys())
    if 'udp' in scanner[ipAddr]:
        print("[Open UDP Ports]",scanner[ipAddr]['udp'].keys())

except Exception as e:
    print(f"An Error Occurred {e}")




