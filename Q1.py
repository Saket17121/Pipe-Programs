import uuid
from multiprocessing import Process, Pipe

def shared(conn):
    conn.send(((':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]))))

if __name__ == "__main__":
    parent, child = Pipe()
    p= Process(target=shared, args=(child,))
    p.start()
    p.join()

    print("MAC Address : ")
    print(parent.recv())