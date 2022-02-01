import tkinter as tk
import paddlemod as p
import bricksmod as b
import ballmod as bl
class Game:
    def __init__(self, root, w, h, color):
        self.speed=20
        self.root=root
        self.width=w
        self.height=h
        self.board=tk.Canvas(master=root, width=w, height=h, bg=color)
        self.board.pack()
        self.label=tk.Label(master=root, text="Use ad to move")
        self.label.pack()
        self.paddle=p.Paddle(self.board, w, h)
        self.bricks=b.Bricks(self.board, w, h)
        self.ball=bl.Ball(self.board, w, h)
        self.root.bind("<KeyPress>", self.paddle.movePaddle)

    def restart(self):
        self.board.delete("all")
        self.paddle = p.Paddle(self.board, self.width, self.height)
        self.bricks = b.Bricks(self.board, self.width, self.height)
        self.ball = bl.Ball(self.board, self.width, self.height)
        self.root.bind("<KeyPress>", self.paddle.movePaddle)

    def update(self):
        if self.ball.collideBottom():
           self.restart()
        self.ball.collidePaddle(self.paddle.paddle_pos)
        self.ball.collideSides()
        self.ball.collideBricks(self.bricks.bricks)
        self.ball.moveBall()

    def run(self):
        self.update()
        self.root.after(self.speed, self.run)