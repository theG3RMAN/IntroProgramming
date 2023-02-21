def main(): 
  #IntroDisplay
  intro()
  
  try:
  #user input the number of miles  
    miles_entered = float(input('Enter the how many miles: ')) 
    
  #convert the miles to km  
    miles_to_kilometers(miles_entered)
    
  #user error message            
  except:
    print("An error occured, try again enter a whole number")
    print()
    main()

  #display intro function
def intro():
    print("This program converts miles to kilometers, 1 miles = 1.609344 kilometers")
    print()
  
  #calculates miles to kilometers
def miles_to_kilometers(miles):  
  kilometers = miles * 3.78541
  print(f'\nTotal miles: {miles}')
  print(f'Total kilometers: {round(kilometers,2)}')

  #Call the main function
main()

  #Thank you message/end program
print("Thank you! Have a nice Day!")