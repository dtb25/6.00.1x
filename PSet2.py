# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 14:59:19 2016

@author: David
"""
#
# Compute & print balance remaining on a credit card
# after a year if you only make the minimum monthly payment
#
# the variables balance, annualInterestRate, and monthlyPaymentRate
# are supplied by the grading system
#

for i in range(12):
    monthlyRate = annualInterestRate/12
    minMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaid = balance - minMonthlyPayment
    balance = monthlyUnpaid + monthlyRate * monthlyUnpaid
print('Remaining balance: ' + str(round(balance, 2)))   

#%%

#
# Compute the lowest payment required (as an integer multiple of $10)
# to fully pay off the balance on a credit card in one year, using a
# guess-and-check approach
#

payment = 0
monthlyRate = annualInterestRate/12
initialBalance = balance
while balance > 0:
    balance = initialBalance
    payment += 10
    for i in range(12):
        monthlyUnpaid = balance - payment
        balance = monthlyUnpaid + monthlyRate * monthlyUnpaid
print('Lowest Payment: ' + str(payment))
#%%

#
# Compute the lowest payment required (to the nearest $0.01)
# to fully pay off the balance on a credit card over one year
# using binary search
#

monthlyRate = annualInterestRate/12
lowerBound = 0
upperBound = balance
initialBalance = balance
while abs(balance) > 0.01:
    balance = initialBalance
    payment = 0.5*(lowerBound + upperBound)
    for i in range(12):
        monthlyUnpaid = balance - payment
        balance = monthlyUnpaid + monthlyRate * monthlyUnpaid
    if balance > 0: lowerBound = payment
    else: upperBound = payment
print('Lowest Payment: ' + str(round(payment, 2)))
#%%

#
# Peer-assessed programming exercise 1
#

import math
def polysum(n,s):
    """Sums the perimeter and the square of the area for a regular polygon
    with n sides (int) of length s (float)"""
    assert (n % 1 == 0) and (s > 0)
    area = (0.25 * n * s**2) / math.tan(math.pi / n)
    perimeter = n * s
    return round((area + perimeter**2), 4)
        
#%%

#
# Guessing game - computer asks player to think of a number
# between 0 and 100, and then guesses their number using
# binary search
#

upperLimit = 100
lowerLimit = 0
print('Please think of a number between 0 and 100!')
while True:
    guess = int((upperLimit + lowerLimit)/2)
    print('Is your secret number %s?' % guess)
    text1 = "Enter 'h' to indicate the guess is too high. "
    text2 = "Enter 'l' to indicate the guess is too low. "
    text3 = "Enter 'c' to indicate I guessed correctly. "
    queryText = text1 + text2 + text3
    response = input(queryText)
    if response == 'l': lowerLimit = guess
    elif response == 'h': upperLimit = guess
    elif response == 'c':
        print('Game over. Your secret number was: %s' % guess)
        break
    else: print('Sorry, I did not understand your input.')
    
