"""
Author: Jacob Blazina
Date: 6/21/2021
File: BankAccount.py
Title: Lab 6
"""

# A Bank Account manager class
class BankAccount:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.num_deposits = 0
        self.deposit_total = 0
        self.num_withdraws = 0
        self.withdraw_total = 0

    # Increments the deposit counter
    def numDeposits (self):
        self.num_deposits = self.num_deposits + 1

    # Increments the withdraw counter
    def numWithdraws (self):
        self.num_withdraws = self.num_withdraws + 1

    # Deposits a certain amount in the account
    def deposit (self, amount):
        self.balance += amount
        self.deposit_total += amount
        self.numDeposits()

    # Remotes a certain amount from the account
    def withdraw (self, amount):
        self.balance -= amount
        self.withdraw_total += amount
        self.numWithdraws()

    # Prints current bank account information
    def endOfMonth (self):
        print("****************")
        print("Bank account : ", self.name)
        print("Balance : $ ", self.balance)
        print("Number of deposits : ", self.num_deposits, " totalling $ ", self.deposit_total)
        print("Number of withdraws : ", self.num_withdraws, " totalling $ ", self.withdraw_total)
        print("****************")

# Example Usage and outputs
bankAccount1 = BankAccount(balance=0, name="Chase")
bankAccount2 = BankAccount(balance=100, name="Bank of America")

bankAccount1.deposit(50)
bankAccount1.deposit(50)
bankAccount1.withdraw(100)
bankAccount1.withdraw(100)
bankAccount1.withdraw(100)

bankAccount2.deposit(25)
bankAccount2.deposit(25)
bankAccount2.deposit(5000)
bankAccount2.withdraw(10)
bankAccount2.withdraw(1000)
bankAccount2.withdraw(70)

bankAccount1.endOfMonth()
bankAccount2.endOfMonth()
