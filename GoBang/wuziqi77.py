import numpy as np
import copy

class GoBang():
    def ifwin(self,a1):  #terminal-test win=1电脑赢 win=2player赢 win=3和棋
        win = 0          #依次对十五横十五纵，以及各条对角线，进行判断是否有五子连珠的情况，若电脑连成五子，返回win=1，玩家连成五子，返回win=2
        a = [1,1,1,1,1]
        b = [2,2,2,2,2]
        for x in a1:
            for j in range(11):
                if (x[j:j+5] ==a).all():
                    win =1
                if (x[j:j+5] ==b).all():
                    win=2
        for i in range(15):
            for j in range(11):
                if (a1[:,i][j:j+5] ==a).all():
                    win =1
                if (a1[:,i][j:j+5] ==b).all():
                    win =2
        for j in range(11):
            if (np.diag(a1)[j:j+5] ==a).all():
                win =1
            if (np.diag(np.fliplr(a1))[j:j+5] == a).all():
                win = 1
        for j in range(11):
            if (np.diag(a1)[j:j+5] ==b).all():
                win =2
            if (np.diag(np.fliplr(a1))[j:j+5] == b).all():
                win = 2


        c1 = a1[:5,10:]
        if (np.diag(c1) == [1,1,1,1,1]).all():
            win =1
        if (np.diag(c1) == [2,2,2,2,2]).all():
            win = 2
        c2 = a1[:6,9:]
        if (np.diag(c2)==[0,1,1,1,1,1]).all() or (np.diag(c2)==[1,1,1,1,1,0]).all() or (np.diag(c2)==[2,1,1,1,1,1]).all() or (np.diag(c2)==[1,1,1,1,1,2]).all():
            win =1
        if (np.diag(c2)==[0,2,2,2,2,2]).all() or (np.diag(c2)==[2,2,2,2,2,0]).all() or (np.diag(c2)==[1,2,2,2,2,2]).all() or (np.diag(c2)==[2,2,2,2,2,1]).all():
            win =2
        c3 = a1[9:,:6]
        if (np.diag(c3)==[0,1,1,1,1,1]).all() or (np.diag(c3)==[1,1,1,1,1,0]).all() or (np.diag(c3)==[2,1,1,1,1,1]).all() or (np.diag(c3)==[1,1,1,1,1,2]).all():
            win =1
        if (np.diag(c3)==[0,2,2,2,2,2]).all() or (np.diag(c3)==[2,2,2,2,2,0]).all() or (np.diag(c3)==[1,2,2,2,2,2]).all() or (np.diag(c3)==[2,2,2,2,2,1]).all():
            win =2
        c4 = a1[10:,:5]
        if (np.diag(c4) == [1,1,1,1,1]).all():
            win =1
        if (np.diag(c4) == [2,2,2,2,2]).all():
            win = 2

        d1 = a1[:5,:5]
        if (np.diag(np.fliplr(d1)) == [1, 1, 1, 1, 1]).all():
            win = 1
        if (np.diag(np.fliplr(d1)) == [2, 2, 2, 2, 2]).all():
            win = 2
        d2 = a1[:6, :6]
        if (np.diag(np.fliplr(d2)) == [0, 1, 1, 1, 1, 1]).all() or (np.diag(np.fliplr(d2)) == [1, 1, 1, 1, 1, 0]).all() or (np.diag(np.fliplr(d2)) == [2, 1, 1, 1, 1, 1]).all() or (np.diag(np.fliplr(d2)) == [1, 1, 1, 1, 1, 2]).all():
            win = 1
        if (np.diag(np.fliplr(d2)) == [0, 2, 2, 2, 2, 2]).all() or (np.diag(np.fliplr(d2)) == [2, 2, 2, 2, 2, 0]).all() or (np.diag(np.fliplr(d2)) == [1, 2, 2, 2, 2, 2]).all() or (np.diag(np.fliplr(d2)) == [2, 2, 2, 2, 2, 1]).all():
            win = 2
        d3 = a1[9:, 9:]
        if (np.diag(np.fliplr(d3)) == [0, 1, 1, 1, 1, 1]).all() or (np.diag(np.fliplr(d3)) == [1, 1, 1, 1, 1, 0]).all() or (np.diag(np.fliplr(d3)) == [2, 1, 1, 1, 1, 1]).all() or (np.diag(np.fliplr(d3)) == [1, 1, 1, 1, 1, 2]).all():
            win = 1
        if (np.diag(np.fliplr(d3)) == [0, 2, 2, 2, 2, 2]).all() or (np.diag(np.fliplr(d3)) == [2, 2, 2, 2, 2, 0]).all() or (np.diag(np.fliplr(d3)) == [1, 2, 2, 2, 2, 2]).all() or (np.diag(np.fliplr(d3)) == [2, 2, 2, 2, 2, 1]).all():
            win = 2
        d4 = a1[10:, 10:]
        if (np.diag(np.fliplr(d4)) == [1, 1, 1, 1, 1]).all():
            win = 1
        if (np.diag(np.fliplr(d4)) == [2, 2, 2, 2, 2]).all():
            win = 2
        if win ==0 and 0 not in a1:
            win =3

        if(win!=0):
            self.win_tag=win
        return win


    def huosi(self,a):  #对活四进行评分，同函数ifwin，对十五横十五纵，以及各条对角线依次判断是否有活四的情况
        huosi1 =0
        huosi2 =0
        silian1 = np.array([[1,1,1,1,0],
                           [1,1,1,0,1],
                           [1,1,0,1,1],
                           [1,0,1,1,1],
                           [0,1,1,1,1]])
        silian2 = np.array([[2,2,2,2,0],
                           [2,2,2,0,2],
                           [2,2,0,2,2],
                           [2,0,2,2,2],
                           [0,2,2,2,2]])
        for x in a:
            for j in range(11):
                for k in silian1:
                    if (x[j:j+5] == k).all():
                        huosi1 +=1
                for m in silian2:
                    if (x[j:j+5] == m).all():
                        huosi2 +=1
        for i in range(15):
            for j in range(11):
                for k in silian1:
                    if (a[:,i][j:j+5] == k).all():
                        huosi1 +=1
                for m in silian2:
                    if (a[:,i][j:j+5] == m).all():
                        huosi2 +=1
        for j in range(11):
            for k in silian1:
                if (np.diag(a)[j:j+5] == k).all():
                    huosi1 +=1
                if (np.diag(np.fliplr(a))[j:j+5] == k).all():
                    huosi1 +=1
            for m in silian2:
                if (np.diag(a)[j:j+5] ==m).all():
                    huosi2 +=1
                if (np.diag(np.fliplr(a))[j:j+5] == m).all():
                    huosi2 +=1

        c1 = a[:5, 10:]
        for k in silian1:
            if (np.diag(c1) == k).all():
                huosi1 += 1
        for m in silian2:
            if (np.diag(c1) == m).all():
                huosi2 += 1
        c2 = a[:6, 9:]
        for i in range(2):
            for k in silian1:
                if (np.diag(c2)[i:i+5] == k).all():
                    huosi1 +=1
            for m in silian2:
                if (np.diag(c2)[i:i+5] == m).all():
                    huosi2 +=1
        c3 = a[9:, :6]
        for i in range(2):
            for k in silian1:
                if (np.diag(c3)[i:i+5] == k).all():
                    huosi1 +=1
            for m in silian2:
                if (np.diag(c3)[i:i+5] == m).all():
                    huosi2 +=1
        c4 = a[10:, :5]
        for k in silian1:
            if (np.diag(c4) == k).all():
                huosi1 += 1
        for m in silian2:
            if (np.diag(c4) == m).all():
                huosi2 += 1

        d1 = a[:5, :5]
        for k in silian1:
            if (np.diag(np.fliplr(d1)) == k).all():
                huosi1 +=1
        for m in silian2:
            if (np.diag(np.fliplr(d1)) == m).all():
                huosi2 +=1
        d2 = a[:6, :6]
        for i in range(2):
            for k in silian1:
                if (np.diag(np.fliplr(d2))[i:i+5] == k).all():
                    huosi1 +=1
            for m in silian2:
                if (np.diag(np.fliplr(d2))[i:i+5] == m).all():
                    huosi2 +=1
        d3 = a[9:, 9:]
        for i in range(2):
            for k in silian1:
                if (np.diag(np.fliplr(d3))[i:i+5] == k).all():
                    huosi1 +=1
            for m in silian2:
                if (np.diag(np.fliplr(d3))[i:i+5] == m).all():
                    huosi2 +=1
        d4 = a[10:, 10:]
        for k in silian1:
            if (np.diag(np.fliplr(d4)) == k).all():
                huosi1 += 1
        for m in silian2:
            if (np.diag(np.fliplr(d4)) == m).all():
                huosi2 +=1
        return [huosi1,huosi2]


    def huosan(self,a):  #对活三进行评分，同活四的思路
        huosan1 =0
        huosan2 =0
        sanlian1 = np.array([[0,0,1,1,1],
                             [0,1,0,1,1],
                             [0,1,1,0,1],
                             [0,1,1,1,0],
                             [1,0,0,1,1],
                             [1,0,1,0,1],
                             [1,0,1,1,0],
                             [1,1,0,0,1],
                             [1,1,0,1,0],
                             [1,1,1,0,0]])
        sanlian2 = np.array([[0,0,2,2,2],
                             [0,2,0,2,2],
                             [0,2,2,0,2],
                             [0,2,2,2,0],
                             [2,0,0,2,2],
                             [2,0,2,0,2],
                             [2,0,2,2,0],
                             [2,2,0,0,2],
                             [2,2,0,2,0],
                             [2,2,2,0,0]])

        for x in a:
            for j in range(11):
                for k in sanlian1:
                    if (x[j:j+5] == k).all():
                        huosan1 +=1
                for m in sanlian2:
                    if (x[j:j+5] == m).all():
                        huosan2 +=1
        for i in range(15):
            for j in range(11):
                for k in sanlian1:
                    if (a[:,i][j:j+5] == k).all():
                        huosan1 +=1
                for m in sanlian2:
                    if (a[:,i][j:j+5] == m).all():
                        huosan2 +=1
        for j in range(11):
            for k in sanlian1:
                if (np.diag(a)[j:j+5] == k).all():
                    huosan1 += 1
                if (np.diag(np.fliplr(a))[j:j+5] == k).all():
                    huosan1 += 1
            for m in sanlian2:
                if (np.diag(a)[j:j+5] ==m).all():
                    huosan2 += 1
                if (np.diag(np.fliplr(a))[j:j+5] == m).all():
                    huosan2 += 1

        c1 = a[:5, 10:]
        for k in sanlian1:
            if (np.diag(c1) == k).all():
                huosan1 += 1
        for m in sanlian2:
            if (np.diag(c1) == m).all():
                huosan2 += 1
        c2 = a[:6, 9:]
        for i in range(2):
            for k in sanlian1:
                if (np.diag(c2)[i:i+5] == k).all():
                    huosan1 += 1
            for m in sanlian2:
                if (np.diag(c2)[i:i+5] == m).all():
                    huosan2 += 1
        c3 = a[9:, :6]
        for i in range(2):
            for k in sanlian1:
                if (np.diag(c3)[i:i+5] == k).all():
                    huosan1 += 1
            for m in sanlian2:
                if (np.diag(c3)[i:i+5] == m).all():
                    huosan2 += 1
        c4 = a[10:, :5]
        for k in sanlian1:
            if (np.diag(c4) == k).all():
                huosan1 += 1
        for m in sanlian2:
            if (np.diag(c4) == m).all():
                huosan2 += 1

        d1 = a[:5, :5]
        for k in sanlian1:
            if (np.diag(np.fliplr(d1)) == k).all():
                huosan1 += 1
        for m in sanlian2:
            if (np.diag(np.fliplr(d1)) == m).all():
                huosan2 += 1
        d2 = a[:6, :6]
        for i in range(2):
            for k in sanlian1:
                if (np.diag(np.fliplr(d2))[i:i+5] == k).all():
                    huosan1 += 1
            for m in sanlian2:
                if (np.diag(np.fliplr(d2))[i:i+5] == m).all():
                    huosan2 += 1
        d3 = a[9:, 9:]
        for i in range(2):
            for k in sanlian1:
                if (np.diag(np.fliplr(d3))[i:i+5] == k).all():
                    huosan1 += 1
            for m in sanlian2:
                if (np.diag(np.fliplr(d3))[i:i+5] == m).all():
                    huosan2 += 1
        d4 = a[10:, 10:]
        for k in sanlian1:
            if (np.diag(np.fliplr(d4)) == k).all():
                huosan1 += 1
        for m in sanlian2:
            if (np.diag(np.fliplr(d4)) == m).all():
                huosan2 += 1
        return [huosan1,huosan2]


    def huoer(self,a): #对活二进行评分，同活四的思路
        huosan1 = 0
        huosan2 = 0
        sanlian1 = [0,1,1,0]
        sanlian2 = [0,2,2,0]
        for x in a:
            for j in range(12):
                if (x[j:j+4] == sanlian1).all():
                    huosan1 +=1
                if (x[j:j+4] == sanlian2).all():
                    huosan2 +=1
        for i in range(15):
            for j in range(12):
                if (a[:,i][j:j+4] == sanlian1).all():
                    huosan1 +=1
                if (a[:,i][j:j+4] == sanlian2).all():
                    huosan2 +=1
        for j in range(12):
            for k in sanlian1:
                if (np.diag(a)[j:j+4] == k).all():
                    huosan1 += 1
                if (np.diag(np.fliplr(a))[j:j+4] == k).all():
                    huosan1 += 1
            for m in sanlian2:
                if (np.diag(a)[j:j+4] ==m).all():
                    huosan2 += 1
                if (np.diag(np.fliplr(a))[j:j+4] == m).all():
                    huosan2 += 1

        c1 = a[:5, 10:]
        for j in range(2):
            if (np.diag(c1)[j:j+4] == sanlian1).all():
                huosan1 += 1
        for j in range(2):
            if (np.diag(c1)[j:j+4] == sanlian2).all():
                huosan2 += 1
        c2 = a[:6, 9:]
        for i in range(3):
            for k in sanlian1:
                if (np.diag(c2)[i:i+4] == k).all():
                    huosan1 += 1
            for m in sanlian2:
                if (np.diag(c2)[i:i+4] == m).all():
                    huosan2 += 1
        c3 = a[9:, :6]
        for i in range(3):
            for k in sanlian1:
                if (np.diag(c3)[i:i+4] == k).all():
                    huosan1 += 1
            for m in sanlian2:
                if (np.diag(c3)[i:i+4] == m).all():
                    huosan2 += 1
        c4 = a[10:, :5]
        for j in range(2):
            if (np.diag(c4)[j:j+4] == sanlian1).all():
                huosan1 += 1
        for j in range(2):
            if (np.diag(c4)[j:j+4] == sanlian2).all():
                huosan2 += 1

        d1 = a[:5, :5]
        for j in range(2):
            if (np.diag(np.fliplr(d1))[j:j+4] == sanlian1).all():
                huosan1 += 1
        for j in range(2):
            if (np.diag(np.fliplr(d1))[j:j+4] == sanlian2).all():
                huosan2 += 1
        d2 = a[:6, :6]
        for i in range(3):
            for k in sanlian1:
                if (np.diag(np.fliplr(d2))[i:i+4] == k).all():
                    huosan1 += 1
            for m in sanlian2:
                if (np.diag(np.fliplr(d2))[i:i+4] == m).all():
                    huosan2 += 1
        d3 = a[9:, 9:]
        for i in range(3):
            for k in sanlian1:
                if (np.diag(np.fliplr(d3))[i:i+4] == k).all():
                    huosan1 += 1
            for m in sanlian2:
                if (np.diag(np.fliplr(d3))[i:i+4] == m).all():
                    huosan2 += 1
        d4 = a[10:, 10:]
        for j in range(2):
            if (np.diag(np.fliplr(d4))[j:j+4] == sanlian1).all():
                huosan1 += 1
        for j in range(2):
            if (np.diag(np.fliplr(d4))[j:j+4] == sanlian2).all():
                huosan2 += 1
        return [huosan1, huosan2]




    def evaluation1(self,a): #电脑下1，player下2 评估函数，对双方进行打分，成五子，活四，活三，活二对电脑和玩家都有不同的赋分
        score1 = 0
        score2 = 0
        ifwin1 = self.ifwin(a)
        if ifwin1 ==1:
            score1 += 1000000
        if ifwin1 ==2:
            score2 += 1000000

        huosi1 = self.huosi(a)
        score1 +=huosi1[0]*33000
        score2 +=huosi1[1]*30000

        huosan1 = self.huosan(a)
        score1 +=huosan1[0]*11000
        score2 +=huosan1[1]*10000

        huoer1 = self.huoer(a)
        score1 +=huoer1[0]*11
        score2 +=huoer1[1]*10

        for i in a:
            if 1 not in i:
                score2 +=1
        for i in a:
            if 2 not in i:
                score1 +=1
        for j in range(7):
            if 1 not in a[:,j]:
                score2+=1
        for j in range(7):
            if 2 not in a[:,j]:
                score1 +=1
        if 1 not in np.diag(a):
            score2 +=1
        if 2 not in np.diag(a):
            score1 +=1
        if 1 not in np.diag(np.fliplr(a)):
            score2 +=1
        if 2 not in np.diag(np.fliplr(a)):
            score1 +=1
        return score1-score2



    def nextstep1(self,a): #电脑下1，player下2 返回所有下一步电脑下的棋，为形成极大极小算法后面构成后面深度范围内的树
        successors =[]
        for i in self.findneighbor(a):
            a1 = copy.deepcopy(a)
            a1[i[0]][i[1]] =1
            successors.append([a1,i])
        return successors

    def nextstep2(self,a): #电脑下1，player下2  返回所有下一步人下的棋
        successors = []
        for i in self.findneighbor(a):
            a1 = copy.deepcopy(a)
            a1[i[0]][i[1]] = 2
            successors.append([a1, i])
        return successors


    def minmaxdecision(self,a,dep): #搜索深度限制为dep，即只往后看dep步骤，一般设定dep为3或4.dep过大计算耗时较长，dep较小则棋力较弱
        value =self.maxvalue(a,-10000000000,10000000000,dep)
        return value[1]


    def maxvalue(self,a,alpha,beta,dep): #极大极小值算法和ab剪枝，同书上伪代码
        dep = dep-1
        if self.ifwin(a)!=0 or dep ==0:
            return [self.evaluation1(a)]
        value = [-100000000000000,[-1,-1]]
        for b in self.nextstep1(a):
            c = self.minvalue(b[0],alpha,beta,dep)
            if c[0] > value[0]:
                value[0] = c[0]
                value[1] = b[1]
            if value[0] >= beta:
                return value
            alpha = max(alpha,value[0])
        return value


    def minvalue(self,a,alpha,beta,dep):
        dep =dep-1
        if self.ifwin(a)!=0 or dep ==0:
            return [self.evaluation1(a)]
        value = [100000000000000,[-1,-1]]
        for b in self.nextstep2(a):
            c = self.maxvalue(b[0],alpha,beta,dep)
            if c[0] < value[0]:
                value[0] = c[0]
                value[1] = b[1]
            if value[0] <= alpha:
                return value
            beta = min(beta,value[0])
        return value


    def position(self,a): #返回玩家下的2和电脑下的1的棋子的坐标
        d = np.where(a == 2)
        c = np.array([d[0],d[1]])
        d1 = np.where(a == 1)
        c1 = np.array([d1[0], d1[1]])
        s = np.hstack((c, c1))
        s = s.T
        return s

    def findneighbor(self,a): #我们为了缩小搜索范围，认为电脑只在离现有的棋的一步远的位置考虑落子，电脑不会下出围棋的“飞”。此函数返回离现有棋一步远的所有位置，作为下一步的考虑范围
        posi =  self.position(a)
        neighbor = []
        for i,x in enumerate(a):
            for j,b in enumerate(x):
                if b !=0:
                    continue
                elif self.ifin([i-1,j-1],posi) or self.ifin([i-1,j],posi) or self.ifin([i-1,j+1],posi) or self.ifin([i,j-1],posi) or self.ifin([i,j+1],posi) or self.ifin([i+1,j-1],posi) or self.ifin([i+1,j],posi) or self.ifin([i+1,j+1],posi):
                    neighbor.append([i,j])
        return neighbor

    def ifin(self,v,posi):
        c = 0
        for i in posi:
            if (v ==i).all():
                c=1
        return c

    def get_chessboard(self):
        return self.chess

    def set_chessboard(self,player_row,player_col):
        self.chess[player_row][player_col]=2
        eva=self.evaluation1(self.chess)
        print(eva)
        [robot_row,robot_col]=self.minmaxdecision(self.chess, 3)
        self.chess[robot_row][robot_col]=1
        return [robot_row,robot_col]

    def is_blank(self,row,col):
        if(self.chess[row][col]==0):
            return True
        else:
            return False

    def is_win(self):
        return self.win_tag

    def __init__(self):
        self.win_tag=0
        self.chess = np.array( [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        print(self.evaluation1(self.chess))
        print(self.minmaxdecision(self.chess,3))
