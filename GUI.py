import tkinter as tk
import generate_img

title = "A.C.E."
master = tk.Tk()
master.title("Sim")
master.resizable(width=False, height=False)

game_frame = tk.Frame(master)

title = tk.Label(game_frame,
                 justify="center",
                 font="Times 25 bold",
                 fg="purple",
                 text=title)

blue_tooth_button = tk.Button(game_frame,
                              justify="right",
                              compound="center",
                              font="Times",
                              text="蓝牙连接",
                              command=lambda: generate_img.blue_tooth_connect())

world_map_button = tk.Button(game_frame,
                             justify="left",
                             compound="center",
                             font="Times",
                             text="世界地图",
                             command=lambda: generate_img.send_one_image("img/colorworld.jpg"))

ace_button = tk.Button(game_frame,
                       justify="left",
                       compound="center",
                       font="Times",
                       text="A.C.E",
                       command=lambda: generate_img.send_images_by_dir("img/ACE"))

quit_button = tk.Button(game_frame,
                        justify="left",
                        compound="center",
                        font="Times",
                        text="Quit",
                        command=master.quit)


def window_init():
    game_frame.grid()
    title.grid(row=0, columnspan=3)
    blue_tooth_button.grid(row=4, column=0)
    world_map_button.grid(row=4, column=1)
    ace_button.grid(row=4, column=2)
    quit_button.grid(row=5, column=1)


window_init()
master.mainloop()
