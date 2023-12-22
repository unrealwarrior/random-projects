import math
import sys
import time
# redo ability and save history
# memory stuff
# parse a full operation
class BasicCalc():
    VALID_OPERATORS = ["+", "-", "*", "/", "%"]
    VALID_OPERATIONS = ["sqrt", "reciproc", "abs"]

    OPERATIONS = {
        "+" : "Add Number",
        "/" : "Divide Number",
        "*" : "Multiply Number",
        "-" : "Subtract Number",
        "%" : "Get the percentage of a number",
        "sqrt": "Get the square root of a number",
        "reciproc" : "Get the reciprocal of a number",
        "abs": "Negate a number",
        "c": "clear everything",
        "h": "show history",
        "e": "Exit the program.",
        "n": "Do nothing."

    }
    def __init__(self) -> None:
        self.history = list()
    
    @property
    def history(self):
        return self._history
    
    @history.setter
    def history(self, value):
        self._history = value

    # display input messages
    def display_available_methods(self):
        while True:
            for key, value in self.OPERATIONS.items():
                print(f"{key} = {value}")
            opr = input("\n> Choose from available methods: ")
            if opr in ["e", "E"]:
                sys.exit()
            elif opr in ["n", "N"]:
                return "n"
            elif opr in ["h", "H"]:
                res = self.show_history()
                if res == "b":
                    continue
                elif isinstance(res, int):
                    return self.get_results_from_history(res)
            while opr not in self.OPERATIONS.keys():
                opr = input("\n> Choose from available methods: ")
                print("Invalid operator.")
                continue
            print(f"User input : {opr}")
            break
        return opr
    
    def get_results_from_history(self, user_input):
        res = 0
        while user_input > len(self.history):
            print("invalid number. Try again.")
            user_input = int(input(f"Choose from 0 to {len(self.history)}: "))
            print(user_input)
            continue

        print(self.history[:(user_input + 1)])
        res = 0
        for n in self.history[: (user_input + 1)]:
            x = n.split(" ")
            if len(x) == 2:
                opr = x[0]
                num = int(x[1])
                res = self.evaluate_results(first_input=num, operator=opr, second_input=res)
            else:
                res += int(x[0])
        print(f"res : {res}")
        return res
    
    # show history of operations made by user
    def show_history(self):
        if len(self.history) <= 1:
            print("no history to show.")
        else:
            for index, his in enumerate(self.history):
                print(f"{index} - {his}")
            user_input = int(input(f"Choose from 0 to {len(self.history)}: "))
            print("b to go back")
            if user_input == "b":
                return "b"
            else:
                return user_input

        
    # negate a number
    def negate(self, num):
        num = int(num)
        if num < 0:
            return abs(num)
        else:
            return -abs(num)
    # get the percentage of a number
    def perc(self, num1, num2):
        print(f"{num1} // {num2}")
        res = (num1 * num2) / 100.0
        print(res)
        return res
    # basic, but it gets the job done
    def reciproc(self, number):
        return (1 / number)
    
    def get_user_input(self, value_string):
        user_input = input("Enter the %s value: " % value_string)
        
        while True:
            try:
                while not float(user_input) and float(user_input).is_integer():
                    print("Input is not a number. Try again.")
                    user_input = input("Enter the %s value: " % value_string)
                break
            except ValueError:
                print("try/block error!")
                print("Input is not a number. Try again.")
                user_input = input("Enter the %s value: " % value_string)    
                continue
        print(user_input)
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
        elif operator == "sqrt":
            res = math.floor(math.sqrt(int(first_input)))
            print(f"The square root of {first_input} is: {res}")
        elif operator == "reciproc":
            res = self.reciproc(int(first_input))
            print(f"Reciprocal of {first_input} is {res}")
        elif operator == "%":
            res = self.perc(first_input, second_input)
        elif operator == "abs":
            res = self.negate(first_input)
        print(f"results : {res}")
        return res
    
    def save_history(self, num, opr):
        if len(self.history) == 0 and opr not in self.VALID_OPERATIONS:
            self.history.append(f"{num}")
        else:
            self.history.append(f"{opr} {num}")
            # if opr in self.VALID_OPERATIONS:
            #     self.history.append(f"{opr}({num})")
            # else:
            #     self.history.append(f"{opr} {num}")
        print("history: ")
        print(self.history)

    def main(self):
        first_input = self.get_user_input("First")
        opr = self.display_available_methods()
        if opr in self.VALID_OPERATORS:
            self.save_history(first_input, opr)
        while True:
            

            while opr in self.VALID_OPERATIONS:
                self.save_history(first_input, opr)
                first_input = self.evaluate_results(first_input, operator=opr)
                opr = self.display_available_methods()

            if isinstance(opr, int): 
                first_input = opr  
                opr = self.display_available_methods()
                continue  

            second_input = self.get_user_input("second")
            subopr = self.display_available_methods()
            if isinstance(subopr, int):
                first_input = subopr
                opr = self.display_available_methods()
                continue

            self.save_history(second_input, opr)
            if subopr == "c":
                break
            if subopr in self.VALID_OPERATIONS:
                self.save_history(second_input, subopr)
                second_input = self.evaluate_results(first_input=second_input, operator=subopr) 

                
            res = self.evaluate_results(first_input=first_input, operator=opr, second_input=second_input)
            print(f"results: first: {first_input} and second: {second_input} = {res}")
            first_input = res
            opr = self.display_available_methods()
            if isinstance(opr, int): 
                first_input = opr  
                opr = self.display_available_methods()
                continue  


        # calling the function itself is a form of resetting everything
        # exiting the program will call sys.exit()
        self.main()




x = BasicCalc()
x.main()
