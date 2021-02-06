#tution increment 

tuition=8000
checker = 2.2/100
year=10


increase_percentage=tuition*checker

#hand this line of codes accept year value bbelow
#year =int(input("Enter  number of years to display:  "))


new_tuition = (tuition + increase_percentage)
#first year...............
for year in range(1,year+1):
    print(f'year {year} Tuition fee ')
    print( (new_tuition * year))
    print('\n')
  