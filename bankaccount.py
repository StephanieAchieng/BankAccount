class Account:
   

    def __init__(self, first_name, last_name, phone_no):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_no = phone_no
        self.bank = bank
        self.balance = 0
        self.withdraw_statement = []
        self.deposit_statement = []
        self.loan_balance = 0
        self.request_loan=0
        self.
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
        try:
            amount + 10
        except TypeError:
            print("Please enter the requested amount in figures")
            return

        if amount <=0:
            print("You cannot request a loan of that amount")
        else:
            self.loan = amount
            print("You have been given a loan of {}".format(amount))
      
    def repay_loan(self, amount):
      try:
          amount + 10
      except TypeError:
          print("Enter your repayment in figures")
          return
       
      if amount<= 0:
        print("You cannot repay with that amount")
      elif self.loan == 0:
        print("You don't have any loan balance at the moment")
        elif amount > self.loan:
          print("Your loan is {}, please enter amount that is less or equal to the amount")
        else:
            self.loan -= amount
            time = datetime.now()
            repayment ={
                "time": time,
                "amount": amount
            }
            self.loan_repayments.append(repayment)
            print("You have repaid your loan with {}. Your balance is {}".format(amount, self.loan)    
       
    def deposit_statement(self, amount):
      self.deposit(self, amount)
      
      return self.deposit_statement.append(amount)
      

class BankAccount(Account):
    def __init__(self, first_name, last_name, phone_number, bank):
        self.bank = bank
        super().__init__(first_name, last_name, phone_number)

class MobileMoneyAccount(Account):
    def __init__(self, first_name, last_name, phone_number, service_provider):
        self.service_provider = service_provider
        self.airtime = []
        super().__init__(first_name, last_name, phone_number)

    def buy_airtime(self, amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter the amount in figures")
            return
        if amount > self.balance:
            print("You don't have enough balance. Your balance is {}".format(self.balance))
        else:
            self.balance -= amount
            time=datetime.now()
            airtime = {
                "time": time,
                "airtime": amount
            } 
            self.airtime.append(airtime)
            print("You have bought airtime worth {} on {}".format(amount, self.get_formatted_time(time)))

   def pay_bill(self, amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter the amount in figures")
            return
        if amount > self.balance:
            print("You don't have enough balance. Your balance is {}".format(self.balance))
        else:
            self.balance -= amount
            time=datetime.now()
            paybill = {
                "time": time,
                "paybill": amount
            } 
            self.paybill.append(paybill)
            print("You have paid bills worth {} on {}".format(amount, self.get_formatted_time(time)))

    def send_money(self, amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter the amount to send in figures")
            return
        if amount > self.balance:
            print("You don't have enough balance. Your balance is {}".format(self.balance))
        else:
            self.balance -= amount
            time=datetime.now()
            sendmoney = {
                "time": time,
                "sendmoney": amount
            } 
            self.sendmoney.append(sendmoney)
            print("You have sent money worth {} on {}".format(amount, self.get_formatted_time(time)))

    def receive_money(self, amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter the amount in figures")
            return
        if amount > self.balance:
            print("You don't have enough balance. Your balance is {}".format(self.balance))
        else:
            self.balance -= amount
            time=datetime.now()
            receivemoney = {
                "time": time,
                "receivemoney": amount
            } 
            self.receivemoney.append(receivemoney)
            print("You have received money worth {} on {}".format(amount, self.get_formatted_time(time)))

             
    
acc1 = Account("Stephanie", "Achieng", +254727088262, "Barclays")
print(acc1.phone_no)
acc1.deposit(450000)
acc1.withdraw(12500)
acc1.withdraw(1390)
acc1.deposit(5700)
acc1.deposit(3500)


print(acc1.deposit_statement)


