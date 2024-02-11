# Importing Modules
from tkinter import *
from tkinter import ttk 
from time import sleep
from PIL import Image, ImageTk

# Initiating tkinter window
root = Tk()
root.title('TIC TAC TOE Game -By Shubham Pathak')
root.geometry('580x580+400+50')

# Some useful Global Variables
click = 0           # no. of clicks
winner = None       # By Default, winner=none, and changes if someone wins
gameover = False    # By Default, gameover=False, and becomes true after win/draw

# Main Function for Game,  is enacted after UserLogin
def Start_game():
    global gameover
    root.configure(bg="#1AFB1A")    # changing BG after UserLogin
    
    # Destroying the previous widgets during UserLogin
    Player1_Label.destroy()
    username1.destroy()
    Player2_Label.destroy()
    username2.destroy()
    Start.destroy()
    Note.destroy()

    # When any of the 9 buttons is clicked, isClicked function is called
    def isClicked(event):
        global click
        global clicked
        click += 1   # if any button is clicked, no. of click increases by 1
    
    # Monitors over game and discloses the result of the game
    def end_game(event):
        global player1_value
        global player2_value
        global gameover
        
        # Label for Player-1 Win
        X_winner = Label(root, text="", fg="black", font="Algerian 30 bold", bg="#1AFB1A")
        X_winner.place(x=150, y=520)

        # Label for Player-2 Win
        Y_winner = Label(root, text="", fg="black", font="Algerian 30 bold", bg='#1AFB1A')
        Y_winner.place(x=150, y=520)

        # when players will win, the matching boxes will have red colour to indicate the win
                        # 1st player wins
        #  when player-1(x) wins by matching 1st row
        if btn1['text'] == btn2['text'] == btn3['text'] == "X":
            X_winner.configure(text=f"{player1_value.get()} WINS")
            btn1.configure(bg='red', fg='white')
            btn2.configure(bg='red', fg='white')
            btn3.configure(bg='red', fg='white')
            gameover = True

        #  when player-1(x) wins by matching 2nd row
        elif btn4['text'] == btn5['text'] == btn6['text'] == "X":
            X_winner.configure(text=f"{player1_value.get()} WINS")
            btn4.configure(bg='red', fg='white')
            btn5.configure(bg='red', fg='white')
            btn6.configure(bg='red', fg='white')
            gameover = True

        #  when player-1(x) wins by matching 3rd row
        elif btn7['text'] == btn8['text'] == btn9['text'] == "X":
            X_winner.configure(text=f"{player1_value.get()} WINS")
            btn7.configure(bg='red', fg='white')
            btn8.configure(bg='red', fg='white')
            btn9.configure(bg='red', fg='white')
            gameover = True

        #  when player-1(x) wins by matching 1st column
        elif btn1['text'] == btn4['text'] == btn7['text'] == "X":
            X_winner.configure(text=f"{player1_value.get()} WINS")
            btn1.configure(bg='red', fg='white')
            btn4.configure(bg='red', fg='white')
            btn7.configure(bg='red', fg='white')
            gameover = True

        #  when player-1(x) wins by matching 2nd column
        elif btn2['text'] == btn5['text'] == btn8['text'] == "X":
            X_winner.configure(text=f"{player1_value.get()} WINS")
            btn2.configure(bg='red', fg='white')
            btn5.configure(bg='red', fg='white')
            btn8.configure(bg='red', fg='white')
            gameover = True

        #  when player-1(x) wins by matching 3rd column
        elif btn3['text'] == btn6['text'] == btn9['text'] == "X":
            X_winner.configure(text=f"{player1_value.get()} WINS")
            btn3.configure(bg='red', fg='white')
            btn6.configure(bg='red', fg='white')
            btn9.configure(bg='red', fg='white')
            gameover = True

        #  when player-1(x) wins by matching Leading-Diagonal
        elif btn1['text'] == btn5['text'] == btn9['text'] == "X":
            X_winner.configure(text=f"{player1_value.get()} WINS")
            btn1.configure(bg='red', fg='white')
            btn5.configure(bg='red', fg='white')
            btn9.configure(bg='red', fg='white')
            gameover = True

        #  when player-1(x) wins by matching Minor-Diagonal
        elif btn3['text'] == btn5['text'] == btn7['text'] == "X":
            X_winner.configure(text=f"{player1_value.get()} WINS")
            btn3.configure(bg='red', fg='white')
            btn5.configure(bg='red', fg='white')
            btn7.configure(bg='red', fg='white')
            gameover = True

                        # 2nd player wins
        # 1st Row
        elif btn1['text'] == btn2['text'] == btn3['text'] == "O": 
            Y_winner.configure(text=f"{player2_value.get()} WINS")
            btn1.configure(bg='red', fg='white')
            btn2.configure(bg='red', fg='white')
            btn3.configure(bg='red', fg='white')
            gameover = True
        
        # 2nd Row
        elif btn4['text'] == btn5['text'] == btn6['text'] == "O":
            Y_winner.configure(text=f"{player2_value.get()} WINS")
            btn4.configure(bg='red', fg='white')
            btn5.configure(bg='red', fg='white')
            btn6.configure(bg='red', fg='white')
            gameover = True
        
        # 3rd Row
        elif btn7['text'] == btn8['text'] == btn9['text'] == "O":
            Y_winner.configure(text=f"{player2_value.get()} WINS")
            btn7.configure(bg='red', fg='white')
            btn8.configure(bg='red', fg='white')
            btn9.configure(bg='red', fg='white')
            gameover = True

        # 1st Column
        elif btn1['text'] == btn4['text'] == btn7['text'] == "O":
            Y_winner.configure(text=f"{player2_value.get()} WINS")
            btn1.configure(bg='red', fg='white')
            btn4.configure(bg='red', fg='white')
            btn7.configure(bg='red', fg='white')
            gameover = True

        # 2nd Column
        elif btn2['text'] == btn5['text'] == btn8['text'] == "O":
            Y_winner.configure(text=f"{player2_value.get()} WINS")
            btn2.configure(bg='red', fg='white')
            btn5.configure(bg='red', fg='white')
            btn8.configure(bg='red', fg='white')
            gameover = True

        # 3rd Column
        elif btn3['text'] == btn6['text'] == btn9['text'] == "O":
            Y_winner.configure(text=f"{player2_value.get()} WINS")
            btn3.configure(bg='red', fg='white')
            btn6.configure(bg='red', fg='white')
            btn9.configure(bg='red', fg='white')
            gameover = True

        # Leading-Diagonal
        elif btn1['text'] == btn5['text'] == btn9['text'] == "O":
            Y_winner.configure(text=f"{player2_value.get()} WINS")
            btn1.configure(bg='red', fg='white')
            btn5.configure(bg='red', fg='white')
            btn9.configure(bg='red', fg='white')
            gameover = True

        # Minor-Diagonal
        elif btn3['text'] == btn5['text'] == btn7['text'] == "O":
            Y_winner.configure(text=f"{player2_value.get()} WINS")
            btn3.configure(bg='red', fg='white')
            btn5.configure(bg='red', fg='white')
            btn7.configure(bg='red', fg='white')
            gameover = True

                        # Draw
        elif click == 9:
            Draw = Label(root, text="DRAW", fg="red", font="Algerian 30 bold", bg="#1AFB1A")
            Draw.place(x=240, y=530)
            gameover = True

    # chance_flip rotates the chance between the players, and is bound with 9 buttons
    def chance_flip(event):
        # fetching global variables
        global clicked
        global turn
        global click
        global player1_value
        global player2_value
        global gameover

        # determining Player-1's Turn
        if click == 0 or click == 2 or click == 4 or click == 6 or click == 8:
            Turn_Label.configure(text=f"{player1_value.get()}'s Turn")

        # determining Player-2's Turn
        elif click == 1 or click == 3 or click == 5 or click == 7:
            Turn_Label.configure(text=f"{player2_value.get()}'s Turn")

    # When button-1 is clicked
    def btn1_click():
        global click
        global clicked
        btn1.configure(bg='#A19A9A')  # changing BG of button after clicked

        # 1st clicked will be of X and it continues as 1, 3, 5, 7, and 9th click
        if click == 1 or click == 3 or click == 5 or click == 7 or click == 9:
            btn1['text'] = 'X'
        # 2st clicked will be of O and it continues as 2, 4, 6, and 8th click
        if click == 2 or click == 4 or click == 6 or click == 8:
            btn1['text'] = 'O'
        chance_flip('<Button-1>') # chance_flip is called after every button-click

    def btn2_click():
        # Same as button1
        global click
        global clicked
        btn2.configure(bg='#A19A9A')
        if click == 1 or click == 3 or click == 5 or click == 7 or click == 9:
            btn2['text'] = 'X'
        if click == 2 or click == 4 or click == 6 or click == 8:
            btn2['text'] = 'O'
        chance_flip('<Button-1>')

    def btn3_click():
        global click
        global clicked
        btn3.configure(bg='#A19A9A')
        if click == 1 or click == 3 or click == 5 or click == 7 or click == 9:
            btn3['text'] = 'X'
        if click == 2 or click == 4 or click == 6 or click == 8:
            btn3['text'] = 'O'
        chance_flip('<Button-1>')

    def btn4_click():
        global click
        global clicked
        btn4.configure(bg='#A19A9A')
        if click == 1 or click == 3 or click == 5 or click == 7 or click == 9:
            btn4['text'] = 'X'
        if click == 2 or click == 4 or click == 6 or click == 8:
            btn4['text'] = 'O'
        chance_flip('<Button-1>')

    def btn5_click():
        global click
        global clicked
        btn5.configure(bg='#A19A9A')
        if click == 1 or click == 3 or click == 5 or click == 7 or click == 9:
            btn5['text'] = 'X'
        if click == 2 or click == 4 or click == 6 or click == 8:
            btn5['text'] = 'O'
        chance_flip('<Button-1>')

    def btn6_click():
        global click
        global clicked
        btn6.configure(bg='#A19A9A')
        if click == 1 or click == 3 or click == 5 or click == 7 or click == 9:
            btn6['text'] = 'X'
        if click == 2 or click == 4 or click == 6 or click == 8:
            btn6['text'] = 'O'
        chance_flip('<Button-1>')

    def btn7_click():
        global click
        global clicked
        btn7.configure(bg='#A19A9A')
        if click == 1 or click == 3 or click == 5 or click == 7 or click == 9:
            btn7['text'] = 'X'
        if click == 2 or click == 4 or click == 6 or click == 8:
            btn7['text'] = 'O'
        chance_flip('<Button-1>')

    def btn8_click():
        global click
        global clicked
        btn8.configure(bg='#A19A9A')
        if click == 1 or click == 3 or click == 5 or click == 7 or click == 9:
            btn8['text'] = 'X'
        if click == 2 or click == 4 or click == 6 or click == 8:
            btn8['text'] = 'O'
        chance_flip('<Button-1>')

    def btn9_click():
        global click
        global clicked
        btn9.configure(bg='#A19A9A')
        if click == 1 or click == 3 or click == 5 or click == 7 or click == 9:
            btn9['text'] = 'X'
        if click == 2 or click == 4 or click == 6 or click == 8:
            btn9['text'] = 'O'
        chance_flip('<Button-1>')
        
    # Frame of Game_Board
    Game_Frame = Frame(root)
    Game_Frame.place(x=80, y=100)

    # Button-1
    btn1 = Button(Game_Frame, text='', bg="skyblue", fg='red', height=5, width=10, command=btn1_click, font='helvatica 15 bold')
    btn1.grid(row=1, column=1)
    btn1.bind("<Button-1>", isClicked)  # Binding with isClicked function 
    btn1.bind('<Motion>', end_game) # Binding with end_game function

    # Button-2
    btn2 = Button(Game_Frame, text='', bg="skyblue", fg='red', height=5, width=10, command=btn2_click, font='helvatica 15 bold')
    btn2.grid(row=1, column=2)
    btn2.bind("<Button-1>", isClicked)
    btn2.bind('<Motion>', end_game)

    # Button-3
    btn3 = Button(Game_Frame, text='', bg="skyblue", fg='red', height=5, width=10, command=btn3_click, font='helvatica 15 bold')
    btn3.grid(row=1, column=3)
    btn3.bind("<Button-1>", isClicked)
    btn3.bind('<Motion>', end_game)

    # Button-4
    btn4 = Button(Game_Frame, text='', bg="skyblue", fg='red', height=5, width=10, command=btn4_click, font='helvatica 15 bold')
    btn4.grid(row=2, column=1)
    btn4.bind("<Button-1>", isClicked)
    btn4.bind('<Motion>', end_game)

    # Button-5
    btn5 = Button(Game_Frame, text='', bg="skyblue", fg='red', height=5, width=10, command=btn5_click, font='helvatica 15 bold')
    btn5.grid(row=2, column=2)
    btn5.bind("<Button-1>", isClicked)
    btn5.bind('<Motion>', end_game)

    # Button-6
    btn6 = Button(Game_Frame, text='', bg="skyblue", fg='red', height=5, width=10, command=btn6_click, font='helvatica 15 bold')
    btn6.grid(row=2, column=3)
    btn6.bind("<Button-1>", isClicked)
    btn6.bind('<Motion>', end_game)

    # Button-7
    btn7 = Button(Game_Frame, text='', bg="skyblue", fg='red', height=5, width=10, command=btn7_click, font='helvatica 15 bold')
    btn7.grid(row=3, column=1)
    btn7.bind("<Button-1>", isClicked)
    btn7.bind('<Motion>', end_game)
    
    # Button-8
    btn8 = Button(Game_Frame, text='', bg="skyblue", fg='red', height=5, width=10, command=btn8_click, font='helvatica 15 bold')
    btn8.grid(row=3, column=2)
    btn8.bind("<Button-1>", isClicked)
    btn8.bind('<Motion>', end_game)

    # Button-9
    btn9 = Button(Game_Frame, text='', bg="skyblue", fg='red', height=5, width=10, command=btn9_click, font='helvatica 15 bold')
    btn9.grid(row=3, column=3)
    btn9.bind("<Button-1>", isClicked)  
    btn9.bind('<Motion>', end_game)  

    # Label for Turn of Players, and text changes according to chance_flip function
    global player1_value
    Turn_Label = Label(root, text=f"{player1_value.get()}'s Turn", font=('Algerian', 20, 'bold'), fg='red', bg='#1AFB1A')
    Turn_Label.place(x=200, y=60)   

            # Out of the Start_Function

# Title of Game, TIC TAC TOE
Label(root, text="TIC TAC TOE", font="Algerian 30 bold", bg="blue").place(x=180, y=10)

root.configure(bg="#00E8FF") # BG color during UserLogin


# Note for user, player-1=X, player-2=O
Note = Label(root, bg="#00E8FF", 
text="Note:- Player-1 should choose 'X' \n Player-2 should choose 'O'",
fg='red', font=('lucida', 15, 'bold'))
Note.pack(side=TOP, pady=100)

# Login Fame
Login_Frame = Frame(root, bg="#00E8FF")
Login_Frame.place(x=100, y=220)

                    # Player-1
# Label with Text, Player-1
Player1_Label = Label(Login_Frame, text="(X)Player-1", font='helvatica 15 bold', bg="#00E8FF",fg="red")
Player1_Label.grid(row=1, column=1, pady=50)

# Taking User-1 Name Entry using ComboBox
player1_value = StringVar()
username1 = ttk.Combobox(Login_Frame, width = 20, textvariable = player1_value) 
username1['values'] = (' Shubham', ' Satyam', ' Gyanendra', ' Shruti') 
username1.grid(column = 2, row = 1) 
username1.current() 

                    # Player-2
# Label with Text, Player-2
Player2_Label = Label(Login_Frame, text="(O)Player-2", font='helvatica 15 bold', bg="#00E8FF", fg="red")
Player2_Label.grid(row=2, column=1, pady=50)

# Taking User-2 Name Entry using ComboBox
player2_value = StringVar()
username2 = ttk.Combobox(Login_Frame, width = 20, textvariable = player2_value) 
username2['values'] = (' Shubham', ' Satyam', ' Gyanendra', ' Shruti') 
username2.grid(column = 2, row = 2) 
username2.current() 

# Start Button for Starting the Game with Start_game function
Start = Button(Login_Frame, text="Start", command=Start_game, bg='#BC5837', fg='white', font='lucida 12 bold')
Start.grid(row=3, column=2)

# Running the mainloop
root.mainloop()