import config
from model.user import User


def gen_js():
    with open("static/js/origin.js") as js_file:
        origin = js_file.read()

        admins = User.get_admin()
        if admins:
            admin = admins[0]
            now = origin.format(domain=config.DOMAIN, token=admin.key)
            with open("static/js/x.js", "w") as now_file:
                now_file.write(now)


if __name__ == "__main__":
    gen()
