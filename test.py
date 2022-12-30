import time
date = input('Date (mm/dd/yyyy): ')
try:
  time.strptime(date, '%m.%d.%Y')
except ValueError:
  print('Invalid date!')

