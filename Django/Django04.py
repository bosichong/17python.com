#codeing=utf-8
# @Time    : 2017-11-20
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : 实战：利用Django开发部署自己的个人博客（4）Models 数据模型
# @Url     : http://www.17python.com/blog/56
# @Details : 实战：利用Django开发部署自己的个人博客（4）Models 数据模型
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 实战：利用Django开发部署自己的个人博客（4）Models 数据模型
###################################
'''
几乎所有的程序都会和数据打交道，之前以极简方式了解了一下`Python`中操作`sqlite3`，应该是很简单了，但如果你更深入的学习了`Django`中的`QuerySet API`，你会发现利用`Django ORM`打理你的数据库会更方便直观。
`Django ORM` 是完全可以脱离WEB使用的，为了更加直观，我们这次只用Django的数据模型做些简单的测试,如果使用ORM方式进行数据库操作就不用写SQL语句了。

## `Django`中配置数据库

你可以创建一个新项目和新应用，我们继续使用之的`blog01`项目。
设置`blog01.settings.py` 

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

这里设置数据库的物理位置及使用何种数据库，我们这里使用`sqlite3`数据库。

## 创建表及字段

在`myblog.models.py`中输入以下代码：

    from django.db import models
    #创建文章表，通过继承models.Model来创建文章表
    class Article(models.Model):
        title = models.CharField(max_length=50, verbose_name = 'blog标题', default = '')#创建标题
        content models.TextField(berbose_name = '博客正文', default = '')

这样的话我就创建了一个博客文章表及两个字段，其中包括标题及文章内容，可能有同学会问，文章怎么可能就只有二个字段？要不要一起都建好？
不要急，Django的强大之处就是可以随时升级修改你的数据库，稍后我们还会继续填添加其它表及字段的。

## 运行终端创建数据库表

终端进入项目目录`blog01`,运行:`python3 manage.py makemigrations `

    ➜  blog01 git:(master) ✗ python3 manage.py makemigrations 
    Migrations for 'myblog':
    myblog/migrations/0001_initial.py
        - Create model Article
    ➜  blog01 git:(master) ✗ 

`0001_initial.py`是什么？我可以打开看看。
通过源代码查看，可以发现，这是一个数据库表创建代码文件，在我们执行这个文件前，数据库是没有创建的，这个可以在数据库管理软件中查看难。
那么我们现在就通过`Django`执行命令创建数据表。

终端运行:`python3 manage.py makemigrations `

    ➜  blog01 git:(master) ✗ python3 manage.py migrate
    Operations to perform:
    Apply all migrations: admin, auth, contenttypes, myblog, sessions
    Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying myblog.0001_initial... OK
    Applying sessions.0001_initial... OK

好家伙，这不对哇，我明明是创建了一个数据表，怎么出来这么多？哈，如果你是头一次创建Django的数据库表，他会把一些项目自带的数据表一起创建了，
当然这其中也包括你刚刚创建的数据库及表`Applying myblog.0001_initial... OK`
我们通过`DBeaver`来查看表结构：
![]()

到这里我们的数据表创建完毕，拉下来我们操作我们的表，进行增删改查。

## `Django ORM CURD`操作

这里我们使用`Django shell`，强大的终端数据库操作命令`python3 manage.py shell `。

    ➜  blog01 git:(master) ✗ python3 manage.py shell   
    Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04) 
    [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> from myblog.models import Article as ac #导入模型类
    >>> ac.objects.create(title='222',content='22222222222222222222222')#添加一条记录
    <Article: Article object>
    >>> s = ac.objects.get(title='222')#查询一条记录
    >>> print(s)
    Article object
    >>> print(s.title)
    222
    >>> print(s.content)
    22222222222222222222222
    >>> print(s.id)
    2

强大无须多言，我觉得有一点点面向对象编程经验的同学一眼就能看明白这些代码的含意。
我们发现，`Django`为表自动创建了一个自增主键，很方便哈。

附一些常用字段参数

    primary_key = False/True   # 是否设置为主键
    blank = False/True         # 是否可为空，这其实是用于Field的判断
    null = False/True          # 是否可为空，这才是真正的数据库里面是否可以为null
    max_length = 3             # 最大长度，对整型无效
    default = ''               # 设置默认值
    verbose_name =             # 相当于备注，如果没给出那么就是该字段,当然，要指定的话，可以直接第一个参数一个字符串就可以指定了
    editable = False/True      # 是否可编辑
    unique = False/True        # 是否唯一
    auto_now = False/True      # 用于时间，每次更新记录的时候更新该字段
    auto_now_add = False/True  # 用于时间，创建新纪录的时候自动更新该字段
    choices # 很实用的一个功能，相当于存储一个枚举列表，其中左边的key是实际存储在数据库中的值，例如，可以这样定义一个字段：
        YEAR_IN_SCHOOL_CHOICES= (
            ('FR', 'Freshman'),
            ('SO', 'Sophomore'),
            ('JR', 'Junior'),
            ('SR', 'Senior'),
        )
        然后在定义字段的时候给个参数choices=YEAR_IN_SCHOOL_CHOICES，在插入字段的时候，使用'RF'这样的，在获取字段值的时候这样：p.get_year_in_school_display()即可显示'Freshman'
    verbose_name        # 定义字段的注释

字段中的常用类型。

    # 数字类型：
    AutoField        # 自增长字段
    IntegerField    # 长度为11的整数
    PositiveIntegerField：
    SmallIntegerField
    PositiveSmallIntegerField
    BigIntegerField：
    BinaryField：
    BooleanField：
    NullBooleanField：
    DecimalField(max_digits = None, decimal_places = None)
    FloatField

    # 字符类型
    CharField    # 字符串类型，可用max_length指定长度，枚举类型也使用该方式，只需要指定枚举枚举元组即可，例如type = models.CharField('类型', choices=CONTENT_TYPE)，其中CONTENT_TYPE=(('a', 'abc'))
    TextField：text类型
    CommaSeparatedIntegerField：用逗号分隔的整数，我擦，这有用

    # 时间类型
    DateField    # DATE类型
    TimeField    # datetime.time，时间
    DateTimeField()    # DATETIME类型，包括了日期和时间，需要注意的是Django默认的TIME_ZONE是UTC，在初始化的时候，格式如"2015-04-27T15:01:00Z"，它属于python里面的datetime.datetime类型，可分别用year/month/day等获取时间。另外Django如果要实用MySQL里面的TIMESTAMP类型也是用该字段表示，并且在插入的时候不能直接插入一个整数，依然只能插入一个datetime.datetime对象，用时间戳的时候USE_TZ必须为False
    unique_for_date属性：比如，如果有一个title字段，其有一个参数unique_for_date = "pub_date"，那么该表就不会出现title和pub_date同时相同的情况，其它的还有unique_for_month,unique_for_year

    其它很有用的类型：
    EmailField：Email邮箱类型
    FileField：文件类型，不过不能设置为primary_key和unique，要使用该字段还有很多需要注意的地方，具体的见官方文档
    FilePathField：同上
    ImageField
    IPAddressField：从1.7开始已经不建议使用了，应该使用下面这个
    GenericIPAddressField：
    URLField
    UUIDField

通过上边简单的小例子，我们体验了强大简单的`Django shell`,ORM使我们从繁琐SQL重复的SQL语句编写中解脱出来，
而且终端下的操作大大提高了对数据库操作验证的简单性，同时我们也可以发现`Django ORM `是完全可以脱离WEB使用的，只要做好配置文件，使用正确的目录即可。


'''

