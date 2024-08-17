# import time
# epoch_time = int(time.time())
# hours = int(epoch_time // 3600) % 24
# minutes = int((epoch_time % 3600) // 60)
# formatted_time = f"{hours:02d}:{minutes:02d}"
# print(formatted_time)
import time
currenttime=time.strftime("%I:%M %p", time.localtime())
print(currenttime)

# print(time.asctime())
# print(time.ctime())
# print(time.time())
