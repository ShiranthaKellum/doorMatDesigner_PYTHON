
def displayDesign (x, y):               
    for i in range(1, x+1):                     # part above the 'welcome' line
        k = (2 * i) - 1
        j = int((y - (3 * (k))) / 2)            # this 3 is the length of '.|.'
        print("-" * j, end="")
        print(".|." * k, end="")
        print("-" * j)

    print("-" * int((y - 7) / 2), end="")       # 7 is the size of 'WELCOME'
    print("WELCOME", end="")                
    print("-" * int((y - 7) / 2))

    for i in range(1, x+1):                     # part bellow the 'welcm' line
        j = (2 * (x+1-i)) - 1
        k = int((y - 3 * (j)) / 2)
        print("-" * k, end="")
        print(".|." * j, end="")
        print("-" * k)
    

if __name__ == "__main__":
    dimentions = list (map (int, input ().split ()))
    n = int ((dimentions [0] - 1) / 2)

    displayDesign (n, dimentions [1])
