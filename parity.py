# x = int(input("whats x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("odd")

def main():
    x = int(input("whats x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd") 

def is_even(n):
  return True if n % 2 == 0 else False

main()               