from easygui import *
import sys
while 1:
   msgbox("Hello,welcome to the supermarket!!")
   l=[]
   while 1:  
     msg="What do you want to buy?"
     title="A1 SUPERMARKET"
     choices=["CHOCOLATES","BISCUITS","SOAPS","CLOTHS"]
     choice=choicebox(msg,title,choices)
     if str(choice)=="CHOCOLATES":
        msg1="Which chocolates do you want?"
        title1="CHOCOLATES"
        choice1=["DairyMilk","Hersheys","Nutella","Kitkat","Gems"]
        choice2=choicebox(msg1,title1,choice1) 
         
        if choice2=="Kitkat":
           a=5
           msgbox(msg=str(a),title="Price of Kitkat")
           l.append(a)
        elif choice2=="DairyMilk":
             b=10
             msgbox(msg=str(b),title="price of DairyMilk")
             l.append(b)
        elif choice2=="Hersheys":
             c=50
             msgbox(msg=str(c),title="price of Hersheys")
             l.append(c) 
        elif choice2=="Nutella":
             d=100
             msgbox(msg=str(d),title="price of Nutella")
             l.append(d) 
        else:
             e=20
             msgbox(msg=str(e),title="price of Gems")
             l.append(e) 
 
     elif str(choice)=="BISCUITS":
          msg2="Which biscuits do you want?"
          title2="BISCUITS"
          choice3=["ParleG","Hide and Seek","Bourbon","Monaco","Marie"]
          choice4=choicebox(msg2,title2,choice3)
          if choice4=="ParleG":
           f=10
           msgbox(msg=str(f),title="Price of ParleG")
           l.append(f)
          elif choice4=="Hide and Seek":
             g=20
             msgbox(msg=str(g),title="price of Hide and Seek")
             l.append(g)
          elif choice4=="Bourbon":
             h=25
             msgbox(msg=str(g),title="price of Bourbon")
             l.append(h) 
          elif choice4=="Monaco":
             i=15
             msgbox(msg=str(i),title="price of Monaco")
             l.append(i) 
          else:
             j=20
             msgbox(msg=str(j),title="price of Marie")
             l.append(j) 
 


     elif str(choice)=="SOAPS":
         msg3="Which soaps do you want?"
         title3="SOAPS"
         choice5=["Lux","Dettol","Lifeboy","Pears","Moti"]
         choice6=choicebox(msg3,title3,choice5) 
         if choice6=="Lux": 
           k=30
           msgbox(msg=str(f),title="Price of Lux")
           l.append(k)
         elif choice6=="Dettol":
             l=20
             msgbox(msg=str(g),title="price of Dettol")
             l.append(l)
         elif choice6=="Lifeboy":
             m=30
             msgbox(msg=str(g),title="price of Lifeboy")
             l.append(m) 
         elif choice6=="Pears":
             n=40
             msgbox(msg=str(i),title="price of Pears")
             l.append(i) 
         else:
             o=100
             msgbox(msg=str(j),title="price of Moti")
             l.append(j) 

     elif str(choice)=="CLOTHS":
         msg4="Which brand do you want?"
         title4="CLOTHS"
         choice7=["US POLO","CottonKing","Blackberry","Levis","Peter England"]
         choice8=choicebox(msg4,title4,choice7)
     msg="Do you want to continue?"
     title="Please Confirm"
     if ccbox(msg,title):
        pass
     else:
          break
   i=0
   sum=0
   for i in l:
      sum+=i
      
      
   msgbox(str(sum),"Total Cost","Result")
   msg="Do you want to shop again?"
   title="Please Confirm"
   if ccbox(msg,title):
        pass
   else:
          sys.exit()
