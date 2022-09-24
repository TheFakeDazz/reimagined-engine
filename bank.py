class account:

    def __init__(self, name, checking, savings):
        self.name = name
        self.checking = checking
        self.savings = savings
        self.check_history = list()
        self.sav_history = list()
        self.line = '------------------------------------------------'

    def balance(self):
        print(f'Owner: {self.name}\nChecking Account Balance: ${self.checking}\nSavings Account Balance: ${self.savings}\n')

    def move(self, amount, account):
        if account.lower() not in ['checking', 'savings']:
            return "Please enter a valid account"

        if account.lower() == 'checking':
            if amount > self.savings:
                return "Insufficient Balance\n"
            self.savings = self.savings - amount
            self.checking = self.checking + amount
            self.sav_history.append(f'Transfer to Checking Account: -${amount}\n| Current Balance ${self.savings}')
            self.check_history.append(f'Transfer from Savings Account: +${amount}\n| Current Balance ${self.checking}')

        if account.lower() == 'savings':
            if amount > self.checking:
                return "Insufficient Balance\n"
            self.savings = self.savings + amount
            self.checking = self.checking - amount
            self.sav_history.append(f'Transfer from Checking Account: +${amount}\n| Current Balance ${self.savings}')
            self.check_history.append(f'Transfer To Savings Account: -${amount}\n| Current Balance ${self.checking}')

    def deposit(self, amount, account):
        if account.lower() not in ['checking', 'savings']:
            return "Please enter a valid account"
        if account.lower() == 'checking':
            self.checking = self.checking + amount
            self.check_history.append(f'Deposit: +${amount}\n| Current Balance ${self.checking}')

        if account.lower() == 'savings':
            self.savings = self.savings + amount
            self.sav_history.append(f'Deposit: +${amount}\n| Current Balance ${self.savings}')

    def withdraw(self, amount, account):
        if account.lower() not in ['checking', 'savings']:
            return "Please enter a valid account"
        if account.lower() == 'checking':
            if amount > self.checking:
                return "Insufficient Balance\n"
            self.checking = self.checking - amount
            self.check_history.append(f'Withdrawal: -${amount}\n| Current Balance ${self.checking}')

        if account.lower() == 'savings':
            if amount > self.savings:
                return "Insufficient Balance\n"
            self.savings = self.savings - amount
            self.sav_history.append(f'Withdrawal: -${amount}\n| Current Balance ${self.savings}')

    def transactions(self, account):
        if account.lower() not in ['checking', 'savings']:
            return "Please enter a valid account"
        if account.lower() == 'checking':
            print(f'{self.line}\nChecking Account Transaction History (Recent to Old)\n{self.line}')
            for item in self.check_history[::-1]:
                print(f'| {item}')
                print(f'{self.line}')
        if account.lower() == 'savings':
            print(f'{self.line}\nSavings Account Transaction History (Recent to Old)\n{self.line}')
            for item in self.sav_history[::-1]:
                print(f'| {item}')
                print(f'{self.line}')

