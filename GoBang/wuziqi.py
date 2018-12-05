from tkinter import *
from tkinter.messagebox import *
from wuziqi77 import *

class wuziqi(object):

    def __init__(self):
        self.size = 150
        self.start=25
        self.gap=50
        self.last=self.start+(self.size-1)*self.gap
        self.init_board()
        self.draw_board()


        self.window.mainloop()
        return

    def init_board(self):
        self.window = Tk()
        self.window.title("五子棋")
        self.window.geometry("1300x940")
        self.window.resizable(0, 0)
        self.canvas = Canvas(self.window, bg="#EEE8AC", width=940, height=940)
        self.canvas.pack()
        self.draw_button()
        return

    def draw_button(self):
        start = Button(self.window, text="开始", width=8, command=self.start_button)
        start.place(relx=0, rely=0, x=573, y=50)
        return

    def start_button(self):
        self.play()

    def draw_board(self):   #画棋盘
        for row in range(self.size):
            if row==0 or row==self.size-1:
                self.canvas.create_line((self.start,self.start + row * self.gap),(self.last,self.start + row * self.gap),width=2)
            else:
                self.canvas.create_line((self.start,self.start + row * self.gap),(self.last,self.start + row * self.gap),width=1)
        for col in range(self.size):
            if col == 0 or col == self.size-1:
                self.canvas.create_line((self.start + col * self.gap, self.start), (self.start + col * self.gap, self.last), width=2)
            else:
                self.canvas.create_line((self.start + col * self.gap, self.start), (self.start + col * self.gap, self.last), width=1)
        point1=self.start+self.gap*1
        point2=self.start+self.gap*(self.size-2)
        point3=self.start+self.gap*(int(self.size/2))
        r=3
        self.canvas.create_oval(point1-r, point1-r, point1+r, point1+r, fill="black")
        self.canvas.create_oval(point1-r, point2-r, point1+r, point2+r, fill="black")  # 棋盘上中心与四角的五个点
        self.canvas.create_oval(point3-r, point3-r, point3+r, point3+r, fill="black")
        self.canvas.create_oval(point2-r, point1-r, point2+r, point1+r, fill="black")
        self.canvas.create_oval(point2-r, point2-r, point2+r, point2+r, fill="black")
        return


    def play(self):
        self.gobang=GoBang()
        self.canvas.bind('<Button-1>', self.get_position)

    def get_position(self,event):
        x=event.x
        y=event.y
        con_gap=self.gap/2
        con_start=self.start-self.gap/2
        con_end=self.last+self.gap/2
        row=int((x-con_start)/self.gap)
        col=int((y-con_start)/self.gap)
        if(self.gobang.is_blank(col,row)):
            self.draw_chess(row,col,True)
            self.set_chess(row,col)
            win=self.gobang.is_win()
            print(win)
            if(win==1):
                showinfo("游戏结束","游戏结束，电脑赢")
            elif(win==2):
                showinfo("游戏结束", "游戏结束，玩家赢")
            elif(win==3):
                showinfo("游戏结束", "游戏结束，平局")
        return

    def set_chess(self,row,col):
        robot=self.gobang.set_chessboard(col,row)
        chess=self.gobang.get_chessboard()
        self.draw_chess(robot[1], robot[0], False)
        print(robot)
        print(chess)
        return

    def draw_chess(self,row,col,player):
        x=self.start+row*self.gap
        y=self.start+col*self.gap
        r=15
        if player==True:
            color="black"
        else:
            color="white"
        self.canvas.create_oval(x-r,y-r,x+r,y+r,fill=color)
        return


if __name__=='__main__':
    game=wuziqi()

