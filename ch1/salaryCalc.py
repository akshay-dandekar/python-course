# This function calculates salary
# Input parameters are
# base : Base salary
# da: dearness allowance in percent
# hra:  in percent
def calculateSalary(base, da, hra):
    finalSal = base + (base * da / 100) + (base * hra / 100)
    return finalSal


def calculateSalaryAndPrint(base, da=10, hra=20):
    mySal = calculateSalary(base, da, hra)
    print(mySal)    
    
calculateSalaryAndPrint(10000, 30, 40)