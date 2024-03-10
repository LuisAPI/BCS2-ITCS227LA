# De La Salle University–Dasmariñas
# S-ITCS227LA — Application Development and Emerging Technologies (Laboratory)

# Luis Anton P. Imperial
# BCS22

# Monday, February 12, 2024
# Laboratory Activity No. 3

# Filename: ActList1.py
# Create a 5-input based that accept numbers and find sum, average and the smallest number of List in Python.
# Note: use sum() function in adding the list and use len() in finding the average of the list.
# Submit a pdf file (LabAct3_Surname) that contains the explanation of the code, include sample output screenshot and python file.

class numberList:
    def __init__(self):
        self.number_list: list = [];
        self.max_input: int = 5;
    
    def add(self):
        list_sum: float = sum(self.number_list);
        
        return list_sum;
    
    def take_average(self):
        list_sum = self.add();
        list_length: int = len(self.number_list);
        
        list_avg: float = list_sum / list_length;
        
        return list_avg;
    
    def take_minimum(self):
        list_min: float = min(self.number_list)
        
        return list_min;
    
    def show_interface(self):
        print("Number List Calculator", end="\n\n");
        
        input_requested = 0
        while input_requested < self.max_input:
            input_requested += 1;
            self.number_list.append(int(input(f"Input #{input_requested}: ")));
        
        print("Your inputs are:", self.number_list, end="\n\n");
        
        list_sum = self.add();
        list_avg = self.take_average();
        list_min = self.take_minimum();
        
        print("The sum of your numbers is:", list_sum);
        print("The average of your numbers is:", list_avg);
        print("The smallest number in your list is:", list_min);
        
        print("");
        print("Have a good day!");

def main():
    localCalc = numberList();
    localCalc.show_interface();

if __name__ == '__main__':
    main();