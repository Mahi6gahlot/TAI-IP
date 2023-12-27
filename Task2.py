import time
def countdown(seconds):
    while seconds>0:
        print(seconds)
        time.sleep(1)
        seconds-=1
seconds=int(input("Enter the number of seconds to countdown:"))
countdown(seconds)
print("Times up!")
