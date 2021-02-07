#Lap Times calculator 
total_time=0.0
lap_time_list =[]


run_time= (int(input('Enter the number laps you ran: ')))
for run_time in range(1,run_time+1):

    lap_time  = (float(input(f'Enter the number of times for Lap {run_time}: ')))
    
    total_time =total_time + lap_time
    lap_time_list.append(lap_time)

avg_time=total_time/lap_time
f_lap =min(lap_time_list)
s_lap = max(lap_time_list)

print('your lapse fastest is',f_lap)
print('your lapse slowest is',s_lap)
print('your average lapse is',avg_time)
print('your Total runtime is',total_time)






      
  