import mathl.core as cr
import mathl.test as ts
import ios.to_metric as mt
import ios.to_str as st

aFeet = 3
aInch = 5
bFeet = 2
bInch = 8
factor = 0.5

test_case = ts.Test_Calc(aFeet, aInch, bFeet, bInch)


print(cr.sum(aFeet, aInch, bFeet, bInch))
print(cr.diff(aFeet, aInch, bFeet, bInch))
print(cr.mul(aFeet, aInch, factor))
print(cr.div(aFeet, aInch, factor))

print(str(mt.tmetric(aFeet, aInch)) + " метров")


print (test_case.test1())
print (test_case.test2())
print (test_case.test3(factor))
print (test_case.test4(factor))