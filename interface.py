#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import tkinter

class Interface(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.geometry("1000x1000")
        self.grid()
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self, textvariable=self.entryVariable)


        button = tkinter.Button(self, text=u"ARRETER",fg="white", bg="red",width="10",height="2",command=self.OnButtonClick2)
        button.place(x=900 , y=600)
        button1 = tkinter.Button(self, text=u"DEMARRER", fg="white", bg="green", width="10", height="2",command=self.OnButtonClick1)
        button1.place(x=800, y=600)
        self.ttle = tkinter.StringVar()


        ttle = tkinter.Label(self, textvariable=self.ttle,
                              anchor="w", fg="white", bg="gray",width="50",height="2")

        ttle.place(x=400, y=0)




        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self, textvariable=self.labelVariable,
                              anchor="w", fg="black", bg="white",width="30",height="4")

        label.place(x=90 ,y=90)
        self.labelVariable2 = tkinter.StringVar()
        label2 = tkinter.Label(self, textvariable=self.labelVariable2,
                              anchor="w", fg="purple", bg="white",width="30",height="4")
        label2.place(x=400 , y=90)
        self.labelVariable3 = tkinter.StringVar()
        label3 = tkinter.Label(self, textvariable=self.labelVariable3,
                               anchor="w", fg="black", bg="white",width="30",height="4")
        label3.place(x=700, y=90)
        self.labelVariable4 = tkinter.StringVar()
        label4 = tkinter.Label(self, textvariable=self.labelVariable4,
                               anchor="w", fg="white", bg="blue",width="30",height="4")
        label4.place(x=90 , y=200)
        self.labelVariable5 = tkinter.StringVar()
        label5 = tkinter.Label(self, textvariable=self.labelVariable5,
                               anchor="w", fg="white", bg="blue",width="30",height="4")
        label5.place(x=90 , y=400)
        self.labelVariable6 = tkinter.StringVar()
        label6 = tkinter.Label(self, textvariable=self.labelVariable6,
                               anchor="w", fg="white", bg="blue",width="30",height="4")
        label6.place(x=90 , y= 600)





        self.ttle.set("                         DETECTION DES OBJETS")
        self.labelVariable.set(u"le nombre de rectangle "
                                u"est   ")
        self.labelVariable2.set(u"le nombre de triangle est")
        self.labelVariable3.set(u"le nombre de cercle est!")
        self.labelVariable4.set(u"la couleur de cercle est !")
        self.labelVariable5.set(u"la couleur de triangle est !")
        self.labelVariable6.set(u"la couleur de rectangle est !")





        self.resizable(True, True)

    def OnButtonClick1(self):
        self.labelVariable.set(self.entryVariable.get() + " le nombre de rectangle est")
        self.labelVariable2.set("1 "+self.entryVariable.get() )
        self.labelVariable3.set("2"+self.entryVariable.get() )
        self.labelVariable4.set("3"+self.entryVariable.get() )
        self.labelVariable5.set("rouge"+self.entryVariable.get() )
        self.labelVariable6.set("vert"+self.entryVariable.get() )
        self.labelVariable.set("jaune"+self.entryVariable.get() )
    def OnButtonClick2(self):
        self.labelVariable.set(u"le nombre de rectangle "
                               u"est   ")
        self.labelVariable2.set(u"le nombre de triangle est")
        self.labelVariable3.set(u"le nombre de cercle est!")
        self.labelVariable4.set(u"la couleur de cercle est !")
        self.labelVariable5.set(u"la couleur de triangle est !")
        self.labelVariable6.set(u"la couleur de rectangle est !")







if __name__ == "__main__":
    detect = Interface(None)
    detect.title('my application')
    detect.mainloop()