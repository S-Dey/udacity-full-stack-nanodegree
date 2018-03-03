import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on " + time.ctime())
while break_count < total_breaks:
    time.sleep(10)
    webbrowser.open("https://youtu.be/D5IlAZ87T9c")
    break_count += break_count
