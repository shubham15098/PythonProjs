#Creating a loan Calculator

monthPay=0
loanAmount=int(input('enter cost of loan'))
intRate=float(input('enter interest rate'))
noOfPay=int(input('enter number of years for the loan'))

monthPay=loanAmount*(intRate*(1+intRate)*noOfPay)/((1+intRate)*(noOfPay-1))

print('Your Monthly Payment is %i' %monthPay)

