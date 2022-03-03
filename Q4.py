from multiprocessing import Process, Pipe


def hextoDandB(conn, x):
    conn.send([x, bin(x)])


if __name__ == "__main__":
    a = int(input("Enter a Hex value : "), 16)
    parent, child = Pipe()
    p = Process(target=hextoDandB, args=(child, a))
    p.start()
    p.join()

    c = parent.recv()
    print("Decimal format : ", c[0])
    print("Binary format : ", c[1])
