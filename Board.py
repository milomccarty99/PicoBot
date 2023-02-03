class Board:
    def __init__(self,xstart, ystart, xsize, ysize, *walls):
        self.xpos = xstart
        self.ypos = ystart
        self.xsize = xsize
        self.ysize = ysize
        self.map = [['' for i in range(xsize)] for j in range (ysize)]
        for x in range(0,xsize):
            for y in range(0,ysize):
                self.map[x][y] = "unvisited"

        for wall in walls:
            coords = wall.split(',')
            self.map[coords[0]][coords[1]] = "wall"

        self.map[self.xpos][self.ypos] = "picobot"

    def getBoard(self):
        return self.map

    def moveDirection(self, dirp):
        self.map[self.xpos][self.ypos] = "visited"
        if(dirp == 'N'):
            self.ypos-=1
        elif(dirp == 'E'):
            self.xpos+=1
        elif(dirp == 'W'):
            self.xpos -=1
        elif(dirp == 'S'):
            self.ypos +=1
        else:
            pass
        print(str(self.xpos) +  ", "+ str(self.ypos))
        self.map[self.xpos][self.ypos]="picobot"

    def getSurr(self):
        result = list("xxxx")
        if self.ypos <= 0 or (self.map[self.xpos][self.ypos-1] == "wall"):
            result[0] = 'N'
        elif self.xpos + 1 >= self.xsize or (self.map[self.xpos+1][self.ypos]=="wall"):
            result[1] = 'E'
        elif self.xpos <= 0 or (self.map[self.xpos-1][self.ypos]=="wall"):
            result[2] = 'W'
        elif self.ypos + 1 >= self.ysize or (self.map[self.xpos][self.ypos+1] == "wall"):
            result[3] = 'S'
        return "".join(result)


