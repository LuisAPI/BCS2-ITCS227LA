# De La Salle University–Dasmariñas
# S-ITCS227LA — Application Development and Emerging Technologies (Laboratory)

# Luis Anton P. Imperial
# BCS22

# Monday, 5 February 2024
# Laboratory Activity No. 2
# Part 2: Budget

# Create a Budgeting program that accept monthly salary using the Chinkee Tan approach (50/30/20 rule).
# Using this method, you would divide your earnings as follows:
# • Needs = 50% (Food, shelter, utilities)
# • Wants = 30% (Shopping, hobbies, dine-out)
# • Savings = 20% (emergency fund)

class finance_manager:
    def __init__(self):
        self.salary: float = 0;
        
        self.needs_total = 0.50;
        self.wants_total = 0.30;
        self.savings_total = 0.20;
        
        self.needs_food = 0.50;
        self.needs_shelter = 0.30;
        self.needs_utilities = 0.20;
        
        self.wants_shopping = 0.40;
        self.wants_hobbies = 0.15;
        self.wants_dineout = 0.45;
        
        self.savings_emergency = 0.70;
        self.savings_jar = 0.30;
        
        self.program_name = "CookedBooks";
        self.program_tagline = "Pepper, spices and resourcefulness.";
        
        self.currency_symbol = "₱";
                
        self.salary_input_label = "Enter salary:";
        self.salary_label = "Salary:";
                
        self.separator_bullets_small = "••"
        self.separator_bullets = "•••••";
        self.separator_line = "================";
        
        self.program_section1_header = "My Monthly Budget";
        self.program_section1_header_x = self.separator_bullets_small + " " + self.program_section1_header.upper() + " " + self.separator_bullets_small;
        
        self.needs_header = "Needs";
        self.needs_header_expanded = self.separator_bullets + " " + self.needs_header + " " + self.separator_bullets;
        self.needs_total_label = "Needs (Total):";
        self.needs_food_label = "Food:";
        self.needs_shelter_label = "Shelter:";
        self.needs_utilities_label = "Utilities:";
        
        self.wants_header = "Wants";
        self.wants_header_expanded = self.separator_bullets + " " + self.wants_header + " " + self.separator_bullets;
        self.wants_total_label = "Wants (Total):";
        self.wants_shopping_label = "Shopping:";
        self.wants_hobbies_label = "Hobbies:";
        self.wants_dineout_label = "Dine Out:";
        
        self.savings_header = "Savings";
        self.savings_header_expanded = self.separator_bullets + " " + self.savings_header + " " + self.separator_bullets;
        self.savings_total_label = "Savings (Total):";
        self.savings_emergency_label = "Emergency:";
        self.savings_jar_label = "Jar:";
        
        self.total_label = "Total:";
    
    def calculate_budget_categories(self):
        self.needs_total_amount: float = self.salary * self.needs_total;
        self.wants_total_amount: float = self.salary * self.wants_total;
        self.savings_total_amount: float = self.salary * self.savings_total;
        
        self.total_amount = self.needs_total_amount + self.wants_total_amount + self.savings_total_amount
        
        return [self.needs_total_amount,
                self.wants_total_amount,
                self.savings_total_amount,
                self.total_amount];
    
    def calculate_needs_types(self):
        self.needs_food_amount = self.needs_total_amount * self.needs_food;
        self.needs_shelter_amount = self.needs_total_amount * self.needs_shelter;
        self.needs_utilities_amount = self.needs_total_amount * self.needs_utilities;
        
        return [self.needs_food_amount,
                self.needs_shelter_amount,
                self.needs_utilities_amount];
    
    def calculate_wants_types(self):
        self.wants_shopping_amount = self.wants_total_amount * self.wants_shopping;
        self.wants_hobbies_amount = self.wants_total_amount * self.wants_hobbies;
        self.wants_dineout_amount = self.wants_total_amount * self.wants_dineout;
        
        return [self.wants_shopping_amount,
                self.wants_hobbies_amount,
                self.wants_dineout_amount];
    
    def calculate_savings_types(self):
        self.savings_emergency_amount = self.savings_total_amount * self.savings_emergency;
        self.savings_jar_amount = self.savings_total_amount * self.savings_jar;
        
        return [self.savings_emergency_amount,
                self.savings_jar_amount];
    
    def display_budget(self):
        needs_total_amount = self.calculate_budget_categories()[0]
        wants_total_amount = self.calculate_budget_categories()[1]
        savings_total_amount = self.calculate_budget_categories()[2]
        
        needs_food_amount = self.calculate_needs_types()[0]
        needs_shelter_amount = self.calculate_needs_types()[1]
        needs_utilities_amount = self.calculate_needs_types()[2]
        
        wants_shopping_amount = self.calculate_wants_types()[0]
        wants_hobbies_amount = self.calculate_wants_types()[1]
        wants_dineout_amount = self.calculate_wants_types()[2]
        
        savings_emergency_amount = self.calculate_savings_types()[0]
        savings_jar_amount = self.calculate_savings_types()[1]
        
        print(self.program_section1_header_x, end="\n\n");
        
        print(self.needs_header_expanded);
        print(self.needs_total_label, self.currency_symbol, needs_total_amount);
        print(self.needs_food_label, self.currency_symbol,  needs_food_amount);
        print(self.needs_shelter_label, self.currency_symbol,  needs_shelter_amount);
        print(self.needs_utilities_label, self.currency_symbol,  needs_utilities_amount);
        print("")
        
        print(self.wants_header_expanded);
        print(self.wants_total_label, self.currency_symbol,  wants_total_amount);
        print(self.wants_shopping_label, self.currency_symbol,  wants_shopping_amount);
        print(self.wants_hobbies_label, self.currency_symbol,  wants_hobbies_amount);
        print("")
        
        print(self.savings_header_expanded);
        print(self.savings_emergency_label, self.currency_symbol,  savings_emergency_amount);
        print(self.savings_jar_label, self.currency_symbol,  savings_jar_amount);
        print("")
        
        print(self.separator_line)
        print(self.total_label, self.currency_symbol, self.total_amount)
        print("")
    
    def display_input_process(self):
        print("")
        print("Welcome to", self.program_name, "—");
        print(self.program_tagline);
        print(self.separator_line, end="\n\n");
        
        self.salary = float(input(f"{self.salary_input_label}  {self.currency_symbol}"));
        print(self.separator_line, end="\n\n");
        
        self.display_budget();
        
        print(self.separator_line)
        print("Remember to always love yourself!", end="\n\n");
        
        print(self.program_name, "—");
        print(self.program_tagline);
        print("");
        
def main():
    app = finance_manager();
    
    app.display_input_process();
    
if __name__ == "__main__":
    main();