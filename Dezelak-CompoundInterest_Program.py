principle = int(input("Enter starting investment -no commas- : ")) 
rate = float (input("Enter Interest Rate : "))
time = int(input("Enter Number of Years to calculate : "))

rate2 = rate * 0.01

i = 0

while i < time:
    principle = (principle) * (1 + rate2)
    i += 1
    print(f"Year {i}:", round(principle,2))