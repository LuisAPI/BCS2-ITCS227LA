# De La Salle University – Dasmariñas
# S-ITCS227LA — Application Development and Emerging Technologies (Laboratory)

# Luis Anton P. Imperial
# BCS22

# Monday, March 11, 2024
# Laboratory Exam

# Create Python program that generates Fibonacci number sequence and find their square in the given sequence based on the user input.

# ; Condition:
# - Fibonacci sequence should be in list format
# - User Input should be only positive input. If the user puts a negative value, it should be an output that accept only positive input.

# Submit a two-sample output screenshot and the python code (LabExam_Surname) only.

# ; Rubrics:
# - Meet the condition | = 10 pts each condition
# - Execute the code properly | = 20 pts

class Fibonacci:
    def __init__(self):
        self.fib_sequence = [];
        self.fib_sequence_completed = 0;
        self.fib_sum = 0;
        self.fib_input = None;
    
    def check_if_positive(self):
        return self.fib_input > 0;

    def reject_input(self, reason):
        if reason.lower() == "negative":
            print("Number for Fibonacci sequence must be a positive integer.")

    def square(self, factor):
        return factor ** 2;

    def generate_fibonacci_sequence(self):
        if self.fib_input <= 1:
            print("Fibonacci sequence:", [0, 1][:self.fib_input])
            return
        
        self.fib_sequence.append(0);
        self.fib_sequence_completed += 1;
        self.fib_sequence.append(1);
        self.fib_sequence_completed += 1;
        print(f"Fibonacci number(1): 0, Square: 0")
    
        for seq_count in range(2, self.fib_input + 1):
            fib_sequence_nextnum = self.fib_sequence[seq_count - 1] + self.fib_sequence[seq_count - 2]
            self.fib_sequence.append(fib_sequence_nextnum);
            seq_count_sq = self.square(self.fib_sequence[seq_count - 1]);
            print(f"Fibonacci number({seq_count}): {self.fib_sequence[seq_count - 1]}, Square: {seq_count_sq}")
            self.fib_sequence_completed += 1
        print("\nThe next number is:", self.fib_sequence[self.fib_sequence_completed - 1])

    def display_menu(self):
        print("Fibonacci Sequence Script —")
        print("Generate a Fibonacci sequence based on the user input, and know their squares.", end="\n\n")

        self.fib_input = int(input("Enter the number for Fibonacci sequence:\n"))
        print("")

        check_input = self.check_if_positive();

        if check_input is False:
            self.reject_input("negative");
        else:
            self.generate_fibonacci_sequence();

        print("")
        print("Fibonacci sequence:", self.fib_sequence)
    
def main():
    fibogen = Fibonacci();
    fibogen.display_menu();

if __name__ == "__main__":
    main();