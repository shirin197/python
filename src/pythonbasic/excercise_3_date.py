from datetime import date
import datetime

# example one
today = date.today()
print("Today's date:", today)

# ---------------------------------------------------------------------------------------------------------------------

# example two
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# ---------------------------------------------------------------------------------------------------------------------

# example three / different formats
today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

#  month, day and year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month-day-year
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)