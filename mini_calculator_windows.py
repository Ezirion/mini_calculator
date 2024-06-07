#!/usr/bin/python3

import tkinter as tk
# Calculator Windows version (this will be fused with linux one using os library later)
class Calculadora:

    def __init__(self, master):
        self.master = master
        self.master.resizable(False, False)
        self.frame = tk.Frame(self.master, bg="#FF8484")
        self.frame.pack(fill=tk.BOTH, expand=1)
        self.primer_num = 0.0
        self.current_num = "" 
        self.operacion = ""
        self.display = tk.Entry(

                self.frame,
                width=13,
                font=("Arial", 23),
                bd=10, insertwidth=1,
                bg="#FFA6A6",
                justify="right"
        )

        self.display.grid(row=0, column=0, columnspan=4, pady=2, padx=2)

        row = 1
        col = 0

        buttons = [
                "7", "8", "9", "/",
                "4", "5", "6", "x",
                "1", "2", "3", "-",
                "C", "0", ".", "+",
                "="
        ]

        for button in buttons:
            self.__build_button(button, row, col)
            col += 1

            if col > 3:
                col = 0
                row += 1

        self.master.bind("<Key>", self.__key_press) # Aqui aunque parezca que no le 
                                                    # pasamos nada a la funcion
                                                    # le estamos pasando el evento
                                                    # de la tecla que presionemos
    def __key_press(self, event):

        key = event.char

        if key == "\r":
            self.funcion_boton("=")
        elif key == "\x08":
            self.funcion_boton("C")
        elif key == "\x1b":
            self.master.quit()
            pass
        elif key in "1234567890+-*/.":
            self.funcion_boton(key)
        #elif event.keysym == 'Right':
        #    self.display.delete(0,1)
        #    calcular_pantalla('R')     # In future versions I will try to add
                                        # displacement to rigth and left to let
                                        # the user see a large operation
        #elif event.keysym == 'Left':
        #    self.display.delete(0,1)
        #    calcular_pantalla('L')
        else:
            pass
    
#    def calcular_pantalla(self, orden)
#        if orden == 'R':


    def es_entero(self):

        if (self.current_num-0.0001).is_integer():
            self.current_num -= 0.0001
        elif (self.current_num + 0.0001).is_integer():
            self.current_num += 0.0001

        if self.current_num.is_integer():
            self.current_num = str(int(self.current_num))
        else:
            
            self.current_num = str(round(float(self.current_num), 4))
        self.display.insert("end", self.current_num)



    def __calculate(self):
        self.display.delete(0, tk.END)
        if self.operacion == "+":
            self.current_num = self.primer_num + float(self.current_num) # FALTA EN EL RESULTADO CONVERTIRLO A ENTERO SI NO TIENE DECIMALES
        if self.operacion == "-":
            self.current_num = self.primer_num - float(self.current_num)
        if self.operacion == "x":
            self.current_num = self.primer_num * float(self.current_num)
        if self.operacion == "/":
            self.current_num = self.primer_num / float(self.current_num)


    def funcion_boton(self, key):
        
        
        if key == "C":
            self.display.delete(0, tk.END)
            self.operacion = ""
            self.current_num = ""
            self.primer_num = 0.0
        elif key == "=":
            if self.operacion != "" and self.current_num != "":
                print("\n[+] Entra")
                self.__calculate()
                self.es_entero()
                self.operacion = ""

                self.primer_num = 0.0
        elif key in "+-/*":
            if self.operacion == "" and self.current_num != "":# Si no hay operacion que permita dar al boton, sino no
                self.operacion = key
                self.primer_num = float(self.current_num)
                self.current_num = ""
                if len(self.display.get()) > 12:
                    self.display.delete(0,1)
                self.display.insert("end", f" {key} ")
                
        elif key == "." and (self.current_num == "" or "." in self.current_num):
            pass
        else:
            print(f"[+] Longitud dwl display: {len(self.display.get())}")
            if len(self.display.get()) > 12:
                self.display.delete(0,1)
            self.display.insert("end", key)
            self.current_num += key

        print(f"\n[+] Este es el num_actual: {self.current_num}")
        print(f"\n[+] Este es el primer_num: {self.primer_num}")
        print(f"\n[+] Esta es la operacion: {self.operacion}")



    def __build_button(self, text, row, col):
        b = tk.Button(
                self.frame,
                text=text,
                fg="#FFFFFF",
                bg="#FF6262",
                width=3,
                height=1,
                bd=2.5,
                font=("Arial bold", 23),
                command=lambda: self.funcion_boton(text)
        )
        b.grid(row=row, column=col, pady=2, padx=2)

root = tk.Tk() # Ventana principal
my_gui = Calculadora(root)
root.mainloop()
