import pickle
from socket import *
# Multicast group parameters
tab=[[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]]
group_addr = "localhost"
port = 2223
# Stworzenie socketa
sock = socket(AF_INET, SOCK_DGRAM)
# Opcje socketa
sock.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, 32)
sock.setsockopt(IPPROTO_IP, IP_MULTICAST_LOOP, 1)
# Wiadomości
czyMojaKolej = sock.recv(4096).decode('utf-8')
while True:
    #odczytaj z klawiatury
    data = input("strzelaj: ")
    #wysłij wiadomość
    sock.sendto(data.encode('utf-8'), (group_addr, port))
    #wypisz wiadomość zwrotną

    while czyMojaKolej == '-1':
        print('Ruch przeciwnika, czekaj...')
        czyMojaKolej = sock.recv(4096).decode('utf-8')
        tab=pickle.loads(sock.recv(4096))
    print(tab)
sock.close()
