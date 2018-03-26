from automa import api as automa
from automa.api import ENTER, ALT, F4, TAB, CTRL, SHIFT
from datetime import datetime

gmail='https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
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
