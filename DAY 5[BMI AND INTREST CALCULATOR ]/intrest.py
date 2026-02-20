# simple interest calculator 
#we require 3 vaiables principle amount , rate of interest , time 
def intrest(principle , rate , time ):
    simple_interest = (principle*rate*time)/100
    print(f"simple interest is {simple_interest}")
    total_amount = simple_interest + principle
    print(f"total amount for {time} years at{rate}percent rate of intrest is {total_amount}")

principle = float(input("write the prinviple amount:"))
rate = float(input("write the rate of interest %per year"))
time = float(input("time in years:"))
intrest(principle , rate , time )

#sample input and output
# write the prinviple amount:1000
# write the rate of interest %per year10
# time in years:2
# simple interest is 200.0
# total amount for 2.0 years at10.0percent rate of intrest is 1200.0
