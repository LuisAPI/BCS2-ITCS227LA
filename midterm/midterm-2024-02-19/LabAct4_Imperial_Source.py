# # De La Salle University–Dasmariñas
# S-ITCS227LA — Application Development and Emerging Technologies (Laboratory)

# Luis Anton P. Imperial
# BCS22

# Monday, February 19, 2024
# Laboratory Activity No. 4

# Create a 5-user input list that accept either string or number then select an item randomly from a list and remove the selected item randomly in the list.
# Submit a pdf file (LabAct4_Surname) that contains the explanation of the code and include 3 sample output screenshot and python file.

# Get module that contains core functionality needed.
import random;

# Create modular class that can be used in other scripts.
class randomFromList:
    def __init__(self):
        # Define name of app, used for greetings at start/end.
        self.app_name: str = "MyRandomizer";
        
        # Initialize list for items to be placed on
        self.list: list = [];
        
        # Describe the number of items to ask for. Default is 5.
        self.list_items: int = 5;
    
    # When this function is run, it will ask for an element one time.
    def add_element(self):
        # Ask for input and place it into a variable.
        input_to_add = input("Enter either a string or a number: ");
        
        # Add value of said variable into the list we created earlier.
        self.list.append(input_to_add);
    
    # Create loop, so we can have the ability to add elements one-by-one to array.
    def add_multiple_elements(self):
        # Define a new variable counting all the items added.
        items_added: int = 0;
        
        # Loop around until “items_added” is equal to limit set in init.
        while(items_added < self.list_items):
            self.add_element();
            items_added += 1;
    
    # Select a random element, remove it, show it, and then show the rest of the list.
    def remove_random_element(self):
        item_to_remove = random.choice(self.list);
        print("Randomly selected item from the list:", item_to_remove);
        
        self.list.remove(item_to_remove);
        print("Items remaining:", self.list);
            
    # This function handles the Terminal User Interface (TUI) of the script.
    def welcome(self):
        # Greet user.
        print("—————", "Welcome to", self.app_name, "—————");
        print("");
        
        # Invoke first function.
        self.add_multiple_elements();
        print("");
        
        # Invoke second function.
        self.remove_random_element();
        
        # Thank user.
        print("");
        print("—————", "Thank you for using", self.app_name, "—————");
        
# Create object using said class.
def main():
    randomizer_app = randomFromList()
    randomizer_app.welcome();

# Launch local function.
if __name__ == "__main__":
    main();