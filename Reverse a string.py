from multiprocessing import Process, Pipe

def revr(conn, x):
  conn.send(x[::-1])


if __name__ == "__main__":
  print("Enter a word : ")
  a= input()
  parent, child = Pipe()
  p= Process(target=revr, args=(child,a))
  p.start()
  p.join()

  print("Reverse of Word : ")
  print(parent.recv())
