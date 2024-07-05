import time

def cdown(h, m, s):
    totalSecond = h*3600 + m*60 +s
    while totalSecond > 0:
        print(totalSecond,"seconds left.")
        time.sleep(1)
        totalSecond -= 1
    print("Countdown ended.")

while True:
    try:
        h = input("Enter hours to count: ")
        m = input("Enter minutes to count: ")
        s = input("Enter seconds to count: ")
        cdown(int(h),int(m),int(s))
        break
    except:
        print("Enter values again.")