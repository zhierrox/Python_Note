Company： Youtube, google
Use: 网站， 后台， 脚本
安装： path 用于找到 exe
解释器： 
	Jython，可以将python代码编译成Java字节码
	IronPython， 将Python编译成.Net字节码
	网路解决Java，.Net平台交互
Python程序： 
	不复制，粘贴， 自己输入，对照代码
编辑器： 
	不能用windows记事本
	#!/usr/bin/env python3”， chmod a+x hello.py， 然后可以./hello.py
	upper 记得 upper()
输入和输出： 
	print 的逗号（，）被空格（“ ”）代替
	input(),括号里是输出信息。
	2.7 用人raw_input
	可以用连续%%， 例如 print "kk%s" % ("(%s)" % a) 
python基础：
	4个空格缩进， 粘贴需要重新检查缩进
	python大小写敏感
数据类型和变量： 
	十六进制用0x开头，英文： hex
	八进制0o， 英文：octal
	二进制， 英文0b
	浮点是指，小数点位置可变；误差是（2的m次方，不能表示-0.1）
	单精度32位，双精度64位，三个部分组成：sign + exponent + fraction
	r'' 表示不转义， '''agag ...'''表示多行
	布尔值可以用 and, or, not， 但&&不可以，&可以
	None 表示空
	动态语言指，变量本身类型不固定
	常量指，不能变的变量， 用全大写（PI）表示
	%是取余
	python整数没有大小限制， 32位java是正负21亿
	python浮点没限制，太大会显示inf（小数点后10位）
字符串与编码：
	1字节255， 2字节65535， 4字节42亿 
	ASCII 一个字节 = 127个字母
	Unicode 两个字节
	UTF-8 可变长编码， 英文1个字节，汉字3个字节，生僻字符4-6字节， 兼容ASCII
	内存用unicode, 硬盘或网络用UTF-8
	python字符串用Unicode
	Unicode encode(ascii or utf-8), decode(ascii or utf-8),参数一致
	#!/usr/bin/env python3
	# -*- coding:utf-8 -*-
	Encode in UTF-8 without BOM
	python格式化方式和C语言一致, 用%分隔
	%02d, 一位数会补零，两位数就不补
	%.2f小数点后两位
	%%来表示一个%
list和tuple:
	list.insert(1, item)指在index 1之前插入
	list.pop(i)删除index i位置元素
	换成别的元素，直接赋值给对应的索引位置
	list用[], tuple用（）且不能修改
	tuple一个元素时，加逗号，（1，）； list不用
	list，字符串转tuple， 可以用tuple(str or list)
条件判断：
	if, elif, else就是多选一
	python是elif,不是else if
	"", 0, [], {}, () 布尔为False
	int(str)转为整数， 但“aba”会报错
	try块有错，块内其他语句不执行；无论对错，finally块语句都执行
循环：
	两种循环， for in（用于罗列）, while（用于次数变化）
	range(5)生成的序列是从0开始小于5
	while条件满足，就不断循环，条件不满足时退出
	用Ctrl+C退出程序
dict和set：
	dict就是map，用{}
	本质：把ｋｅｙ变成数组index
	两种方法：　ｋｅｙ　in，　ｇｅｔ（ｋｅｙ）判断ｋｅｙ是否存在，不能判断value
	a['Adam']index添加， pop(key)删除
	dict不能用索引访问，它会把index Hash掉
	key必须是不可变对象
	通过key计算位置的算法称为哈希算法（Hash）
	Touple可以hash， list不行
	set 用{} 只有key，没有value 没有重复元素，
	set用[]初始化
	set用add(key), remove(key), pop()无参数
	&表示交， |表示并
	replace（old，new）
	不变对象，调用对象自身的任意方法，不会改变该对象自身的内容
调用函数：
	help(abs)
	max()可以比较字符大小max("ag"）
	函数名指向一个函数模块
定义函数：
	1 if 5>3 else 0， 两边结果，中间判断
	如果没有return语句，函数执行完返回None
	...按两次回车重新回到>>>
	from 文件 import 模块
	import math语句表示导入math包
	检查参数类型错误，isinstance(num, (int, float))， raise TypeError("your_str")
	函数返回多值就是返回一个tuple, 多个变量按位置赋给对应的值
函数参数：
	必选参数， 默认参数、可变参数， 关键字参数，
	必选参数在前，默认参数在后， 变化小的参数作为默认参数
	默认参数可以兼容旧代码
	不按顺序提供部分默认参数时，需要参数名
	默认参数必须指向不变对象
	不可变对象复制一份去操作，可变对象直接操作自身
	可变参数当作一个tuple,*num; 关键字参数组装为一个dict, **kw
	一颗*传一个值， 两颗*传两个值
	def person(name, age, *, city, job)
	如果函数中有了一个可变参数，后面跟着的命名关键字参数就不再需要特殊分隔符*
	命名关键字参数和关键字参数区别在于，它限制了参数的名字
	命名关键字参数必须传入参数名，和位置参数就差*
	参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
	对于任意函数，都可以通过类似func(*args, **kw)的形式调用，无论它的参数是如何定义的
	递归函数就是调用自身，都可以写成循环， 但要防止栈溢出
高级特性：
	1行代码能实现的功能，决不写5行代码。请始终牢记，代码越少，开发效率越高。
切片：
	[左，又）区间。 
	[:]开头表示最左，和末尾表示最右。
	[-2:]比[-2：-1]多一个元素
	L[::5]所有数，每5个取一个
迭代：
	用for循环遍历叫迭代（Iteration）,for ... in
	for value in d.values()
	for k, v in d.items()
	字符串是可迭代对象
	用以下代码判断对象是否可迭代
	from collections import Iterable
	isinstance('abc', Iterable)
	enumerate把list变成索引-元素对
	任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。
列表生成式：
	List Comprehensions
	range(左开， 右闭)
	[表达式 + for in循环 +　ｉｆ 判断]： [x * x for x in range(1, 11) if x % 2 == 0]
	两层循环，生成全排列:
	[m + n for m in 'ABC' for n in 'XYZ']
	python 2.7 isinstance(x, basestring)
生成器：
	generator不必创建完整的list, 一边循环一边计算的机制
	节省内存， 而且可以操作无限循环，例如斐波那契
	方法一： 把列表生成式的[]改成()， 用for in , a.next(), next(a)
	print(b)及时打印， yield b 单个打印
	方法二： 函数定义中包含yield关键字就是generator， 本质是next（）启动，yield返回值
	想要拿到返回值，必须捕获StopIteration， StopIteration.value
	python 没有catch, 用except代替
	普通函数调用直接返回结果， generator函数返回一个generator对象
	前后值有关系的，考虑用generator
迭代器：
	直接作用于for循环的对象统称为可迭代对象
	list、dict、str不是数据类型原因： 能提前知道序列的长度
	凡是可作用于for循环的对象都是Iterable类型
	凡是可作用于next()函数的对象都是Iterator类型
	集合数据类型如list、dict、str等是Iterable但不是Iterator
	可以通过iter()函数获得一个Iterator对象。
	Python的for循环本质上就是通过不断调用next()函数实现的
函数式编程：
	允许把函数本身作为参数传入另一个函数，还允许返回一个函数
	函数本质也是一个变量
	import builtins; builtins.abs = 10
高阶函数：
	一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
map/reduce: 
	map()函数接收两个参数，一个是函数，一个是Iterable, 返回Iterator
	reduce(函数， Iterable), 返回
	reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数
	reduce把结果继续和序列的下一个元素做累积计算
	switch case 可以考虑用 dict代替 {'0': 0, '1': 1}[s]
	函数体内可以定义函数
	python2.7 注意除法， 最好被除数加.0,例如 s/3.0
filter:
	用于过滤序列
	filter(布尔函数， 序列)， 返回满足条件的值
	一个无限序列，调用时需要设置一个退出循环的条件
	s[::-1]可以倒序字符串
排序：
	sorted(序列， 比什么， 正反序)
	排序的核心是比较两个元素的大小
	可以加key， 确定“比什么”；例如sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
    第三个参数 reverse=True， 反向排序
返回函数：
	返回一个函数时，牢记该函数并未执行
	内部函数sum可以引用外部函数lazy_sum的参数和局部变量
	闭包就是，内部定义的函数可以使用外部函数的参数或变量
	内部定义的函数不能直接单独调用
	返回函数不要引用任何循环变量，或者后续会发生变化的变量。
	一定要引用循环变量，就用该函数的参数绑定循环变量当前的值
匿名函数：
	lambda 输入：输出
	匿名函数只能有一个表达式
	好处:因为函数没有名字，不必担心函数名冲突
	匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
	python 2.7 注意调用顺序，例如，build(x, y)(x, y)
装饰器：
	__name__ 获得函数名字
	“装饰器”（Decorator）在代码运行期间动态增加功能的方式
	本质上，decorator就是一个返回函数的高阶函数
	@decorator置于函数的定义处
	在定义wrapper()的前面加上@functools.wraps(func)保证装饰过后函数名不变
	wrapper里面返回的是func（）执行结果，不是返回func引用， 后面的wrapper， decorator都是返回引用
	now = log('execute')(now)是核心
	python三目运算符：  结果 if True else 反结果
	decorator本质是得到wrapper函数名。
	分析问题时候，可以画出传参过程：log(func), log("execute")(func)，log(func)(func)
	先看return 再看定义， 定义不是函数的运行部分
	callable(func)判断变量是不是函数，str， int都返回 False
偏函数：
	不是数学意义， 是部分参数的意思
	作用： functools.partial创建一个新函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。 例如int2
	functools.partial（函数对象， *args, **kw）	
	functools.partial(max, 10), 把10作为*args的一部分自动加到左边， 注意此刻再传list，tuple，结果不正确
	split分开字符串， join连接字符串， strip()是去前后空格
	string.split("用什么分", 分几个)， “用什么连”.join(list)
	split()可以去除连续空格， split（" "）不可以
模块：
	一个.py文件就称之为一个模块（Module）
	一个包（Package）有多个.py文件
	包目录必须有__init__.py， 因此不同于普通目录
	__init__.py本身就是一个模块，可以为空，也可以有python代码，而它的模块名是包名
使用模块：
	第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释
	第6行使用__author__变量把作者写进去（__version__， __license__）
	args = sys.argv argv,命令行的参数，是一个list, 至少有一个元素，因为第一个参数永远是该.py文件的名称
	if __name__=='__main__': Command line 上运行时，会把__name__置为__main__, 常用于运行测试
	外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public, 没有protect
安装第三方模块：
	导入模块时， 不要用.py后缀
	pip 安装第三方模块
	图片三要素： format（PNG）, size（400， 300）, mode（RGB）
	thumbnail（）用于压缩图片
	MySQL库：mysql-connector-python， 科学计算numpy， 生成文本的模板工具Jinja2
	模块搜索路径：：Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中
	使用自己写的模块，方法一::直接在sys.path.append(your_path)
	方法二：：设置环境变量PYTHONPATH， 与设置Path环境变量相似，会用到setenv命令
面向对象：
	面向过程是一系列的命令集合， 把大块函数切割成小块函数来降低系统的复杂度
	面向对象是一组对象的集合，每个对象都可以接收、处理消息，程序就是一系列消息在各个对象之间传递
	思考法：：首先确定对象（object, instance）和属性（Property）， 然后确定调用函数（Method）， 然后再归纳出类（Class），不要一上来就想执行流程
	三大特点：：封装、继承和多态
	通常，如果没有合适的继承类，就使用object类
类和和实例：
	类可以起到模板的作用
	self，表示创建的实例本身
	类中定义的函数只有一点不同，就是第一个参数永远是实例变量self, 仍然可以用默认参数、可变参数、关键字参数和命名关键字参数
	和静态语言不同，Python允许对实例变量绑定任何数据
访问限制：
	属性的名称前加上两个下划线__，表示 private
	__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途， 可以直接访问， 不是private变量
	__doc__ 访问文档注释， 例如sys.__doc__
	_xxx和__xxx这样的函数或变量就是非公开的（private）
	_xxx，比如_name，这样的实例变量外部是可以访问的， 但约定为私有变量
	_class_name__name来访问__name变量
	一旦加了__ 下划线, 其他所有函数里都需要加__
	注意bart.__name错误写法， 这是新增了变量， 不是修改原来变量
继承和多态：
	继承最大的好处是，子类获得了父类的全部功能
	继承的另一个好处：：多态
	多态本质：：使用上层数据类型
	构造函数不继承的原因是， 数据和类名绑定
	子类覆盖父类相同方法
	当定义一个class，本质定义了一种数据类型， 和自带str, list, dict相同
	isinstance(b, Animal)判断变量类型
	静态语言有类型检查， python没有类型限制
	Python 的 “file-like object”, 是指method（）相同， 继承关系可以不同, 因此继承不像静态语言那样是必须的
获取对象信息：
	基本类型用type()，返回对应的Class类型， 它的常量例如FunctionType， BuiltinFunctionType， LambdaType， GeneratorType
	对象类型isinstance()， 返回True or False， 
	能用type()判断的基本类型也可以用isinstance()判断
	注意是bytes 不是 byte
	isinstance([1, 2, 3], (list, tuple))， 判断一个变量是否是某些类型中的一种
	dir(对象)获得所有属性和方法
	自己写的类，想用len(myObj)，就自己写一个__len__()方法：
	getattr(对象， “属性”， 如不存在返回默认值)、setattr(对象， “属性”， 设置值)以及hasattr(对象， “属性”)，我们可以直接操作一个对象的状态
	获取不存在的属性，会抛出AttributeError
	有在不知道对象信息的时候，我们才会去获取对象信息， 可以避免用getattr, hasattr, setattr
实例属性和类属性：
	直接在class中定义属性，这种属性是类属性
	>>>del s.name 删除实例的name属性
	>>>del Student.name 删除类的name属性
	可以用 Student.name = "gag" 动态添加类属性
	千万不要把实例属性和类属性使用相同的名字, 因为删除实例属性后，再使用相同的名称，访问到的是类属性
高级编程：
	__slots__, @property, 多重继承、定制类、元类, 枚举类
	实例绑定方法::对象.函数名 = MethodType（函数名， 对象）
	类绑定方法：：类名.函数名 = 函数名
	__slots__限制实例的属性, 在定义类时， __slots__ = ('name', 'age')
	__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
	显式调用父类构造函数， 父类名.__init__(self,父类参数) 
@property:
	因为需要get 和 set， 所有用@property， setter 来包装
	只定义getter方法，不定义setter方法就是一个只读属性
	@property本质是把函数包装成属性
多重继承：
	本质： 子类扩展父类的功能， 层次不要太复杂
	多继承： 目的是用于添加额外功能（MinIn）； class Dog(Mammal, Runnable)
	Java 不能多继承，所以用接口实现添加额外功能
定制类：
	__xxx__形式
	__str__, __iter__, __getitem__, __getattr__, __call__
	__str__用print， __repr__不需print, 默认功能都是打印对象， 所以__repr__ = __str__
	__iter__需要调用__next__(), 用于 for in 
	__getitem__用于index []访问， 传int或者切片对象slice
	切片对象slice, 有start, stop变量
	__setitem__()把对象视作list或dict来对集合赋值, __delitem__()用于删除某个元素
	python 动态语言， 不需要强制继承某个接口
	__getattr__()， 动态返回一个属性
	函数执行结束，没有返回值时，默认返回None
	只有在没有找到属性的情况下，才调用__getattr__， "."就是调用方法
	用__getattr__， __call__()写出链式调用, 本质是递归(或迭代)
	可以格式字符串传参， 例如Chain('%s/%s' % (self._path, path))
	能被调用的对象就是一个Callable对象， 带有__call__()
	__call__把对象当成函数用, 函数也是callable
	格式化字符串， %后多个参数需要加（ ） 
	写链式调用，一定分析串的调用顺序
枚举类：
	大写所有字母定义常量
	Enum类，每个常量都是class的一个唯一实例，把一组相关常量定义在一个class中
	value是自动赋给成员的int常量，默认从1开始计数
	@unique定义在新枚举类前
	枚举类的本质： 实例确定的类
	注意， Enum（）是创建一个类，如Weekday, 而Weekday.Mon表示一个对象， Weekday.__memebers__.items()相当于遍历每个实例， Weekday(1)是取value为1的对象
	可以调用： Month.__memebers__['Jan'].__dict__
元类：
	动态语言和静态语言最大的不同，是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
	创建class对象，type(class名称， 继承的父类tuple， 类方法dict)
	先定义metaclass，然后创建类； 先定义类，然后创建实例， 可以把类看成是metaclass创建出来的“实例”
	metaclass的类名总是以Metaclass结尾
	metaclass是类的模板，所以必须从’type‘类型派生
	定制类时， 传入关键字参数metaclass， 例如class MyList(list, metaclass=ListMetaclass):
	__new__(当前准备创建的类的对象cls, 类的名字， 类继承的父类集合， 类的方法集合)
	ORM本质： 关系数据库的一行映射为一个对象， 一个类对应一个表
	ORM需要通过metaclass修改类定义， 因为用户需要定义表，因此， 动态定义类
	编写底层模块的第一步，就是先把调用接口写出来
	子类初始化： super(子类名， self).__init__(没有self)
	从对象保存为到数据库， 本质是调用sql语句
	metaclass可以隐式地继承到子类，但子类自己却感觉不到
	ORM-metaclass本质： class 定义时就调用metaclass； object初始化时才调用类； 类属性map到数据表属性
	self.是操作对象， 不加self是操作类
错误、调试、测试：
	三种错误： 编写错误， 用户输入错误， 异常（磁盘， 网络等）
	调试： 跟踪程序的执行
	测试： 程序修改后可反复运行
错误处理：
	错误码，不利： 与函数返回结果混淆
	try 检查代码 except as 异常处理 finally 始终执行
	在try以内的代码， 一旦执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码
	可以有多个except来捕获不同类型的错误
	except语句块后面加一个else，当没有错误发生时，会自动执行else语句
	所有的错误类型都继承自BaseException； 异常类型，捕获该类型的错误，还把其子类也“一网打尽”， 注意Exception hierarchy
	try...except 好处： 不需要在每个可能出错的地方写try， 只需要在需要的地方捕获错误， 大大减少了写try...except...finally的麻烦
	如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获
	最底层的错误是错误源头， 格式是错误类型：错误描述
	logging模块记录错误信息, 可以把错误记录到日志文件里，方便事后排查
	捕获一个错误就是捕获到一个错误类的实例
	错误并不是凭空产生的，而是有意创建并抛出的， 内置函数会抛出很多类型的错误
	一个错误可以简单理解为错误名 + 一个提示字符串
	raise之后的语句不执行, 但如果raise之后有finally语句一定执行
	raise语句如果不带参数，就会把当前错误原样抛出
	在except中raise可以把一种类型的错误转化成另一种合理逻辑的类型 
调试：
	方法一： print, 不利： 需要删掉
	方法二： assert 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代,抛出AssertionError， False 时， 执行后面提示字符串
	可以用-O (大写字母O)参数来关闭assert， 关闭后，把所有的assert语句当成pass来看
	方法三： 把print()替换为logging.info()， 利好： logging不会抛出错误，且可以输出到文件， 用法： logging.info()
	添加logging.basicConfig(filename='example.log', level=logging.INFO)得到log info输出
	指定记录信息的级别, debug，info，warning，error等几个级别
	logging通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件, 例如输出到console， logging.getLogger().addHandler(logging.StreamHandler())
	方法四： pdb， 单步方式运行， -m pdb； 1 查看代码； n 单步执行； p 变量名 查看变量； q 退出, 不利： 行数过多时
	方法五： pdb.set_trace(), import pdb, 一个pdb.set_trace()为一个断点， p查看变量，c继续运行
	方法六： IDE
	logging才是终极武器
单元测试：
	覆盖常用的输入组合、边界条件和异常
	单元测试， TDD：Test-Driven Development， 检查一个模块、一个函数或者一个类， 意义：： 验证代码修改
	继承： unittest.TestCase, 不以test开头的方法， 不会被执行
	self.assertEqual, self.assertTrue, self.assertRaises
	两种方法运行： __name__, unittest.main(); 或者 -m unittest, 不带.py
	setUp(), tearDown()分别在每调用一个测试方法的前后分别被执行， 不必在每个测试方法中重复相同的代码。 例如每个方法都要开，关数据库
	单元测试代码要非常简单，防止本身有bug。
文档测试：
	测试代码可以写在注释中，然后，由一些工具来自动生成文档
	“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试, doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确
	只有测试异常的时候，可以用...表示中间一大段烦人的输出
	doctest.testmod()
	"" 和 ''是不同的， 要严格区分
	没有输出，说明都是正确的
	当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执行doctest，因为__main__.Dict， 不必担心doctest会在非测试环境下执行
	作用：：作为测试 +　示例代码
	文档生成工具（pydoc）自动把包含doctest的注释提取出来给用户
	python -m pydoc my_doc   # 比如说: python -m pydoc math   
	pydoc 提供HTML python -m pydoc -w my_doc my_doc.html (或者：python -m pydoc -p 1234 #比如说: 端口为1234;   http://localhost:1234/；)
IO编程：
	IO接口， Stream（流）， 数据就是水管里的水，但是只能单向流动， Input Stream是流进内存， Output Stream从内存流到外面去
	问题：：速度严重不匹配
	CPU等，叫同步IO; 不等，叫异步IO【等汉堡模型】
	异步复杂但性能高， 难度在于通知的时间和方式
	跑过来找到你，这是回调模式； 发短信通知你，你就得不停地检查手机，这是轮询模式
	操作IO的能力都是由操作系统提供的， 每一种编程语言都会把操作系统提供的低级C接口封装起来方便使用
文件读写：
	读写文件是最常见的IO操作， thon内置了读写文件的函数，用法和C是兼容的
	在磁盘上读写文件的功能都是由操作系统提供的， 现代操作系统不允许普通的程序直接操作磁盘
	读写文件的根本：：从操作系统拿到一个文件对象（通常称为文件描述符）， 基本操作就是读和写
	open（encoding="", errors="ignore"）[r, rb, w, wb][IOError, UnicodeDecodeError], close(有错不会调用)
	read()[str 对象], read(size字节), readline(), readlines(按行返回list) 
	write("")
	with...as 抛出异常就关闭， 没有异常就执行with的block
	strip()可以去空格和"\n"
	open()返回对象有read（）， 叫file-like Object， （例如file, StringIO【临时缓冲】， 内存字节流， 网络流， 自定义流）
	默认都是读取文本文件，并且是UTF-8编码的文本文件， 图片、视频是二进制文件["rb"]
	只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失
StringIO和BytesIO：
	本质：：内存中读写
	StringIO在内存中读写str， BytesIO操作二进制数据
	StringIO要么用来读，要么用来写，不能同时用
	StringIO(初始化),BytesIO(), write(), readline(), getvalue()用于获得写入后的str
	本质：：把StringIO类比为内存的文件
操作文件和目录：
	系统：：
	os.name[posix--Linux, Unix, Mac OS X; nt--Windows]
	os.uname[详细系统信息， windows 不提供]
	环境变量：：
	os.environ包含所有操作系统中的环境变量， os.environ.get("key")
	文件和目录：：os 和 os.path， 
	路径变换::一般会有.path
	os.path.abspath('.')--当前目录
	os.getcwd()--获得当前路径
	os.path.join(ori, dirname, 可接多个)--只拼接路径， 不新建目录， 作用： 处理不同操作系统的路径分隔符
	os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)) 得到父目录
	os.path.split()路径拆分为两部分，后一部分总是最后级别的目录或文件名
	os.path.splitext()直接得到文件扩展名
	合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作
    文件操作：：os
	os.mkdir(path)--新建目录
	os.rmdir(path)--删除目录
	os.rename(old, new)
	os.remove删除文件
	shutil模块的copyfile()[shutil.copy(ori, new)]，用于复制文件， 复制文件并非由操作系统提供的系统调用
	sys.stdout = open("stdout.txt", "w")把标准输出定向到文件
	创建新文件要open写， 不能用open读
	过滤文件：：用列表生成器
	listdir列出当前路径的目录和文件， 不包括下一层目录； isdir, isfile
	递归目录：：最好用 root, dirs, files os.walk(path)
	字符串可以用 "sub" in "src"
序列化：
	把变量从内存中变成可存储或传输的过程称之为序列化(变为bytes， string)， Python中叫pickling， 其他语言中也被称之为serialization，marshalling，flattening
	把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling
	pickle.dumps(对象)把任意对象序列化成一个bytes
	pickle.dump(对象， 文件)直接把对象序列化后写入一个file-like Object
	pickle.loads(bytes)反序列化出对象
	pickle.load(文件)从一个file-like Object中直接反序列化出对象
	不加s， 操作文件和file-like object
	这个变量和原来的变量是完全不相干的对象， 它们只是内容相同而已
	pickle版本不兼容， 只能用Pickle保存那些不重要的数据
JSON：对象转化为JSON字符串， Web通用
	在不同的编程语言之间传递对象，就必须把对象序列化为标准格式， 例如XML， JSON
	JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输， 可直接在Web页面中读取
	JSON表示的对象就是标准的JavaScript语言的对象
	json.dumps(对象)， json.dump(对象， 文件)
	json.loads(str), json.load(file)
	定义了__slots__的类， 没有__dict__
	default把对象变dict::json.dumps(s, default=lambda obj: obj.__dict__)
	object_hook把dict变对象：：print(json.loads(json_str, object_hook=dict2student))
进程和线程：
	一边上网，一边听音乐，一边放视频，就是多任务
	打开两个word就启动了两个word进程, 一个Word同时进行打字、拼写检查、打印就是线程
	一个进程至少有一个线程
	多线程的执行方式和多进程是一样的， 由操作系统在多个线程之间快速切换，让每个线程都短暂地交替运行，看起来就像同时执行一样
	为了完成多任务： 方法一：：多进程； 方法二：：一个进程多个线程
	多任务目的：：同时看视频和听音频
	问题：：同步和数据共享
	方法：：画图
多进程：multiprocessing
	本质：：fork()复制一份当前进程， 子进程永远返回0， 父进程返回子进程的ID
	父进程要记下每个子进程的ID， 子进程只需要调用getppid()就可以拿到父进程的ID
	os.fork()放回两次，要么返回0， 要么返回
	os.getpid()获得当前进程ID, getppid（）获得父进程ID
	一旦看到fork， 就把程序走两遍
	Windows没有fork调用
	multiprocessing跨平台版本的多进程模块, Process类来代表一个进程对象
	Process(target=将要执行函数， args=（函数参数）)
	p.start()启动进程， p.join()等待子进程结束， 用于进程间同步
	Process启动单个进程， Pool启动大量的子进程
	p.apply_async(将要执行函数, （函数参数）)
	p.close()不能再添加新的Process， p.join()等待所有子进程执行完毕
	pool默认大小是本机核数
子进程：
	subprocess启动一个子进程，然后控制其输入和输出。常用于执行命令行
	subprocess.call(list)
	subprocess.Popen([list], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	p.communicate(bytes 输入， 例如b'set q=mx\npython.org\nexit\n')
	p.returncode返回退出号
进程间通信：
	进程读写Queue、Pipes来实现通信
	multiprocessing有Queue, Pipes
	time.sleep(random.random())， 写进程常用
	p.terminate()强行终止
	windows 模拟fork(), 父进程所有Python对象都必须通过pickle序列化再传到子进程去, multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了
多线程：
	两个模块， _thread是低级模块，threading是对_thread进行了封装
	threading.Thread(target=函数名, name=线程名)
	current_thread()永远返回当前线程的实例
	主线程实例的名字叫MainThread
Lock:
	多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改
	线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
	本质：：因为高级语言的一条语句在CPU执行时是若干条语句
	目标：：把分步执行的块变为一步执行
	lock = threading.Lock()创建一个锁
	lock.acquire()取锁， lock.release()放锁
	当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁, 然后继续执行代码，其他线程就继续等待直到获得锁为止。
	用try...finally来确保锁一定会被释放。
	不利::
		单线程：：阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行
		死锁：：由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
	解释器执行代码时，有一个GIL锁：Global Interpreter Lock, 线程可创建多个， 但要执行， 必须GIL锁， 100行后释放
	Python中，可以使用多线程，但不要指望能有效利用多核
	可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响
ThreadLocal:
	线程可以有自己的局部变量
	本质：：让线程局部变量，不用传参。 不用查找dict，ThreadLocal自动匹配线程局部参数, 解决了参数在一个线程中各个函数之间互相传递的问题。
	ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息
进程vs.线程：
	多任务Master-Worker模式，Master负责分配任务，Worker负责执行任务
	多进程有利：：稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程
			 当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低
		不利：：创建进程的代价大（内存和CPU），操作系统能同时运行的进程数是有限的
	多线程有利：：通常比多进程快一点
		不利：：任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存
	在Windows下，多线程的效率比多进程要高（进程开销大）
	多进程+多线程的混合模式， 更加复杂
	是否采用多任务考虑两点：：
					线程切换：
						单任务模型 = 批处理任务模型。
						开销：：保存现场（CPU寄存器状态、内存页等）， 准备新环境（恢复上次的寄存器状态，切换内存页等）
						操作系统可能就主要忙着切换任务症状：：硬盘狂响，点窗口无反应，系统处于假死状态
					计算密集型 vs. IO密集型：
						计算密集型：：进行大量的计算，消耗CPU资源， 最高效地利用CPU，代码运行效率至关重要，计算密集型任务同时进行的数量应当等于CPU的核心数， 最好用C语言
						IO密集型：：涉及到网络、磁盘IO的任务都是， 常见的大部分任务都是IO密集型任务，比如Web应用， 代码量越少越好， 选脚本
	异步IO：：用单进程单线程模型来执行多任务（主要是IO任务）， 称为事件驱动模型	
		  用异步IO编程模型来实现多任务是一个主要的趋势
		  本质：：多线程是两个人（多个）完成一个任务
		  	  异步是一个人和一个机器完成一个任务
		  单进程的异步编程模型称为协程
分布式进程：
	Process更稳定， 可分布到多台机器上， Thread最多只能分布到同一台机器的多个CPU上
	multiprocessing， managers子模块把多进程分布到多台机器上
	一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信， 不必了解网络通信的细节，就可以很容易地编写分布式多进程程序
	在一台机器上写多进程程序时，创建的Queue可以直接拿来用, 在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加
	get()有timeout设置

#############################################
补上分布式和正则表达式
#############################################

正则表达式：
	"^"表示行的开头, "$"表示行的结束(它前面的字符，表示必须以这个字符结尾)
	re模块，包含所有正则表达式的功能
	强烈建议使用Python的r前缀， 消除"\\"转义问题
	random.choice(list)随机选择
	三个用处：：匹配， 切分， 提取子串
	re.match(正则表达式， 输入字符串)， 成功返回一个Match对象，否则返回None
	re.split(用来分割的字符串正则表达式， 输入字符串), 但
	正则表达式写法：："字符种类 +　个数　＋顺序"　
	()表示要提取的分组， m = re.match（）， m.group(0) = m.group（）永远是原始字符串, m.group(1)表示第1个子串，m.groups()显示所有分组
	"|"左边是贪婪匹配，右边的最近匹配， 所以位数少的串放后面， 尽量在一个子串内只用一个[], 有[]的地方最好加括号， 慎用"|"
	用正则还是识别不了，或者说写出来非常困难，这时就需要程序配合识别了
	正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符, 个数后面附加"?"就可以转换成非贪婪匹配(和"?"表示"0-1"个不同)， 例如"r'^(\d+?)(0*)$'" 和 "r'^(\d+)(0*)$'"
	编译：：
		正则表达式大量重复使用时，预编译正则表达式更高效，因为每次使用re.match()有两件事：：编译表达式和匹配字符串
		正则对象 = re.compile(正则表达式)， 正则对象.match(输入字符串)
内建模块：
	batteries included, 内置，无需安装
datetime:
	处理日期， 时间
	当前日期和时间：：datetime.now()， 指定日期和时间：：datetime（年，月，日，时，分）【用数字】
	两类导入方法：： （from 模块 import 类） 或者 （import 模块.类）【python2.7不行】
	timestamp是相对1970（epoch time）的秒数， 在1970之前，用负数
	timestamp的值与时区无关， 计算机存储的当前时间用timestamp表示， datetime是有时区的
	datetime类型转换为timestamp用timestamp()【2.7不同】
	Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数（是几百毫秒， 不是几毫秒）
	Java和JavaScript的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法
	datetime.fromtimestamp()把timestamp转换为datetime
	UTC+0:00是格林威治标准时间，datetime.utcfromtimestamp()转换到相对于UTC标准的时间
	处理日期和时间：：首先必须把str转换为datetime
	字符串-->datetime::datetime.strptime（输入字符串， %格式串【'%Y-%m-%d %H:%M:%S'】）（"parse time"）(注意Y大写， 时间HMS大写， 格式串最好不要变)
	datetime-->字符串：：date对象.strftime（%格式串'%a, %b %d %H:%M'）("formatting time")（"%a"星期， "%b"月份， "%d"日期 ）
	timedelta（days=, seconds=, hours=...）对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime
	日期-->其他（string， timestamp）用日期对象函数； 其他-->日期用datetime库函数
	timezone， tzinfo，可以设置时区, now.replace(和当前系统时区相同)
	先通过utcnow()拿到当前的UTC时间，再对象.astimezone()[assert的意思]转换为任意时区的时间
collections：集合模块
	namedtuple：：Point = namedtuple('Point', ['x', 'y'])，函数， 返回自定义的类，规定了tuple元素的个数，用属性引用tuple的某个元素， 不能用索引
				格式：：类名 +　ｔｕｐｌｅ
××××××××××××××××××××××××××××××××××××××××××××××××××××××
补上集合模块
××××××××××××××××××××××××××××××××××××××××××××××××××××××
ｂａｓｅ64:
	本质：：解决不可显示字符， 三个二进制字符， 变成4四个64字符
	64个字符来表示任意二进制数据, 3个字节的二进制数，再分成4组，每组6个bit， 2e6 = 64， 然后查字符表， 4组变成4个字符，
	不是3的倍数， "\x00"字节在末尾补足后, 再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉
	"\x00"表示一个字节, 始终按6bit分组
	base64.b64encode(b'普通字符串')， base64.b64decode(b'64字符串')
	"url safe"的base64编码， 把字符+和/分别变成-和_， 因为+和/，在URL中就不能直接作为参数
	base64.urlsafe_b64encode(), base64.urlsafe_b64decode()
	Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行
	Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等
	=用在URL、Cookie里面会造成歧义， 很多Base64编码后会把=去掉， 但一个字节需保留两个字符， 解码时候加上=把Base64字符串的长度变为4的倍数
	Base64常用于在URL、Cookie、网页中传输少量二进制数据
	4*"="可以产生4个等号
	Python的思想是：：一定不要把问题想复杂了
	"%"是取余， "/"是除法
struct:
	本质：：单字节和多字节的转换
	意义：：可以处理图像数据
	C语言用struct、union来处理字节，以及字节和int，float的转换
	字节数组b'str' ＝ 二进制str
	本质是用位运算， 例如（"&", ">>"）解决
	struct.pack（'处理命令'， 数字）， 例如 struct.pack('>I', 10240099)，>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数 
	参数个数要和处理指令一致
	struct.unpack（'处理命令'， bytes串）
	例如struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数：：(4042322160, 32896) 
	.bmp文件，读入前30个字节分析， 例如struct.unpack('<ccIIIIIIHH', s)， 'c'表示字符，一个字节, '<'看作图片序（小端方式little-endian）,不同于网络序, 'H'两个字节, "I"， 4个字节
	Little-Endian：：低位字节排放在内存的低地址端，是反序； Big-Endian高位字节排放在内存的低地址端，是正序
hashlib:
	哈希算法本质：：一个函数，把任意长度的数据转换为一个长度固定的数据串， 目的是为了发现原始数据是否被人篡改过
	提供常见哈希算法（digest）：：MD5, SHA1
	MD5：：固定的128bit字节， 通常用一个32位的16进制字符串 
		hashlib.md5(), 对象.update('utf-8'的字符串)， 对象.hexdigest()
		如果数据量很大，可以分块多次调用update(), 调用时注意, update()返回None
		两个字符串的MD5值一样的概率非常非常低。
	SHA1：:
		160 bit字节，通常用一个40位的16进制字符串
		hashlib.sha1(), 对象.update('utf-8'的字符串)， 对象.hexdigest()
		比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长
	算法应用：：保存用户密码
		    对比用户输入的明文口令的MD5和数据库中的MD5，如果一致，说明口令输入正确，如果不一致，口令肯定错误
		    即使运维人员能访问数据库，也无法获知用户的明文口令
		    不同输入串可能有相同MD5串， 但不同的MD5串，一定有不同的输入串
		    'the-Salt'加盐法， 对原始口令加一个复杂字符串， 计算出哈希值， 然后存入数据库， get_md5(password + 'the-Salt')
		    把登录名作为Salt的一部分来计算MD5， 实现相同口令的用户也存储不同的MD5
		    摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令
itertools:
	用于操作迭代对象， 返回值不是list，而是Iterator
	无限迭代器：：
			itertools.count(1)自然数序列； itertools.cycle（字符串）传入的序列无限重复，itertools.repeat（"A", 3）可限定重复次数 
			无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来
			itertools.takewhile根据条件判断来截取出一个有限的序列， 例如：：itertools.takewhile(lambda x: x <= 10【True】, natuals)
	迭代器操作函数：：
		chain(str, str)把一组迭代对象串联起来，形成一个更大的迭代器
		groupby(str)把迭代器中相邻的重复元素挑出来放在一起
		groupby挑选规则是通过函数返回值一致判定的， 例如itertools.groupby('AaaBBbcCAAa', lambda c: c.upper())
XML:
	操作XML两种方法：DOM和SAX, 大量处理用beautifulsoup
	DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点
	SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件
	正常情况下，优先考虑SAX，因为DOM太占内存
	SAX本质：：为三个事件传入处理函数, 可以是单独函数， 也可以是类里函数(StartElementHandler, EndElementHandler, CharacterDataHandler)
	SAX::当SAX解析器读到一个节点时，如<a href="/">python</a>产生3个事件::
															  start_element事件，在读取<a href="/">时::def start_element(self, name, attrs)
															  char_data事件，在读取python时::end_element(self, name)
															  end_element事件，在读取</a>时::char_data(self, text)
    from xml.parsers.expat import ParserCreate
    StartElementHandler可以处理</>模式
    读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存起来，在EndElementHandler里面再合并
    最简单也是最有效的生成XML的方法是拼接字符串, L.append(), ''.join(L), 复杂拼接用JSON
HTMLParser:
	最方便的还是beautifulsoup
	HTML本质上是XML的子集, 语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML
	搜索引擎::
			第一步是用爬虫把目标网站的页面抓下来
			第二步就是解析该HTML页面
	解析HTML本质：：继承HTMLParser， 重写函数（handle_starttag，handle_endtag，handle_startendtag，handle_data，handle_comment，handle_entityref，handle_charref）
	feed()方法可以多次调用，不需传入整个HTML字符串，可部分传入
	两种特殊字符：：英文，"&nbsp;"(解析出来是nbsp), 数字"&#1234;"
	soup = BeautifulSoup(HTML文件, "html.parser"), soup.select(str)
	正则：：re.findall("正则表达式"， HTML文件)
urllib:
	操作URL::Get, Post, Handler
	Get::
		request模块抓取URL内容, request.urlopen("url"), url文件对象.getheaders(), url文件对象.status（200）, url文件对象.reason（OK）， url文件对象.read()
		GET请求是浏览器发送的， 使用Request对象， 然后添加HTTP头，可把请求伪装成浏览器(request.Request("url")), request对象.add_header（key, value）, request.urlopen(request对象)
		遇到中文等， 要记得decode('utf-8')
		import requests， requests.get("url").text和from urllib import request, request.urlopen("url")都可以返回html给浏览器解析， 后者可以拿到报文的metadata（header）
	Post::
		以POST发送一个请求，两步：：
							一、把参数data变为"&"bytes("data=parse.urlencode([(),])"变为"username=email&password=passwd&")
							二、传入data，例如request.urlopen(req, data=)
	Handler::
			实现更复杂的控制
			通过一个Proxy去访问网站，需要利用ProxyHandler来处理,Proxy Server是网络信息的中转站（cache）， VPN（Virtual Private Network）企业内部专线
			代理：：帮助内网client访问外网server用的（比如HTTP代理）
			反向代理：：将来自外网client的请求forward到内网server
			本质：：Proxy帮助client集中request发送到server， 反向Proxy帮助server分配request给各个server
			"User-Agent"头就是用来标识浏览器的
			代理访问两步分：：proxy_handler（代理器地址）, proxy_auth_handler（password等）
			注意导入：：from urllib import request， 不要直接import urllib
常用第三方模块:
	在PyPI-the Python Package Index上注册, 用pip安装
PIL：
	PIL：Python Imaging Library, 图像处理标准库; Pillow是新版PIL
	操作图像::
			切片、旋转、滤镜、输出文字、调色板
			图像缩放::Image.open()【不用关闭】, im.size【就是w, h】,im.thumbnail((w, h)), im.save(str."格式")
			模糊效果::本质是加滤镜，Image.open(), im.filter(ImageFilter.BLUR), im.save()
			绘图::生成字符验证码::八步法::
							  随机生成字符chr(random.randint(65, 90))
							  随机生成颜色(random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
							  图片大小width， height
							  生成图片Image.new('RGB', size, color)
							  生成字体ImageFont.truetype('Arial.ttf', 36)【下载字体文件】
							  填充每个像素ImageDraw.Draw(image), draw.point((x, y),fill=(a,b,c)【color】))
							  填充文字draw.text((x, y), 字符, font=字体, 颜色)
							  模糊，保存image.filter(ImageFilter.BLUR), image.save()
			itertools.combinations(list, 几个槽)， itertools.permutations(list, 几个槽)
			sys.version_info判断python版本















