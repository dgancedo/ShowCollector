######
# Author: Diego S. Gancedo <dgancedo@gmail.com>
# Desc: Script to connect nexus or ios switches over ssh and execute a command passed the script generate an output file using the hostname of the switch + the command
# Requirements: Netmiko
######

import sys, getopt, os, getpass
from netmiko import ConnectHandler


def main(argv):
   user = ''
   password = ''
   switch = ''
   devtype = ''
   command = ''
   try:
      opts, arg = getopt.getopt(argv,"hi:o:",["user=","password=","switch=","type=","command="])
   except getopt.GetoptError:
      print('ShowCollector.py --user <username> --password <ask|password> --switch <hostname|IP|list separated with ","|file.txt> --type [nxos|ios] --command <"command">')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('ShowCollector --user <username> --password <ask|password> --switch <hostname|IP|list separated with ","|file.txt> --type [nxos|ios] --command <"command">')
         sys.exit()
      elif opt in ("--user"):
         user = arg
      elif opt in ("--type"):
         if arg == 'nxos':
            devtype = 'cisco_nxos'
         elif arg == 'ios':
            devtype = 'cisco_ios'
         else:
            print ('Invalid device type')
            sys.exit()
      elif opt in ("--password"):
         if arg == 'ask':
            password = getpass.getpass()
         else:
            password = arg
      elif opt in ("--switch"):
         switch = arg
      elif opt in ("--command"):
         command = arg
   return user,password,switch,devtype,command

if __name__ == "__main__":
   values=main(sys.argv[1:])
   if values[0] != "" and values[1] != "" and values[2] != "" and values[3] !="" and values[4] !="":
      switches = []
      if ".txt" in values[2]:
         s = open(values[2],'r')
         for line in s:
            switches.append(line.replace("\n",""))
      elif "," in values[2]:
         switches = values[2].split(",")
      else:
         switches.append(values[2])
      for switch in switches:
         net_connect = ConnectHandler(device_type=values[3], ip=switch, username=values[0], password=values[1]) 
         if values[3] == "nxos":
            switchname = net_connect.send_command("show hostname")
         else:
            switchname = net_connect.send_command("show running-config | i hostname").split(" ")[1]
         print("Executing "+ values[4] + " on " + switchname)
         show = net_connect.send_command(values[4])
         filename = switchname.replace(" ","_") + "-" + values[4].replace(" ", "_") + ".txt"
         f = open(filename,'w')
         f.write(show)
         f.close
         print("File " + filename + " generated with the output")
   else:
      print('ShowCollector.py --user <username> --password <ask|password> --switch <hostname|IP|list separated with ","|file.txt> --type [nxos|ios] --command <"command">')  
