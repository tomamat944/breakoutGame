import gamemod as g

def main():
    root=g.tk.Tk()
    game=g.Game(root, 200, 400, "black")
    game.run()
    root.mainloop()

if __name__=="__main__":
    main()