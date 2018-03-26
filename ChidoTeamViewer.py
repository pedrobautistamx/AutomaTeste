from automa import api as automa
from automa.api import ENTER, ALT, F4,F6, TAB, CTRL, SHIFT
from datetime import datetime


gmail='https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin'

automa.start("TeamViewer 13")
automa.click("CONNECT")
automa.write("5631", into="Password")
automa.click("Log On")
automa.press(TAB)

automa.press(TAB)
automa.press(ENTER)
automa.press(F6)
automa.press(CTRL + "a")
automa.press(CTRL + "c")
automa.start("WordPad")
automa.press(CTRL + "v")
automa.press(CTRL + "s")
automa.write("COPIADO.txt", into="File name:")
automa.click("Save")
automa.click("Yes")
automa.start("Google Chrome")
automa.press(CTRL + SHIFT + "n")
automa.write(gmail)
automa.press(ENTER)
automa.write("marisol.hernandez@interware.com.mx")
automa.click("SIGUIENTE")
automa.write("2433499561M.")
automa.click("SIGUIENTE")
automa.click("REDACTAR")
automa.write("pbautista@interware.com.mx")
automa.press(TAB,TAB)
automa.write("Esto es el codigo que acabo de copiar!!!!!!!!")
automa.press(TAB)
automa.press(CTRL + "v")
automa.press(TAB, ENTER)
