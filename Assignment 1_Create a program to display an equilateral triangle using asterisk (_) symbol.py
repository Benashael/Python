def triangle(n):
   for i in range(1, n+1):
      print(' ' * n, end='')
      print('* '*(i))
      n -= 1
n = int(input("Please enter no of rows:"))
triangle(n)