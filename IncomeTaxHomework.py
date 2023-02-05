'''Calculate income tax owed'''
grossInc = float(input("Enter the gross income: "))
dependants = int(input("Enter the number of dependants: "))
stdDed = 10000
taxRate = float(0.2)
depDeduction = dependants * 3000
netIncome = grossInc - stdDed
incomeMinusDeductions = netIncome - depDeduction
netTax = incomeMinusDeductions * taxRate
print ("The income tax is:", netTax)
       
