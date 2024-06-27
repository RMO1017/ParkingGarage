##Your assignment for today is to create a parking garage class to get more familiar with Object Oriented Programming(OOP).

##Your parking gargage class should have the following methods:
#- takeTicket
## This should decrease the amount of tickets available by 1
## This should decrease the amount of parkingSpaces available by 1
#payForParking
## Display an input that waits for an amount from the user and store it in a variable
## If the payment variable is not empty then -> display a message to the user that their ticket has been paid and they have 15mins to leave
## This should update the "currentTicket" dictionary key "paid" to True
#leaveGarage
## If the ticket has been paid, display a message of "Thank You, have a nice day"
## If the ticket has not been paid, display an input prompt for payment
## Once paid, display message "Thank you, have a nice day!"

class ParkingGarage():
    '''
    The ParkingGarage class will have the ability to take a ticket, pay for a ticket and leave the parking garage once the ticket has been paid for. 
    
    '''
    def __init__(self, capacity, tickets):
        self.tickets = tickets
        self.capacity = capacity
    
    def takeTicket(self, capacity, tickets):
        self.capacity -= 1
        print(f'There are {self.capacity} spaces left')
        self.tickets -= 1
        print(f'There are {self.tickets} tickets left')

    def payForParking(self): 
        payment = ""
        if payment == None:
            payment = input('Please input your payment')
        if payment != None:
            currentTicket = [Paid, True]
            print('Your ticket has been paid. You have 15 minutes to leave the garage.')
    
    def leaveGarage(self):
        if currentTicket != True:
            print('Sorry, your ticket has not been paid')
            leaveGarage.payForParking()
            print('Thank you, have a nice day!')
        elif currentTicket == True:
            print('Thank you, have a nice day!')
