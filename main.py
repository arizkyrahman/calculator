from tkinter import *
import math

answerVariableGlobal = ""
answerLabelForSquareRoot = ""

root = Tk()
root.title('Calculator App')

answerEntryLabel = StringVar()
Label(root, font=('futura', 25, 'bold'), textvariable=answerEntryLabel, justify=LEFT, height=2, width=7).grid(columnspan=4, ipadx=120)

answerFinalLabel = StringVar()
Label(root, font=('futura', 25, 'bold'), textvariable=answerFinalLabel, justify=LEFT, height=2, width=7).grid(columnspan=4, ipadx=120)

def changeAnswerEntryLabel(entry):
    global answerVariableGlobal
    global answerLabelForSquareRoot

    answerVariableGlobal = answerVariableGlobal + str(entry)
    answerLabelForSquareRoot = answerLabelForSquareRoot
    answerEntryLabel.set(answerVariableGlobal)

def clearAnswerEntryLabel():
    global answerVariableGlobal
    global answerLabelForSquareRoot

    answerLabelForSquareRoot = answerLabelForSquareRoot
    answerVariableGlobal = ""
    answerEntryLabel.set(answerVariableGlobal)

def evaluateSquareRoot():
    global answerVariableGlobal
    global answerLabelForSquareRoot

    try:
        sqrtAnswer = math.sqrt(eval(str(answerLabelForSquareRoot)))
        clearAnswerEntryLabel()
        answerFinalLabel.set(sqrtAnswer)
    except (ValueError, SyntaxError, TypeError, ZeroDivisionError):
        try:
            sqrtAnswer = math.sqrt(eval(str(answerLabelForSquareRoot)))
            clearAnswerEntryLabel()
            answerFinalLabel.set(sqrtAnswer)
        except (ValueError, SyntaxError, TypeError, ZeroDivisionError):
            clearAnswerEntryLabel()
            answerFinalLabel.set("Error!")