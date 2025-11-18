#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 11:57:12 2025

@author: karaha
"""

from banking_system import BankingSystem

class Account:
    def __init__(self, timestamp: str, account_id: str):
        self._timestamp = timestamp
        self._account_id = account_id
        
        self._balance = 0

    #def get_account_id(self): return self._account_id
    
    def print_account_details(self):
        print(f"Timestamp: {self._timestamp}")
        print(f"Accound ID: {self._account_id}")
        print(f"Balance: {self._balance}\n")

class BankingSystemImpl(BankingSystem):

    def __init__(self):
        # TODO: implement
        self._accounts_list = []
        
    def _find_account(self, account_id: str): 
        for account in self._accounts_list:
            if account_id == account._account_id:
                return account
        return None # if not account found 
    
    # helper function for testing only 
    def _all_accounts(self): 
        for account in self._accounts_list: 
            account.print_account_details()


    # TODO: implement interface methods here
    def create_account(self, timestamp: int, account_id: str) -> bool:
        if self._find_account(account_id) is not None:
            return False
        
        # Create new account
        new_account = Account(timestamp, account_id)
        self._accounts_list.append(new_account)
        return True
    
    def deposit(self, timestamp: int, account_id: str, amount: int) -> int | None:
        account = self._find_account(account_id)
        if account is None:
            print(f"Timestamp: {timestamp} | Error: Account '{account_id}' not found.")
            return None

        if amount <= 0:
            print(f"Timestamp: {timestamp} | Error: Invalid deposit amount: {amount}")
            return None

        print(f"Timestamp: {timestamp} \nStarting account balance: {account._balance}")
        account._balance += amount
        print(f"Timestamp: {timestamp} \nNew account balance: {account._balance}\n")

        return account._balance

        

    def transfer(self, timestamp: int, source_account_id: str, target_account_id: str, amount: int) -> int | None:
        
        source = self._find_account(source_account_id)
        target = self._find_account(target_account_id)
        
        #missing accounts 
        if source is None or target is None:
            print("Error: Please enter a valid amount or source/target account IDs.")
            return None

        #cannot transfer to self
        if source == target:
            print("Error: Please enter a valid amount or source/target account IDs.")
            return None
        
        #change >= to > so full balance transfers are allowed
        if amount <= 0 or amount > source._balance:
            print("Error: Please enter a valid amount or source/target account IDs.")
            return None
        
        #removed list membership checks because source/target already validated by _find_account
        
        print(f"Timestamp: {timestamp} \nStarting balance (source): {source._balance} \nStarting balance (target): {target._balance}\n")
        
        source._balance -= amount 
        target._balance += amount 
        
        print(f"Timestamp: {timestamp} \nNew account balance (source): {source._balance} \nNew account balance (target): {target._balance}\n")

        return source._balance

