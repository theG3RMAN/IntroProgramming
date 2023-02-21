#user_input starting investment
principle = int(input("Enter starting investment -no commas- : ")) 
#user_input interest rate
rate = float (input("Enter Interest Rate : "))
#user_input how many years to calculate
time = int(input("Enter Number of Years to calculate : "))
#actual rate formula
rate2 = rate * 0.01
i = 0
while i < time:
    principle = (principle) * (1 + rate2)
    i += 1
    print(f"Year {i}:", round(principle,2))#rounding to 2 dec.