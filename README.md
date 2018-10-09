# ShowCollector

<<<<<<< HEAD
The script requires Python3 and netmiko to automatically install the dependecies do: pip3 install -r requirements.txt
=======
Simple script to do a *show* command on a bunch of Cisco IOS or NX-OS switches and create files that capture the output.

The script requires Python3 and netmiko.
>>>>>>> 588b204da1cb9759771eff9ec3ab7cd4934a5f45

Usage:

ShowCollector.py with the following parameters:

* --user [username to login in the switches]
* --password [cleartext password | ask]
* --switch [hostname | ip address | "," separated list of values | file.txt with switches in rows]
* --type [switch type nxos | ios]
* --command [the show command to execute between ""]

The script gives output in individual files using the switch name + the command.

Examples:

* ShowCollector.py --user john --password C1sco12345 --switch 1.1.1.1 --type nxos --command "show version"

* ShowCollector.py --user john --password ask --switch 1.1.1.1,2.2.2.2 -type ios --command "show running-config"

* ShowCollector.py --user john --password C1sco12345 --switch list.txt -type nxos --command "show ip bgp neighbor"
