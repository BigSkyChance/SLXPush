import netmiko
import time

IPlist = []
for ip in open('iplist.txt', 'r').readlines():
  IPlist.append(ip.strip())
  
def main(IPlist):
  for IP in IPlist:
    VCPSLX = netmiko.ConnectHandler(ip = IP, device_type = 'extreme_slx', username = 'username', password = 'password')
    print(VCPSLX.send_command('show version'))
    time.sleep(2)
    VCPSLX.send_command('firmware download REDACTED LINE') # Code download begins on first switch
    VCPSLX.disconnect() # disconnects from switch
    time.sleep(300) # Spaces out downloads as to not overload jump server
    
main(IPlist)

