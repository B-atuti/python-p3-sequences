
#!/usr/bin/env python3

def print_fibonacci(length):
   fibonacci_arr = list()
   if length == 0:
      print( fibonacci_arr)
   elif length == 1:
      fibonacci_arr.append(0)
      print(fibonacci_arr)
   elif length == 2:
      fibonacci_arr.extend([0,1])
      print(fibonacci_arr)
   elif length > 2:
      fibonacci_arr.extend([0,1])
      for i in range(length-2):
         fibonacci_arr.append(fibonacci_arr[-1] + fibonacci_arr[-2])
      print(fibonacci_arr)

print_fibonacci(10)