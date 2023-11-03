import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        minutes, sec = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(minutes, sec)
        print(f"倒计时剩余时间: {timeformat}", end='\r')
        time.sleep(1)
        seconds -= 1

    print("时间到！专注结束")

if __name__ == "__main__":
    focus_minutes = int(input("请输入希望的专注时间（分钟）："))
    focus_timer(focus_minutes)
