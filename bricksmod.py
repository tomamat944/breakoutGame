class Bricks:
    def __init__(self, b, w, h):
        self.board=b
        self.width=w
        self.height=h
        self.brick_x=30
        self.brick_y=20
        self.bricks=[]
        self.createBricks()

    def createBricks(self):
        for i in range(int(self.width/self.brick_x)-1):
            for j in range(int(self.height/self.brick_y/3)-1):
                x=i*self.brick_x+self.brick_x
                y=j*self.brick_y+2*self.brick_y
                current=self.board.create_rectangle(x, y,
                                                    x+self.brick_x, y+self.brick_y,
                                                    fill="white")
                self.bricks.append(current)
