import getpass
import telnetlib

user = raw_input("Enter your username:")
password = getpass.getpass()       
          
HOST = ("192.168.10.158", "192.168.10.159", "192.168.10.160")
   
for i in HOST:
        print ("\n\nconnecting to " + i)
        tn = telnetlib.Telnet(i, timeout = 15)
        if i is "192.168.10.158":
            tn.read_until("login:")  
            tn.write(user + "\n")
            if password:
                tn.read_until("Password:")
                tn.write(password + "\n")
            tn.write("sh configuration | display set\n")    
            tn.write("exit\n")
         
        elif i is "192.168.10.159":
            tn.read_until("Username:")  
            tn.write(user + "\n")
            if password:   
                tn.read_until("Password:")
                tn.write(password + "\n")   
            tn.write("terminal length 0\n")
            tn.write("show runni\n")
            tn.write("exit\n")

        elif i is "192.168.10.160":
            tn.read_until("Username:")  
            tn.write(user + "\n")
            if password:   
                tn.read_until("Password:")
                tn.write(password + "\n")   
            tn.write("en\n")
            tn.write("terminal length 0\n")
            tn.write("show runn\n\n")
            tn.write("exit\n\n")
            print(tn.read_all())
        readall + tn.read_all()
        File = open("File "+ str(i), "w")
        File.write(readall)
        File.write("\n")
        File.close()
        print("Backup of "+i+" completed") 
