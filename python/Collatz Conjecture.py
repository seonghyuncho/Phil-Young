def Collatz():
    start = int(input("Enter a number: "))
    steps = 0
    while(start > 1):
                        if(start % 2 == 0):
                                start = start / 2
                                steps = steps + 1
                        elif(start % 2 == 1):
                                start = (start * 3) + 1
                                steps = steps + 1
                        if(start == 1):
                                print("It took ", steps, " steps to get to 1.")

Collatz()
