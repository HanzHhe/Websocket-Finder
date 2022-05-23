import socket, ssl, sys, warnings, os

us = "Penggunaan: python wsfind.py <FILE LIST SUBDOMAIN>"
warnings.simplefilter('ignore', category=DeprecationWarning)

if len(sys.argv) == 1:
   print(us)
try:
  host = open(sys.argv[1], 'r')
except:
  exit()

ssh = 'sg-public1.sshws.net'
payload = "GET / HTTP/1.1\r\nHost: {}\r\nUpgrade: websocket\r\n\r\n".format(ssh)
hasil = open('hasil.txt', 'w')
hsr = open('hasil.txt', 'r')
hsa = open('hasil.txt', 'a')

os.system('clear')
print("Timeout: 10")
print('Author: \033[1;31m./Brainerror\n\033[0;0mFacebook: \033[1;31mhttps://www.facebook.com/hanz.ii.180\n\033[0;0m')

for dom in host.read().splitlines():
  try:
    ip = socket.gethostbyname( dom )
  except:
    print(f"Host: {dom} Tidak Ditemukan")
    pass
  port = 80
  sock = socket.socket()
  sock.settimeout(7)
  try:
     sock.connect_ex((ip, port))
  except:
     pass
  print(f"Mengirim Payload Ke: {dom}")
  try:
     sock.send(payload.encode())
     data = sock.recv(8192).decode()
     if '101' in data:
        print(f"\033[1;32mBug Ditemukan: {dom}\nSocket: {ip}:{port}\n\033[0;0m")
        print(data)
        if 'Bug' in hsr.read():
           hsa.write(f"Bug: {dom}\nSocket: {ip}:{port}\nPayload: GET / HTTP/1.1[crlf]Host: isi ssh klean[crlf]Upgrade: websocket[crlf][crlf]\n\nYNTKTS: {data}\n\n")
        else:
           hasil.write(f"Bug: {dom}\nSocket: {ip}:{port}\nPayload: GET / HTTP/1.1[crlf]Host: isi ssh klean[crlf]Upgrade: websocket[crlf][crlf]\nYNTKTS: {data}")
     else:
        print(f"\033[1;31mBug WS Tidak Ditemukan Di Host: {dom}\nSocket: {ip}:{port}\n\033[0;0m")
     sock.close()
  except:
     sock.close()
     pass
  payload = "GET wss://{}/ HTTP/1.1\r\nHost: {}\r\nUpgrade: websocket\r\n\r\n".format(dom, ssh)
  sock = socket.socket()
  cont = ssl.SSLContext()
  sl = cont.wrap_socket(sock, server_hostname=dom)
  sl.do_handshake_on_connect
  sl.settimeout(7)
  port = 443
  try:
     sl.connect_ex((dom, port))
     sl.getpeercert()
     sl.context.load_default_certs()
  except:
     print(f"\033[1;31mHandshake Timeout")
     pass
  try:
     sl.send(payload.encode())
     data = sl.recv(1024).decode()
     if '101 S' in data:
         print(f"\033[1;32mBug Ditemukan: {dom}\nSocket: {ip}:{port}\nSni: {dom}\n\033[0;0m")
         print(data)
         if 'Bug' in hsr.read():
           hsa.write(f"Bug: {dom}\nSocket: {ip}:{port}\nPayload: GET / HTTP/1.1[]Host: isi ssh klean[crlf]Upgrade: websocket[crlf][crlf]\n\nYNTKTS: {data}\n\n")
         else:
           hasil.write(f"Bug: {dom}\nSocket: {ip}:{port}\nPayload: GET / HTTP/1.1[crlf]Host: isi ssh klean[crlf]Upgrade: websocket[crlf][crlf]\nYNTKTS: {data}")
     else:
         print(f"\033[1;31mBug WSS Tidak Ditemukan Di Host: {dom}\nSocket: {ip}:{port}\n\033[0;0m")
         print(data)
  except:
     print(f"\033[1;31mHost SNI Dari: {dom} Tidak Ditemukan\n\033[0;0m")
