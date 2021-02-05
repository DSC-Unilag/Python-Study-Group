#1 min = 60
#1 hour = 3600
#1 day = 86400

my_seconds =input('enter a number in seconds: ')

t=int(my_seconds)

day= t//86400
hour= (t-(day*86400))//3600
minute= (t - ((day*86400) + (hour*3600)))//60
seconds= t - ((day*86400) + (hour*3600) + (minute*60))
print( day, 'days' , hour,' hours', minute, 'minutes',seconds,' seconds')