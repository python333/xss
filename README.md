这是基于tornado的一个简单的xss平台，只要几个步骤即可在服务器运行。

每次运行，都将依据static/js/origin.js以及config.py中的参数生成static/js/x.js，

1、可自行修改config.py中的DOMAIN来调整域名

2、可自行修改static/js/origin.js模板

使用步骤

1、pip3 install -r requirments.txt

2、python3 app.py

3、注册一个管理员账号(只能注册一个)

4、在config.py中设置参数DOMAIN，设置自己的ip或者网址

5、T+C终止运行后，重新启动即可使用
