def leapYear(year):
  return True if(year % 4 == 0 
            and year % 100 != 0) or (year % 400 == 0) else False
def month_check(year,month,day):
  month_31 = [1,3,5,7,8,10,12]
  if month in month_31:
    return 31
  elif month == 2 and leapYear(year):
    return 29
  elif month == 2:
    return 28
  else: 
    return 30

def nextDay(year, month, day):
  if day < month_check(year,month,day):
    return year, month, day + 1 
  elif month == 12 and day == month_check(year,month,day):
    return year + 1, 1, 1 
  else: 
    return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")

test()






# def nextDay(year, month, day):
#     """Simple version: assume every month has 30 days"""
#     if day < 30:
#         return year, month, day + 1
#     else:
#         if month == 12:
#             return year + 1, 1, 1
#         else:
#             return year, month + 1, 1
        
# def dateIsBefore(year1, month1, day1, year2, month2, day2):
#     """Returns True if year1-month1-day1 is before
#        year2-month2-day2. Otherwise, returns False."""
#     if year1 < year2:
#         return True
#     if year1 == year2:
#         if month1 < month2:
#             return True
#         if month1 == month2:
#             return day1 < day2
#     return False        

# def daysBetweenDates(year1, month1, day1, year2, month2, day2):
#     """Returns the number of days between year1/month1/day1
#        and year2/month2/day2. Assumes inputs are valid dates
#        in Gregorian calendar."""
#     # program defensively! Add an assertion if the input is not valid!

#     days = 0 
#     while dateIsBefore(year1, month1, day1, year2, month2, day2):
#       year1, month1, day1 = nextDay(year1, month1, day1)
#       days += 1
#     assert days != 0, "First year cannot be after the second year"  
#     return days
         

        

# def test():
#   test_cases = [((2012,9,30,2012,10,30),30), 
#                   ((2012,1,1,2013,1,1),360),
#                   ((2012,9,1,2012,9,4),3),
#                   ((2013,1,1,1999,12,31), "AssertionError")]
#   for (args, answer) in test_cases:
#         try:
#             result = daysBetweenDates(*args)
#             if result == answer and answer != "AssertionError":
#                 print("Test case passed!")
#             else:
#                 print("Test with data:", args, "failed")
    
#         except AssertionError:
#             if answer == "AssertionError":
#                 print("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
#             else:
#                 print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))           
# test()