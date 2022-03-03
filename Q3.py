from multiprocessing import Process, Pipe

def ascend(conn, x):
  x.sort(reverse = False)
  conn.send(x)

if __name__ == "__main__":
  print("Enter 10 numbers to get sorted list")
  num_list= [int(input()) for item in range(10)]
  parent, child = Pipe()
  p= Process(target=ascend, args=(child,num_list))
  p.start()
  p.join()

  print("Sorted List : ")

  print(parent.recv())