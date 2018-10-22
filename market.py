from easygui import *
import sys
while 1:
     msgbox("welcome to the supermarket")

     msg1=("what would you like to buy")
     title1=("all at one place")
     choices1=("chocolates","cold drinks","soaps","cadbury","groceries","biscuits","packed items","ready to eat")
     choice=buttonbox(msg1,title1,choices1)
     if choice==str("chocolates"):
          msg2=("CHOCOLATES","which chocolate would you like to buy")
          title=("choco palace")
          choices=("Eclairs","Parle","mangobite","orbit","kaccha mango bite")
          choice=buttonbox(msg2,title,choices)
     if  choices==str("Eclairs"):
	  msg3=("Eclairs cost Re.1 per piece/n","how many would you like to buy?")
 	  title=("CHOCOLATE(S)")
          eclair=ccbox(msg3,title)
     if choices==str("Parle"):
          msg4=("Parle cost Re.1 per piece/n","how many would you like to buy?")
          title=("CHOCOLATE(S)")
          parle=ccbox(msg4,title)
     
