# De La Salle University–Dasmariñas
# S-ITCS227LA — Application Development and Emerging Technologies (Laboratory)

# Luis Anton P. Imperial
# BCS22

# Monday, 5 February 2024
# Laboratory Activity No. 2
# Part 1: CustomerBill
# A fine dine-in restaurant charges 15% service charge and 10% sales tax on the gross bill. Write a program that would input the gross bill of the customer and the amount tendered by the customer to the waiter. Display the customer’s gross bill, taxes and charges as well as the customer’s change.

from time import sleep


class receipt:
    def __init__(self):
        self.subtotal: float = 0;
        self.service_charge: float = 0.15;
        self.sales_tax: float = 0.10;
        
        self.business_name = "Ibarraville";
        self.business_tagline = "Your beloved Filipino delights with a new twist!";
        
        self.subtotal_input_label = "Enter subtotal:";
        self.subtotal_label = "Subtotal:";
        self.service_charge_label = "Service Charge:";
        self.sales_tax_label = "Sales Tax:";
        self.net_total_label = "Net Total:";
        self.currency_symbol = "₱";
        
        self.separator_line = "================";
    
    def calculate_service_charge(self):
        service_charge_amount: float = self.subtotal * self.service_charge;
        
        return service_charge_amount;
    
    def calculate_sales_tax(self):
        sales_tax_amount: float = self.subtotal * self.sales_tax;
        
        return sales_tax_amount;
    
    def calculate_net_total(self):
        service_charge_amount: float = self.calculate_service_charge();
        sales_tax_amount: float = self.calculate_sales_tax();
        
        net_total: float = self.subtotal - service_charge_amount - sales_tax_amount;
        
        return net_total
        
    def display_bill(self):
        service_charge_amount = self.calculate_service_charge();
        sales_tax_amount = self.calculate_sales_tax();
        net_total = self.calculate_net_total();
              
        print(self.subtotal_label, self.currency_symbol, self.subtotal);
        print(self.service_charge_label, self.currency_symbol, service_charge_amount);
        print(self.sales_tax_label, self.currency_symbol, sales_tax_amount);
        print(self.separator_line, end="\n\n")
        
        print(self.net_total_label, self.currency_symbol, net_total);
        print("")
        
    def display_input_process(self):
        print("")
        print("Welcome to", self.business_name);
        print(self.business_tagline);
        print(self.separator_line, end="\n\n");
        sleep(1);
        
        self.subtotal = float(input(f"{self.subtotal_input_label}  {self.currency_symbol} "));
        print(self.separator_line, end="\n\n")
        sleep(1);
        
        self.display_bill();
        sleep(1);
        
        print("Thank you for your order!", end="\n\n");
        sleep(1);
        
        print("Come again next time to:", self.business_name);
        print(self.business_tagline);

def main():  
    point_of_sale_terminal = receipt();
    sale_terminal_running = True;
    
    point_of_sale_terminal.display_input_process();


if __name__ == "__main__":
    main();