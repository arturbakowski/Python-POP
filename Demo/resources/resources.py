from datetime import datetime
import random
import string

PRZEGLADARKA = "C:\\\\Program Files\\Python36\\drivers\\chromedriver.exe"
TODAY = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
DAY = datetime.now().strftime('%d-%H:%M')

app_link = 'http://demoqa.com/'


def get_first_name():
    names = ['Jan', 'Marek', 'Tomasz']
    name = random.choice(names)
    return name


def get_last_name():
    last_names = ['Kowalski', 'Nowak', 'Lewandowski']
    last_name = random.choice(last_names)
    return last_name


def get_phone_number():
    number = ''
    while len(number) != 10:
        x = random.randrange(1, 10)
        number += str(x)
    return number


def get_username():
    username = 'TestUser ' + 'Day: '
    username += DAY
    return username


def get_email():
    name = 'testemail' + str(random.randrange(1, 10)) + str(random.randrange(1, 10)) + str(random.randrange(1, 10))
    domain = 'testemaildomain'
    email = name + '@' + domain + '.pl'
    return email


def get_password(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
