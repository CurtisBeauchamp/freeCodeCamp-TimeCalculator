day_list = [
    "",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

day_list_lower = [string.lower() for string in day_list]

def add_time(start, duration, current_day=""):
    start_period = start[-2:]
    end_period = ""
    start_time = ""
    duration_time = ""
    days_later = 0
    newtime_raw = 0
    
    for char in start:
        if char.isdigit():
            start_time += char
            
    if start_period == "PM":
        start_time = int(start_time) + 1200       
            
    for char in duration:
        if char.isdigit():
            duration_time += char
            
    newtime24h = int(start_time) + int(duration_time)
    newtime24h_minutes = int(str(newtime24h)[-2:])
    
    if newtime24h_minutes == 60:
        newtime24h = newtime24h + 100
    elif newtime24h_minutes > 60:
        newtime24h = newtime24h + 100
      
        hour_portion = str(newtime24h)[:-2]
        minute_portion =  str(newtime24h - 60)[2:]
 
        newtime24h = hour_portion + minute_portion   
        newtime24h = int(newtime24h)
        
    if (newtime24h / 2400) >= 1.0:
        days_later = (newtime24h // 2400)
        
    if days_later > 0:
        newtime24h = newtime24h - (days_later * 2400)
        
    if newtime24h > 1200 and newtime24h < 1300:
        newtime_raw = newtime24h
        end_period = "PM"
    elif newtime24h == 1200:
        newtime_raw = 1200
        end_period = 'PM'
    elif newtime24h >= 1300:
        newtime_raw = newtime24h - 1200 
        end_period = 'PM'
    elif len(str(newtime24h)) <= 2:
        newtime_raw = int(newtime24h) + 1200
        end_period = "AM"  
    else:
        newtime_raw = newtime24h
        end_period = "AM"
        
    if current_day != "":
        current_day = current_day.casefold()
        day_index = day_list_lower.index(current_day) + days_later

        if day_index > 7 and day_index < 14:
            day_index = day_index - 7
        elif day_index > 14:
            weeks = (day_index //  7) #Gets a rounded down number of weeks
            day_index = day_index - (weeks * 7) #New index disregarding full weeks
               
    days_later_string = ""

    if days_later == 1:
        days_later_string = "(next day)"
    elif days_later > 1:
        days_later_string = f"({days_later} days later)"
        
    newtime_raw_string = str(newtime_raw)
    
    if len(newtime_raw_string) == 4:
        newtime = newtime_raw_string[:2] + ":" + newtime_raw_string[2:]
    else:
        newtime = newtime_raw_string[:1] + ":" + newtime_raw_string[1:]
    
    newtime = f"{newtime} {end_period}"
    
    if current_day != "":
        newtime = f"{newtime}, {day_list[day_index]}"
    
    if days_later > 0:
        newtime = f"{newtime} {days_later_string}"
    
    return newtime

print(add_time("11:59 PM", "24:05"))
