from time import sleep
def start_prompt():
    while True:
        print("""Would you like to start the game?
Select 1 to start.
Press anyother button to back-off.    
        """)
        choice = input("Enter your choice:")

        if choice == "1":
            start_story()
        else:
            print("Hmm! Thought you could make it.")
            sleep(5)
            quit()
    scr()

def start_story():
    while True:
        scr()
        print("""You've entered a room with a corpse inside. 
The murdered person was the owner of the house named James Brooks.
The body was found in the study room.
The room is locked with all the doors and windows shut and with no hidden escape doors.
There were only 2 keys to the room one with the dead person and the other one was with you.
You enter the room first and discover the body.
As a famous detective you have been assigned the job to find out the culprit.
""")
        print("""There were three people living in the house with the master.
The chef Mr.Ripper Jack,
the house maid Mrs.Agatha Christie
and the gardner Mr.Bojack Kai.
Mr.Jack enters the room after which you tell him to call for the police quickly.
 """)
        choice = input("Type 1 to listen to their statements or press any other button to quit:")
        if choice == "1":
            start_story1()
        else:
            print("Hmm! Thought you could find the culprit.")
            sleep(5)
            quit()
    scr()


def start_story1():
    scr()
    while True:
        opt = ["1", "2", "3", "4"]
        print("""To listen to Mr.Ripper Jack's statement press 1,
to listen to Mrs.Agatha Christie's statement press 2,
to listen to Mr.Bojack Kai's statement press 3,
press 4 to continue with the story.        
""")
        choice = input("Select an option:")
        if choice not in opt:
            scr()
            continue
        if choice == "1":
            Jack_story()
        elif choice == "2":
            Agatha_story()
        elif choice == "3":
            Bojack_story()
        elif choice == "4":
            start_story2()
def Jack_story():
    scr()
    print("""I was in the kitchen preparing for dinner when I suddenly heard the master calling out for help.
The murder has nothing to do with me but Mrs.Agatha was borrowing money from the master
and couldn't pay him back on time. The master was nagging her each day to pay him back and also 
he was going to harm her family if she did not pay on time.
By the way weren't you going to meet him today?""")
    choice = input("Press enter after reading:")
    if choice == 1:
        Jack_story()
    else:
        start_story1()

def Agatha_story():
    scr()
    print("""It is true that the master was asking me back for his money but 
I was going to pay him back the money today itself besides 
I was cleaning the Living room when I heard the master crying out.
I only saw Mr.Bojack going towards masters room why don't you question him instead of framing me.""")
    choice = input("Press enter after reading:")
    if choice == 1:
        Agatha_story()
    else:
        start_story1()

def Bojack_story():
    scr()
    print("""I was going to ask the master for money as I have been in a lot of debt due to gambling.
The master was busy so he told me to pursue the matter some other time maybe
he had plans to meet someone else. The master was always very kind to me Please apprehend the culprit immediately.""")
    choice = input("Press enter after reading:")
    if choice == 1:
        Bojack_story()
    else:
        start_story1()

def start_story2():
    while True:
        scr()
        choice = input("If you want to hear their statements press 1 or to continue press any other button:")
        if choice == "1":
            start_story1()
            scr()
        else:
            start_story3()
            scr()


def start_story3():
    scr()
    print("""Hearing their stories YOU now know who the culprit is.
You head to the Chief Investigation Officer to tell him who Killed Mr.James Brooks""")
    choice = input("Press enter to select the culprit:")
    if choice == 1: start_story3()
    else:
        scr()
        end()

def end():
    while True:
        opt = ["1", "2", "3"]
        choice = input("""select 1 to choose Mr.Jack as the culprit.
select 2 to choose Mrs.Agatha as the culprit.
select 3 to choose Mr.Bojack as the culprit.
select 4 to select someone else as the culprit:""")
        if choice in opt:
            scr()
            print("Sorry he/she is not the killer")
            print("Try again")
            end()
        elif choice == "4":
            scr()
            print("""Since you have selected this option I congratulate you on solving the mystery.
The first clue is that YOU have the spare key.
The second clue is that YOU had a meeting with the master.
The third and final clue is that the room was locked with no other evidences to be found.
This all points to only one deduction that YOU are the killer.""")
            print("Thank YOU for Playing!")
            sleep(10)
            quit()
        else:
            continue



def scr():
    print("\n" * 100)

start_prompt()
quit()
