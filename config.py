# coding:utf-8

DOMAIN = "http://127.0.0.1"  # 1、最后不要有/ 2、记得要有http://
PORT = 80
HOST = '0.0.0.0'
DEBUG = False
TITLE = '饼干'
TEMPLATE = 'mako'  # jinja2/mako/tornado
DATABASE_URI = "sqlite:///database.db"
COOKIE_SECRET = "6aOO5ZC55LiN5pWj6ZW/5oGo77yM6Iqx5p+T5LiN6YCP5Lmh5oSB44CD"
try:
    from private import *
except:
    pass
