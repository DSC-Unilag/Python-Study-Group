#A program that coverts users minutes to second
T_sec =60
T_min =3600
T_hr =86400

Total_secs = float(input('Enter a number of seconds: '))
if Total_secs>=T_sec:

    # Display the results.
    # Get the number of remaining seconds.
    seconds = Total_secs % 60
    
    # Get the number of remaining minutes.
    minutes = (Total_secs // 60) % 60

    # Get the number of hours.
    hours = int(Total_secs // 3600)

    # Get the number of days.
    days = int(Total_secs // 86400)



    print('Here is the time in Days, hours, minutes, and seconds:')
    print(days, 'Days:',end='  ' )
    print(hours, 'Hours:',end='  ')
    print(minutes, 'Minutes:',end='  ')
    print(seconds, 'Seconds')

else:
     print("Oops!! Your entry Is not up to a minutes!!! ")
     print(0, 'Days:',end='  ' )
     print(0, 'Hours:',end='  ')
     print(0.0, 'Minutes:',end='  ')
     print(Total_secs, 'Seconds')






     
#print('One', end=' ')
#print('Two', end=' ')
#print('Three')