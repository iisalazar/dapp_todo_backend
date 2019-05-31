import random, string

SECRET_KEY = ''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(100)])
