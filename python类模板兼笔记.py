#python3面向对象，入门介绍参考：https://www.runoob.com/python3/python3-class.html
class class_name:   #定义类名称
    #类只有在实例化才能成为能够操作的对象，例如object_name=class_name(initial_parameter)


    #类中变量名规则介绍https://www.cnblogs.com/hls-code/p/14777980.html
    #竟然能够通过实例.新变量名=xx的方式给实例对象新增属性.....诡异，太随便了喂
    #类的 公有 属性【变量】（能从外部能够访问，如：object.public_class_attrs=）
    public_class_attrs=''

    #类的 私有 属性【变量】（只能在类的内部调用，不能在类的外部调用，如在类中使用self.__private_class_attrs访问，注意self是关键字，且双下划线也是变量名的组成部分）
    __private_class_attrs=''

    def __init__(self,): #构造方法，类的实例化操作时会自动调用该方法，self表示将调用 类的实例中的内容（属性或方法【变量或函数】）
        
        parent_class_name_0.__init__(self,)#单继承
        parent_class_name_1.__init__(self,)#多重继承
        pass
    
    #类的 公有 方法【函数】（能从外部能够访问，如：object.method(...) ）
    def method(self,):#与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例，而不是类。
        pass

    #类的 私有 方法【函数】（能从外部能够访问，如：object.__method(...) ）
    def __method(self,):#注意事项同上，且不能被子类覆写（重写）
        pass

    #在继承中，使用与父类相同的方法【函数】名称，实现对父类的方法的覆写（重写），注意会导致父类原先的方法无法被重载（无法在实现原函数调用），（即用当前子类方法【函数】，覆盖原先父类中同名称的方法【函数】功能)
    def parent_class_method(self,):#通过
        pass

    '''#类的（保留）专有方法(同样支持重载)：
    __init__ : 构造函数，在生成对象时调用
    __del__ : 析构函数，释放对象时使用
    __repr__ : 打印，转换
    __setitem__ : 按照索引赋值
    __getitem__: 按照索引获取值
    __len__: 获得长度
    __cmp__: 比较运算
    __call__: 函数调用
    __add__: 加运算
    __sub__: 减运算
    __mul__: 乘运算
    __truediv__: 除运算
    __mod__: 求余运算
    __pow__: 乘方
    '''

#以下为在程序中的演示
#重载，对父类方法的调用，可在继承后使用父类方法的同名称方法实现。
super(child.child_class_object).parent_class_method()# super(子类名称，子类实例名称).同名父类函数名称()