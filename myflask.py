# 引入flask模块
from flask import Flask
# 引入flask_bootstrap模块
from flask_bootstrap import Bootstrap
# 引入render_template
from flask import render_template

import time

# 实例化app
app = Flask(__name__)

# 实例化bootstrap并关联app
bootstrap = Bootstrap(app)

# 设定根路由
@app.route("/")
# 根路由处理函数
def hello():
	#return "Hello World!"
	datetime = time.asctime(time.localtime(time.time()))
	return render_template('base.html',time = datetime)

# 若为程序入口则执行app
if __name__ == '__main__':
	# host为开放地址
	app.run(host = '0.0.0.0',debug = True)