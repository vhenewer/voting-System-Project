from tkinter import Tk
from mainPageNotLogined.gui import show_mainPageNotLogined

if __name__ == '__main__':
    window = Tk()

    window.geometry("1440x1024")
    window.configure(bg="#FFFFFF")
    show_mainPageNotLogined(window, switch_page=None, user_id=None)

    window.mainloop()