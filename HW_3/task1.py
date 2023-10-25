import tkinter
import tkinter.messagebox as mb
from random import randint

window = tkinter.Tk()
window.title("КрестикиНолики")
window.geometry('200x250')
window.size()
mult = 60  # ох уж эти магические числа
arr_btn = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
count_move = 0


class MyBtn(tkinter.Button):
    def __init__(self, form, col, row):
        self.is_input = False
        self.value = ""
        super(MyBtn, self).__init__(form, command=lambda x=col, y=row: clicked(x, y))
        self.place(x=col * mult, y=row * mult, width=mult, height=mult)

    def settext(self, text):
        self.configure(text=text)
        self.value = text
        self.is_input = True


def clicked(x, y):
    global arr_btn
    btn = arr_btn[x][y]
    if btn.is_input:
        return None
    btn.settext('X')
    analis(x, y)


def check_win(text, x, y):
    global arr_btn, count_move, window
    if count_move == 9:
        mb.showinfo("Результат", "Ничья!")
        return True
    sum_x, sum_y, sum_d, sum_d_ = 0, 0, 0, 0
    for i in range(3):
        if arr_btn[x][i].value == text:
            sum_x += 1
        if arr_btn[i][y].value == text:
            sum_y += 1
        if arr_btn[i][i].value == text:
            sum_d += 1
        if arr_btn[i][2 - i].value == text:
            sum_d_ += 1
    if sum_x == 3 or sum_y == 3 or sum_d == 3 or sum_d_ == 3:
        if text == 'X':
            mb.showinfo("Результат", "Вы выиграли!")
        else:
            mb.showinfo("Результат", "Вы проиграли!")
        return True


def analis(x, y):
    global count_move, window
    count_move += 1
    if check_win("X", x, y):
        return
    x, y = get_move()
    if check_win("O", x, y):
        return
    count_move += 1

    # checkWin("O", x, y )


def get_move():
    sum_x_d, sum_o_d = 0, 0
    sum_x_d_, sum_o_d_ = 0, 0
    for i in range(3):
        sum_x_g, sum_o_g = 0, 0
        sum_x_v, sum_o_v = 0, 0

        if arr_btn[i][i].value == "O":
            sum_o_d += 1
        elif arr_btn[i][i].value == "X":
            sum_x_d += 1
        if arr_btn[i][2 - i].value == "O":
            sum_o_d_ += 1
        elif arr_btn[i][2 - i].value == "X":
            sum_x_d_ += 1

        for j in range(3):
            if arr_btn[i][j].value == "O":
                sum_o_g += 1
            elif arr_btn[i][j].value == "X":
                sum_x_g += 1
            if arr_btn[j][i].value == "O":
                sum_o_v += 1
            elif arr_btn[j][i].value == "X":
                sum_x_v += 1

        if sum_o_g == 2 and sum_x_g == 0:
            for k in range(3):
                if arr_btn[i][k].value == "":
                    arr_btn[i][k].settext('O')
                    return (i, k)
        if sum_o_v == 2 and sum_x_v == 0:
            for k in range(3):
                if arr_btn[k][i].value == "":
                    arr_btn[k][i].settext('O')
                    return (k, i)
        if sum_o_g == 0 and sum_x_g == 2:
            for k in range(3):
                if arr_btn[i][k].value == "":
                    arr_btn[i][k].settext('O')
                    return (i, k)
        if sum_o_v == 0 and sum_x_v == 2:
            for k in range(3):
                if arr_btn[k][i].value == "":
                    arr_btn[k][i].settext('O')
                    return k, i
    if sum_o_d == 2 and sum_x_d == 0:
        for k in range(3):
            if arr_btn[k][k].value == "":
                arr_btn[k][k].settext('O')
                return k, k
    if sum_o_d_ == 2 and sum_x_d_ == 0:
        for k in range(3):
            if arr_btn[k][2 - k].value == "":
                arr_btn[k][2 - k].settext('O')
                return k, 2 - k
    if sum_o_d == 0 and sum_x_d == 2:
        for k in range(3):
            if arr_btn[k][k].value == "":
                arr_btn[k][k].settext('O')
                return k, k
    if sum_o_d_ == 0 and sum_x_d_ == 2:
        for k in range(3):
            if arr_btn[k][2 - k].value == "":
                arr_btn[k][2 - k].settext('O')
                return k, 2 - k
    while True:
        point_x = randint(0, 2)
        point_y = randint(0, 2)
        if not arr_btn[point_x][point_y].is_input:
            arr_btn[point_x][point_y].settext('O')
            return (point_x, point_y)


def init():
    global window, arr_btn
    btn = tkinter.Button(window, text="Начать заново", command=init)
    btn.place(x=1, y=3 * mult + 5, width=mult * 3, height=mult)
    arr_btn = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        arr_btn.append([])
        for j in range(3):
            arr_btn[i][j] = MyBtn(window, i, j)


a = analis
init()
window.bind_class(analis)
window.mainloop()
