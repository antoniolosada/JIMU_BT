import bluetooth
import time
from bluetooth import Protocols
from alpha_1s import Command

# ************************************************************************************************************************
# Mover un servo en continuo
#                  cmd   mode    s     d     v1    v2 (s=servo, d=direccion 1-2), v1, v2 = velocidad)
#const payload  = 0x07, [0x01, 0x01, 0x02, 0x01, 120];
#msg = message(b'\x07', [b'\x02',b'\x01',b'\x01',b'\x78'])
#msg = message(b'\x07', [b'\x01',b'\x01',b'\x01',b'\x01',b'\x00'])
#cmd 0x07 (modo x01 (mover s) modo x04 (todos menos s), modo x05 (todos))
# ************************************************************************************************************************

def main():
    #msg = message(b'\x22', [b'\x00',b'\x10',b'\x70',b'\x10',b'\x00'])
    #msg = message(b'\x09', [b'\x00',b'\x00',b'\x00',b'\x1c',b'\x01',b'\x01',b'\x01',b'\x20',b'\x01',b'\x79'])
    #msg = message(b'\x09', [b'\x00',b'\x00',b'\x00',b'\x1d',b'\x01',b'\x01',b'\x90',b'\x90',b'\x01',b'\x79'])

    #msg = message(b'\x07', [b'\x02',b'\x01',b'\x01',b'\x78'])
    #msg = message(b'\x07', [b'\x01',b'\x01',b'\x01',b'\x01',b'\x00'])
    #cmd 0x07 (modo x01 (mover s) modo x04 (todos menos s), modo x05 (todos))

    #msg = message(b'\x09', [b'\x00',b'\x00',b'\x00',b'\x1d',b'\x01',b'\x01',b'\x01',b'\x01',b'\x20',b'\x01',b'\x79'])
    #msg = message(b'\x09', [b'\x00',b'\x00',b'\x00',b'\x1e',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x20',b'\x01',b'\x79'])
    #msg = message(b'\x09', [b'\x00',b'\x00',b'\x00',b'\x1f',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x20',b'\x01',b'\x79'])
    #msg = message(b'\x09', [b'\x00',b'\x00',b'\x00',b'\x4d',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x20',b'\x01',b'\x79'])
    #msg = message(b'\x09', [b'\x00',b'\x00',b'\x00',b'\x4f',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x20',b'\x01',b'\x79'])
    #msg = message(b'\x09', [b'\x00',b'\x00',b'\x00',b'\xff',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x20',b'\x01',b'\x79'])
    #msg = message(b'\x09', [b'\x00',b'\x00',b'\x01',b'\x1d',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x20',b'\x01',b'\x79'])
    #activa todas las patas
    #msg = message(b'\x09', [b'\x00',b'\x00',b'\x0f',b'\xff',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x20',b'\x01',b'\x79'])
    #Activa todas las patas y la trompa del elefante
    #msg = message(b'\x09', [b'\x00',b'\x00',b'\xff',b'\xff',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x20',b'\x01',b'\x79'])
    
    #                                                           1       2       3       4      5       6       7       8       9       10      11      12      13      14      15      16
    msg = message(b'\x09', [b'\x00',b'\x00',b'\xff',b'\xff',b'\x70',b'\x18',b'\x5a',b'\x70',b'\x18',b'\x5a',b'\x78',b'\x14',b'\x35',b'\x78',b'\x14',b'\x35',b'\x73',b'\xa0',b'\x5a',b'\x5a',b'\x20',b'\x01',b'\x79'])
    
    print(msg)
    #bd_addr = discover()
    bd_addr = '88:1B:99:0A:B5:4F'
    if bd_addr:
        port = 6
        sock = bluetooth.BluetoothSocket(Protocols.RFCOMM)
        sock.connect((bd_addr, port))
        print('Connected')
        sock.settimeout(60.0)
        sock.send(msg)
        
        #for i in range(100):
        #    msg = message(b'\x09', [b'\x00',b'\x00',b'\x00',0x1c+i,b'\x01',b'\x01',b'\x01',b'\x20',b'\x01',b'\x79'])
        #    print(msg)
        #    sock.settimeout(60.0)
        #    sock.send(msg)
        #    c=input()
        print('Sent data 1')
        response = sock.recv(1024)
        print("Salida:")
        print(Command().get(response))
        
        #time.sleep(3)
        #print('Sent data 2')
        #msg = message(b'\x09', [b'\x00',b'\x00',b'\xff',b'\xff',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x01',b'\x20',b'\x01',b'\x79'])
        #sock.send(msg)
        sock.close()


def message(command, parameters):
    header = b'\xFB\xBF'
    end = b'\xED'
    parameter = b''.join(parameters)
    # len(header + length + command +parameters + check)
    length = bytes([len(parameters)+5])
    data = [command, length]
    data.extend(parameters)
    control = [sum(ord(x) for x in data) % 256] 
    check = bytes(control)
    return header+length+command+parameter+check+end


def discover():
    print("searching ...")
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("found %d devices" % len(nearby_devices))

    for addr, name in nearby_devices:
        if name == "Jimu_B54F":
            return addr


if __name__ == '__main__':
    main()
