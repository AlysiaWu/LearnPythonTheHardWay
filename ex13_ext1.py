#Author Zhu Xiuwei
#Date 2014-3-19
from sys import argv

print "This function is to perform add operation."
firstNum = int(raw_input("The first number: "))
secondNum = int(raw_input("The first number: "))

ss, thirdNum = argv

print "The 3rd number is", thirdNum
print "The script name is: " , ss

print "The result is: %d" % (firstNum + secondNum + int(thirdNum))