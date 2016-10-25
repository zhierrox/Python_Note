# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-

# ' a test module '

# __author__ = 'Xun Zou'

# # import sys

# # def test():
# #     args = sys.argv
# #     print args
# #     if len(args)==1:
# #             print('Hello, world!')
# #     elif len(args)==2:
# #         print('Hello, %s!' % args[1])
# #     else:
# #         print('Too many arguments!')

# # if __name__=='__main__':
# #     test()

# # class Student(object):

# # 	__slots__ = ("name", "score", "height", "sex")

# # 	def __init__(self, name, score):
# # 		self.__name = name
# # 		self.__score = score
# # 	def __len__(self):
# # 		return 100
# # 	def print_score(self):
# # 		print self.__name
# # 		print self.__score
# # 	def print_good(self):
# # 		print "good"

# # class Highschool(Student):



# # 	__slots__ = ("name", "score", "sex")

# # 	def __init__(self, name, score):
# # 		self.__name = name
# # 		self.__score = score

# # 	def print_score(self):
# # 		print "Highschood" + self.__name
# # 		print "Highschood" + self.__score

# # 	def print_name(self):
# # 		print self.__name

# # class T(object):
# # 	def __init__(self):
# # 		pass
	
# # 	def print_score(self):
# # 		print "test"


# # # def display(s):
# # # 	s.print_score()

# # def set_age(self, age):
# # 	self.age = age

# # class Student(object):
# #     __slots__ = ('name', 'age') 
    
# #     def __init__(self, name, age):
# #     	self.name = name
# #     	self.age = age

# # class Classmate(Student):

# # 	def __init__(self, name, age, Gener):
# # 		Student.__init__(self, name, age)
# # 		self.Gener = Gener

# # 	__slots__ = ('Gener')
# # 	pass

# # 	@property
# # 	def score(self):
# # 		return self.__score

# # 	@score.setter
# # 	def score(self, value):
# # 		if not isinstance(value, int):
# # 			raise ValueError('score must be an integer')
# # 		if value < 0 or value > 100:
# # 			raise ValueError('score must between 0 ~ 100 !')
# # 		self.__score = value

# # 	@property
# # 	def birth(self):
# # 	    return self.__birth

# # 	@birth.setter(self, value):
# # 		self.__birth = value

# # 	@property
# # 	def age(self):
# # 	    return 2015 - self.__birth


# # class Screen(object):
	
# # 	@property
# # 	def width(self):
# # 		return self.__width

# # 	@width.setter
# # 	def width(self, value):
# # 		self.__width = value

# # 	@property
# # 	def height(self):
# # 	    return self.__height

# # 	@height.setter
# # 	def height(self, value):
# # 		self.__height = value


# # 	@property
# # 	def resolution(self):
# # 	    return self.__width * self.__heig
	
# # class Animal(object):
# # 	pass

# # class Mammal(Animal):
# # 	pass

# # class Bird(Animal):
# # 	pass

# # class Dog(Mammal):
# # 	pass

# # class Bat(Mammal):
# # 	pass

# # class Parrot(Bird):
# # 	pass

# # class Ostrich(Bird):
# # 	pass

# # class Runnable(object):
# # 	def run(self):
# # 		print('Running...')

# # class Flyable(object):
# # 	def fly(self):
# # 		print("Flying")

# # class MyTCPServer(TCPServer, ForkingMixIn):
# # 	pass

# # class MyUDPServer(UDPServer, ThreadingMixIn):
# # 	pass

# # class Student(object):
# # 	def __init__(self, name):
# # 		self.name = name
# # 	def __str__(self):
# # 		return "Student object (name=%s)" % self.name
# # 	__repr__ = __str__

# # class Fib(object):
# # 	def __init__(self):
# # 		self.a ,self.b = 0, 1

# # 	def __iter__(self):
# # 		return self

# # 	def __next__(self):
# # 		self.a, self.b = self.b, self.a + self.b
# # 		if self.a > 100000:
# # 			raise StopIteration();
# # 		return self.a

# # 	def __getitem__(self, n):
# # 		a, b = 1, 1
# # 		for x in range(n):
# # 			a, b = b, a + b
# # 			return a 

# # class Fib(object):
# # 	def __getitem__(self, n):
# # 		if isinstance(n, int):
# # 			a, b = 1, 1
# # 			for x in range(n):
# # 				a, b = b, a + b
# # 			return a
# # 		if isinstance(n, slice):
# # 			start = n.start
# # 			stop = n.stop
# # 			if start is None:
# # 				start = 0
# # 			a, b = 1, 1
# # 			L = []
# # 			for x in range(stop):
# # 				if x >= start:
# # 					L.append(a)
# # 				a, b = b, a + b
# # 			return L

# # class Student(object):


# # 	def __init__(self):
# # 		self.name = 'Michael'

# # 	def __getattr__(self, attr):
# # 		if attr == "age":
# # 			return 99


# # class Student(object):

# # 	def __getattr__(self, attr):
# # 		if attr == 'age':
# # 			return lambda: 25


# # class Student(object):

# # 	def __getattr__(self, attr):
# # 		if attr == 'age':
# # 			return lambda: 25
# # 		raise AttributeError('\'Student\' object  has no attribute \'%s\'' % attr)


# # class Chain(object):

# # 	def __init__(self, path):
# # 		self.path = path

# # 	def __getattr__(self, path):
# # 		return Chain("%s/%s", self.path, path)

# # 	def __str__(self):
# # 		return self._path

# # 	__repr__ = __str__

# # class Student(object):
	
# # 	def __init__(self, name):
# # 		self.name = name

# # 	def __call__(self, age):
# # 		s = "%s is good %s" % (self.name, age)
# # 		return s

# class Chain(object):

# 	def __init__(self, path = ""):
# 		self.__path = path

# 	def __getattr__(self, path):
# 		print 'call __getattr__ (%s)' % path
# 		return Chain('%s%s' % (self.__path, path))

# 	def __str__(self):
# 		return self.__path

# 	def __call__(self, param):
# 		print "call __call__(%s)" % param
# 		return Chain("%s%s" % (self.__path, param)

# 	__repr__ = __str__

# from enum import Enum, unique

# @unique
# class Weekday(Enum):
# 	sum = 0
# 	sat = 6


# from enum import Enum

# Month = Enum("Month", ("Jan", "Feb", "Dec"))
# for name, member in Month.__members__.items():
# 	print(name, "=>", member.value)

# from enum import Enum, unique

# @unique
# class Weekday(Enum):
# 	sun = 0


# # class ListMetaclass(type):
# # 	def __new__(cls, name, bases, attrs):
# # 		attrs['add'] = lambda self, value: self.append(value)
# # 		return type.__new__(cls, name, bases, attrs)

# # class MyList(list, metaclass=ListMetaclass)


# # class User(Model):
# # 	id = IntergerField("id")
# # 	name = StringField("Username")
# # 	email = StringField("email")
# # 	password = StringField("password")

# # u = User(id=12345, name="Michael", email="test@orm.org", password="my-pwd")

# # u.save()

# class Field(object):

# 	def __init__(self, name, column_type):
# 		self.name = name
# 		self.column_type = column_type

# 	def __str__(self):
# 		return '<%s:%s>' % (self.__class__.__name__, self.name)

# class StringField(Field):
# 	def __init__(self, name):
# 		super(StringField, self).__init__(name, "varchar(100)")

# class IntegerField(Field):
# 	def __init__(self, name):
# 		super(IntegerField, self).init(name, 'bigint')

# class ModelMetaclass(type):

# 	def __new__(cls, name, bases, attrs):
# 		if name==="Model":
# 			return type.__new__(cls, name, bases, attrs)
# 		print("Found model: %s" % name)
# 		mappings = dict()
# 		for k, v in attrs.items():
# 			if isinstance(v, Field):
# 				print("Found mapping: %s ==> %s" % (k, v))
# 				mappings[k] = v
# 		for k in mappings.keys():
# 			attrs.pop(k)
# 		attrs["__mappings__"] = mappings
# 		attrs["__table__"] = name
# 		return type.__new__(cls, name, bases, attrs)

# class ModelMetaclass(type):

# 	def __new__(cls, name, bases, attrs):
# 		if name=="Model":
# 			return type.__new__(cls, name, bases, attrs)
# 		print ("Found model: %s" % name)
# 		mappings = dict()
# 		for k, v in attrs.items():
# 			if isinstance(v, Field):
# 				print ("Found mapping: %s ==> %s" % (k, v))
# 				mappings[k] = v
# 		for k in mappings.keys():
# 			attrs.pop(k)
# 		attrs["__mappings__"] = mappings
# 		attrs["__table__"] = name
# 		return type.__new__(cls, name, bases, attrs)

# class Model(dict, metaclass=ModelMetaclass):

# 	def __init__(self, **kw):
# 		super(Model, self).__init__(**kw)

# 	def __getattr__(self, key):
# 		try:
# 			return self[key]
# 		except KeyError:
# 			raise AttributeError(r"'Model object has no attribute '%s'" % key)

# 	def __setattr__(self, key, value):
# 		self[key] = value

# 	def save(self):
# 		fields = []
# 		params = []
# 		args = []
# 		for k, v in self.__mappings__.items:
# 			fields.append(v.name)
# 			params.append('?')
# 			args.append(getattr(self, k, None))
# 		sql = 'insert into %s (%s) values (%s)' % (self.__table, ','.join(fields), ",".join(params))
# 		print("SQL: %s" % sql)
# 		print("ARGS: %s" % str(args))

# class User(Model):
# 	id = IntegerField("id")
# 	name = StringField("username")
# 	email = StringField("email")
# 	password = StringField('password')

# u = User(id=12345, name="Michael", email="test@orm.org", password="my-pwd")
# u.save

# class Field(object):

# 	def __init__(self, name, column_type):
# 		self.name = name
# 		self.column_type = column_type

# 	def __str__(self):
# 		return '<%s:%s>' % (self.__class__.__name__, self.name)

# class StringFied(Field):

# 	def __init__(self, name):
# 		super(StringFied, self).__init__(name, "varchar(100)")

# class IntergerField(Field):

# 	def __init__(self, name):
# 		super(IntergerField, self).__init__(name, 'bigint')

# class ModelMetaclass(type):
# 	if name=="Model":
# 		return type.__new__(cls, name, bases, attrs)
# 	print("Found model: %s" % name)
# 	mappings = dict()
# 	for k, v in attrs.items():
# 		if isinstance(v, Field):
# 			print("Found mapping: %s ==> %s" % (k, v))
# 			mappings[k] = v
# 	for k in mappings.keys():
# 		attrs.pop(k)
# 	attrs["__mappings__"] = mappings
# 	attrs["__table__"] = name
# 	return type.__new__(cls, name, bases, attrs)

# class Model(dict, metaclass=ModelMetaclass):

# 	def __init__(self, **kw):
# 		super(Model, self).__init__(**kw)

# 	def __getattr__(self, key):
# 		try:
# 			return self[key]
# 		except KeyError:
# 			raise AttributeError(r"'Model' object has no attribute '%s'" % key)

# 	def __setattr__(self, key, value):
# 		self[key] = value

# 	def save(self):
# 		fields = []
# 		params = []
# 		args = []

# 		for k, v in self.__mappings__.items():
# 			fields.append(v.name)
# 			params.append('?')
# 			args.append(getattr(self, k, None))
# 		sql = "insert into %s (%s) values (%s) % (self.__table__, ",".join(fields), ",".join(params))"
# 		print("SQL: %s" % sql)
# 		print("ARGS: %s" % str(args))

# class  Uber(Model):
	
# 	if = IntergerField("id")
# 	name = StringField("username")
# 	email = StringField("email")
# 	password = StringField("password")

# u = User(id=123456, name="Michael", email="test@orm.org", password="my-pwd")
# u.save()

# class Field(object):

# 	def __init__(self, name, column_type):
# 		self.name = name
# 		self.column_type = column_type

# 	def __str__(self):
# 		return "<%s:%s>" % (self.__class__.__name__, self.name)

# class StringField(Field):

# 	def __init__(self, name):
# 		super(StringField, self).__init__(name, "varchar(100)")

# class IntegerField(Field):
# 	def __init__(self, name):
# 		super(IntegerField, self).__init__(name, "bigint")


# class ModelMetaclass(type):

# 	def __new__(cls, name, bases, attrs):
# 		if name=="Model":
# 			return type.__new__(cls, name, bases, attrs)
# 		print("Found model: %s" % name)
# 		mappings = dict()
# 		for k, v in attrs.items():
# 			if isinstance(v, Field):
# 				print("Found mapping: %s ==> %s" % (k, v))
# 				mappings[k] = v
# 		for k in mappings.keys():
# 			attrs.pop(k)
# 		attrs["__mappings__"] = mappings
# 		attrs["__table__"] = name
# 		return type.__new__(cls, name, bases, attrs)

# class Model(dict, metaclass=ModelMetaclass):

# 	def __init__(self, **kw):
# 		super(Model, self).__init__(**kw)

# 	def __getattr__(self, key):
# 		try:
# 			return self[key]
# 		except KeyError:
# 			raise AttributeError(r"'Model' object has no attribute '%s'"% key)

# 	def __setattr__(self, key, value):
# 		self[key] = value

# 	def save(self):
# 		fields = []
# 		params = []
# 		args = []

# 		for k, v in self.__mappings__.items():
# 			fields.append(v.name)
# 			params.append("?")
# 			args.append(getattr(self, k, None))
# 		sql = "insert into %s (%s) values (%s)" % (self.__table__, ",".join(fileds), ",".join(params))
# 		print("SQL: %s" % sql)
# 		print("ARGS: %s" % str(args))


# def foo():
# 	r = some_function()
# 	if r==(-1):
# 		return (-1)
# 	return r

# def bar():
# 	r = foo()
# 	if r==(-1):
# 		print("Error")
# 	else:
# 		pass

# try:
# 	print（"try..."）
# 	r = 10 / 0
# 	print("result", r)
# except ZeroDivisionError as e:
# 	print("except:", e)
# finally:
# 	print("finally...")
# print("END")

# try:
# 	print("try...")
# 	r = 10 / int('a')
# 	print("result:", r)
# except ValueError as e:
# 	print("ValueError:", e)
# except ZeroDivisionError as e:
# 	print("ZeroDivisionError:", e)
# finally:
# 	print("finally...")
# print("END")

# try:
# 	print("try...")
# 	r = 10 / int('2')
# 	print('result:', r)
# except ValueError as e:
# 	print("ValueError:", e)
# except ZeroDivisionError as e:
# 	print("ZeroDivisionError:", e)
# else:
# 	print("no error!")
# finally:
# 	print("finally...")
# print("END")

# # err.py
# def foo(s):
# 	return 10 / int(s)

# def bar(s):
# 	return foo(s) * 2

# def main():
# 	bar("0")


# import logging

# def foo(s):
# 	return 10 / int(s)

# def bar(s):
# 	return foo(s) * 2

# def main():
# 	try:
# 		bar("0")
# 	except Exception as e:
# 		logging.exception(e)


# # err_raise.py

# class FooError(ValueError):
# 	pass

# def foo(s):
# 	n = int(s)
# 	if n==0:
# 		raise FooError("invalid value: %s" % s)
# 	print "interrupt"
# 	print 10 / n
# foo("1")

# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n

# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise
#     finally:
#     	print('Good')

# bar()

# def foo(s):
# 	n = int(s)
# 	print ('>>> n = %d' % n)
# 	return 10 / n

# def main():
# 	foo('0')

# main()

# def foo(s):
# 	n = int(s)
# 	assert n != 0, "n is zero!"
# 	return 10 / n

# def main():
# 	foo("0")

# main()

# python3 -0 err.py

# import logging
# logging.basicConfig(level=logging.WAENING)


# s = "0"
# n = int(s)
# # logging.info("n = %d" % n)
# # logging.warning
# # logging.debug("n = %d" % n)
# print(10 / n)

# import pdb

# s = "1"
# pdb.set_trace()
# n = int(s)
# pdb.set_trace()
# print(10 / n)

# class Dict(dict):

# 	def __init__(self, **kw):
# 		super().__init__(**kw)

# 	def __getattr__(self, key):
# 		try:
# 			reutrn self[key]
# 		except KeyError:
# 			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

# 	def __setattr__(self, key, value):
# 		self[key] = value

# import unittest

# from mydict import Dict


# class TestDict(unittest.TestCase):

# 	def test_init(self):
# 		d = Dict(a=1, b="test")
# 		self.assertEqual(d.a, 1)
# 		self.assertEqual(d.b, 'test')
# 		self.assertTrue(isinstance(d, dict))

# 	def test_key(self):
# 		d = Dict()
# 		d["key"] = "value"
# 		self.assertEqual(d.key, "value")

# 	def test_attr(self):
# 		d = Dict()
# 		d.key = "value"
# 		self.assertTrue('key' in d)
# 		self.assertEqual(d["key"], "value")

# 	def test_keyerror(self):
# 		d = Dict()
# 		with self.assertRaises(KeyError):
# 			value = d['empty']

# 	def test_attrerror(self):
# 		d = Dict()
# 		with self.assertRaises(AttributeError):
# 			value = d.empty

# def abs(n):
# 	'''
# 	Function to get absolute value of number.

# 	Example:
# 	>>>abs(1)
# 	1
# 	>>>abs(-1)
# 	1
# 	>>>abs(0)
# 	0
# 	'''

# # mydict2.py
# class Dict(dict):
# 	'''
# 	Simple dict but also support access as x.y style

# 	>>> d1 = Dict()
# 	>>> d1['x'] = 100
# 	>>> d1.x
# 	100
# 	>>> d1.y = 200
# 	>>> d1['y']
# 	200
# 	>>> d2 = Dict(a=1, b=2, c="3")
# 	>>> d2.c
# 	'3'
# 	>>> d2['empty']
# 	Traceback (most recent call last):
# 		...
# 	KeyError: 'empty'
# 	>>> d2.empty
# 	Traceback (most recent call last):
# 		...
# 	AttributeError: 'Dict' object has no attribute 'empty'
# 	'''

# 	def __init__(self, **kw):
# 		super(Dict, self).__init__(**kw)

# 	def __getattr__(self, key):
# 		try:
# 			return self[key]
# 		except KeyError:
# 			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

# 	def __setattr__(self, key, value):
# 		self[key] = value

# if __name__=="__main__":
# 	import doctest
# 	doctest.testmod()

# f = open("/User/test.txt", "r")

# f.read()

# f.close()

# try:
# 	f = open("/path/to/file", "r")
# 	print(f.read())
# finally:
# 	if f:
# 		f.close()

# with open("/path/to/file", "r") as f:
# 	print(f.read())

# f = open("/Users/test.jpg", "rb")
# f = read()

# f = open("/Users/gbk.txt", "r", encoding="gbk")
# f.read()


# f = open("/Users/michael/test.txt", "w")
# f.write("Hello, World!")
# f.close()

# with open("/User/test.txt", "wb") as f:
# 	f.write("Hello")



# with open("/User/test.txt", "rb") as f:
# 	print f.readlines() 

# from io import StringIO

# f = StringIO()
# f.write("Hello")
# print(f.getvalue())

# from io import StringIO

# f = StringIO("Hello\nHi!\nGoodbye")

# while True:
# 	f.readline()
# 	if s == "":
# 		break
# 	print (s.strip())

# from io import BytesIO

# f = BytesIO()
# f.write("中文".encode('utf-8'))

# print(f.getvalue())


# from io import BytesIO
# f = BytesIO('中文'.encode("utf-8"))
# print f.read()


# import os
# print(os.getcwd())


# def main():
# 	for root, dirs, files in os.walk(r'C:\Users\502618456\Desktop\UserGuid_ScreenShot\testpython'):
# 		# for dir in dirs:
# 		# 	if dir==".git":
# 		# 		print os.path.join(root, dir)
# 			# print dir
# 			# print(os.path.join(root, dir))
# 		for file in files:
# 			# print file.split(".")[0]
# 			if "ss" in file.split(".")[0]:
# 				print(os.path.join(root, file))

# if __name__=="__main__":
# 	main()

# import pickle


# def main():
# 	for root, dirs, files in os.walk(r'C:\Users\502618456\Desktop\UserGuid_ScreenShot\testpython'):
		# for dir in dirs:
		# 	if dir==".git":
		# 		print os.path.join(root, dir)
			# print dir
			# print(os.path.join(root, dir))

# import sys
# import commands
# import re
# import json
# import urllib
# import subprocess
# import os
# import platform

# def getWorkspaceList(searchDirectory):
# 		# raise Exception("Not implemented")
# 		lwsp_list = []
# 		if searchDirectory is None:
# 			sysstr = platform.system()

# 			if sysstr.lower() =="windows":
# 				# Get all drive in local Windows
# 				drivelist = subprocess.Popen('wmic logicaldisk get name,description', shell=True, stdout=subprocess.PIPE)
# 				drivelisto, err = drivelist.communicate()
# 				driveLines = drivelisto.split('\n')
# 				drives = []
# 				drive = ''
# 				# ['Local Fixed Disk         D:    \r\r']
# 				pathLine = re.compile('^[\s]*[Ll]ocal[\s]*[Ff]ixed[\s]*[Dd]isk[\s]*([a-zA-Z\_][0-9a-zA-Z\_]*:)[\s]*[\r][\r]$')
# 				for driveLine in driveLines:
# 					line = pathLine.search(driveLine)
# 					if line:
# 						drive = line.group(1)
# 						drives.append(drive + "\\")
# 				# Get all git repository on whole system
# 				for drive in drives:
# 					for root, dirs, files in os.walk(drive):
# 						if ".git" in dirs:
# 							# Process root path case, such as: C:\\.git, it should be C: :C:
# 							if os.path.split(root.strip())[1] == "":
# 								lwsp_list.append(os.path.split(root.strip())[0] + ": " + root)
# 							else:
# 								lwsp_list.append(os.path.split(root.strip())[1] + ": " + root)
# 				return lwsp_list

# 			elif sysstr.lower() == "linux":
# 				drives = ["/root", "/home", "/workspaces"]
# 				for drive in drives:
# 					for root, dirs, files in os.walk(drive):
# 						if ".git" in dirs:
# 							lwsp_list.append(os.path.split(root.strip())[1] + ": " + root)
# 				return lwsp_list
# 			else:
# 				return None
# 		else:
# 			for root, dirs, files in os.walk(searchDirectory):
# 				if ".git" in dirs:
# 					lwsp_list.append(os.path.split(root.strip())[1] + ": " + root)
# 			return lwsp_list


# if __name__ == "__main__":
# 	# sd1 = r"C:\Users\502618456\Desktop"
# 	# print getWorkspaceList(sd1)
# 	sd2 = None
# 	print getWorkspaceList(sd2)
# 	# sd3 = "c:\\"
# 	# print getWorkspaceList(sd3)

# # <type 'list'>: ['new-repo: C:\\Users\\502618456\\AppData\\Local\\GitHub\\TutorialRepository_d0aa732a2b4666b3029e2320f1a06cd39e99c9fc\\new-repo', 'git_remote_test: C:\\Users\\502618456\\Desktop\\GE-GIT\\git_remote_test', 'remote_path_test: C:\\Users\\502618456\\Desktop\\GE-GIT-03\\remote_path_test', 'getFullPath: C:\\Users\\502618456\\Desktop\\GE_Full_Path\\getFullPath', 'git_test: C:\\Users\\502618456\\Desktop\\gitConnection\\git_test', 'git_remote_test: C:\\Users\\502618456\\Desktop\\git_remote_test', 'Git_Repo: C:\\Users\\502618456\\Desktop\\Git_Repo', 'mygitworkspace: C:\\Users\\502618456\\Desktop\\Git_Repo\\mygitworkspace', 'test_SpecFlow_Trx_Data: C:\\Users\\502618456\\Desktop\\Git_Repo\\test_SpecFlow_Trx_Data', 'Git_Test_Repo: C:\\Users\\502618456\\Desktop\\Git_Test_Repo', 'mygitworkspace: C:\\Users\\502618456\\Desktop\\mygitworkspace', 'Git_Remote_Test: C:\\Users\\502618456\\Desktop\\mygitworkspace\\Git_Remote_Test', 'Git_Test: C:\\Users\\502618456\\Desktop\\mygitworkspace\\Git_Test', 'my_git_test: C:\\Users\\502618456\\Desktop\\my_git_test', 'git_remote_test: C:\\Users\\502618456\\Desktop\\my_git_test\\git_remote_test', 'GE-GIT-02: C:\\Users\\502618456\\Desktop\\New folder\\GE-GIT-02', 'remote_path_test: C:\\Users\\502618456\\Desktop\\New folder\\GE-GIT-02\\remote_path_test', 'visual_git: C:\\Users\\502618456\\Documents\\GitHub\\visual_git', 'gehc-uom-services-bdd: C:\\XunZouWorkspace\\GitHub_Features\\gehc-uom-services-bdd']

# {'changeTime': 'N/A', 
# 'url': 'https://github.build.ge.com/healthcloud/gehc-uom-services-bdd/blob/master/src/main/resources/features/UserRegistry/ActivateUser.feature', 
# 'preMoveChangelist': 'N/A', 
# 'changelist': '0c98673f475f446d9c15ef77b041af757b1d3016', 
# 'localPath': 'C:\\XunZouWorkspace\\GitHub_Features\\gehc-uom-services-bdd\\src\\main\\resources\\features\\UserRegistry\\ActivateUser.feature', 
# 'hasChanged': 'N/A', 
# 'oldChange': '8c3901354a50716163a5e0d76fa0ef342ab485f4', 
# 'depotPath': 'https://github.build.ge.com/healthcloud/gehc-uom-services-bdd/blob/master/src/main/resources/features/UserRegistry/ActivateUser.feature', 
# 'preMovePreChangelist': 'N/A', 
# 'changeAction': 'N/A', 
# 'revisionNumber': '99ae849'}

# {'changeTime': 'N/A',
# 						   'preMoveChangelist': 'N/A',
# 						   'changelist': '0c98673f475f446d9c15ef77b041af757b1d3016',
# 						   'localPath': '/root/Desktop/gehc-uom-services-bdd/src/main/resources/features/UserRegistry/ActivateUser.feature',
# 						   'hasChanged': 'N/A', 'oldChange': '8c3901354a50716163a5e0d76fa0ef342ab485f4',
# 						   'depotPath': 'https://github.build.ge.com/healthcloud/gehc-uom-services-bdd/blob/master/src/main/resources/features/UserRegistry/ActivateUser.feature',
# 						   'preMovePreChangelist': 'N/A', 'changeAction': 'N/A', 'revisionNumber': '99ae849'
# 						   }

# # GitHub implementation
# class GitHub:
# 	# Initialize the object. Internal code to the interface.
# 	def __init__(self):
# 		self.ready = True # After initilization, try to connect and login


# 	# Connect the object to the version control system
# 	# Returns: True for success, False for failure
# 	def connect(self):
# 		# raise Exception("Not implemented")
# 		##
# 		return True

# 	# Disconnect the object from the version control system
# 	# Returns: True for success, False for failure
# 	def disconnect(self):
# 		return True


# 	# Login to the version control system using the user specified credentials
# 	# Returns: True for success, False for failure
# 	def login(self):
# 		# raise Exception("Not implemented")
# 		return True

# 	# Set the version control system to use the local workspace specified by the user
# 	# Returns: True for success, False for failure
# 	def setLocalWorkspace(self, configDict):
# 		# raise Exception("Not implemented")

# 		foundWorkspace = False
# 		localWorkspaceName = configDict["workspacename"]
# 		localWorkspacePath = configDict["workspacepath"]
# 		configDict['startingdirectoryvcs'] = "VCS workspace mapping not found"
# 		tempName = ''
# 		tempList = []

# 		# should be add exception process. Write debug log
# 		# Need next step format input
# 		# and localWorkspacePath.strip()[-1] != "\\" and localWorkspacePath.strip()[-1] != "/"
# 		if self.exist_path(localWorkspacePath):
# 			if self.exist_git_dir(localWorkspacePath):
# 				sysstr = platform.system()
# 				if sysstr.lower() == "windows":
# 					tempList = localWorkspacePath.strip().split("\\")
# 					if tempList[-1] == "":
# 						tempName = tempList[-2]
# 					else:
# 						tempName = tempList[-1]

# 				elif sysstr.lower() == "linux":
# 					if localWorkspacePath.strip() == "/":
# 						tempName = "/"
# 					else:
# 						tempList = localWorkspacePath.strip().split("/")
# 						if tempList[-1] == "":
# 							tempName = tempList[-2]
# 						else:
# 							tempName = tempList[-1]
# 				else:
# 					# print "Do not support %s" % sysstr
# 					return False
# 				if tempName == localWorkspaceName:
# 					configDict['startingdirectoryvcs'] = self.getRemoteGHWorkSpace(localWorkspacePath)
# 					return True
# 				else:
# 					return False
# 			else:
# 				return False
# 		else:
# 			return False
# 		## AFTER validate
# 		# configDict['startingdirectoryvcs'] = self.getRemoteGHWorkSpace(localWorkspacePath)
# 		## step1: Checke  localWorkspaceName and localWorkspacePath valid path, actual path


# 	# Get metadata from the version control system for a specified file
# 	def getVCmetadata(self, file):
# 		# raise Exception("Not implemented")
# 		depotData = {}

# 		commit_id = ""
# 		revision_id = ""
# 		oldChange_id = ""
# 		fileName = ""
# 		reposPath = ""
# 		remotePath = ""


# 		sysstr = platform.system()
# 		if sysstr.lower() == "windows":
# 			fileName = file.strip().split("\\")[-1]
# 			reposPath = file.strip()[:-(len(fileName)+1)]

# 		elif sysstr.lower() == "linux":
# 			fileName = file.strip().split("/")[-1]
# 			reposPath = file.strip()[:-(len(fileName)+1)]
# 		else:
# 			print "Do not support %s" % sysstr
# 			# Write debug log at here

# 		commit_id, revision_id, oldChange_id = self.gitLogParserIndexID(reposPath, fileName)
# 		# remotePath = self.getRemoteGHWorkSpace(reposPath)
# 		remotePath = self.getFileAbsoluteURL(file)

# 		depotData['revisionNumber'] = revision_id	# Need Current revison
# 		depotData['depotPath'] = remotePath		# Need remote path
# 		depotData['localPath'] = file # Need  have done
# 		depotData['changelist'] = commit_id # Need Current commit id
# 		depotData['changeTime'] = "N/A" # Do not need
# 		depotData['changeAction'] = "N/A" # Do not need
# 		depotData['hasChanged'] = "N/A" # Do not need
# 		depotData['oldChange'] = oldChange_id # Need previous commit id
# 		depotData['preMoveChangelist'] = "N/A" # Do not need
# 		depotData['preMovePreChangelist'] = "N/A" # Do not need

# 		return depotData


# 	def getWorkspaceList(self, searchDirectory):
# 		# raise Exception("Not implemented")
# 		lwsp_list = []
# 		if searchDirectory is None:
# 			sysstr = platform.system()

# 			if sysstr.lower() == "windows":
# 				# Get all drive in local Windows
# 				drivelist = subprocess.Popen('wmic logicaldisk get name,description', shell=True,
# 											 stdout=subprocess.PIPE)
# 				drivelisto, err = drivelist.communicate()
# 				driveLines = drivelisto.split('\n')
# 				drives = []
# 				drive = ''
# 				# ['Local Fixed Disk         D:    \r\r']
# 				pathLine = re.compile(
# 					'^[\s]*[Ll]ocal[\s]*[Ff]ixed[\s]*[Dd]isk[\s]*([a-zA-Z\_][0-9a-zA-Z\_]*:)[\s]*[\r][\r]$')
# 				for driveLine in driveLines:
# 					line = pathLine.search(driveLine)
# 					if line:
# 						drive = line.group(1)
# 						drives.append(drive + "\\")
# 				# Get all git repository on whole system
# 				for drive in drives:
# 					for root, dirs, files in os.walk(drive):
# 						if ".git" in dirs:
# 							# Process root path case, such as: C:\\.git, it should be C: :C:
# 							if os.path.split(root.strip())[1] == "":
# 								lwsp_list.append(os.path.split(root.strip())[0] + ": " + root)
# 							else:
# 								lwsp_list.append(os.path.split(root.strip())[1] + ": " + root)
# 				return lwsp_list

# 			elif sysstr.lower() == "linux":
# 				drives = ["/root", "/home", "/workspaces"]
# 				for drive in drives:
# 					for root, dirs, files in os.walk(drive):
# 						if ".git" in dirs:
# 							lwsp_list.append(os.path.split(root.strip())[1] + ": " + root)
# 				return lwsp_list
# 			else:
# 				return None
# 		else:
# 			for root, dirs, files in os.walk(searchDirectory):
# 				if ".git" in dirs:
# 					lwsp_list.append(os.path.split(root.strip())[1] + ": " + root)
# 			return lwsp_list

# 	# # Get a list of available workspaces for the user to select from
# 	# def getWorkspaceList(self):
# 	# 	# raise Exception("Not implemented")
# 	# 	sysstr = platform.system()
# 	#
# 	# 	if sysstr.lower() =="windows":
# 	# 		return self.getLocalGHWorkSpaceWin()
# 	# 	elif sysstr.lower() == "linux":
# 	# 		return self.getLocalGHWorkSpaceNix()
# 	# 	else:
# 	# 		return None
# 	# 	# print "Do not support %s" % sysstr
# 	# 	#  logs.debuglog()


#  	# Get GE GitHub base URL
# 	def getURLBase(self):
# 		# github.build.ge.com:443
# 		# return customization.getCustomizationValue("GitHubBase")
# 	    return ""


# 	# Return whether the object is ready for usage
# 	def isReady(self):
# 		return self.ready

# 	# Get current Commit ID, current revision ID, and the oldChange commit id.
# 	def gitLogParserIndexID(self, reposPath, fileName):
# 		"""
# 		This method can parse git log --follow -p and return a json object.
# 		:param reposPath str :
# 			   fileName  str :
# 		:returns: dict
# 		"""
# 		app_path = ''
# 		sysstr = platform.system()
# 		if  sysstr.lower() == "windows":
# 			if reposPath.strip()[-1] != "\\":
# 				app_path = "\\"
# 		elif  sysstr.lower() == "linux":
# 			if reposPath.strip()[-1] != "/":
# 				app_path = "/"
# 		else:
# 			# Write debug log here
# 			print "Do not support %s" % sysstr

# 		p_commits   = re.compile('^commit ', re.MULTILINE)
# 		p_index     = re.compile('^index[\s]*([0-9a-zA-Z]+)([\.]*)([0-9a-zA-Z]+)([\n\s]*)(.*)$')
# 		pr = subprocess.Popen( "git log --follow -p " + fileName, cwd = os.path.dirname(reposPath + app_path), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
# 		(out, error) = pr.communicate()
# 		if str(error) == '':
# 			stdin = str(out)
# 		else:
# 			stdin = str(error)
# 		commits = p_commits.split(stdin)
# 		if len(commits) < 2:
# 			print "[error] no log"
# 			sys.exit()
# 		commits.pop(0)
# 		logs = []
# 		for commit in commits:
# 			lines = commit.splitlines()
# 			commit_id = lines.pop(0)
# 			index   = ""
# 			for line in lines:
# 				m_index     = p_index.search(line)
# 				if m_index:
# 					index = m_index.group(3)
# 			try:
# 				logs.append({
# 					'commit_id': commit_id,
# 					'revision_id': index
# 				})
# 			except:
# 				print '[error] ', sys.exc_info()[0]
# 				sys.exit()
# 		# print json.dumps(logs)
# 		# return json.dumps(logs)
# 		# return logs[0]['commit_id']
# 		# return logs[0]['revision_id']

# 		# return logs[0]['commit_id'], logs[0]['revision_id'], logs

# 		# logs[1] means oldChange commit id.

# 		changelist_commit_id = ""
# 		special_revision_id = ""
# 		oldchange_commit_id = ""

# 		changelist_commit_id = logs[0]['commit_id']
# 		for dict in logs:
# 			if dict['revision_id'].strip() != "":
# 				special_revision_id = dict['revision_id']
# 				break
# 		if special_revision_id == "":
# 			special_revision_id = None
# 		if len(logs) < 2:
# 			oldchange_commit_id = None
# 		else:
# 			oldchange_commit_id = logs[1]['commit_id']

# 		return changelist_commit_id, special_revision_id, oldchange_commit_id
# 		# return logs[0]['commit_id'], logs[0]['revision_id'], logs[1]['commit_id']

# 	# Get all Old Change commit_id
# 	def gitLogParserOldChange(self, reposPath):
# 		"""
# 		This method can parse git log and return a json object.
# 		:param reposPath str :
# 			   fileName  str :
# 		:returns: dict
# 		"""
# 		p_commits   = re.compile('^commit ', re.MULTILINE)
# 		pr = subprocess.Popen( "git log ", cwd = os.path.dirname(reposPath), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
# 		(out, error) = pr.communicate()
# 		if str(error) == '':
# 			stdin = str(out)
# 		else:
# 			stdin = str(error)
# 		commits = p_commits.split(stdin)
# 		if len(commits) < 2:
# 			print "[error] no log"
# 			sys.exit()
# 		commits.pop(0)

# 		logs = []
# 		for commit in commits:
# 			lines = commit.splitlines()
# 			commit_id = lines.pop(0)
# 			try:
# 				logs.append({
# 					'old_change': commit_id,
# 				})
# 			except:
# 				print '[error] ', sys.exc_info()[0]
# 				sys.exit()

# 		# return json.dumps(logs)
# 		return logs


# 	# return GitHub local workspace path list in windows
# 	# lwsp_list = []
# 	# workspace_path_list = []
# 	# workspace_name_list = []
# 	# def getLocalGHWorkSpaceWin(self):
# 	#
# 	# 	# drives = win32api.GetLogicalDriveStrings()
# 	# 	# drives = drives.split('\000')[:-1]
# 	# 	# ASCII \000 is NUL
# 	# 	# # print drives
# 	# 	# example: ['C:\\', 'D:\\']
# 	#
# 	# 	# 'C:\\Users\\502618456\\AppData\\'
# 	# 	# drives = ['C:\\Users\\502618456\\Documents\\']
# 	# 	# drives = ['C:\\Users\\502618456\\Desktop\\']
# 	#
# 	# 	drivelist = subprocess.Popen('wmic logicaldisk get name,description', shell=True, stdout=subprocess.PIPE)
# 	# 	drivelisto, err = drivelist.communicate()
# 	# 	driveLines = drivelisto.split('\n')
# 	# 	drives = []
# 	# 	drive = ''
# 	#
# 	# 	# ['Local Fixed Disk         D:    \r\r']
# 	# 	pathLine = re.compile('^[\s]*[Ll]ocal[\s]*[Ff]ixed[\s]*[Dd]isk[\s]*([a-zA-Z\_][0-9a-zA-Z\_]*:)[\s]*[\r][\r]$')
# 	#
# 	# 	for driveLine in driveLines:
# 	# 		line = pathLine.search(driveLine)
# 	# 		if line:
# 	# 			drive = line.group(1)
# 	# 			drives.append(drive)
# 	#
# 	# 	count = 0
# 	# 	# local_workspace_path
# 	# 	lwsp_list = []
# 	# 	workspace_path_list = []
# 	# 	workspace_name_list = []
# 	#
# 	# 	for drive in drives:
# 	# 		stdin = ''
# 	# 		if os.path.exists(drive):
# 	# 			pr = subprocess.Popen( "dir .git /AD /s" , cwd = os.path.dirname(drive + "\\"), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
# 	# 			(out, error) = pr.communicate()
# 	# 			# if str(error) == '':
# 	# 			# 	stdin = str(out)
# 	# 			# else:
# 	# 			# 	stdin = str(error)
# 	# 			stdin = str(out)
# 	# 			# some directoris have  Permission denied
# 	# 			if str(error) != "":
# 	# 				# need to write error information into debug log
# 	# 				pass
# 	#
# 	# 			# write erro message to log
# 	# 			# print stdin
# 	#
# 	# 		# search_result = re.compile('^Volume[\s]*in[\s]*drive ', re.MULTILINE)
# 	# 		r_wsp = re.compile('^[\s]*Directory[\s]*of[\s]*(.*)$')
# 	#
# 	# 		# line.lower() need to change .search()
# 	# 		lines = stdin.splitlines()
# 	# 		for line in lines:
# 	# 			wsp = r_wsp.search(line)
# 	# 			if wsp:
# 	# 				count += 1
# 	# 				workspace_path = wsp.group(1)
# 	# 				workspace_name = workspace_path.split('\\')[-1]
# 	# 				local_workspace_path = workspace_name + ": " + workspace_path
# 	# 				lwsp_list.append(local_workspace_path)
# 	# 				workspace_path_list.append(workspace_path)
# 	# 				workspace_name_list.append(workspace_name)
# 	#
# 	# 				# print local_workspace_path
# 	# 				# print "Local_Workspace %d: %s" % (count, local_workspace_path)
# 	# 	# return lwsp_list, workspace_path_list, workspace_name_list
# 	# 	return lwsp_list
# 	#
# 	#
# 	# # return GitHub local workspace path list in Linux
# 	# # Here For test, we search begin at /root, our finally version will use / (root path)
# 	# # lwsp_list = []
# 	# # workspace_path_list = []
# 	# # workspace_name_list = []
# 	# def getLocalGHWorkSpaceNix(self):
# 	#
# 	# 	count = 0
# 	# 	# local_workspace_path
# 	# 	lwsp_list = []
# 	# 	workspace_path_list = []
# 	# 	workspace_name_list = []
# 	#
# 	# 	stdin = ''
# 	# 	# find / -name ".git"
# 	# 	# use /root /home for testing, should be /
# 	# 	pr = subprocess.Popen( "find /root /home /workspaces -name \".git\"", cwd = os.path.dirname("/"), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
# 	# 	(out, error) = pr.communicate()
# 	# 	# if str(error) == '':
# 	# 	# 	stdin = str(out)
# 	# 	# else:
# 	# 	# 	stdin = str(error)
# 	# 	stdin = str(out)
# 	# 	# some directoris have  Permission denied
# 	# 	if str(error) != "":
# 	# 		# need to write error information into debug log
# 	# 		pass
# 	#
# 	# 	# write erro message to log
# 	#
# 	# 	# ^(/[^/ ]*)+/?$
# 	# 	# /root/Desktop/GE_GIT_01/.test
# 	#
# 	# 	r_wsp = re.compile('^[\s]*(/(.*))/\.git$')
# 	#
# 	# 	# line.lower() need to change .search()
# 	# 	lines = stdin.splitlines()
# 	# 	for line in lines:
# 	# 		wsp = r_wsp.search(line)
# 	# 		if wsp:
# 	# 			count += 1
# 	# 			workspace_path = wsp.group(1)
# 	# 			workspace_name = workspace_path.split('/')[-1]
# 	# 			local_workspace_path = workspace_name + ": " + workspace_path
# 	# 			lwsp_list.append(local_workspace_path)
# 	# 			workspace_path_list.append(workspace_path)
# 	# 			workspace_name_list.append(workspace_name)
# 	# 			# print local_workspace_path
# 	# 			# print "Local_Workspace %d: %s" % (count, local_workspace_path)
# 	# 	# return lwsp_list, workspace_path_list, workspace_name_list
# 	# 	return lwsp_list


# 	# For Linux, local_path need to add "/"
# 	# For Windows, local_path need to add "\\"
# 	def getRemoteGHWorkSpace(self, local_path):
# 		# git config --get remote.origin.url
# 		# git@github.build.ge.com:502618456/remote_path_test.git
# 		# s[:-4]  delete .git

# 		app_path = ''
# 		sysstr = platform.system()
# 		if sysstr.lower() =="windows":
# 			if local_path.strip()[-1] != "\\":
# 				app_path = "\\"
# 		elif sysstr.lower() == "linux":
# 			if local_path.strip()[-1] != "/":
# 				app_path = "/"
# 		else:
# 			print "Do not support %s" % sysstr
# 		# write bug log here

# 		stdin = ''
# 		remote_path = ''
# 		pr = subprocess.Popen( "git config --get remote.origin.url" , cwd = os.path.dirname(local_path + app_path), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
# 		(out, error) = pr.communicate()
# 		if str(error) == '':
# 			stdin = str(out)
# 		else:
# 			stdin = str(error)
# 		re_path = re.compile('^[\s]*(git@(.)*)\.git[\s]*$')

# 		# remember check NULL and search fault
# 		lines = stdin.splitlines()
# 		for line in lines:
# 			temp_path = re_path.search(line)
# 			if temp_path:
# 				remote_path = temp_path.group(1)
# 			# temp_path = temp_path.strip()
# 			# remote_path = temp_path[:-4]
# 		return remote_path


# 	# Check whether the input path is valid. if valid return True, else return False.  Currently it can not check "D:User" like path
# 	def exist_path(self, path):
# 		if not os.path.exists(os.path.dirname(path)):
# 			return False
# 		# os.makedirs(os.path.dirname)
# 		else:
# 			return True

# 	# Check whether the input has .git direcotory
# 	def exist_git_dir(self, path):
# 		if ".git" in os.listdir(path):
# 			return True
# 		else:
# 			return False

# 	# Get file absolute URL, if nonexist, return N/A
# 	def getFileAbsoluteURL(self, file):

# 		fileName = ""
# 		reposPath = ""
# 		remoteReposPath = ""
# 		fileSshURL = ""
# 		fileHttpsURL = ""
# 		localReposPath = ""
# 		postfixStr = ""
# 		branchPath = "/blob/"
# 		branchName = ""

# 		sysstr = platform.system()
# 		if sysstr.lower() == "windows":
# 			fileName = file.strip().split("\\")[-1]
# 			reposPath = file.strip()[:-(len(fileName))]
# 		elif sysstr.lower() == "linux":
# 			fileName = file.strip().split("/")[-1]
# 			reposPath = file.strip()[:-(len(fileName))]
# 		else:
# 			print "Do not support %s" % sysstr

# 		# get git@github.build.ge.com:502618456/remote_path_test
# 		remoteReposPath = self.getRemoteGHWorkSpace(reposPath)
# 		pr = subprocess.Popen( "git rev-parse --show-toplevel", cwd = os.path.dirname(reposPath), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
# 		(out, error) = pr.communicate()
# 		if str(error) == '':
# 			stdin = str(out)
# 		else:
# 			stdin = str(error)

# 		top_levels = []
# 		top_level = ""
# 		top_levels = stdin.split('\n')

# 		for top_level in top_levels:
# 			if (top_level.find("\\") != -1) or (top_level.find("/") != -1):
# 				localReposPath = top_level

# 		# print localReposPath

# 		if sysstr.lower() == "windows":
# 			tempStr = file.strip().replace("\\", "/")
# 			postfixStr = tempStr.split(localReposPath)[-1]
# 		elif sysstr.lower() == "linux":
# 			postfixStr = file.strip().split(localReposPath)[-1]

# 		# If URL is not exist, return "N/A"

# 		branchName = self.getCurrentBranch(reposPath)
# 		if branchName in self.getBranchList(reposPath):
# 			# fileSshURL = remoteReposPath + branchPath + branchName + postfixStr
# 			# fileHttpsURL =
# 			fileHttpsURL = remoteReposPath.replace(":", "/").replace("git@", "https://") + branchPath + branchName + postfixStr
# 			return fileHttpsURL
# 		else:
# 			# Write debug info about URL nonexist
# 			return "N/A"


# 	# s = "origin/HEAD -> origin/master"
# 	# s = "origin/branch_test"
# 	# s = "origin/dev"
# 	# s = "origin/master"
# 	# Get a branches set of current directory
# 	def getBranchList(self, current_reposPath):
# 		pr = subprocess.Popen( "git branch -r" , cwd = os.path.dirname(current_reposPath), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
# 		(out, error) = pr.communicate()
# 		if str(error) == '':
# 			stdin = str(out)
# 		else:
# 			stdin = str(error)
# 		# write debug log here

# 		# save all the branches of current directory
# 		branchSet = set([])
# 		# Get all result lines
# 		lines = []
# 		line = ""
# 		lines = stdin.split('\n')
# 		# This path keep the same format between Windows and Linux
# 		for line in lines:
# 			if line.find("/") != -1:
# 				branchSet.add(line.strip().split("/")[-1])

# 		return branchSet

# 	# Get current branch name
# 	def getCurrentBranch(self, current_reposPath):
# 		pr = subprocess.Popen( "git branch" , cwd = os.path.dirname(current_reposPath), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
# 		(out, error) = pr.communicate()
# 		if str(error) == '':
# 			stdin = str(out)
# 		else:
# 			stdin = str(error)
# 		# write debug log here

# 		# branch name
# 		branch = ""
# 		lines = []
# 		line = ""
# 		lines = stdin.split('\n')
# 		# The line start with "*" includes current branch name
# 		for line in lines:
# 			if (line.strip() != "") and (line.strip()[0] == "*"):
# 				branch = line.strip()[1:].strip()

# 		return branch








































# if __name__ == "__main__":
# 	# stu1 = Student("xiaoming", 90)
# 	# stu1.print_score()
# 	# # stu1.height = "1.79"
# 	# print stu1._Student__name
# 	# hs = Highschool("xiao", 97)
# 	# hs.print_score()
# 	# hs.print_name()

# 	# display()
# 	# from types import MethodType

# 	# hs = Highschool("xiao", '99')
# 	# t = T()
# 	# display(hs)
# 	# display(t)
# 	# hs.print_good()
# 	# print len(hs)
# 	# Student.hh = 10
# 	# print hs.hh
# 	# del Student.hh
# 	# hs.hh = 100
# 	# print hs.hh
# 	# # print Student.hh
# 	# Student.hh = 10000
# 	# print Student.hh
# 	# print hs.hh

# 	# hs.set_age = MethodType(set_age, hs)
# 	# hs.set_age(25)
# 	# print hs.age
# 	# Highschool.set_age = set_age
# 	# hs2 = Highschool("xiaohei", "90")
# 	# hs2.set_age(100)
# 	# print hs2.age

# 	# s = Student("ggg", "10")
# 	# cls = Classmate("kakk", " 109", "M")
# 	# cls.name = "100"
# 	# cls.Gener = "men"
# 	# print cls.name
# 	# print cls.Gener
# 	# # s.Gener = "kk"

# 	# # s.score = 60
# 	# # s.score

# 	# for n in Fib():
# 	# print(n)

# 	# f= Fib()

# 	# f = Fib()
# 	# f[0: 5]
# 	# f[: 10]

# 	# f[:10: 2]

# 	# s = Student()
# 	# print s.age

# 	s = Student('MMMK')
# 	print s("31")
# 	# print callable(s)
# 	# print callable(max)
# 	# print callable([1, 2, 3])
# 	# print callable(None)
# 	# print callable('str')

# 	from enum import Enum

# 	Month = Enum("Month", ('Jan', 'Dec'))

# 	Month.Jan

# 	for name, member in Month.__members__.items():
# 		print name, "=>", member, ',', member.value

# 	day1 = Weekday.Month
# 	print(Weekday.Tue)
# 	print(Weekday['Tue'])
# 	print(Weekday.Tue.value)

# 	print(day1 == Weekday.Mon)
# 	print(day1 == Weekday.Tue)

# 	print(Weekday(1))
# 	print(day1 == Weekday(1))

# 	Weekday(7)

# 	for name, member in Weekday.__members__.items():
# 		print name, "=>", member

# 	Weekday.Mon
# 	Weekday.Tue

# 	Weekday["Tue"]

# 	Weekday.Tue.value

# 	Weekday(1)

# 	for name, member in Weekday.__members__.items():
# 		print name, member

# import json

# class Student(object):
# 	__slots__ = ('name', 'age', 'score')
# 	def __init__(self, name, age, score):
# 		self.name = name
# 		self.age = age
# 		self.score = score

# def student2dict(std):
# 	return {'name': std.name, 'age': std.age, 'score': std.score}

# def dict2student(d):
# 	return Student(d['name'], d['age'], d['score'])


# # s = Student('Bob', 20, 88)
# # print(json.dumps(s, default=lambda obj: obj.__dict__))
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# kk = json.loads(json_str, object_hook=dict2student)

# print kk.age 



# import os

# pid = os.fork()
# if pid == 0:
# 	print "P" + os.getppid()
# 	print "S" + os.getpid()
# else:
# 	print "P" + os.getppid()
# 	print pid

# from multiprocessing import Process

# import os

# def run_proc(name):
# 	print "Run child process %s (%s)..." % (name, os.getpid())

# if __name__=="__main__":
# 	print "Parent process %s." % os.getpid()
# 	p = Process(target=run_proc, args=('test',))
# 	print("Child process will start.")
# 	p.start()
# 	p.join()
# 	print("Child process end.")

# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
# 	print("Run task %s (%s)" % (name, os.getpid()))
# 	start = time.time()
# 	time.sleep(random.random() * 3)
# 	end = time.time()
# 	print("Task %s runs %0.2f seconds." % (name, (end - start)))

# if __name__=="__main__":
# 	print("Parent process %s." % os.getpid())
# 	p = Pool(4)
# 	for i in range(5):
# 		p.apply_async(long_time_task, args=(i,))
# 	print("Waiting for all subprocess done...")
# 	p.close()
# 	p.join()
# 	print ("All subprocesses done.")

# import subprocess

# print('$ nslookkup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print("Exit code:", r)

# import subprocess

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)

# from multiprocessing import Process, Queue
# import os, time, random

# def write(q):
# 	print('Process to write: %s' % os.getpid())
# 	for value in ['A', 'B', 'C']:
# 		print('Put %s to queue...' % value)
# 		q.put(value)
# 		time.sleep(random.random())

# def read(q):
# 	print('Process to read: %s' % os.getpid())
# 	while True:
# 		value = q.get(True)
# 		print('Get %s from queue.' % value)

# if __name__=="__main__":
# 	q = Queue()
# 	pw = Process(target=write, args=(q,))
# 	pr = Process(target=read, args=(q,))
# 	pw.start()
# 	pr.start()
# 	pw.join()
# 	pr.terminate()

# import time, threading

# balance = 0

# def change_it(n):
# 	global balance
# 	balance = balance + n
# 	balance = balance -n

# def run_thread(n):
# 	for i in range(100000):
# 		change_it(n)

# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# balance = 0
# lock = threading.Lock()

# def run_thread(n):
# 	for i in range(100000):
# 		lock.acquire()
# 		try:
# 			change_it(n)
# 		finally:
# 			lock.release


# import threading, multiprocessing

# def loop():
# 	x = 0
# 	while True:
# 		x = x ^ 1

# for i in range(multiprocessing.cpu_count()):
# 	t = threading.Thread(target=loop)
# 	t.start()


# def process_student(name):
# 	std = Student(name)
# 	do_task_1(std)
# 	do_task_2(std)

# def do_task_1(std):
# 	do_subtask_1(std)
# 	do_subtask_2(std)

# def do_task_2(std):
# 	do_subtask_2(std)
# 	do_subtask_2(std)

# global_dict = {}

# def std_thread(name):
# 	std = Student(name)
# 	global_dict[threading.current_thread()] = std
# 	do_task_1()
# 	do_task_2()

# def do_task_1():
# 	std = global_dict[threading.current_thread()]

# def do_task_2():
# 	std = global_dict[threading.current_thread()]


# import threading

# local_school = threading.local()

# def process_student():
# 	std = local_school.student
# 	print('Hello, %s (in %s)' % (std, threading.current_thread().name))

# def process_thread(name):
# 	local_school.student = name
# 	process_student()

# t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# task_master.py

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


# # task_worker.py
# import time, sys, Queue
# from multiprocessing.managers import BaseManager

# class QueueManager(BaseManager):
# 	pass

# QueueManager.register('get_task_queue')
# QueueManager.register('get_result_queue')

# server_addr = '3.232.126.147'
# print('Connect to server %s...' % server_addr)
# m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# m.connect()
# task = m.get_task_queue()
# result = m.get_result_queue()

# for i in range(10):
# 	try:
# 		n = task.get(timeout=1)
# 		print('run task %d * %d...' % (n, n))
# 		r = '%d * %d = %d' % (n, n, n*n)
# 		time.sleep(1)
# 		result.put(r)
# 	except Queue.Empty:
# 		print('task queue is empty.')
# print('worker exit.')

# import re

# test = '用户输入字符串'
# if re.match(r"正则表达式", test):
# 	print('ok')
# else:
# 	print('failed')


# t = '19:05:30'
# t1 = "19"

# # m = re.match(r"^([1-9]|[0-2][0-9])\:()\:()")

# m = re.match(r"[1-9]|[0-2][0-9]")

# from datetime import datetime, timedelta, timezone

# tz_utc_8 = timezone(timedelta(hours=8))
# now = datetime.now()

# now
# dt = now.replace(tzinfo=tz_utc_8)
# dt


# from datetime import datetime, timedelta, timezone

# tz_utc_8 = timezone(timedelta(hours=8))

# now = datetime.now()
# now

# dt = now.replace(tzinfo=tz_utc_8)
# dt



# utc_dt = datetiem.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)
# bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# print(bj_dt)

# tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
# print(tokyo_dt)
# tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
# print(tokyo_dt2)




# datetime.strptime()

# import hashlib

# md5 = hashlib.md5()

# import hashlib

# m1 = hashlib.md5()
# m1.update('how to'.encode('utf-8'))
# s1 = m1.hexdigest()
# m2 = hashlib.md5()
# m2.update('how'.encode('utf-8'))
# m2.update(' t'.encode('utf-8'))
# s2 = m2.hexdigest()
# print s1
# print s2
# print s1 == s2
 

# db = {}

# def register(username, password):
# 	db[username] = get_md5(password + username + 'the-Salt')

# def login(username, password):
# 	pass

# from xml.parsers.expat import ParserCreate

# class DefaultSaxHandler(object):


# 	def start_element(self, name, attrs):
# 		print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

# 	def end_element(self, name):
# 		print('sax:end_element: %s' % name)

# 	def char_data(self, text):
# 		print("sax:char_data: %s" % text)

# def start_element(name, attrs):
# 	print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

# def end_element(name):
# 	print('sax:end_element: %s' % name)

# def char_data(text):
# 	print("sax:char_data: %s" % text)


# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''
# # handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = start_element
# parser.EndElementHandler = end_element
# parser.CharacterDataHandler = char_data
# parser.Parse(xml)

# from xml.parsersexpat import ParserCreate

# class DefaultSaxHandler(object):

# 	def start_element(self, name, attrs):
# 		print()


# from xml.parsers.expat import ParserCreate

# class DefaultSaxHandler(object):

# 	def start_element(self, name, attrs):
# 		print("sax:start_element: %s, attrs: %s" % (name, str(attrs)))

# 	def end_element(self, name):
# 		print("sax:end_element: %s" % name)

# 	def char(self, text):
# 		print("sax:char: %s" % text)

# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''

# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char
# parser.Parse(xml)

# L = []
# L.append(r'<?xml version="1.0"?>')
# L.append(r'<root>')
# L.append(r'some & data')
# L.append(r'</root>')
# print  "".join(L)

# from xml.parsers.expat import ParserCreate


# rst = {}
# forecasts = []

# def start_element(name, attrs):
# 	global rst
# 	global forecasts
# 	if name == 'yweather:location':
# 		rst['city'] = attrs['city']
# 		rst['country'] = attrs['country']
# 	if name == 'yweather:forecast':
# 		forecasts.append({'text':attrs['text'], 'low': int(attrs['low']), 'high': int(attrs['high'])})

# def parse_weather(xml):
# 	parser = ParserCreate()
# 	parser.StartElementHandler = start_element
# 	parser.Parse(xml)
# 	rst['today'] = forecasts[0]
# 	rst['tomorrow'] = forecasts[1]
# 	return rst

# xml=r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
#     <rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
#     <channel>
#     <title>Yahoo! Weather - Beijing, CN</title>
#     <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
#     <yweather:location city="Beijing" region="" country="China"/>
#     <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
#     <yweather:wind chill="28" direction="180" speed="14.48" />
#     <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
#     <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
#     <item>
#     <geo:lat>39.91</geo:lat>
#     <geo:long>116.39</geo:long>
#     <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
#     <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
#     <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
#     <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
#     <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
#     <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
#     <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
#     </item>
#     </channel>
#     </rss>
#     '''
# weather=parse_weather(xml)
# assert weather['city'] == 'Beijing', weather['city']
# assert weather['country'] == 'China', weather['country']
# assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
# assert weather['today']['low'] == 20, weather['today']['low']
# assert weather['today']['high'] == 33, weather['today']['high']
# assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
# assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
# assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']
# print('Weather:', str(weather))


# from html.parser import HTMLParser
# from html.entities import name2codepoint

# class MyHTMLParser(HTMLParser):

# 	def handle_starttag(self, tag, attrs):
# 		print('<%s>' % tag)

# 	def handle_endtag(self, tag):
# 		print('</%s>' % tag)

# 	def handle_startendtag(self, tag, attrs):
# 		print("<%s/>" % tag)

# 	def handle_data(self, data):
# 		print(data)

# 	def handle_comment(self, data):
# 		print('!--', data, '-->')

# 	def handle_entityref(sef, name):
# 		print('&%s;' % name)

# 	def handle_charref(self, name):
# 		print('&#%s;' % name)

# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')

# import requests
# from html.parser import HTMLParser

# class MyHTMLParser(HTMLParser):
# 	bool_title = False
# 	bool_time = False
# 	bool_place = False
# 	bool_miss = True

# 	def __init__(self):
# 		HTMLParser.__init__(self)
# 		self.message = []

# 	def handle_starttag(self, tag, attrs):
# 		if len(attrs) > 0:
# 			if tag == "h3" and attrs[0][1] == "event-title":
# 				self.bool_title = True
# 			elif tag == "time" and attrs[0][0] == "datetime":
# 				sefl.bool_time = True
# 			elif tag == "span" and attr[0][1] == "event-location":
# 				self.bool_place = True
# 			elif tag == "h3" and attrs[0][1] == "widget-title just-missed":
# 				self.bool_miss = False

# 	def handle_data(self, data):
# 		if self.bool_title and self.bool_miss:
# 			self.message.append([])
# 			sefl.message[-1].append(data)
# 			self.bool_title = False

# 		if self.bool_time and self.bool_miss:
# 			self.message[-1].append(data)
# 			self.bool_time = False

# 		if self.bool_place and self.bool_miss:
# 			self.message[-1].append(data)
# 			self.bool_place = False
# def homework():
# 	parser = MyHTMLParser()
# 	html = requests.get("")
# 	parser.feed(html)
# 	a = parser.message
# 	a = parser.message
# 	for x in a:
# 		print("==========================================")
# 		print x
# homework()

# import requests

# from bs4 import BeautifulSoup

# resp = requests.get('https://www.python.org/events/python-events/')

# soup = BeautifulSoup(resp.text, "html.parser")

# for li in soup.select(".list-recent-events > li"):
# 	print('title:', li.find('a').text)
# 	print("time:", li.find("time").text)
# 	print("location:", li.select_one('.event-location').text)
# 	print("*"*100)

# import re
# import urllib.request

# with urllib.request.urlopen("url") as url:
# 	data = url.read().decode("utf-8")

# when1 = re.findall(r"<time\sdatetime=.{27}(.+?)")


# from urllib import request

# with request.urlopen('http://www.douban.com/') as f:
# 	data = f.read()
# 	print("Status:", f.status, f.reason)
# 	for k, v in f.getheaders():
# 		print('%s: %s' % (k, v))
# 	print('Data:', data.decode('utf-8'))

# from urllib import request

# req = request.Request('http://www.douban.com/')

# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

# with request.urlopen(req) as f:
# 	print('Status:', f.status, f.reason)
# 	for k, v in f.getheaders():
# 		print("%s: %s" % (k, v))
# 	print("Data:", f.read().decode('utf-8'))

# from urllib import request, parse

# print("Login to weibo.cn...")
# email = input("Email: ")
# passwd = input("Password: ")
# login_data = parse.urlencode([
# 	('username', email),
# 	('password', passwd),
# 	('entry', 'mweibo'),
# 	('client_id', ''),
# 	('savestate', '1'),
# 	('ec', ''),
# 	('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')])

# req = request.Request("https://passport.weibo.cn/sso/login")
# req.add_header("Origin", 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
# 	print('Status:', f.status, f.reason)
# 	for k, v in f.getheaders():
# 		print('%s: %s' % (k, v))
# 	print('Data:', f.read().decode('utf-8'))

# from ulllib import request, parse

# print('Login to weibo.cn...')
# email = input('Email: ')
# passwd = input('Password: ')
# login_data = parse.urlencode([
# 	('username', email),
# 	('password', passwd),
# 	('entry', 'mweibo'),
# 	('client_id', ''),
# 	('savestate', '1'),
# 	('ec', ''),
# 	('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')])

# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')


# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
# 	print('Status: ', f.status, f.reason)
# 	for k, v in f.getheaders():
# 		print('%s: %s' % (k, v))
# 	print('Data: ', f.read().decode('utf-8'))


# from urllib import request, parse

# print('Login to weibo.cn...')
# email = input('Email')
# passwd = input('Password')
# login_data = parse.urlencode([
# 	('username', email),
# 	('passwd', passwd),
# 	('entry', 'mweibo'),
# 	('client_id', ''),
# 	('savestate', '1'),
# 	('ec', ''),
# 	('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')])

# req = request.Request("https://passport.weibo.cn/sso/login")
# req.add_header("Origin", "https://passport.weibo.cn")
# req.add_header("User-Agent", 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header("Referer", 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
# 	print('Status: ', f.status, f.reason)
# 	for k,v in f.getheaders():
# 		print('%s: %s' % (k, v))
# 	print('Data: ', f.read().decode('utf-8'))


# proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
# proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
# opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
# with opener.open("http://www.example.com/login.html") as f:
# 	pass

# proxy_handler = urllib.request.ProxyHandler({"http": "http://www.example.com:3128/"})
# proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password("realm", "host", "username", "password")
# opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
# with opener.open("http://www.example.com/login.html") as f:
# 	pass


# response = urllib2.urlopen(url)

# data = response.read()
# r= ET.parse(data).getroot()

# print r.attrib.get('status')


# from PIL import Image, ImageDraw, ImageFont, ImageFilter
# import sys, os

# import random

# version = sys.version_info.major
# if version == 2:
# 	ls = list(raw_input("Input: "))
# elif version == 3:
# 	ls = list(input("Input: "))


# origin_len = len(ls)

# def rndChar():
# 	# return chr(random.randint(0, len(ls)-1))
# 	global ls
# 	i = random.randint(0, len(ls)-1)
# 	return ls.pop(i)

# def rndColor():
# 	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# def rndColor2():
# 	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# width = 60 * origin_len
# height = 60

# image = Image.new('RGB', (width, height), (255, 255, 255))

# font_list =["Windsong.ttf", "AlexBrush-Regular.ttf", "arial.ttf", "GoodDog.otf", "GreatVibes-Regular.otf", "KaushanScript-Regular.otf"]
# file = random.randint(0, len(font_list)-1)
# font = ImageFont.truetype(os.path.join(".", "font", font_list[file]) , 36)

# draw = ImageDraw.Draw(image)

# for x in range(width):
# 	for y in range(height):
# 		draw.point((x, y), fill=rndColor())

# for t in range(origin_len):
# 	draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 	# draw.text((60 * t + 10, 10), ls[t], font=font, fill=rndColor2())
# image = image.filter(ImageFilter.BLUR)
# image.save('code.jpg')

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

def rndChar():
	return chr(random.randint(65, 90))

def rndColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 60 * 4
height = 60

image = Image.new('RGB', (width, height), (255, 255, 255))

font = ImageFont.truetype('Arial.ttf', 36)
draw = ImageDraw.Draq(image)

for x in range(width):
	for y in range(height):
		draw.poin((x, y), fill=rndColor())

for t in range(4):
	draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2)

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')


