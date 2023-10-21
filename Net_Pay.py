''' First time learning about arithmetic operations in Python '''

hour=input("how many hours have you worked?\n")

rate=input("How much did you earn per hour for the work?\n")

try:
  float(hour)
  float(rate)
  if float(hour)==40 or float(hour)<40:
    netpay=float(hour)*float(rate)
    print(netpay)
  elif float(hour)>40:
    pay1=float(hour)-40
    extrapay=pay1*1.5*float(rate)+40*float(rate)
    print(extrapay)
except:
    if type(hour)==type("nine") or type(input)==type(nine):
        print("Please type in integers only!")

#Calculates net pay for an employee, every hour worked over 40 is payed at a rate 1.5 times the original rate
