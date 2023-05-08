# THM-Flask
A simple script to make LFI even easier on the THM [Flask](https://tryhackme.com/room/flask) box. 

<p align="center">
  <img src="https://tryhackme-badges.s3.amazonaws.com/wuu.png" alt="Tryhackme | Wuu"/>
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/csduncan06/THM-Flask/main/Screenshot%202023-01-28%20054330.png" alt="Tryhackme | Wuu"/>
</p>


This is a Python script for exploiting a local file inclusion (LFI) vulnerability in a Flask web application on TryHackMe.

## Prerequisites
Python 3.x
requests library


$ python exploit.py --ip 10.10.10.10 --lfi /etc/passwd --port 8080
This command will send a GET request to http://10.10.10.10:8080/vuln?name=/etc/passwd, exploiting the LFI vulnerability to retrieve the contents of the /etc/passwd file.

## Usage

```bash
$ python exploit.py [--ip <machine_ip>] [--lfi <lfi_payload>] [--port <port_number>]
```
## Options
--ip: The IP address of the machine running the vulnerable Flask server.
--lfi: The LFI payload to use.
--port: The port number to use for the Flask server (default 5000).

## Dependencies
This script requires the `argparse` and `requests` Python libraries.

