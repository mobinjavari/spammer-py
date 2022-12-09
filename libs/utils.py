import requests
import time
import json
import os

# cmd
class cmd:
    ## clear screen
    def clear():
        os.system('clear' if os.name == 'posix' else 'cls')
    ## run command
    def run(path):
        os.system(path)