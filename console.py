# spammer console 

from libs.utils import spam
from libs.utils import cmd
from libs.utils import text

try:

    while True:
        cmd.clear()
        text.welcome()
        spam.menu()

        menu = input(text.status("+")+"Choose an option (1/2/3/..) : ")
        if (menu == "1"):
            target = input(text.status("+","Enter phone number (9348xxxxxx) : "))
            if (target == ""): 
                print(text.status("-","The number cannot be empty"))
                input(text.status("+")+"Press enter to refresh the page ")
            else : 
                repetition = input(text.status("+","Number of messages (max = 20,000) : "))
                if (repetition == ""): print(text.status("*","The empty value is equal to 20 messages"))
                spam.sms(target,repetition)

        elif (menu == "2"):
            print(text.status("*","The desired service is not active"))
            input(text.status("+","Press enter to refresh the page "))
        
        elif (menu == "3"):
            print(text.status("*","The desired service is not active"))
            input(text.status("+","Press enter to refresh the page "))
        
        else :
            print(text.status("*","The desired option does not exist"))
            input(text.status("+","Press enter to refresh the page "))

except:
    print(text.status("*","You Exit Tools !!\n"))

