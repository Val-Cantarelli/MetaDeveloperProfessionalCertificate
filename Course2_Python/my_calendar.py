import calendar
'''Muito cuidado!!! Havia nomeado esse arquivo como "calendar", mas em Python já existe esse módulo. Então quando
fui usar ele retornava um erro dizendo que não encontrava os parâmetros em calendar. 
 Isso aconteceu pq Python dá prioridade ao ao path local e entendeu que eu estava importando meu próprio módulo'''

# Calculate leap years between 2000 and 2050
leap_days = sum(1 for year in range(2000, 2051) if calendar.isleap(year))
print("Number of leap years between 2000 and 2050:", leap_days)

# Check if the year 2036 is a leap year
is_leap = calendar.isleap(2036)
print("Is 2036 a leap year?", is_leap)