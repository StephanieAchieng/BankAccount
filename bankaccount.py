class BankAccount:
   

    def __init__(self, first_name, last_name, phone_no, bank):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_no = phone_no
        self.bank = bank
        self.balance = 0
        self.withdraw_statement = []
        self.deposit_statement = []
        self.loan_balance = 0

    def account_name(self):
        name = "{} account for {} {}".format(
            self.bank, self.first_name, self.last_name, self.phone_no, self.bank)
        return name

    def deposit(self, amount):
      
      if amount <= 0:
               
          print("You cannot deposit that amount")
      else:
            self.balance += amount
            print("You have deposited {} to {}".format(amount, self.account_name()))
            return 
            
            
          
    def withdraw(self, amount):
         
      if amount <= 0:
          print("You cannot withdraw that amount")
          
       
      elif amount > self.balance:
            print("You have insufficient balance")
      self.balance += amount
            time = datetime.now()
            get_time = time.strftime("%H:%M%p %d/%m/%Y")
            get_time = time.strftime("%H:%M%p , %d/%m/%Y")
            deposit = {
                "time": "time",
                "amount" : "amount"
            }
            print("Dear {} you have deposited {} at {}.Your current balance is {}".format(self.account_name(),amount,get_time,self.balance))
            print("Dear {} ,you have deposited {} at {}.Your current balance is {}".format(self.account_name(),amount,get_time,self.balance))

    def withdraw(self,amount):
        try:
@@ -63,7 +63,7 @@ def withdraw(self,amount):
        else:
            self.balance -= amount
            time = datetime.now()
            get_time = time.strftime("%H:%M%p  %d/%m/%Y")
            get_time = time.strftime("%H:%M%p ,  %d/%m/%Y")
            deposit = {
                "time": "time",
                "amount" : "amount"
@@ -73,19 +73,19 @@ def withdraw(self,amount):

    def get_balance(self):
        time = datetime.now()
        get_time = time.strftime("%H:%M%p  %d/%m/%Y")
        get_time = time.strftime("%H:%M%p ,  %d/%m/%Y")
        return "The balance for {} is {} at".format(self.account_name(), self.balance,get_time)

    def deposit_statement(self):
        for deposit in self.deposits:
            time = datetime.now()
            get_time = time.strftime("%H:%M%p  %d/%m/%Y")
            get_time = time.strftime("%H:%M%p  , %d/%m/%Y")
            print("{} at {}".format(deposit(),get_time))

    def withdrawal_statement(self):
        for withdraw in self.withdrawals:
            time = datetime.now()
            get_time = time.strftime("%H:%M%p  %d/%m/%Y")
            get_time = time.strftime("%H:%M%p , ++ %d/%m/%Y")
            print("{} at {}".format(withdraw(),get_time))
             def request_loan(self, amount):
      if amount<= 0:
        print("You cannot request for a loan of this amount")
        
      else: 
        self.loan = amount
        print("You have received a loan of {}".format (amount)
      
    def repay_loan(self, amount):
      if amount<= 0:
        print("You cannot repay with that amount")
      elif self.loan == 0:
        print("You don't have any loan balance at the moment")
        elif amount > self.loan:
          print("Your loan is {}, please enter amount that is less or equal to the amount")
        else:
        print(" You have repayed your loan with {}. Your loan balance is{}".format(mount))
       
    def deposit_statement(self, amount):
      self.deposit(self, amount)
      
      return self.deposit_statement.append(amount)
      
      
    
    
acc1 = BankAccount("Stephanie", "Achieng", +254727088262, "Barclays")
print(acc1.phone_no)
acc1.deposit(450000)
acc1.withdraw(12500)
acc1.withdraw(1390)
acc1.deposit(5700)
acc1.deposit(3500)
acc1.lend_loan(71000)
acc1.lend_loan(5000)
acc1.pay_loan(57000) 
print(acc1.loan_balance)

print(acc1.deposit_summary)


