from Tkinter import *    #using tkinter
from time import *       #for inserting time 
right=0
x=16
t=int()                 
def check(letter, view,view1):            #answer checking display
        global right
        if letter == correctLetter[index]:
            label = Label(view, text="Right!")
            right += 1
        else:
            label = Label(view, text="Wrong!")
        label.pack()
        view.after(1000,lambda *arg: unpackView(view,view1))


def getView(window):                      #designing the window
        view = Frame(window,width=90, height=60)
        view1= Frame(window,width=90, height=60)
        view.pack()
        view1.pack()
        #view3=Frame(window)
        #view3.pack()
        lbl=Label(view, text=questions)
        button1=Button(view1, text=answers[0],bg="blue", fg="white",width=30, command=lambda *args: check("A\n", view,view1))
        button2=Button(view1, text=answers[1],bg="blue", fg="white",width=30, command=lambda *args: check("B\n", view,view1))
        button3=Button(view1, text=answers[2],bg="blue", fg="white",width=30, command=lambda *args: check("C\n", view,view1))
        button4=Button(view1, text=answers[3],bg="blue", fg="white",width=30, command=lambda *args: check("D\n", view,view1))
        lbl.pack(side=TOP)
        lvl=Label(view,text="")
        lvl.pack(fill=X)
        button1.grid(row=0,column=0,pady=10)
        button2.grid(row=0,column=1,pady=10)
        button3.grid(row=1,column=0,pady=10)
        button4.grid(row=1,column=1,pady=10)
        
        def countdown():                  #introducing timer
                
                global t
                t-=1          #decrementing time varible for dramatic effect.
                if t==0:
                    label1 = Label(view, text="Wrong!") #displaying wrong if timer runs out
                    label1.pack()
                    view.after(1000,lambda *arg: unpackView(view,view1))
            
                lvl.config(text=str(t))
                if t%2==0:                  #changing colour for timer background, flashy timer 
                    lvl["fg"]="black"
                    lvl["bg"]="white"
                else:
                    lvl["fg"]="white"
                    lvl["bg"]="black"
                view.after(1000,countdown)
        countdown()

def unpackView(view,view1):
        view.destroy()
        view1.destroy()
        #view3.pack_forget()
        #window.destroy()
        askQuestion()

def askQuestion():
    global t,x,view,view1,a,answers,answer,questions,question, window, index, button,right, number_of_questions 
    if(len(question) == index + 1):
        Label(window, text="Thank you for answering the questions. " + str(right) + " of " + str(number_of_questions) + " questions answered right").pack()
        return
    button.destroy()
    index += 1
    questions=question[index]
    answers=answer[index]
    t=x
    getView(window)
    
#questions=[]           (code for if the questions are given right in the program)  
#question= ["Who is the captain of the Indian cricket team?","Albert Einstein was awarded Nobel Prize for which of his work","If a moving object's velocity is changed by a factor of 1.5, what will its impact on its kinetic energy ?","Which is the most electronegative atom ?"]
#answer = [["Virat Kohli","M.S Dhoni","Rohit Sharma","Shikhar Dhawan"],["Theory of Relativity","Photoelectric Effect","Principle of Wave-Particle Duality","Theory of Critical Opalescence"],["1.5 times","3 times","2.25 times","6 times"],["O","F","Cl","Br"]]
#correctLetter = ["A","B","C","B"]
question = []                         #(code for if questions in another text file  )
correctLetter=[]
answer=[]
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
    question.append(line)
    answer1 = []
    for i in range (4):
        answer1.append(file.readline())
    answer.append(answer1)
    correctLetter.append(file.readline())
    line = file.readline()
file.close()
index = -1
number_of_questions = len(question)
print(correctLetter)
print(question)
window = Tk()
view=Frame(window,width=15, height=10)
button = Button(view, text="Start", command=askQuestion,width=10,height=2)
view.pack()
button.pack()
window.mainloop()