# Sneaky Ransom Malware
## Overview
Sneaky Ransom is a stealthy ransomware designed to attack Linux machines running version 6.6.15-arm64. The ransomware encrypts all files from a specified root directory and creates a ransom message file on the desktop of the victim's computer. Additionally, it exfiltrates sensitive data to the attacker's server using HTTP POST requests.

The malware uses several obfuscation techniques to evade detection and ensure that the attack remains undetected for as long as possible.


## Demo
### Message Disiplayed
Malware Saves Text file to the desktop of the Victim. The text file contains information about the malware and provides details for the user to make payment.
The message contains a way to make payment through cryptocurrency so that the payment can be made anonymously to the attacker and the attacker cannot be traced.

![Display Message](https://snipboard.io/x07vAP.jpg)

![Display Message](https://snipboard.io/A7nv24.jpg)

### Data Exfiltrated
The ransomware exfiltrates sensitive data by sending it to a remote server using HTTP POST requests. The following files are targeted for exfiltration:

**/etc/passwd** (user account info)

**/etc/shadow** (hashed passwords)

**/etc/network/interfaces** (network configuration)

**/etc/sysctl.conf** (kernel parameters)

**/var/log/auth.log** (login attempts)

**/var/log/syslog** (system messages)


The data is exfiltrated in small, **Base64-encoded** chunks at random intervals to avoid detection.

*WireShark Screenshot of small chunks of data being sent to exfiltrated server*

![Wireshark Data](https://snipboard.io/qnuScP.jpg)


 *Decoded Data*

 ![Decoded Data](https://snipboard.io/ux0iry.jpg)
## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the obfuscated code directory : dist

```bash
  cd LabQ1
```

Install dependencies
```bash
  pip3 install -r requirements.txt
```

Start the server

```bash
  cd server_exfil && python3 server.py
```

Nanvigate to Obfuscated code and Run Malware

```bash
  cd ../dist && python3 Lab_Quiz1_Malware.py
```

