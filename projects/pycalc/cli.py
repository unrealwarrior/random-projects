import math
import sys
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
        "M" : "Memory Operations",
        "c": "clear everything",
        "h": "show history",
        "e": "Exit the program.",
        "n": "Do nothing."
        

    }
    MEMORY_OPERATIONS = {
        "MC" : "Memory Clear",
        "MR": "Memory Recall",
        "MS" : "Memory Save",
        "M+" : "Memory Add",
        "M-": "Memory Subtract"
    }
    def __init__(self) -> None:
        self.history = list()
        self.first_run = True
        self.memory = 0
        self.user_input = ""
    
    @property
    def first_run(self):
        return self._first_run
    
    @first_run.setter
    def first_run(self, value):
        self._first_run = value

    @property
    def user_input(self):
        return self._user_input

    @user_input.setter
    def user_input(self, value):
        self._user_input = value

    @property
    def memory(self):
        return self._memory
    
    @memory.setter
    def memory(self, value):
        self._memory = value
    
    @property
    def history(self):
        return self._history
    
    @history.setter
    def history(self, value):
        self._history = value

    # clear everything after a restart
    def clear_all(self):
        self.memory = 0
        self.user_input = ""
        self.history.clear()
        self.first_run = True

    # memory operations
    def clear_memory(self):
        print("Memory Cleared!!!")
        self.memory = 0
    
    def recall_memory(self):
        print(f"Value stored in memory: {self.memory}")
        return self.memory
    
    def save_memory(self):
        print(f"Last memory value : {self.memory} \\ Changed to: {self.user_input}")
        self.memory = int(self.user_input)
        
    def memory_add(self):
        # add the current value in self.user_input
        res = self.memory + int(self.user_input)
        print(f"Memory added from {self.memory} to {res}")
        self.memory = res

    def memory_subtract(self):
        res = self.memory - int(self.user_input)
        print(f"Memory subtracted from {self.memory} to {res}")
        self.memory = res    
    
    # display and execute memory operations
    def mem_operations(self):
        while True:
            for key, value in self.MEMORY_OPERATIONS.items():
                print(f"{key}: {value}")
            opr = input("> Select your operation, Q to quit: ")
            if opr in ["mc", "MC"]:
                self.clear_memory()
            elif opr in ["mr", "MR"]:
                self.recall_memory()
            elif opr in ["ms", "MS"]:
                self.save_memory()
            elif opr in ["m+", "M+"]:
                self.memory_add()
            elif opr in ["m-", "M-"]:
                self.memory_subtract()
            elif opr in ["q", "Q"]:
                break
            else:
                print("Wrong input. Choose from the options above.")
                continue

    # display input messages
    def display_available_methods(self):
        while True:
            if self.first_run:
                for key, value in self.OPERATIONS.items():
                    print(f"{key}= {value}")
                self.first_run = False
            if self.first_run == False:
                print("d to display all available methods.")
            opr = input("\n> Choose from available methods: ")
            if opr in ["e", "E"]:
                sys.exit()
            elif opr in ["n", "N"]:
                return "n"
            elif opr in ["d", "D"]:
                self.first_run = True
                continue
            elif opr in ["m", "M"]:
                self.mem_operations()
                continue
            elif opr in ["c", "C"]:
                print("Restarting...")
                self.clear_all()
                self.main()
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
        self.history = self.history[:(user_input + 1)]
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
        print("history: ")
        print(self.history)

    def main(self):
        res = 0
        self.user_input = self.get_user_input("First")
        opr = self.display_available_methods()
        if opr in self.VALID_OPERATORS:
            self.save_history(self.user_input, opr)
        while True:

            while opr in self.VALID_OPERATIONS:
                self.save_history(self.user_input, opr)
                self.user_input = self.evaluate_results(self.user_input, operator=opr)
                opr = self.display_available_methods()

            if isinstance(opr, int): 
                self.user_input = opr  
                opr = self.display_available_methods()
                continue  

            temp = self.user_input

            self.user_input = self.get_user_input("second")
            subopr = self.display_available_methods()
            if isinstance(subopr, int):
                self.user_input = subopr
                opr = self.display_available_methods()
                continue

            self.save_history(self.user_input, opr)
            if subopr in self.VALID_OPERATIONS:
                self.save_history(self.user_input, subopr)
                self.user_input = self.evaluate_results(first_input=self.user_input, operator=subopr) 

                
            res = self.evaluate_results(first_input=temp, operator=opr, second_input=self.user_input)
            print(f"results: first: {temp} and second: {self.user_input} = {res}")
            # first_input = res

            # hacky, I know, but this will override the temp variable with the last results
            # from the the input from the first one
            self.user_input = res

            opr = self.display_available_methods()
            if isinstance(opr, int): 
                self.user_input = opr  
                opr = self.display_available_methods()
                continue  

        # # calling the function itself is a form of resetting everything
        # # exiting the program will call sys.exit()
        # self.main()




x = BasicCalc()
x.main()

