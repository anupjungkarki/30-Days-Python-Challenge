import psutil

battery = psutil.sensors_battery()
percent = str(battery.percent)
print('''Your Device has been running on: ''' +percent + "% battery")