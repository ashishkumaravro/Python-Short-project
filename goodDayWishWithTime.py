import time

timestamp = time.strftime('%H')

if int(timestamp) >= 5 and int(timestamp) < 12:
    print(f"Good Morning, wake up!😊 It's {time.strftime('%H:%M')}. ")

elif int(timestamp) >= 12 and int(timestamp) < 15:
    print(f"Good Noon. It's {time.strftime('%H:%M')}. It's a hot day!🥵")

elif int(timestamp) >= 15 and int(timestamp) < 18:
    print(f"Good Afternoon! It's {time.strftime('%H:%M')}.  \nEnjoy the beauty of nature!😊")

elif int(timestamp) >= 18 and int(timestamp) <= 20:
    print(" A beautiful Sunset.")
    print(f"Good evening. It's {time.strftime('%H:%M')}. Let's read the book!😊")

else:
    print("Good Night.Have a satiate sleep😚")
