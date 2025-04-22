from tkinter import Tk
from mainPageNotLogined.gui import show_mainPageNotLogined
from loginPage.gui import show_loginPage
from mainPageLogined.gui import show_mainPageLogined
from votePageLogined.gui import show_votePageLogined
from message.gui import show_message

def main():
    window = Tk()

    window.geometry("1440x1024")
    window.configure(bg="#FFFFFF")
    show_mainPageNotLogined(window, switch_page="main", user_id=None)
    def switch_page(page_name, user_id=None):
        if page_name == "main":
            show_mainPageNotLogined(window, switch_page, user_id)
        elif page_name == "login":
            show_loginPage(window, switch_page, user_id)
        elif page_name == "mainLogined":
            show_mainPageLogined(window, switch_page)
        elif page_name == "vote":
            show_votePageLogined(window, switch_page)
        elif page_name == "message":
            show_message(window, switch_page)

    switch_page("main")
    window.mainloop()


if __name__ == '__main__':
    main()
