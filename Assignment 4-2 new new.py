EmployeeName = input("Enter employee's name: ")
NumberOfShifts = int(input("Enter number of shifts:"))
NumberOfTransactions = int(input("Enter number of transactions:"))
TransactionDollarValue = float(input("Enter transaction dollar value:"))
ProductivityScore = (NumberOfTransactions/TransactionDollarValue) * NumberOfShifts
if ProductivityScore < 30:
    Bonus = 50.00
elif ProductivityScore >=30 and ProductivityScore < 69:
    Bonus = 75.00
elif ProductivityScore >=70 and ProductivityScore < 199:
    Bonus = 100.00
else:
    Bonus = 200.0
    TotalOutput = Bonus
    print("Employee Name:",EmployeeName)
    print("Bonus: $", round(TotalOutput, 2))
    
    EmployeeName = int(input("Dave mathews:"))
    NumberOfShifts = int(input("Enter number of shifts:"))
    NumberOfTransactions + int(input("Enter number of transactions"))
    TransactionDollarValue = float(input("Enter transactions dollar value:"))
    if NumberOfTransactions/TransactionDollarValue * NumberOfShifts >= 1:
        Bonus = 200.0
    else:
        Bonus = 0.00
        print("Employee Name:", EmployeeName)
        print("200.0: $", round(Bonus, 1))
        
        EmployeeName = input("Enter Employee Name:")
        NumberOfShifts = int(input("Enter number of shifts"))
        NumberOfTransactions = int(input("Enter number of transactions"))
        TransactionDollarValue = float(input("Enter transactions dollar value"))
        if NumberOfTransactions/TransactionDollarValue * NumberOfShifts >= 2.5:
            Bonus = 200.0
        elif NumberOfTransactions/TransactionDollarValue * NumberOfShifts >= 2:
            Bonus = 180.00
        else:
            Bonus = 0.00
            print("EmployeeName:", EmployeeName)
            print("Employee Bonus: $", round(Bonus,1))
        
        
