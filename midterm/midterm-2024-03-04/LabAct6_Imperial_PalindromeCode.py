# De La Salle University – Dasmariñas
# S-ITCS227LA — Application Development & Emerging Technologies (Laboratory)

# Monday, March 4, 2024
# Laboratory Activity No. 6
# A palindrome is a word, sentence, verse, or even number that reads the same backward or forward.

# Create a user input that accept either string or number then detects if the string or number is a palindrome or not using conditional statement/Loops.

# Luis Anton P. Imperial
# BCS-2-2

class Node:
    def __init__(self, node_input):
        self.data = node_input
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None

    def push(self, push_input):
            new_element = Node(push_input)

            if self.top is None:
                self.top = new_element
                self.top.next = None
            else:
                new_element.next = self.top
                self.top = new_element
    
    def pop(self):
        if self.top is None:
            print("There is no input to pop!")
        else:
            popped_element = self.top.data
            self.top = self.top.next
            return popped_element

    def display(self):
        if self.top is None:
            print("No input to test!")
            print("")
        else:
            print("Your input, squished into one word, is reversed as: ")
            temp = self.top
            all_elements = []
            while temp:
                all_elements += temp.data
                temp = temp.next
            
            print("".join(all_elements))


class PalindromeChecker:
    def __init__(self, stack_object_input):
        self.stack_object_used = stack_object_input.lower()

    def customization_options(self):
        ### Use this only if checker is to be restricted to certain letters / numbers
        # characters_allowed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # return characters_allowed
        return None;

    def isPalindrome(self):
        sentence = []
        reversed_sentence = []
        # characters_to_check_for = self.customization_options()

        for character in self.stack_object_used:
            if character.isalnum():
                sentence.append(character)
                stack_object.push(character)

        ### For debugging purposes — Letters pushed and popped:
        # print(letters_pushed, letters_popped)
        # print("")

        stack_object.display()

        for character in self.stack_object_used:
            if character.isalnum():
                popped_element = stack_object.pop()
                reversed_sentence.append(popped_element)

        ### For debugging purposes — Sentences to test:
        print("Your input is: ", sentence)
        print("Your reversed input is: ", reversed_sentence)
        print("")

        return sentence == reversed_sentence
    
    @staticmethod
    def display_menu():
        print("Welcome to RennmontTech Palindrome Checker!")
        print("")

        print("A palindrome is a set of characters that, when backwards, is read the same way. This checker ignores spaces, punctuation and capitalization.")
        print("")

        menu_input = input("Input a number/string: ")

        return menu_input

        
def main():
    while True:
        user_input = PalindromeChecker.display_menu()
        print("")
        
        sentence_to_check = PalindromeChecker(user_input)

        if sentence_to_check.isPalindrome() is True:
            print("The input IS a palindrome.")
        else:
            print("The input IS NOT a palindrome.")
        print("")

        running_input = input("Do you wish to check again? (y/n): ")
        if running_input.lower() in ['n', "no", "false", "f"]:
            break

if __name__ == "__main__":
    stack_object = Stack()
    main()