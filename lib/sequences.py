
#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = []
    
    if length > 0:
        fibonacci_sequence.append(0)
        
        if length > 1:
            fibonacci_sequence.append(1)
            
            if length > 2:
                for i in range(2, length):
                    fibonacci_sequence.append(
                        fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
                
    return fibonacci_sequence

length = int(input("Enter the length of Fibonacci sequence: "))
fibonacci_sequence = print_fibonacci(length)
print(fibonacci_sequence)
