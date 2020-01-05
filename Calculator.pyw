
"""
Python program to create a simple GUI
calculator using Tkinter
"""

##### I have to add a feature that returns approximate value of the result if '=' is double-clicked or even clicked twice.
##### I have to bind respective keys to buttons in the calculator GUI.

## Importing `math` module as `m`
import math as m

## Importing `choice` from `random` as `ch`
from random import choice as ch

## Importing `sleep` from `time` as `ch` to delay processes and animations
from time import sleep as s

## Import everything from `tkinter` module
from tkinter import *
from tkinter import messagebox as mb

## Globally declare the expression variable
expression = ""





def evalall(string1):   ## Advanced `evalall()` function to evaluate mathematical constants as well
    if ((type(string1) == int) or (type(string1) == float)):
        string1 = str(string1)
    if ((string1 == '') or (string1.isspace() == True)):
        return 1
    string1 = string1.replace(' ', '')
    string1 = string1.replace('π', str(m.pi))
    string1 = string1.replace('p', str(m.pi))
    string1 = string1.replace('e', str(m.e))
    string1 = string1.replace('j', str(1j))
    string1 = string1.replace('ι', str(1j))
    string1 = string1.replace('×', '*')
    string1 = string1.replace('•', '*')
    string1 = string1.replace('÷', '/')
    string1 = string1.replace('^', '**')
    string1 = string1.replace('∞', str(inf))
    string1 = string1.replace('/0', '*'+str(inf))
    string1 = string1.replace('sin(', 'm.sin(')
    string1 = string1.replace('cos(', 'm.cos(')
    string1 = string1.replace('tan(', 'm.tan(')
    string1 = string1.replace('csc(', '1/m.sin(')
    string1 = string1.replace('sec(', '1/m.cos(')
    string1 = string1.replace('cot(', '1/m.tan(')
    string1 = string1.replace('fact(', 'm.gamma(1+')
    string1 = string1.replace('log(', 'm.log10(')
    string1 = string1.replace('log2(', 'm.log2(')
	string1 = string1.replace('log₂(', 'm.log2(')
    string1 = string1.replace('ln(', 'm.log(')
    string1 = string1.replace('√(', 'm.sqrt(')

    number = eval(string1)
    if (type(number) != complex):	## `number` is Real; Real Numbers set is a subset of Imaginary Numbers set
        if (number >= 9999999999999999):
            return '∞'
        if (number == int(number)):
            number = int(number)
        if (round(number, 8) == 0):
            number = round(number, 5)
        if (int(number) == number):
            number = int(number)
        return number
    
    a = number.real
    b = number.imag
    number = a + (b * 1j)
    if (round(a, 8) == 0):
        a = 0
        if not (round(b, 8) == 0):
            if (b == int(b)):
                b = int(b)
            number = b * 1j
        else:
            number = b = 0
    if (round(b, 8) == 0):
        b = 0
        if not (round(a, 8) == 0):
            if (a == int(a)):
                a = int(a)
            number = a
        else:
            number = 0
    if (number == (-1+1.2246467991473532e-16j)):
        return -1
    if (number == (0.20787957635076193+0j)):
        return 0.20787957635076193
    if (number == 1j):
        number = 'ι'
    if (number == (0+0j)):
        return 0
    return str(number).replace('1j', 'ι').replace('j', 'ι').replace('(', '').replace(')', '').replace('+', ' + ').replace('-', ' - ').replace(' - 0 ', '').replace(' + 0 ', '').replace(' - 0ι', '').replace(' + 0ι', '')





class HoverButton(Button):
    """
    Class `HoverButton` to modify `Button` for repairing `activeforeground` and `activebackground` in Python 3.7.4 and earlier
    """
    def __init__(self, master, **kw):
        Button.__init__(self, master=master, **kw)
        self.defaultForeground = self["foreground"]
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.onEnter)
        self.bind("<Leave>", self.onLeave)

    def onEnter(self, e):
		global s
		s(0.015)
        self["foreground"] = self["activeforeground"]
        self["background"] = self["activebackground"]

    def onLeave(self, e):
		global s
		s(0.015)
        self["foreground"] = self.defaultForeground
        self["background"] = self.defaultBackground





def press(num): ## Function to update expression in the text entry box 
    ## Point out the global expression variable 
    global expression, equation

    if (num == 'fact('):
        ## Special case for factorials
        expression = 'fact(' + str(expression) + ')'
    else:
        operatorList = [' + ', ' - ', ' × ', ' ÷ ']
        if (expression != ''):
            if ((expression[-1] == ' ') and (str(num) in operatorList)): ## For replacing operators
                if not (((str(num) == ' - ') or (str(num) == ' + ')) and ((expression[-3: len(expression): 1] == ' × ') or (expression[-3: len(expression): 1] == ' ÷ '))):
                    expression = expression[0: -3: 1]
        ## Concatenation of string 
        expression += str(num) 

    ## Update the expression by using set method 
    equation.set(expression)

 
def evaluate():   ## Function to evaluate the final expression
    ## Try and except statement is used for handling the errors like zero division error etc.
    ## Put that code inside the try block which may generate the error
    global expression, equation

    try:
        ## evalall() function evaluate the expression and str function convert the result into string
        expression = str(evalall(expression))
        equation.set(expression)

    ## If error is generated, then handles it by the except block
    except ZeroDivisionError:
        equation.set('∞')
        expression = ""

    except:
        equation.set("ERROR")
        expression = ""


def baseConvertingCalculator():
    global expression, equation, baseCounter
    expression = evalall(expression)
    if (expression == int(expression)):
        expression = int(expression)

    def decimalToBinary(number):
        ## `split()` seperates whole number and decimal part and stores it in two seperate variables
        if (type(number) == float):
            whole, dec = str(number).split(".")
            ## Convert both whole number and decimal part from string type to integer type
            whole = int(whole)
            dec = int (dec)
            ## Convert the whole number part to it's respective binary form and remove the  "0b" from it.
            res = bin(whole).lstrip("0b") + "."
            ## Iterate the number of times, we want the number of decimal places to be
            for x in range(0, len(str(dec)), 1):
                ## Multiply the decimal value by 2 and seperate the whole number part and decimal part
                whole, dec = str((decimalToBinary(dec)) * 2).split(".")
                ## Convert the decimal part to integer again
                dec = int(dec)
                ## Keep adding the integer parts receive to the result variable
                res += whole
        else:
            res = bin(number)     
        equation.set(str(res)[2: len(str(res)): 1])

    ## Function converts the value passed as parameter to it's decimal representation
    def binaryToDecimal(number):
        num = number
        decValue = 0
        ## Initializing base value to 1, i.e 2 ^ 0
        base = 1
        temp = num
        while (temp):
            lastDigit = temp % 10
            temp = int(temp / 10)
            decValue += lastDigit * base
            base = base * 2
        equation.set(str(decValue))

    if (baseCounter == 0):
        decimalToBinary(expression)
        baseCounter = 1
    else:
        binaryToDecimal(expression)
        baseCounter = 0



def epii(): ## Secret function 1. to type and evaluate e**(π*ι) = -1
    global expression, equation
    expression = 'e^(π×ι)'
    equation.set('e^(πι)')
    evaluate()


def showe():    ## Secret function 2. to type and evaluate e = 2.71828
    global expression, equation
    expression = 'e'
    equation.set(expression)
    evaluate()


def showPi():   ## Secret function 3. to type and evaluate π = 3.14159
    global expression, equation
    expression = 'π'
    equation.set(expression)
    evaluate()


def showi():    ## Secret function 4. to type and evaluate ι = √-1
    global expression, equation
    expression = 'ι'
    equation.set(expression)
    evaluate()


def epowe():    ## Secret function 5. to type and evaluate e**e = 15.15426
    global expression, equation
    expression = 'e^e'
    equation.set(expression)
    evaluate()


def pipowpi():  ## Secret function 6. to type and evaluate π**π = 36.46216
    global expression, equation
    expression = 'π^π'
    equation.set(expression)
    evaluate()


def epowpi():   ## Secret function 7. to type and evaluate e**π = 23.14069
    global expression, equation
    expression = 'e^π'
    equation.set(expression)
    evaluate()


def pipowe():   ## Secret function 8. to type and evaluate π**e = 22.45916
    global expression, equation
    expression = 'π^e'
    equation.set(expression)
    evaluate()


def ipowi():    ## Secret function 9. to type and evaluate ι**ι = e**(-π/2) = 0.20788
    global expression, equation
    expression = 'ι^ι'
    equation.set(expression)
    evaluate()


def ipowe():    ## Secret function 10. to type and evaluate ι**e = -0.42822-0.90368j
    global expression, equation
    expression = 'ι^e'
    equation.set(expression)
    evaluate()


def ipowpi():   ## Secret function 11. to type and evaluate ι**π = 0.22058-0.97537j
    global expression, equation
    expression = 'ι^π'
    equation.set(expression)
    evaluate()


def epowi():    ## Secret function 12. to type and evaluate e**ι = 0.54030+0.84147j
    global expression, equation
    expression = 'e^ι'
    equation.set(expression)
    evaluate()
    

def pipowi():   ## Secret function 13. to type and evaluate π**ι = 0.41329+0.91060j
    global expression, equation
    expression = 'π^ι'
    equation.set(expression)
    evaluate()


def datetime(): ## Secret function 14. return today's date and time
    global expression, equation
    expression = str(datetime.now())
    equation.set(expression)


def clear():    ## Function to clear the whole expression
    global expression, equation
    expression = ''
    equation.set(expression)


def delete():   ## Function to clear the last entered character
    global expression, equation

    try:
        if (expression[-1] != ' '):
            expression = expression[0: -1: 1]

        else:
            expression = expression[0: -3: 1]
        
        equation.set(expression)

    except:
        pass


def onClosing():    ## User clicks ' X ' in attempt to exit the application
    if (mb.askyesnocancel("Leavin' so early?", "Do you want to exit the Calculator?")):    ## Prompts if user wants to leave the GUI; `Yes`: Leaves GUI, `No`: Stays in the GUI, `Cancel`: Closes and prompt and continues to stay in the GUI (similar to `No`)
        calculatorGUI.destroy()






## Driver/Main code
if (__name__ == "__main__"):
	
	## Create a GUI window 
	calculatorGUI = Tk()

	## Set the icon of the app
	calculatorGUI.iconbitmap('Calculator_Icon.ico')

	## Set the background colour of GUI window 
	calculatorGUI.configure(background="#000000") 

	## Set the title of GUI window
	calculatorGUI.title("Mathematical-Expression-Value-Evaluating-Machinator!")

	## Set the configuration of GUI window 
	calculatorGUI.geometry("1320x675")

	## StringVar() is the variable class
	## We create an instance of this class
	equation = StringVar()

	## Create the text entry box for showing the expression
	expression_field = Entry(calculatorGUI,
	textvariable=equation,
	font="MathJax_Main-Regular 30",
	justify='center',
	relief=FLAT,
	bg='#000000',
	fg='#FFFFFF')

	## Grid method is used for placing the widgets at respective positions in table like structure
	expression_field.grid(column=1, columnspan=100, ipadx=200, ipady=4) 

	equation.set('') 

	## Create HoverButtons and place at a particular location inside the root window `calculatorGUI`. When user press the button, the command or function affiliated to that button is executed
	button1 = HoverButton(calculatorGUI, text=' \n 1 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['Product Sans', 28], command=lambda: press(1), height=1, width=7).grid(row=6, column=1)

	button2 = HoverButton(calculatorGUI, text=' \n 2 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['Product Sans', 28], command=lambda: press(2), height=1, width=7).grid(row=6, column=2) 

	button3 = HoverButton(calculatorGUI, text=' \n 3 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['Product Sans', 28], command=lambda: press(3), height=1, width=7).grid(row=6, column=3) 

	button4 = HoverButton(calculatorGUI, text=' \n 4 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['Product Sans', 28], command=lambda: press(4), height=1, width=7).grid(row=5, column=1) 

	button5 = HoverButton(calculatorGUI, text=' \n 5 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['Product Sans', 28], command=lambda: press(5), height=1, width=7).grid(row=5, column=2) 

	button6 = HoverButton(calculatorGUI, text=' \n 6 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['Product Sans', 28], command=lambda: press(6), height=1, width=7).grid(row=5, column=3) 

	button7 = HoverButton(calculatorGUI, text=' \n 7 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['Product Sans', 28], command=lambda: press(7), height=1, width=7).grid(row=4, column=1) 

	button8 = HoverButton(calculatorGUI, text=' \n 8 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['Product Sans', 28], command=lambda: press(8), height=1, width=7).grid(row=4, column=2) 

	button9 = HoverButton(calculatorGUI, text=' \n 9 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['Product Sans', 28], command=lambda: press(9), height=1, width=7).grid(row=4, column=3) 

	button0 = HoverButton(calculatorGUI, text=' \n 0 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['Product Sans', 28], command=lambda: press(0), height=1, width=7).grid(row=7, column=1) 

	plus = HoverButton(calculatorGUI, text=' \n + \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28, 'bold'], command=lambda: press(" + "), height=1, width=7).grid(row=7, column=4) 

	minus = HoverButton(calculatorGUI, text=' \n - \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28, 'bold'], command=lambda: press(" - "), height=1, width=7).grid(row=6, column=4) 

	multiply = HoverButton(calculatorGUI, text=' \n × \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28, 'bold'], command=lambda: press(" × "), height=1, width=7).grid(row=5, column=4) 

	divide = HoverButton(calculatorGUI, text=' \n ÷ \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28, 'bold'], command=lambda: press(" ÷ "), height=1, width=7).grid(row=4, column=4) 

	equal = HoverButton(calculatorGUI, text=' \n = \n ', fg='#000000', bg='#0000FF', relief=FLAT, activebackground='#0064FF', activeforeground='#FFFFFF', font=['CircularStd', 28, 'bold'], command=evaluate, height=1, width=7).grid(row=7, column=3) 

	clear = HoverButton(calculatorGUI, text=' C ', fg='#000000', bg='#FF0000', relief=FLAT, activeforeground='#FFFFFF', activebackground='#FF1111', font=['CircularStd', 26], command=clear, height=1, width=7).grid(row=4, column=6)

	parentheses1 = HoverButton(calculatorGUI, text=' \n ( \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['Product Sans', 28], command=lambda: press("("), height=1, width=7).grid(row=7, column=5)

	parentheses2 = HoverButton(calculatorGUI, text=' \n ) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['Product Sans', 28], command=lambda: press(")"), height=1, width=7).grid(row=7, column=6)

	power = HoverButton(calculatorGUI, text=' \n xⁿ \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("^"), height=1, width=7).grid(row=5, column=5)

	ι = HoverButton(calculatorGUI, text=' \n ι \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['Product Sans', 28], command=lambda: press("ι"), height=1, width=7).grid(row=5, column=6)

	e = HoverButton(calculatorGUI, text=' \n e \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['Product Sans', 28], command=lambda: press("e"), height=1, width=7).grid(row=6, column=5)

	π = HoverButton(calculatorGUI, text=' \n π \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['Product Sans', 28], command=lambda: press("π"), height=1, width=7).grid(row=6, column=6)

	decimal = HoverButton(calculatorGUI, text=' \n . \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("."), height=1, width=7).grid(row=7, column=2)

	delete = HoverButton(calculatorGUI, text=' \n ⪻ \n ', fg='#FF0000', bg='black', relief=FLAT, activeforeground='#FFFFFF', activebackground='#FF0000', font=['CircularStd', 28], command=delete, height=1, width=7).grid(row=4, column=5)

	sin = HoverButton(calculatorGUI, text=' \n sin(x) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("sin("), height=1, width=7).grid(row=8, column=1)

	cos = HoverButton(calculatorGUI, text=' \n cos(x) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("cos("), height=1, width=7).grid(row=8, column=2)

	tan = HoverButton(calculatorGUI, text=' \n tan(x) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("tan("), height=1, width=7).grid(row=8, column=3)

	cosec = HoverButton(calculatorGUI, text=' \n cosec(x) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("csc("), height=1, width=7).grid(row=8, column=4)

	sec = HoverButton(calculatorGUI, text=' \n sec(x) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("sec("), height=1, width=7).grid(row=8, column=5)

	cot = HoverButton(calculatorGUI, text=' \n cot(x) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("cot("), height=1, width=7).grid(row=8, column=6)

	ln = HoverButton(calculatorGUI, text=' \n ln(x) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("ln("), height=1, width=7).grid(row=9, column=1)

	log = HoverButton(calculatorGUI, text=' \n log(x) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("log("), height=1, width=7).grid(row=9, column=2)

	log2 = HoverButton(calculatorGUI, text=' \n log₂(x) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("log₂("), height=1, width=7).grid(row=9, column=3)

	sqrt = HoverButton(calculatorGUI, text=' \n √x \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("√("), height=1, width=7).grid(row=9, column=4)

	fact = HoverButton(calculatorGUI, text=' \n x! \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("fact("), height=1, width=7).grid(row=9, column=5)

	baseCounter = 0
	baseConverter = HoverButton(calculatorGUI, text=' \n 10 ↔ 2 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=baseConvertingCalculator, height=1, width=7).grid(row=9, column=6)

	magicList = [epii, showe, showPi, showi, epowe, pipowpi, epowpi, pipowe, ipowi, ipowe, ipowpi, epowi, pipowi, datetime]
	magicButton = HoverButton(calculatorGUI, text='The Magic HoverButton!', relief=FLAT, fg='black', bg='black', activeforeground='black', activebackground='black', font=['CircularStd', 28], command=ch(magicList), height=2, width=7).grid(row=0, column=0)

	## A protocol to check if the cursor clicked on the exit `X` button
	calculatorGUI.protocol("WM_DELETE_WINDOW", onClosing)

	## Start the GUI
	calculatorGUI.mainloop()


	
##################################################
###"""##### ----- End Of Program ----- #####"""###
##################################################
