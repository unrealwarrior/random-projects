import math
import sys
class BasicCalc():
    VALID_OPERATORS = ["+", "-", "*", "/"]
    VALID_OPERATIONS = ["sqrt", "reciproc"]

    OPERATIONS = {
        "+" : "Add Number",
        "/" : "Divide Number",
        "*" : "Multiply Number",
        "-" : "Subtract Number",
        "sqrt": "Get the square root of a number",
        "reciproc" : "reciproc = Get the reciprocal of a number",
        "e": "\n Exit the program."

    }
    def __init__(self) -> None:
        pass
    
    # display input messages
    def display_available_methods(self):
        for key, value in self.OPERATIONS.items():
            print(f"{key} = {value}")
        opr = input("\n > Choose from available methods: ")
        if opr in ["e", "E"]:
            sys.exit()
        while opr not in self.OPERATIONS.keys():
            opr = input("\n > Choose from available methods: ")
            print("Invalid operator.")
        print(f"User input : {opr}")
        return opr


    # basic, but it gets the job done
    def reciproc(self, number):
        return (1 / number)
    
    def get_user_input(self, value_string):
        user_input = input("Enter the %s value: " % value_string)
        while not user_input.isnumeric() and (float(user_input).is_integer()):
            print("Input is not a number. Try again.")
            user_input = input("Enter the %s value: " % value_string)
        return user_input
    

    def get_user_operator(self):
        opr = input("Enter the operator: ")
        while opr not in self.VALID_OPERATIONS and opr not in self.VALID_OPERATORS:
            print(f"Wrong operator, try again with the following: {self.VALID_OPERATORS}")
            opr = input("Enter the operator: ")
        return opr
    
    def evaluate_results(self, first_input, operator, second_input=None):
        if first_input == None:
            raise ValueError("You need at least to enter the first input.")
        if operator in self.VALID_OPERATORS:
            if second_input == None:
                raise ValueError("You need to enter the second input.")
            res = eval(f"{first_input} {operator} {second_input}")
            # print(f"The result of {first_input} {operator} {second_input} is: {res}")
            return res 
        elif operator == "sqrt":
            res = math.floor(math.sqrt(int(first_input)))
            print(f"The square root of {first_input} is: {res}")
        elif operator == "reciproc":
            res = self.reciproc(int(first_input))
            print(f"Reciprocal of {first_input} is {res}")
        
        
        
    def main(self):
        while True:
            first_input = self.get_user_input("First")
            # opr = self.get_user_operator()
            opr = self.display_available_methods()
            if opr in self.VALID_OPERATIONS:
                self.evaluate_results(first_input, operator=opr)
            else:
                second_input = self.get_user_input("Second")
                res = self.evaluate_results(first_input, operator=opr, second_input=second_input)
                print(f"{first_input} {opr} {second_input} = {res}")

                while True:
                    opr = self.display_available_methods()
                    if opr in self.VALID_OPERATIONS:
                        self.evaluate_results(res, operator=opr)
                    else:
                        x = input("Enter next input: ")
                        res = self.evaluate_results(first_input=res, operator=opr, second_input=x)
                        print(f"{res} {opr} {x} = {res}")







x = BasicCalc()
x.main()