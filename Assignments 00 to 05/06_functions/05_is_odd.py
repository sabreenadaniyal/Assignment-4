# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

def Odd():
    for num in range(10, 20):
        if num % 2 == 0:
            print(f"{num} even")
        else:
            print(f"{num} odd")

if __name__ == "__main__":
    Odd()
