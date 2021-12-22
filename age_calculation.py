# here we calculate age of a person.
current_year=int(input('enter current year:'))
birth_year=int(input('enter birth year:'))
print()
current_month=int(input('enter current month:'))
birth_month=int(input('enter birth month:'))
print()
current_day=int(input('enter current day:'))
birth_day=int(input('enter your birthday:'))
print()
if birth_year>0 and birth_month>0 and birth_day>0:
    age=current_year-birth_year
    print('your current age is:',age)
    # print('your current age is:',current_day-birth_day,'days',current_month-birth_month,'months',current_year-birth_year,'years')
    print('your current age is:',current_year-birth_year,'years old',current_month-birth_month,'months',current_day-birth_day,'days')
elif birth_year<1:
    age=current_year-birth_year
    print('your current age is:',age)
else:
    print('invalid age')
