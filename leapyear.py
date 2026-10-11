#identifying a leap year, taks details: https://informatics.msk.ru/mod/statements/view.php?id=276#1

year = int(input())

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("YES")
else:
    print("NO")

# if we input 2007, we will get NO. Inputting 2000 will result in YES