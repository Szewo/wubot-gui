from view.gui import Gui
import tkinter as tk


def main():
    root = tk.Tk()
    gui = Gui(root)
    gui.setup()
    gui.event_window()
    root.mainloop()


if __name__ == '__main__':
    main()

# def checkStaminaBar():
#     if pyautogui.pixelMatchesColor(35, 100, (70, 60, 52), tolerance=10):
#         return 'Stamina low'
#     elif pyautogui.pixelMatchesColor(185, 100, (70, 60, 52), tolerance=10):
#         return 'Stamina normal'
#     else:
#         return 'Stamina full'