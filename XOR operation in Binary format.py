from multiprocessing import Process, Pipe


def revr(conn, x):
    res = 0
    s = bin(x)
    print("Binary of the input number : ",s)
    d = 0b10101011

    for i in range(32, -1, -1):
        val1 = x & (1 << i)
        val2 = d & (1 << i)

        val1 = min(val1, 1)
        val2 = min(val2, 1)

        BitVal = 0
        if (val1 & val2):
            BitVal = 0
        else:
            BitVal = (val1 | val2)
        res <<= 1;
        res |= BitVal

    conn.send(res)


if __name__ == "__main__":
    print("Enter a value : ")
    a = int(input())
    parent, child = Pipe()
    p = Process(target=revr, args=(child, int(a)))
    p.start()
    p.join()

    print("After XOR with 10101011 the decimal value : ")
    print(parent.recv())
