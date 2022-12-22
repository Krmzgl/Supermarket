"""

    Stage: Development-01
    @author: Amin Habiballah-119202002
    @author: Taha Mert Kırmızıgül-120202009
     Stage: Development-02 (there names are not included)
    stage: code  review 
    ‌@author:Deniz Kuzey 119202077
    @author: Almustafa Alshekfeh 119202008

"""

import tkinter as SuperMarket


class LoginWindow:
    # constructor
    def _init_(self):
        self.window = SuperMarket.Tk()

        self._initializeGUI()
        self._addGUIElementsToFrame()

        # start the GUI frame
        self.window.mainloop()


    """
        Initialize GUI elements. If it is necessary, you can add
        more elements.
        ! PLEASE RENAME THE OBJECTS ACCORDING TO THEIR PURPOSES !
        ! YOU CAN ADD MORE ELEMENTS IF IT IS NECESSARY !
    """
    def _initializeGUI(self):
        self.lbl01 = SuperMarket.Label(text="Username")
        self.lbl02 = SuperMarket.Label(text="Password")

        self.txt01 = SuperMarket.Entry()
        self.txt02 = SuperMarket.Entry()

        self.btn01 = SuperMarket.Button(text="login")
        self.btn02 = SuperMarket.Button(text="register")

        self.btn01.bind("<Button-1>", self.handle_click)
        self.btn02.bind("<Button-1>", self.handle_click)


    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        self.lbl01.grid(row=0, column=0, padx=10, pady=5)
        self.txt01.grid(row=0, column=1, padx=10, pady=5)

        self.lbl02.grid(row=1, column=0, padx=10, pady=5)
        self.txt02.grid(row=1, column=1, padx=10, pady=5)

        self.btn01.grid(row=2, column=0, padx=10, pady=5)
        self.btn02.grid(row=2, column=1, padx=10, pady=5)


    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.
        :param event: action event for detecting which button is clicked
    """
    def handle_click(self, event):
        self.txt01.get()
        self.txt02.get()
        if self.txt01 != ("admin")  & self.txt02 != (123):
           def _init_(self):
            self.window = SuperMarket.Tk()
        return


# main method for testing the application
if _name_ == "_main_":
    LoginWindow()