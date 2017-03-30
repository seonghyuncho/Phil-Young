def FizzBuzz():
    start = 1
    end = 100
    while(start <= end):
        if(start % 3 == 0):
            if(start % 5 == 0):
                print("FizzBuzz")
                start = start + 1
            print("Fizz")
            start = start + 1
            elif(start % 5 == 0):
                print("Buzz")
                start = start + 1
            else:
                print(start)
                start = start + 1
FizzBuzz()
