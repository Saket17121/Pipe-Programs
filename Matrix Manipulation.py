import numpy as np
from multiprocessing import Process, Pipe

def matrixM(conn, a):
    mat1 = np.array(a[0:4]).reshape(2,2)
    print("Matrix 1 :\n",mat1)
    mat2 = np.array(a[4:8]).reshape(2,2)
    print("Matrix 2 :\n",mat2)
    conn.send([mat1 + mat2, mat1 - mat2])


if __name__ == "__main__":
    print("Enter 8 elements")
    num_list= [int(input()) for item in range(8)]
    parent, child = Pipe()
    p= Process(target=matrixM, args=(child,num_list))
    p.start()
    p.join()
    output = parent.recv()
    print("matrix sum :\n", output[0])
    print("matrix difference :\n", output[1])
