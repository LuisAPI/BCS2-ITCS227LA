# De La Salle University—Dasmariñas
# Luis Anton P. Imperial
# BCS22
# Monday, January 29, 2024

# Input: Workdays
# Constant: 
# Output: Gross Pay, Income Tax, Net Pay

class payrollSystem:
    def __init__(self, days_worked: int):
        self.days_worked = days_worked
        # Given daily rate
        self.daily_rate: float = 347.00
        # Given tax deduction
        self.income_tax: float = 0.10
    
    def computeGrossWeeklyPay(self):
        gross_weekly_pay: float = (self.daily_rate * self.days_worked)

        return gross_weekly_pay
    
    def computeNetWeeklyPay(self):
        gross_weekly_pay = self.computeGrossWeeklyPay()

        net_weekly_pay = gross_weekly_pay - (gross_weekly_pay * self.income_tax)

        return net_weekly_pay
    
    def showPay(self):
        print("Daily Rate:", self.daily_rate, end="\n\n")

        print("Gross Weekly Pay:", '{0:,.2f}'.format(self.computeGrossWeeklyPay()))
        print("Income Tax (as a %):", (self.income_tax)*100)

        print("")
        print("Net Weekly Pay:", '{0:,.2f}'.format(self.computeNetWeeklyPay()))
    
def main():
    print("Welcome to SEESMyRoll.", end="\n\n")
    days_worked_input = int(input("Input number of days worked: "))
    
    payroll = payrollSystem(days_worked_input)

    payroll.showPay()

if __name__ == "__main__":
    main()