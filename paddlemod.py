class Paddle:
    def __init__(self, b, w, h):
        self.board=b
        self.width=w
        self.height=h
        self.paddle_x=50
        self.paddle_y=10
        self.speed=20
        self.paddle_pos=None
        self.createPaddle()

    def createPaddle(self):
        if self.paddle_pos is None:
            self.paddle_pos=self.board.create_rectangle(self.width/2, self.height-self.paddle_y,
                                                        self.width/2+self.paddle_x, self.height, fill="white")
    def movePaddle(self, event):
        current=self.board.coords(self.paddle_pos)
        if event.char=="a" and current[0]>0:
            self.board.move(self.paddle_pos, -self.speed, 0)
        if event.char=="d" and current[2]<self.width:
            self.board.move(self.paddle_pos, self.speed, 0)