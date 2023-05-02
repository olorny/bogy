import random
from tkinter import *



window = Tk()
window.title("2048")

def key_pressed(event):
    print("key pressed", event.keycode)
    act_game.move(event.keycode)
    show(act_game)
    



weight_list = [2,2,2,2,2,4]
values = [[0,2,0,2],[2,32,4,4],[0,0,0,0],[0,2,0,2]]
number = [[2,4,8,16],[16,8,4,2],[1,2,3,4],[5,6,7,8]]
tiles = [[2,4,8,16],[16,8,4,2],[1,2,3,4],[5,6,7,8]]

def compose(x):
    overline2_frame = Frame(overline_frame, bg = "black", height = 82, width = 125)
    overline2_frame.place(x=155, y=0)
    overline2_label = Label(overline2_frame, text = "Score:", fg="white", bg = "black", font=("72 Condensed", 20))
    overline2_label.place(relx=0.5 , rely=0.5, anchor = S)
    overline2_label = Label(overline2_frame, text = x.score, fg="white", bg = "black", font=("72 Condensed", 28))
    overline2_label.place(relx=0.5 , rely=0.5, anchor = N)

    overline2_frame = Frame(overline_frame, bg = "black", height = 82, width = 125)
    overline2_frame.place(x=290, y=0)
    overline2_label = Label(overline2_frame, text = "Best:", fg="white", bg = "black", font=("72 Condensed", 20))
    overline2_label.place(relx=0.5 , rely=0.5, anchor = S)
    overline2_label = Label(overline2_frame, text = game.highscore, fg="white", bg = "black", font=("72 Condensed", 28))
    overline2_label.place(relx=0.5 , rely=0.5, anchor = N)

    for i in range(4):
        for j in range(4):     
            if x.values[i][j]==0:
                tiles[i][j] = Frame(play_frame, bg = "#bfafa0", height = 88, width = 88)
                tiles[i][j].place(x=12+j*100, y=12+i*100)
                number[i][j] = Label(tiles[i][j], text = x.values[i][j], fg="#bfafa0", bg = "#bfafa0", font=("72 Condensed", 48))
                number[i][j].place(relx=0.5 , rely=0.5, anchor = CENTER)
            elif x.values[i][j]==2:
                tiles[i][j] = Frame(play_frame, bg = "#eee4da", height = 88, width = 88)
                tiles[i][j].place(x=12+j*100, y=12+i*100)
                number[i][j] = Label(tiles[i][j], text = x.values[i][j], fg="#756c63", bg = "#eee4da", font=("72 Condensed", 48))
                number[i][j].place(relx=0.5 , rely=0.5, anchor = CENTER)
            elif x.values[i][j]==4:
                tiles[i][j] = Frame(play_frame, bg = "#eee1ce", height = 88, width = 88)
                tiles[i][j].place(x=12+j*100, y=12+i*100)
                number[i][j] = Label(tiles[i][j], text = x.values[i][j], fg="#7b7269", bg = "#eee1ce", font=("72 Condensed", 48))
                number[i][j].place(relx=0.5 , rely=0.5, anchor = CENTER)
            elif x.values[i][j]==8:
                tiles[i][j] = Frame(play_frame, bg = "#f4b27e", height = 88, width = 88)
                tiles[i][j].place(x=12+j*100, y=12+i*100)
                number[i][j] = Label(tiles[i][j], text = x.values[i][j], fg="#f8f5ec", bg = "#f4b27e", font=("72 Condensed", 48))
                number[i][j].place(relx=0.5 , rely=0.5, anchor = CENTER)
            elif x.values[i][j]==16:
                tiles[i][j] = Frame(play_frame, bg = "#f6976b", height = 88, width = 88)
                tiles[i][j].place(x=12+j*100, y=12+i*100)
                number[i][j] = Label(tiles[i][j], text = x.values[i][j], fg="#f7f7f5", bg = "#f6976b", font=("72 Condensed", 48))
                number[i][j].place(relx=0.5 , rely=0.5, anchor = CENTER)
            elif x.values[i][j]==32:
                tiles[i][j] = Frame(play_frame, bg = "#f77e69", height = 88, width = 88)
                tiles[i][j].place(x=12+j*100, y=12+i*100)
                number[i][j] = Label(tiles[i][j], text = x.values[i][j], fg="#f7f7f5", bg = "#f77e69", font=("72 Condensed", 48))
                number[i][j].place(relx=0.5 , rely=0.5, anchor = CENTER)
            elif x.values[i][j]==64:
                tiles[i][j] = Frame(play_frame, bg = "#f76148", height = 88, width = 88)
                tiles[i][j].place(x=12+j*100, y=12+i*100)
                number[i][j] = Label(tiles[i][j], text = x.values[i][j], fg="#f7f7f5", bg = "#f76148", font=("72 Condensed", 48))
                number[i][j].place(relx=0.5 , rely=0.5, anchor = CENTER)
            elif x.values[i][j]==128:
                tiles[i][j] = Frame(play_frame, bg = "#edce73", height = 88, width = 88)
                tiles[i][j].place(x=12+j*100, y=12+i*100)
                number[i][j] = Label(tiles[i][j], text = x.values[i][j], fg="#f7f7f5", bg = "#edce73", font=("72 Condensed", 48))
                number[i][j].place(relx=0.5 , rely=0.5, anchor = CENTER)
            elif x.values[i][j]==256:
                tiles[i][j] = Frame(play_frame, bg = "#edca64", height = 88, width = 88)
                tiles[i][j].place(x=12+j*100, y=12+i*100)
                number[i][j] = Label(tiles[i][j], text = x.values[i][j], fg="#f7f7f5", bg = "#edca64", font=("72 Condensed", 48))
                number[i][j].place(relx=0.5 , rely=0.5, anchor = CENTER)
            elif x.values[i][j]==512:
                tiles[i][j] = Frame(play_frame, bg = "#edc651", height = 88, width = 88)
                tiles[i][j].place(x=12+j*100, y=12+i*100)
                number[i][j] = Label(tiles[i][j], text = x.values[i][j], fg="#f7f7f5", bg = "#edc651", font=("72 Condensed", 48))
                number[i][j].place(relx=0.5 , rely=0.5, anchor = CENTER)
            elif x.values[i][j]==1024:
                tiles[i][j] = Frame(play_frame, bg = "#eec744", height = 88, width = 88)
                tiles[i][j].place(x=12+j*100, y=12+i*100)
                number[i][j] = Label(tiles[i][j], text = x.values[i][j], fg="#f7f7f5", bg = "#eec744", font=("72 Condensed", 37))
                number[i][j].place(relx=0.5 , rely=0.5, anchor = CENTER)
            elif x.values[i][j]==2048:
                tiles[i][j] = Frame(play_frame, bg = "#eccc5f", height = 88, width = 88)
                tiles[i][j].place(x=12+j*100, y=12+i*100)
                number[i][j] = Label(tiles[i][j], text = x.values[i][j], fg="#f7f7f5", bg = "#eccc5f", font=("72 Condensed", 37))
                number[i][j].place(relx=0.5 , rely=0.5, anchor = CENTER)
            elif x.values[i][j]==4096:
                tiles[i][j] = Frame(play_frame, bg = "#fe3d3e", height = 88, width = 88)
                tiles[i][j].place(x=12+j*100, y=12+i*100)
                number[i][j] = Label(tiles[i][j], text = x.values[i][j], fg="#f7f7f5", bg = "#fe3d3e", font=("72 Condensed", 37))
                number[i][j].place(relx=0.5 , rely=0.5, anchor = CENTER)


def show(x):
    print("highscore: ", game.highscore)
    print("score:", x.score)
    print("Moves:", x.moves)

    for i in range(4):
        for j in range(4):
            print(x.values[i][j], end = '\t')
        print()
    print()
    compose(x)

def num_values(x):
    counter = 0
    for i in range(4):
        for j in range(4):
            if(x[i][j] != 0):
                counter += 1
    return counter

class game:
    values = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,1]]
    values_old = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    score = 0
    score_old = 0
    moves = 0
    highscore = 0
    alive = 1

    def __init__(self):
        for i in range(4):
            for j in range(4):
                self.values[i][j] = 0
        while (num_values(self.values) < 2):
            self.values[random.randrange(4)][random.randrange(4)] = random.choice(weight_list)
        self.backup()
        self.score_old = self.score

    def backup(self):
        for i in range(4):
            for j in range(4):
                self.values_old[i][j] = self.values[i][j]

    def reset(self):
        self.backup()
        for i in range(4):
            for j in range(4):
                self.values[i][j] = 0
        while (num_values(self.values) < 2):
            self.values[random.randrange(4)][random.randrange(4)] = random.choice(weight_list)
        self.score = 0
        self.moves  = 0
        self.alive = 1


    def step_back(self):
        if self.moves != 0 and self.values != self.values_old:
            self.moves -= 1
        for i in range(4):
            for j in range(4):
                self.values[i][j] = self.values_old[i][j]
        self.score = self.score_old
        self.alive = 1
        
    def move(self, command):
        if command == 8:
            self.step_back()
        elif command == 82:
            self.reset()
        elif (command > 36 and command < 41):
            self.backup()
            self.score_old = self.score

            if(command == 37):
                self.swipe_l()
            elif(command == 38):
                self.swipe_u()
            elif(command == 39):
                self.swipe_r()
            elif(command == 40):
                self.swipe_d()

            if (num_values(self.values) < 16 and self.values != self.values_old):
                i = random.randrange(4)
                j = random.randrange(4)
                while (self.values[i][j] != 0):
                    i = random.randrange(4)
                    j = random.randrange(4)
                self.values[i][j] = random.choice(weight_list)
                self.moves += 1
            else:
                self.alive = 0
            if game.highscore < self.score:
                game.highscore = self.score       

    def swipe_l(self):
        for i in range(4):
            j = 0
            while j < 3:
                atj = j + 1
                while(self.values[i][atj] == 0 and atj < 3):
                    atj += 1
                if self.values[i][j] == 0:
                    self.values[i][j] = self.values[i][atj]
                    self.values[i][atj] = 0
                    if self.values[i][j] == 0:
                        j += 1
                elif(self.values[i][j] == self.values[i][atj]):
                    self.values[i][j] += self.values[i][atj]
                    self.score += self.values[i][j]
                    self.values[i][atj] = 0
                    j += 1
                else:
                    j += 1

    def swipe_r(self):
        for i in range(4):
            j = 0
            while j < 3:
                atj = j + 1
                while(self.values[i][3-atj] == 0 and atj < 3):
                    atj += 1
                if self.values[i][3-j] == 0:
                    self.values[i][3-j] = self.values[i][3-atj]
                    self.values[i][3-atj] = 0
                    if self.values[i][3-j] == 0:
                        j += 1
                elif(self.values[i][3-j] == self.values[i][3-atj]):
                    self.values[i][3-j] += self.values[i][3-atj]
                    self.score += self.values[i][3-j]
                    self.values[i][3-atj] = 0
                    j += 1
                else:
                    j += 1

    def swipe_u(self):

        for j in range(4):
            i = 0
            while i < 3:
                ati = i + 1
                while(self.values[ati][j] == 0 and ati < 3):
                    ati += 1
                if self.values[i][j] == 0:
                    self.values[i][j] = self.values[ati][j]
                    self.values[ati][j] = 0
                    if self.values[i][j] == 0:
                        i += 1
                elif(self.values[i][j] == self.values[ati][j]):
                    self.values[i][j] += self.values[ati][j]
                    self.score += self.values[i][j]
                    self.values[ati][j] = 0
                    i += 1
                else:
                    i += 1

    def swipe_d(self):
        for j in range(4):
            i = 0
            while i < 3:
                ati = i + 1
                while(self.values[3-ati][j] == 0 and ati < 3):
                    ati += 1
                if self.values[3-i][j] == 0:
                    self.values[3-i][j] = self.values[3-ati][j]
                    self.values[3-ati][j] = 0
                    if self.values[3-i][j] == 0:
                        i += 1
                elif(self.values[3-i][j] == self.values[3-ati][j]):
                    self.values[3-i][j] += self.values[3-ati][j]
                    self.score += self.values[3-i][j]
                    self.values[3-ati][j] = 0
                    i += 1
                else:
                    i += 1




zwischen_frame = Frame(window, height = 50, width = 600)
zwischen_frame.pack()

overline_frame = Frame(window, height = 140, width = 412)
overline_frame.pack()

overline1_frame = Frame(overline_frame, bg = "#eccc5f", height = 140, width = 140)
overline1_frame.place(x=0,y=0)
overline1_label = Label(overline1_frame, text = "2048", fg="#f7f7f5", bg = "#eccc5f", font=("72 Condensed", 37))
overline1_label.place(relx=0.5 , rely=0.5, anchor = CENTER)


zwischen_frame = Frame(window, height = 50, width = 412)
zwischen_frame.pack()

play_frame = Frame(window, bg = "#a59281", height = 412, width = 412)
play_frame.pack()

zwischen_frame = Frame(window, height = 50, width = 412)
zwischen_frame.pack()


act_game = game()
show(act_game)
compose(act_game)

window.bind("<Key>", key_pressed)

window.mainloop()