Python3自定义模块安装到site-packages
##模块就是将一个或多个函数保存在文件中
前提条件：
1、创建一个mymodules的文件夹
2、有一份你的函数所在的py文件（我这里命名为vsearch.py）

####使用‘setuptools’将模块安装到site-packages中需要以下3个步骤：
①第一步创建一个发布描述，必须有一个名为setup.py的文件
```
#from setup.py
from setuptools import setup
setup(
    name='vsearch',  #name参数指定发布包，一般以模块命名发布包
    version='1.0',
    description='The Head First Python Search Tools',
    author='testerZ',
    author_email='testerZ@qq.com',
    py_modules=['vsearch'],  #里面包含所有.py文件，当前只有vsearch.py
)
```
除了setup.py还要求有README.txt文件，当如包的描述，允许为空

②生成发布文件
在mymodules目录下，运行命令行窗口
```
py -3 setup.py sdist
```
![image.png](https://upload-images.jianshu.io/upload_images/23087403-6f4497442b487bfb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

removing 'vsearch-1.0' (and everything under it)看到这个消息表示发布成功，vsearch-1.0这是一个可安装文件里面包含了你的源代码，mymodules目录下多了两个文件
![image.png](https://upload-images.jianshu.io/upload_images/23087403-80c6799f4c540e50.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


③安装发布文件
你会在dist文件夹下找到新创建的这个Zip（或tar）文件（根据自身系统），cd进入到dist目录下进行安装
```
py -3 -m pip install vsearch-1.0.tar.gz
```
![image.png](https://upload-images.jianshu.io/upload_images/23087403-ec41d5f6bfe65cc6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

最后在你任意的py文件中就可以使用
```
import vsearch
```

注意：如果后续决定更新某个模块的代码，按照前面3个步骤重新安装到site-packages，但是要在setup.py文件中指定一个新的版本。