from datetime import datetime, timedelta


def is_same_days(date1: datetime, date2: datetime) ->bool:
# функція приймає два об'єкта datetime та порівнює чи співпадає день та місяць. 
# поаертає True чи False 
    
    same_day = False
    same_month = False
    if date1.day == date2.day:
        same_day = True
    if date1.month == date2.month:
        same_month = True
    return same_day and same_month



def get_birthdays_per_week(users: list) -> list:
# функція повертає список унікальних ідентифікаторів бази даних зі словника
#  participants в кількості quantity. 
    
    today = datetime.now()
    count = 0
    weekend_list = [] # список імен працівників, дні народження яких припадають на вихідні
    if today.weekday() == 6: # якщо функія запущена в неділю то цикл починається з суботи
        count = -1
    if today.weekday() == 0: # якщо функія запущена в понеділок то цикл починається з суботи
        count = -2

    while count < 7:
        x_day = today + timedelta(days=count)
        week_day = x_day.strftime('%A') # день тижня який виводиться перед списком іменинників
        users_list = [] # список імен працівників, дні народження яких припадають на нокретний день в циклі
        count += 1
        
        for person in users: # перебираємо словники з датою народження в списку 
            if is_same_days(x_day, person['birthday']): # порівнюємо чи співпадають дні народження з конкретним днем в циклі
                if x_day.weekday() == 0: # якщо в циклі понеділок то додаємо до списку імен імениннивів імена працівників, дні народження яких припадають на вихідні 
                    for i in weekend_list:
                        users_list.append(i)
                    users_list.append(person['name'])
                if x_day.weekday() == 5 or x_day.weekday() == 6: # якщо в циклі субота або неділя то іменинників додаємо до списку імен працівників, дні народження яких припадають на вихідні
                    weekend_list.append(person['name'])
                else:
                    users_list.append(person['name']) 
        
        if users_list != []: # ігноруємо дні в яких спсок імен пустий
            print(f"{week_day}: {users_list}")
        