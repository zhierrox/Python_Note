# import random, time, Queue
# from multiprocessing.managers import BaseManager

# task_queue = Queue.Queue()
# result_queue = Queue.Queue()

# class QueueManager(BaseManager):
# 	pass

# QueueManager.register('get_task_queue', callable=lambda: task_queue)
# QueueManager.register('get_result_queue', callable=lambda: result_queue)

# manager = QueueManager(address=('', 5000), authkey=b'abc')
# manager.start()
# task = manager.get_task_queue()
# result = manager.get_result_queue()

# for i in range(10):
# 	n = random.randint(0, 10000)
# 	print('Put task %d...' % n)
# 	task.put(n)
# print('Try get results...')
# for i in range(10):
# 	r = result.get(timeout=10)
# 	print("Result: %s" % r)
# manager.shutdown()
# print('master exit.')

# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.connect('127.0.0.1', 9999)

# print(s.recv(1024).decode('utf-8'))
# for data in [b'Michael', b'Tracy', b'Sarah']:
# 	s.send(data)
# 	print(s.recv(1024).decode("utf-8"))
# s.send(b"exit")
# s.close()

# from wsgiref.simple_server import make_server
# from hello import application

# def application(environ, start_response):
# 	start_response("200 OK", [("Content-Type", "text/html")])
# 	return [b"<h1>Test POST and GET</h1>"]

# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return [b'<h1>Hello, web!</h1>']

# httpd = make_server('', 8000, application)
# print("Serving HTTP on port 8000...")
# httpd.serve_forever()

# from wsgiref.simple_server import make_server
# from hello import application

# httpd = make_server("", 8000, application)
# print("Serving HTTP on port 8000...")
# httpd.serve_forever()

# from flask import Flask
# from flask import request

# app = Flask(__name__)

# @app.route("/", methods=['GET'])
# def home():
# 	return '''<form action="/" method="post">
# 			  <p>Home: <input name="homename"></p>
# 			  <p><button type="submit">Sign In</button></p>
# 			  </form>'''
# 	# return '''<form action='/' method="post">
# 	# 	  <p><input name="homename"></p>
# 	# 	  <p><button type="submit">Sign In</button></p>
# 	# 	  </form>'''

# @app.route("/", methods=['POST'])
# def home_post():
# 	if request.form['homename'].lower() == "xun":
# 		return '<h1>Success</h1>'
# 	else:
# 		return '<h1>Not Good!</h1>'

# @app.route('/signin', methods=['GET'])
# def signin_form():
# 	return '''<form action='/signin' method="post">
# 			  <p><input name="username"></p>
# 			  <p><input name="password" type="password"></p>
# 			  <p><button type="submit">Sign In</button></p>
# 			  </form>'''
# @app.route('/signin', methods=['POST'])
# def signin():
# 	if request.form['username'].lower()=='admin' and request.form['password'].lower()=='password':
# 		return '<h3>Hello, admin!</h3>'
# 	return '<h3>Bad username or password.</h3>'

# if __name__=="__main__":
# 	app.run()


# # @app.route

# # @app.route('/', )

# from flask import Flask
# from flask import request

# app = Flask(__name__)


# @app.route("/", methods=["GET"])
# def Home():
# 	return '<h1>Welcome Web!</h1>'

# @app.route('/signin', methods=["GET"])
# def signin():
# 	return '''
# 	<form action='/signin' method="post">
# 	<p>Username: <input name="username"></p>
# 	<p>Password: <input name="password" type="password"></p>
# 	<p><button type="submit">Sign In</button></p>
# 	</form>'''

# @app.route('/signin', methods=["POST"])
# def signPost():
# 	if request.form['username'] == 'admin' and request.form['password'] == 'password':
# 		return '<h1>Success</h1>'
# 	return '<h1>Can not access</h1>'

# if __name__=="__main__":
# 	app.run()


# from flask import Flask, request, render_template

# app = Flash(__name__)


# @app.route('/', methods=['GET', 'POST'])
# def home():
# 	return render_template('home.html')

# @app.route('/signin', methods=['GET'])
# def signin_form():
# 	return render_template('form.html')

# @app.route('/signin', methods=['POST'])
# def signin():
# 	username = request.form['username']
# 	password = request.form['password']
# 	if username == 'admin' and password == 'password':
# 		return render_template('signin-ok.html', username=username)
# 	return render_template('form.html', message='Bad username or password', username=username)

# if __name__=='__main__':
# 	app.run()


# def customer():
# 	r = ""
# 	print("Customers are comming....")
# 	while True:
# 		n = yield r
# 		print("swith")
# 		if not str(n):
# 			return
# 		print('[Consuming...%d]' % n)
# 		r = "Git Perforce OK"

# def producer(c):
# 	c.send(None)
# 	n = 0
# 	while n < 5:
# 		print('[Producing...%d]' % n)
# 		k = c.send(n)
# 		print('[local consumming %s]' % k)
# 		n = n + 1
# 	c.close()

# if __name__ == "__main__":
# 	c = customer()
# 	producer(c)

# import asyncio

# @asyncio.coroutine
# def hello():
# 	print("Hello World!")
# 	# r = yield from aysncio.sleep(1)
# 	r = yield from asyncio.sleep(1)
# 	print("Hello Again! %s" % r)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()

# import asyncio

# @asyncio.coroutine
# def hello():
# 	pritn("Hello WOrld!")
# 	r = yield from asyncio.sleep(1)
# 	print("Hello Again!" % r)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()

# import threading
# import asyncio

# @asyncio.coroutine
# def hello():
# 	print("Hello World! (%s)" % threading.currentThread())
# 	yield from asyncio.sleep(1)
# 	print("Hello Again! (%s)" % threading.currentThread())

# loop = asyncio.get_event_loop()
# task = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# import asyncio

# @asyncio.coroutine
# def hello():
# 	print("Hello World!")
# 	r = yield from asyncio.sleep(1)
# 	print("Hello again!")

# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()

import threading
import asyncio

@asyncio.coroutine









