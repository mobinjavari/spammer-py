from libs.utils import spam
from libs.utils import cmd
from libs.utils import text

try:

    while True:
        cmd.clear()
        text.welcome()
        spam.menu()

except:
    print(text.status("*","You Exit Tools !!\n"))

