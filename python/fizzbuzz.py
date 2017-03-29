#Not the most efficient code...
def FizzBuzz():
        start = 1
        end = 100
        while(start <= end):
                #It first checks whether it's divisible by 3 and 5
                if(start % 5 == 0 and start % 3 == 0):
                        print("fizzbuzz")
                        start = start + 1
                elif(start % 3 == 0):
                        print("fizz")
                        start = start + 1
                elif(start % 5 == 0):
                        print("buzz")
                        start = start + 1
                else:
                        print(start)
                        start = start + 1

FizzBuzz()
