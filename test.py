import datetime 

if datetime.datetime.now().strftime("%H") == "23":
   print(True)
else:
    print(False)