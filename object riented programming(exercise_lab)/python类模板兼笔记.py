#python3面向对象，入门介绍参考：《Python编程：从入门到实践（第2版）》 网站博客不如好书
#按过程逐行调试程序、变量查看是debug神器
class parent_class_name_0:#父类0
    #...
    def __init__(self,praent_init_vale):
        print('praent_0_init_vale: ',praent_init_vale)
        pass
    def parent_class_name_0_method(self,):#通过
        
            pass

class parent_class_name_1:#父类1
    def __init__(self,praent_init_vale):
        print('praent_1_init_vale: ',praent_init_vale)
    #...
    pass

class another_class:#其他类
    def __init__(self,init_vale):
        print('another_class init:',init_vale)
    pass


class class_name(parent_class_name_0,parent_class_name_1):   #定义类名称；class_name后的括号及括号内的内容仅在需要继承父类时才需要。
    #类只有在实例化才能成为能够操作的对象，例如object_name=class_name(initial_parameter)

    #类的属性【变量】声明定义方法有两种：
    #1.直接在这里（类方法【函数之外】）直接声明定义，！！注意该方法有坑，不建议使用，说明见下和底部！！
    #2.在类函数中以self.变量名=值，的方式声明定义
    #类中变量名规则介绍https://www.cnblogs.com/hls-code/p/14777980.html
    #类的 公有 属性【变量】（能从外部能够访问，如：object.public_class_attrs=）
    public_class_attrs=[]#注意在这里定义的属性【变量】只会被运行一次，即在程序第一次从头开始运行时，解释器仅会在第一次记录类的命名信息时会运行在此的程序内容。
    #所以即意味着，如果后期多次调用该类的初始化方法__init__(...)实例化变量，！但是！该区域内的定义属性【变量】语句将不再被执行，即该区域定义的属性【变量】无法被清空刷新，且上一次若该属性【变量】被改变，则下一次实例化类时将继续使用上一次被改变的值。

    public_class_attrs_object=another_class('another_class')#将其他类的实例用作属性，可以将大型类拆分成多个协同工作的小类，与继承无关。

    #类的 私有 属性【变量】（只能在类的内部调用，不能在类的外部调用，如在类中使用self.__private_class_attrs访问，注意self是关键字，且双下划线也是变量名的组成部分）
    __private_class_attrs=[]#同上，非函数内定义类变量会导致可能因变量变动导致对下一次实例化影响

    def __init__(self,init_vale): #类基本方法【函数】--构造方法，类的实例化操作时会第一个运行该方法，self表示将调用 类的实例中的内容（属性或方法【变量或函数】）
        self.public_class_attrs.append(init_vale)#将初始化值作为类公有变量存储
        self.__private_class_attrs.append(init_vale)#将初始化值作为私有类变量存储
        self.public_class_attrs_in_init=[]#在__init__初始化方法中，同样能申明定义类变量，如此处定义了一个类公有变量public_class_attrs_in_init。
        self.public_class_attrs_in_init.append(init_vale)#并且为public_class_attrs_in_init赋值形参init_vale；并且通常建议使用这种方式申明定义变量，因为该方法申明定义的变量不会对下一次再实例化类时产生影响，即每次实例化时都会被重新申明定义，而不像在如上面那样。
        #【可选】：类的继承，继承是指子类（）从父类（超类、基类）获得所有属性和方法，从而使实例化的子类对象能够具有父类所有的方法和属性，通常用于编写另一个现成类的特殊版本。
        super().__init__('to_parent_class_0')#单继承,【子类继承父类所有属性方法】 #父类也称为超类 （superclass），名称super 由此而来。
        super().__init__('to_parent_class_1')#多重继承,【子类继承所有父类的所有属性方法】
        pass
    
    #类的 公有 方法【函数】（能从外部能够访问，如：object.method(...) ）
    def method(self,):#与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例，而不是类。
        print('public_class_attrs,self:',self.public_class_attrs)#打印类实例化的传入参数
        print('public_class_attrs_in_init:',self.public_class_attrs_in_init)
        pass

    #类的 私有 方法【函数】（能从外部能够访问，如：object.__method(...) ）
    def __method(self,):#注意事项同上，且不能被子类覆写（重写）
        pass

    #【可选】覆写（重写）：在继承中，使用与父类相同的方法【函数】名称，实现对父类的方法的覆写（重写），注意会导致子类实例中，父类原先的方法无法【函数】再调用，（即用当前子类方法【函数】，覆盖原先父类中同名称的方法【函数】功能)，该功能通常用于保留从父类那里继承而来的精华，并剔除不需要的糟粕。
    def parent_class_name_0_method(self,):#通过
        pass
    


#类具有（保留）专有属性和方法。
#附：python不支持函数（方法）重载,该特性允许创建多个具有不同实现的同名函数。对重载函数的调用会运行其适用于调用上下文的具体实现，即允许一个函数调用根据上下文执行不同的任务。。
child_class_object=class_name('test_class_init_vale0')
child_class_object.method()
child_class_object=class_name('test_class_init_vale1')
child_class_object.method()#注意！运行结果：another_class init: another_class仅出现一次，还有public_class_attrs,self: ['test_class_init_vale0', 'test_class_init_vale1']
#由运行结果another_class...出现一次和['test_class_init_vale0']→['test_class_init_vale0', 'test_class_init_vale1']可发现于类函数之外定义申明的变量将不会在类实例化时重置，即对其影响将延续到下一次类的实例化