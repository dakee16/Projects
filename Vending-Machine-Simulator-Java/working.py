import random
class Pantry:
    def __init__(self):
        self.items = {} #defining the dictionary
    
    def __repr__(self):
        #--- YOUR CODE STARTS HERE
        return f"I am a Pantry object, my current stock is {self.items}" #returning the stock in the form of a dictionary, with its item as the key

    def stock_pantry(self, item, qty):
        #--- YOUR CODE STARTS HERE
        self.item = item
        self.qty = qty
        qt = float(qty) #converting the quantity into a float 
        if item in self.items: 
            self.items[item] = self.items[item] + self.qty #if the item is in the dictionary, then add the given qty into the existing one
            qt = self.items[item] 
        self.items[item] = qt #updating the existing variable or adding it if not in the dictionary
        return f"Pantry Stock for {item}: {qt}"


    def get_item(self, item, qty): 
        #--- YOUR CODE STARTS HERE
        self.item = item
        self.qty = float(qty)
        if item in self.items: # checking if the given item is in self.items
            if self.qty < self.items[item]:
                self.items[item] -= self.qty #if the given quantity is less than the existing one then substracting it as we are taking it out
                return f"You have {self.items[item]} of {item} left"
            elif self.qty == self.items[item]:
                self.items[item] = 0.0 #if both are equal nothing of that item will be left in their stock
                return f"Add {item} to your shopping list!"
            elif self.qty > self.items[item]:
                self.items[item] = 0.0 #if the existing one is less than what has been asked, it will come down to zero but will still need more
                return f"Add {item} to your shopping list!"
        else:
            return f"You don't have {item}" #if not present in self.items
                    
                    
    
    def transfer(self, other_pantry, item):
        #--- YOUR CODE STARTS HERE
        self.other_pantry = other_pantry #old stock
        self.item = item 
        if item in other_pantry.items: #if given item in the old stock dictionary
            if other_pantry.items[item] > 0: #if its quantity is more than zero which means its not finished     
                self.items[item] += other_pantry.items[item] #adding the qty to the new dictionary
                other_pantry.items[item] -= other_pantry.items[item] #removing it from the old dictionary
                
                


# -------- SECTION 3
class Vendor:

    def __init__(self, name):
        self.name = name
        self.vendor_id = random.randint(999, 999999)
        
    def install(self):
        return VendingMachine()
        
    def restock(self, machine, item, amount):
        return machine._restock(item, amount)
            


class VendingMachine:
    def __init__(self):
        #--- YOUR CODE STARTS HERE
        self.balance = 0.0 #setting the default balance as 0
        self.items = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]} #defining the dictionary

    def purchase(self, item, qty=1):
        #--- YOUR CODE STARTS HERE
        self.item = item
        self.qty = qty
        value_lst = [] #defining an empty list to be used in the following code
        num_of_keys = len(self.items.keys()) #storing the number of keys in a variable by converting it into a list and then taking its length
        if item not in self.items:
         return f"Invalid item" #return invalid item if not present in self.items
     
        for key,value in self.items.items(): #defining the key value pair of the dictionary
            if value[1] == 0:
                value_lst.append(value) #adding the value in the list if the stock is zero
                
        if len(value_lst) == num_of_keys: #checking if the length of the list containing the value whose stock is zero is equal to the number of keys stored 
            return f"Machine out of stock" #then it will return the machine is out of stock as nothing is left
        
        if self.items[item][1] == 0:
            return f"Item out of stock" #if the stock of a particular item asked is zero then it will return the item as out of stock
        
        if self.items[item][1] < qty: 
            return f"Current {self.item} stock: {self.items[item][1]}, try again" #if the asked qty is more than the existing one, it will ask for more
        
        if self.balance < qty * self.items[item][0]: #if the balance is less than the cost which is price * quantity
             num_of_keys  = qty * self.items[item][0] - self.balance #storing the remaining cost which has to deposited before the purchase
             return f"Please deposit ${num_of_keys}"
        
        if self.balance == qty * self.items[item][0]: #if the balance is equal to the cost
            self.items[item][1] -= qty #reduce the quantity by one 
            self.balance = 0.0 #the balance will come down to zero
            return "Item dispensed" #item is dispensed
        
        if self.balance > qty * self.items[item][0]: #if the balance is more than the cost
             num_of_keys  = self.balance - qty * self.items[item][0] #storing the remaining balance
             self.items[item][1] -= qty #reducing the quantity
             self.balance = self.balance - qty * self.items[item][0] - num_of_keys  #deducting the balance after the purchase
             return f"Item dispensed, take your ${num_of_keys} back"
        

        


    def deposit(self, amount):
        #--- YOUR CODE STARTS HERE
        if self.isStocked == True: #calling the isStocked function to check if the stock is not zero
            self.balance += amount #adding the amount in the balance
            return f"Balance: ${self.balance}"
        
        return f"Machine out of stock. Take your ${float(amount)} back" #if the stock is zero, it returns machine out of stock with the amount in a float form



    def _restock(self, item, stock):
        #--- YOUR CODE STARTS HERE
        self.item=item
        self.stock=stock
        if item in self.items: 
            self.items[item][1]+=stock #if item is in self.items then the it will be restocked by adding the stock into the existing one
            return f"Current item stock: {self.items[item][1]}"
        else:
            return f"Invalid item" #if not then it will return as a invalid item


    @property
    #--- YOUR CODE STARTS HERE
    def isStocked(self):
        for item in self.items:
            if self.items[item][1] > 0: #if the given item in self.items has a stock of more than zero, it will return as True
                return True
        return False #if not then False
        
        
        
    @property
    #--- YOUR CODE STARTS HERE
    def getStock(self):
        return self.items #returns the dictionary




    def cancelTransaction(self):
        #--- YOUR CODE STARTS HERE
        if self.balance == 0.0: #if the balance is zero then None will be returned
            return None
        else:
            a = self.balance
            self.balance = 0.0
            return f"Take your ${a} back" #if not then it will ask you to take your balance back as the transaction is canceled   