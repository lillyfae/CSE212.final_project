"""Back story: You are making pancakes for your family and friends. Every time you make a pancake, it comes out a 
little bit different. 

For your program:

Write an add_pancakes function and an eat_a_pancake function so that it will either add to the stack or remove from the stack of pancakes. 
"""



class Pancakes():
    def __init__(self):
        self.stack_of_pancakes = []

    def add_pancake(self, pancake):
        self.stack_of_pancakes.append(pancake)

    def eat_a_pancake(self):
        self.stack_of_pancakes.pop()



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