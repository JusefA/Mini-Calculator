while True:
   print("Options:")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'quit' to end the program")
   user_input = input(": ")

   if user_input == "quit":
      print("program ended")
      break

   elif user_input == "add":
       print('enter first number')
       first_input1 = int(input(""))

       print('enter second number')
       second_input1 = int(input(""))

       result = first_input1 + second_input1
       print(result)

   elif user_input == "subtract":
       print('enter first number')
       first_input = int(input(""))

       print('enter second number')
       second_input = int(input(""))

       result = first_input - second_input
       print(result)

   elif user_input == "multiply":
       print('enter first number')
       first_input1 = int(input(""))

       print('enter second number')
       second_input1 = int(input(""))

       result = first_input1 * second_input1
       print(result)

   elif user_input == "divide":
       print('enter first number')
       first_input = int(input(""))
   
       print('enter second number')
       second_input = int(input(""))
       if second_input == 0:
           print("choose another number")
           print('enter second number')
           second_input = int(input(""))
       
           
       result = first_input / second_input
       print(result)

   else:
      print("Unknown input")

   break

