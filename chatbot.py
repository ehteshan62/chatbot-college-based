


from tkinter import *
# TKinter used for graphical user interfaces (GUIs) 

# GUI
root = Tk()

#here we titled our project
root.title("Chatbot")


BG_GRAY = "#ABB2B9"
#bg colour define

BG_COLOR = "#17202A"
#here we defined our chatbot color

TEXT_COLOR = "#EAECEE"
#text color 

FONT = "Helvetica 14"
#font name
FONT_BOLD = "Helvetica 13 bold"
#font bold

# Send function
def send():
	send = "You -> " + e.get()
	txt.insert(END, "\n" + send)

	user = e.get().lower()
	
	#from here  client ask questions to our Bot

	if (user == "hello"):
		txt.insert(END, "\n" + "Bot -> Hi there, how can I help?" "\n")

  

	elif (user == "hi" or user == "hii" or user == "hiiii"):
		txt.insert(END, "\n" +  "Bot -> Hi there, what can I do for you?" "\n")

	elif (user == "how are you" or user == "how r u" ):
		txt.insert(END, "\n" + "Bot -> fine! and you" "\n")

	elif (user == "fine" or user == "i am good" or user == "i am doing good" or user == "i am fine" ):
		txt.insert(END, "\n" + "Bot -> Great! how can I help you." "\n")

	elif (user == "thanks" or user == "thank you" or user == "now its my time"):
		txt.insert(END, "\n" + "Bot -> My pleasure !" "\n")

	elif (user == "what do you sell" or user == "what kinds of items are there" or user == "have you something" or user == "sell"):
		txt.insert(END, "\n" + "Bot -> We didn't sell any thing," "\n" + "We provide courses." "\n")

	elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
		txt.insert(
			END, "\n" + "Bot -> What is Room with no walls? A mushroom!" "\n") 

	elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
		txt.insert(END, "\n" + "Bot -> Have a nice day!" "\n")

	elif (user == "fee" or user == "fees" or user =="fee detail"):
		txt.insert(END, "\n" + "Bot->There are different fees, they are based on which course you choose," "\n")

	elif (user == "b.tech" or user == "B.tech" or user == "process for admission in b.tech" or user == "i want to take admission in B.tech"):
		txt.insert(END, "\n" + "Bot->you choose a brilliant course," "\n" + "for taking admission in b.tech""\n" + "you have to submit" "\n" + "your 10th marksheet as well as 12th marksheet" "\n" + "and government IDs" "\n" + "also requires your T.C Migration " "\n" + "from your privious School" "\n" + "Most important thing is you have complete" "\n" + "your 12th/diploma with Mathematics" "\n" )

	elif (user == "M.tech" or user == "M.tech" or user == "process for admission in M.tech" or user == "i want to take admission in m.tech"):
		txt.insert(END, "\n" + "Bot->you choose a brilliant course," "\n" + "for taking admission in m.tech""\n" + "you have to submit" "\n" + "your 10th marksheet as well as 12th marksheet" "\n" + "and government IDs" "\n" + "also requires your T.C Migration " "\n" + "from your privious College" "\n" + "Most important thing is you have complete" "\n" + "your B.tech" "\n" )

	elif (user == "b.pharma" or user == "B.pharma" or user == "process for admission in pharma" or user == "i want to take admission in B.Pharma"):
		txt.insert(END, "\n" + "Bot->you choose a brilliant course," "\n" + "for taking admission in b.pharma""\n" + "you have to submit" "\n" + "your 10th marksheet as well as 12th marksheet" "\n" + "and government IDs" "\n" + "also requires your T.C Migration " "\n" + "from your privious School" "\n" + "Most important thing is you have complete" "\n" + "your 12th/diploma with Biology" "\n" + "also can do with mathematic")

	elif (user == "bba" or user == "BBA" or user == "Bba" or user == "process for admission in bba" or user == "i want to take admission in bba"):
		txt.insert(END, "\n" + "Bot->you choose a brilliant course," "\n" + "for taking admission in bba""\n" + "you have to submit" "\n" + "your 10th marksheet as well as 12th marksheet" "\n" + "and government IDs" "\n" + "also requires your T.C Migration " "\n" + "from your privious School" "\n" + "Most important thing is you have complete" "\n" + "your 12th with Mathematics/Biology" "\n" )

	elif (user == "MBA" or user == "mba" or user == "process for admission in mba" or user == "i want to take admission in Mba"):
		txt.insert(END, "\n" + "Bot->you choose a brilliant course," "\n" + "for taking admission in MBA""\n" + "you have to submit" "\n" + "your 10th marksheet as well as 12th marksheet" "\n" + "and government IDs" "\n" + "also requires your T.C Migration " "\n" + "from your privious college" "\n" + "Most important thing is you have complete" "\n" + "your BBA Course" "\n" )

	elif (user == "Agriculture" or user == "agriculture" or user == "process for admission in agriculture" or user == "i want to take admission in agriculture"):
		txt.insert(END, "\n" + "Bot->you choose a brilliant course," "\n" + "for taking admission in b.tech""\n" + "you have to submit" "\n" + "your 10th marksheet as well as 12th marksheet" "\n" + "and government IDs" "\n" + "also requires your T.C Migration " "\n" + "from your privious School" "\n" + "Most important thing is you have complete" "\n" + "your 12th/diploma with Mathematics" "\n" )

	elif (user == "Nursing" or user == "nusing" or user == "process for admission in nursing" or user == "i want to take admission in nursing"):
		txt.insert(END, "\n" + "Bot->you choose a brilliant course," "\n" + "for taking admission in nursing""\n" + "you have to submit" "\n" + "your 10th marksheet as well as 12th marksheet" "\n" + "and government IDs" "\n" + "also requires your T.C Migration " "\n" + "from your privious School" "\n" + "Most important thing is you have complete" "\n" + "your 12th with Biology" "\n" )

	elif (user == "Hotel management" or user == "hotel management" or user == "process for admission in hotel management" or user == "i want to take admission in hotel management"):
		txt.insert(END, "\n" + "Bot->you choose a brilliant course," "\n" + "for taking admission in hotel management""\n" + "you have to submit" "\n" + "your 10th marksheet as well as 12th marksheet" "\n" + "and government IDs" "\n" + "also requires your T.C Migration " "\n" + "from your privious School" "\n" + "Most important thing is you have complete" "\n" + "your 12th/diploma with Any subject" "\n" )

	




	elif (user == "you are male or female" or user == "male female" or user == "male or female" or user == "male / female" or user == "you r male or female" or user == "u r male or female" or user == "boy or girl" or user == "you are boy or girl"):
		txt.insert(END, "\n" + "Bot-> As I am an Artificial intelligent," "\n" + "I am not male or female in practical," + "\n" "But my owner says I have to behave like Female." "\n")


	
	elif ( user == "who are you" or user == "you" or user == "who r u" ):
		txt.insert(END, "\n" + "Bot -> I am Your Assistant." "\n")

	elif ( user == "Ehteshan" or user == "Ehteshan alam" or user == "who is Ehteshan" or user == "who is Ehteshan alam"):
		txt.insert(END, "\n" + "Bot-> Ehteshan Alam is a student of B.tech cse, from IES UNIVERSITY" "\n" + "he develops me" "\n" + "you can follow him on instagram" "\n" + "his instagram  id is :- @Ehteshan.62" "\n")
	
	elif ( user ==  "your name" or user == "what is your name" or user == "name" ):
		txt.insert(END, "\n" + "Bot-> I'm EKARI" "\n")

	elif ( user == "placement" or user == "highest pakage of your college" or user == "what are the best placement your student got"):
		txt.insert(END, "\n" + "Bot->our best placement got by a student is 23 LPA")
	
	elif (user == "email" or user == "email id" or user == "contact" or user == "contact info" or user == "contact information"):
		txt.insert(END, "\n" + "Bot-> you can contact us by " "\n" + "Email:-ehteshanalam1@gmail.com" "\n" )


	elif (user == "who develop you" or user == "who is your father" or user == "who make you" ):
		txt.insert(END, "\n" + "Bot -> Ehteshan ALAM developes me" "\n")

	elif (user == "course" or user == "courses" or user == "which courses you provide" or user == "which course your college provide " ):
		txt.insert(END, "\n" + "Bot-> IES UNIVERSITY provides you  :-" "\n" "(1) B.TECH" "\n" + "(2) M.TECH" "\n" +"(3)B.PHARMA " "\n" + "ETC..." "\n")

		#and now if all condition given above did not matched then our chatbot replies to client



	else:
		txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that, I am still Learning..." "\n")

	e.delete(0, END)
	

	
#here we designed color, location of texts in chatbot 
#here we defined our chatbots header name
lablel = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="EKARI", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60, height=30)
txt.grid(row=1, column=0, columnspan=2)



scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)


e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send",font=FONT_BOLD, bg=BG_GRAY,
			command=send,).grid(row=2, column=1)




root.mainloop()


