# Stacks
    
    The way a stack works is first in, last out. A good way to visualize this is a stack of pancakes. When you add pancakes to the plate, 
    
    the first one gets cover up and the last ones added get taken first, because they are on the top. An easy way to see one of the  
    
    purposes of a stack is any where there is more than one function call. When we call a function, it then goes to that function and 
    
    runs it. Where will go after it runs that function? It will go back to the code it was running before the function call and keep 
    
    going. The `Big O notation` of using a stack is `O(1)` because it never doubles up, it never cuts in half, it just keeps running  
    
    until the stack is empty. 

    When running any program that has more than one funtion call, it uses stacks. In python, let's look at if we were to call main that 
    
    has several other function calls in it:
```
     def main():
        director()
        gains()
        losses()
        totals()
```

    In this example, the stack is straight forward, you call main and it gets added on to the stack:
    
       ` main `

    And before main is able to finish running, you call director and it gets added onto the stack.

       ` main, director `
    
    When director is finished running, it is taken off of the stack:

      `  main `

    And the program goes back to main to finish running it. Next it calls gains, so that is added to the stack:

      `  main, gains `

    and so on, the rest of the stack for main would look like:

      `  main

        main, losses

        main

        main, totals

        main `
    
    and finally, when main is done running, that is taken off the stack as well. 

    Now let's say instead of all the functions being called by main, they were instead called by different functions.  
    
    For the sake of the example, we will only being showing the function calls and where they are in the code instead of working code: 

```
    main()

    def main():

        director()
        totals()

    def director():

        gains()

    def gains():

        losses()
```


    In this example, the stack would look like this:
       
        -main is called and added to the stack

        `main`

        -while main is still running, it calls director

        `main, director`

        -while director is still running, it calls gains

        `main, director, gains`

        -while gains is still running, it calls losses

        `main, director, gains, losses`

        -when losses is finished running, the program goes back to finish gains

        `main, director, gains`

        -when gains in finished running, it goes back to finish director

        `main, director`

        -when director is finished running, it goes backto finish main

       ` main`

        -the next code in main is the totals function call, so that is added to the stack

        `main, totals`

        -once totals is done running, the program goes back to main to finish running

        `main`

        and finally, the program finishes and main is taken off the stack.

    When using a stack, error codes in python will show all the functions that were called up until that point. 
    
    Let's say that we had an error in the losses function of our last example. The error code would look something like:

       ` Error Has Occurred: TypeError

         File "Example.path/file_name.py" in line number in main

         File "Example.path/file_name.py" in line number in director

         File "Example.path/file_name.py" in line number in gains

         File "Example.path/file_name.py" in line number in losses `
        
# Example of using a stack in Python:

```
def main():

    call_stack = ["main"]
    print(call_stack)

    # sets the return of director equal to wins
    wins = director(call_stack) # calls director

    totals(wins, call_stack) # calls totals with the parameter of wins
    call_stack.pop()
    print(call_stack)

def director(call_stack):

    call_stack.append("director")
    print(call_stack)

    print("Welcome. This program will tell you your win/lose stats")

    # sets the result of gains equal to the gains function
    won = gains(call_stack) # calls gains

    call_stack.pop()
    print(call_stack)

    return won # returns the result od gains back to director

def gains(call_stack):

    call_stack.append("gains")
    print(call_stack)

    # sets the result of the losses function equal to lost  
    lost = losses(call_stack) # calls the losses function

    # calculates how many wins from how many losses  
    wins = 10 - lost 

    call_stack.pop()
    print(call_stack)

    return wins


def losses(call_stack):

    call_stack.append("losses")
    print(call_stack)

    # gets the number of losses from the user
    user_input = int(input("How many games out of 10 did you lose?   "))

    call_stack.pop()
    print(call_stack)

    # returns number of losses for the gains function to use 
    return user_input

def totals(wins, call_stack):

    call_stack.append("totals")
    print(call_stack)

    #calculates the percent won by number of wins pass in as a parameter
    percent_won = wins * 10

    # finds the percentage lost
    percent_lost = 100 - percent_won

    # prints the results
    print("You won " + str(percent_won) + " percent of the time and lost " + str(percent_lost) 
    + " percent of the time. ")

    # tells the user if the won more, they did ok if not, they could do better
    if percent_won < 50:
        print("You lost more often than not...Come on, you can do better than that!")

    else:
        print("I guess you did ok.")

    call_stack.pop()
    print(call_stack)

main()

```

# Student Problem:

```
"""Back story: You are making pancakes for your family and friends. Every time you make a pancake, it comes out a 
little bit different. 

For your program:

Write an add_pancakes function and an eat_a_pancake function so that it will either add to the stack or remove from the stack of pancakes. 
"""



class Pancakes():
    def __init__(self):
        self.stack_of_pancakes = []

    def add_pancake(self, pancake):
        pass

    def eat_a_pancake(self):
        pass



# Test Case 

def main():
    pancakes = ["one with the lump", "one a little burnt", "undercooked", "perfect", "too round", "too fat",
    "too thin"]

    pancake = Pancakes()
    pancake.add_pancake(pancakes[0])
    pancake.add_pancake(pancakes[1])
    pancake.add_pancake(pancakes[2])
    pancake.eat_a_pancake()
    pancake.add_pancake(pancakes[3])
    pancake.eat_a_pancake()
    pancake.eat_a_pancake()
    pancake.add_pancake(pancakes[4])
    pancake.add_pancake(pancakes[5])
    pancake.add_pancake(pancakes[6])
    pancake.eat_a_pancake()
    pancake.eat_a_pancake()
    print(pancake.stack_of_pancakes) # ('one with the lump', 'too round')

main()

```