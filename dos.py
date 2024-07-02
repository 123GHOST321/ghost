from random import choice
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askokcancel as aoc, showerror as se, showinfo as si

p1 = "x"
p2 = "+"
font = ["font name", 20, "bold"]
file = open("them.txt", "r+")


def btn_selector() : return choice([b00, b10, b20, b01, b11, b21, b02, b12, b22])


def c_move() :
    tb100 = b00["text"] == p1
    tb110 = b10["text"] == p1
    tb120 = b20["text"] == p1
    tb101 = b01["text"] == p1
    tb111 = b11["text"] == p1
    tb121 = b21["text"] == p1
    tb102 = b02["text"] == p1
    tb112 = b12["text"] == p1
    tb122 = b22["text"] == p1

    tb200 = b00["text"] == p1
    tb210 = b10["text"] == p1
    tb220 = b20["text"] == p1
    tb201 = b01["text"] == p1
    tb211 = b11["text"] == p1
    tb221 = b21["text"] == p1
    tb202 = b02["text"] == p1
    tb212 = b12["text"] == p1
    tb222 = b22["text"] == p1

    if b11["text"] == "" :
        b11["text"] = p2

    # =|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|= #

    elif (tb200 and tb210) and (b20["text"] == "") :
        b20["text"] = p2
    elif (tb201 and tb211) and (b21["text"] == "") :
        b21["text"] = p2
    elif (tb202 and tb212) and (b22["text"] == "") :
        b22["text"] = p2
    elif (tb220 and tb210) and (b00["text"] == "") :
        b00["text"] = p2
    elif (tb221 and tb211) and (b01["text"] == "") :
        b01["text"] = p2
    elif (tb222 and tb212) and (b02["text"] == "") :
        b02["text"] = p2
    elif (tb200 and tb220) and (b10["text"] == "") :
        b10["text"] = p2
    elif (tb201 and tb221) and (b11["text"] == "") :
        b11["text"] = p2
    elif (tb202 and tb222) and (b12["text"] == "") :
        b12["text"] = p2

    elif (tb200 and tb201) and (b02["text"] == "") :
        b02["text"] = p2
    elif (tb210 and tb211) and (b12["text"] == "") :
        b12["text"] = p2
    elif (tb220 and tb221) and (b22["text"] == "") :
        b22["text"] = p2
    elif (tb202 and tb201) and (b00["text"] == "") :
        b00["text"] = p2
    elif (tb212 and tb211) and (b10["text"] == "") :
        b10["text"] = p2
    elif (tb222 and tb221) and (b20["text"] == "") :
        b20["text"] = p2
    elif (tb200 and tb202) and (b01["text"] == "") :
        b01["text"] = p2
    elif (tb210 and tb212) and (b11["text"] == "") :
        b11["text"] = p2
    elif (tb220 and tb222) and (b21["text"] == "") :
        b21["text"] = p2
    # =|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|= #
    elif (tb100 and tb110) and (b20["text"] == "") :
        b20["text"] = p2
    elif (tb101 and tb111) and (b21["text"] == "") :
        b21["text"] = p2
    elif (tb102 and tb112) and (b22["text"] == "") :
        b22["text"] = p2

    elif (tb120 and tb110) and (b00["text"] == "") :
        b00["text"] = p2
    elif (tb121 and tb111) and (b01["text"] == "") :
        b01["text"] = p2
    elif (tb122 and tb112) and (b02["text"] == "") :
        b02["text"] = p2

    elif (tb100 and tb120) and (b10["text"] == "") :
        b10["text"] = p2
    elif (tb101 and tb121) and (b11["text"] == "") :
        b11["text"] = p2
    elif (tb102 and tb122) and (b12["text"] == "") :
        b12["text"] = p2

    elif (tb100 and tb101) and (b02["text"] == "") :
        b02["text"] = p2
    elif (tb110 and tb111) and (b12["text"] == "") :
        b12["text"] = p2
    elif (tb120 and tb121) and (b22["text"] == "") :
        b22["text"] = p2

    elif (tb102 and tb101) and (b00["text"] == "") :
        b00["text"] = p2
    elif (tb112 and tb111) and (b10["text"] == "") :
        b10["text"] = p2
    elif (tb122 and tb121) and (b20["text"] == "") :
        b20["text"] = p2

    elif (tb102 and tb100) and (b01["text"] == "") :
        b01["text"] = p2
    elif (tb112 and tb110) and (b11["text"] == "") :
        b11["text"] = p2
    elif (tb122 and tb120) and (b21["text"] == "") :
        b21["text"] = p2

    elif (tb100 and tb111) and (b22["text"] == "") :
        b22["text"] = p2
    elif (tb102 and tb111) and (b20["text"] == "") :
        b20["text"] = p2

    elif (tb122 and tb111) and (b00["text"] == "") :
        b00["text"] = p2
    elif (tb120 and tb111) and (b02["text"] == "") :
        b02["text"] = p2

    elif (tb100 and tb122) and (b11["text"] == "") :
        b11["text"] = p2
    elif (tb120 and tb102) and (b11["text"] == "") :
        b11["text"] = p2
    # =|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|= #
    else :
        r_move()


def r_move() :
    try :
        pl2 = btn_selector()
        if pl2["text"] == "" :
            pl2["text"] = p2
        else :
            c_move()
    except :
        win()


def clear() :
    b00["text"] = ""
    b10["text"] = ""
    b20["text"] = ""
    b01["text"] = ""
    b11["text"] = ""
    b21["text"] = ""
    b02["text"] = ""
    b12["text"] = ""
    b22["text"] = ""


def win() :
    tb00 = b00["text"] == p1
    tb10 = b10["text"] == p1
    tb20 = b20["text"] == p1
    tb01 = b01["text"] == p1
    tb11 = b11["text"] == p1
    tb21 = b21["text"] == p1
    tb02 = b02["text"] == p1
    tb12 = b12["text"] == p1
    tb22 = b22["text"] == p1
    if (
            (tb00 and tb01 and tb02) or
            (tb10 and tb11 and tb12) or
            (tb20 and tb21 and tb22) or

            (tb00 and tb10 and tb20) or
            (tb01 and tb11 and tb21) or
            (tb02 and tb12 and tb22) or

            (tb00 and tb11 and tb22) or
            (tb02 and tb11 and tb20)
    ) :
        si("YOU WIN", "you win the round!")
        clear()

    tb00 = b00["text"] == p2
    tb10 = b10["text"] == p2
    tb20 = b20["text"] == p2
    tb01 = b01["text"] == p2
    tb11 = b11["text"] == p2
    tb21 = b21["text"] == p2
    tb02 = b02["text"] == p2
    tb12 = b12["text"] == p2
    tb22 = b22["text"] == p2
    if (
            (tb00 and tb01 and tb02) or
            (tb10 and tb11 and tb12) or
            (tb20 and tb21 and tb22) or

            (tb00 and tb10 and tb20) or
            (tb01 and tb11 and tb21) or
            (tb02 and tb12 and tb22) or

            (tb00 and tb11 and tb22) or
            (tb20 and tb11 and tb02)
    ) :
        si("COMPUTER WIN", "COMPUTER win the round!")
        clear()

    elif (
            (b00["text"] == p1 or b00["text"] == p2) and
            (b10["text"] == p1 or b10["text"] == p2) and
            (b20["text"] == p1 or b20["text"] == p2) and
            (b01["text"] == p1 or b01["text"] == p2) and
            (b11["text"] == p1 or b11["text"] == p2) and
            (b21["text"] == p1 or b21["text"] == p2) and
            (b02["text"] == p1 or b02["text"] == p2) and
            (b12["text"] == p1 or b12["text"] == p2) and
            (b22["text"] == p1 or b22["text"] == p2)
    ) :
        si("EQUAL", "nobody wins!")
        clear()


def btn00() :
    if b00["text"] == "" :
        b00["text"] = p1
        c_move()
    else :
        se("Error", "this place is not empty.")
    win()


def btn10() :
    if b10["text"] == "" :
        b10["text"] = p1
        c_move()
    else :
        se("Error", "this place is not empty.")
    win()


def btn20() :
    if b20["text"] == "" :
        b20["text"] = p1
        c_move()
    else :
        se("Error", "this place is not empty.")
    win()


def btn01() :
    if b01["text"] == "" :
        b01["text"] = p1
        c_move()
    else :
        se("Error", "this place is not empty.")
    win()


def btn11() :
    if b11["text"] == "" :
        b11["text"] = p1
        c_move()
    else :
        se("Error", "this place is not empty.")
    win()


def btn21() :
    if b21["text"] == "" :
        b21["text"] = p1
        c_move()
    else :
        se("Error", "this place is not empty.")
    win()


def btn02() :
    if b02["text"] == "" :
        b02["text"] = p1
        c_move()
    else :
        se("Error", "this place is not empty.")
    win()


def btn12() :
    if b12["text"] == "" :
        b12["text"] = p1
        c_move()
    else :
        se("Error", "this place is not empty.")
    win()


def btn22() :
    if b22["text"] == "" :
        b22["text"] = p1
        c_move()
    else :
        se("Error", "this place is not empty.")
    win()


def destroy() :
    if aoc("are you sure ?", "are you sre you want get out ?") :
        t.destroy()


def get_them() :
    them = askcolor(file.read(), title="choose color...")[1]
    set_them(them)
    file.seek(0)
    file.write(them)
    file.seek(0)


def set_them(them) :
    b00["bg"] = them
    b10["bg"] = them
    b20["bg"] = them
    b01["bg"] = them
    b11["bg"] = them
    b21["bg"] = them
    b02["bg"] = them
    b12["bg"] = them
    b22["bg"] = them
    bd["bg"] = them
    be["bg"] = them
    bt["bg"] = them
    b00["activebackground"] = them
    b10["activebackground"] = them
    b20["activebackground"] = them
    b01["activebackground"] = them
    b11["activebackground"] = them
    b21["activebackground"] = them
    b02["activebackground"] = them
    b12["activebackground"] = them
    b22["activebackground"] = them
    bd["activebackground"] = them
    be["activebackground"] = them
    bt["activebackground"] = them


t = Tk()
t.title("dos")
t.resizable(False, False)

b00 = Button(t, font=font, fg="white", width=4, command=btn00)
b10 = Button(t, font=font, fg="white", width=4, command=btn10)
b20 = Button(t, font=font, fg="white", width=4, command=btn20)
b01 = Button(t, font=font, fg="white", width=4, command=btn01)
b11 = Button(t, font=font, fg="white", width=4, command=btn11)
b21 = Button(t, font=font, fg="white", width=4, command=btn21)
b02 = Button(t, font=font, fg="white", width=4, command=btn02)
b12 = Button(t, font=font, fg="white", width=4, command=btn12)
b22 = Button(t, font=font, fg="white", width=4, command=btn22)

bd = Button(t, text="clear", fg="green3", font=font, width=4, command=clear)
be = Button(t, text="Exit", fg="red3", font=font, width=4, command=destroy)
bt = Button(t, text="them", fg="orange", font=font, width=4, command=get_them)
# === #
set_them(file.read())
# === #
b00.grid(row=0, column=0)
b10.grid(row=1, column=0)
b20.grid(row=2, column=0)
b01.grid(row=0, column=1)
b11.grid(row=1, column=1)
b21.grid(row=2, column=1)
b02.grid(row=0, column=2)
b12.grid(row=1, column=2)
b22.grid(row=2, column=2)
bd.grid(row=3, column=0)
be.grid(row=3, column=1)
bt.grid(row=3, column=2)
t.mainloop()
