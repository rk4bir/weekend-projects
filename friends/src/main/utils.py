from django.utils.text import slugify
import re, math, string, random
from random import randint
from django.contrib.auth.models import User
import requests, json
from django.conf import settings


def uploadToGoogleDrive(fileName, TARGET='ROOT'):
    TARGET_FOLDER  = settings.ROOT_FOLDER
    if TARGET == "POST":
        TARGET_FOLDER = settings.POST_FOLDER
    elif TARGET  == 'PROFILE':
        TARGET_FOLDER = settings.PROFILE_FOLDER

    try:
        token = "Bearer " + settings.ACCESS_TOKEN
        headers = {"Authorization": token} # token after the word Bearer
        para = {
            "name": fileName, #file name to be uploaded
            "parents": [TARGET_FOLDER] # folder id of google drive
        }
        files = {
            'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
            'file': open(fileName, "rb") #file to upload
        }
        r = requests.post(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            headers=headers,
            files=files
        )
        print(r.json()['id'])
        return r.json()['id']
    except:
        return ''



# Get unique username
def usernameGenerator(email):
    username = email.split('@')[0]
    qs = User.objects.filter(username=username)
    if qs.exists():
        while True:
            username += string.digits[randint(0, 9)]
            qs = User.objects.filter(username=username)
            if not qs.exists():
                break
    return username

# Generates random numbers
def get_random_number(size=6, numbers=string.digits):
    return ''.join(random.choice(numbers) for _ in range(size))

def get_random_password(size=8):
    stock = string.printable.strip()
    passwd = ""
    for _ in range(randint(6,8)):
        passwd += random.choice(stock)
    return passwd
#=============================================
def getStars(s):
    whole = int(s)
    ar = []
    for i in range(whole):
        ar.append('fa-star')
    if len(ar) == 5: return ar
    if (s - whole) == 0:
        for i in range(len(ar),5,1):
            ar.append('fa-star-o')
    else:
        ar.append('fa-star-half-o')
        for i in range(len(ar),5,1):
            ar.append('fa-star-o')
    return ar

def getReviewStatus(score):
    if score == 0.00: return 'n/a'
    if score >= 1.00 and score < 2.00:
        return 'Very Poor'
    elif score >= 2.00 and score < 3.00:
        return "Poor"
    elif score >= 3.00 and score < 4.00:
        return "Medium"
    elif score >= 4.00 and score < 4.50:
        return "Good"
    elif score >= 4.50 and score <= 5.00:
        return "Very Good"

def valid_phone(phone):
    if len(phone) != 11 or phone[0] != '0' or phone[1] != '1':
        return False
    if not re.compile("^[0-9]+$").match(phone):
        return False
    return True
def phone_already_exist(phone):
    from accounts.models import Account
    qs = Account.objects.filter(phone=phone)
    if qs.exists():
        return True
    return False

# valid name
def valid_name(name):
    return bool(re.compile("^[A-Za-z .-]+$").match(name))

# Generating username from name field
def getUsername(name):
    numerics = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_']
    username = name.split(' ')[0].lower()
    # checking username exists or not, if exist create one
    from accounts.models import User
    qs = User.objects.filter(username=username)
    if qs.exists():
        while True:
            random_str = numerics[randint(0, 10)] + numerics[randint(0, 10)]
            username += random_str
            qs = User.objects.filter(username=username)
            if not qs.exists():
                break
    return username

# Return 4 digit code
def getRandomCode(size=4):
    numerics = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    random_str = ""
    for _ in range(size):
        random_str += numerics[randint(0, 9)]
    return random_str


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_key_generator(instance, size=10):
    key = random_string_generator(size=size).upper()
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(key=key).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return key


def unique_order_no_generator(instance):
    Klass        = instance.__class__
    lastObj      = Klass.objects.all()
    base         = instance.cart.restaurant.title[:3] + '-'
    last         = lastObj.count() + 1
    order_no     = base + str(last)
    while True:
        qs = Klass.objects.filter(order_no=order_no).exists()
        if qs:
            last += 1
            order_no = base + str(last)
            continue
        else:
            break
    return order_no

def unique_order_id_generator(instance):
    order_new_id = random_string_generator(size=32)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=order_new_id).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return order_new_id


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=1)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


from django.contrib.auth.models import User


