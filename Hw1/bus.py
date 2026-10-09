start_hour = 9
start_minute = 35

trip_length = 47 
number_of_trips = 9

travel_minutes = trip_length * number_of_trips

total_minutes = start_minute + travel_minutes

hours_passed = total_minutes // 60
finish_minute = total_minutes % 60
finish_hour = start_hour + hours_passed

if finish_hour > 12:
    finish_hour = finish_hour - 12

print (finish_hour) 
print (finish_minute)