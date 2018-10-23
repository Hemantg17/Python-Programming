s='login'
for i in range(0,5):
 T=input("Enter the password=")
 if (T == s):
  print("You are logged in") 
  break
 else:
  print("Re Enter password=")
  if(i==4):
   print("Your all login atempts are failed")  
