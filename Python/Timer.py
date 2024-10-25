import time

timer_h = int(input("Please enter hours (0 To Skip): "))
timer_m = int(input("Please enter minutes (0 To Skip): "))
timer_s = int(input("Please enter seconds (0 To Skip): "))

total = (timer_h * 3600) + (timer_m * 60) + timer_s

for x in range(total, 0, -1):
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = x // 3600

    print(f"{hours:02}:{minutes:02}:{seconds:02}", end='\r')  
    time.sleep(1)

print("TIMES UP")
