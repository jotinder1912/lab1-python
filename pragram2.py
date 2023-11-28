def takeInput():
   a = float(input("Enter first number: "))
   print("your first  number: " ,a)
   b = float(input("Enter second number: "))
   print("your second number; " ,b)
   x = input("Enter any method (add,subtract,multiply,divide): ")
   print("you chose to" ,x ," the number." )
   return a, b, x  
def displayResult():
   a, b, x = takeInput()
   if x == 'add':
       method = a + b
       print("Ans:",method)
   elif x == 'subtract':
       method = a-b
       print("Ans:",method)
   elif x == 'multiply':
       method = a*b
       print("Ans:",method)
   elif x == 'divide':
       method= a/b 
       print("Ans:",method)
   else:
       print("you entered the wrong operator")
displayResult()