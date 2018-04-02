# python-spyder
python爬虫教程与实战
## <font color="red">一、依赖库与环境</font>
 
 - python3.X（3.6）
 - [BeautifulSoup (bs4)][1]
 - [requests][2]
上述依赖的安装教程和文档不再赘述，看↑的链接~
 ---
## <font color="red">二、基础教程</font>

### 爬虫简介
**网络爬虫**[（百度百科）][3]（又被称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者），是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫。
简单来讲，爬虫也就是按照需求抓取某一个网站上的内容和子链接上的内容。
### 审查元素
在了解爬虫之前，我们需要知道审查元素的概念。
所谓的**审查元素**，是Google Chrome浏览器提供的一项服务功能，用户只需右键点击“审查元素”（名字），即可打开Chrome Inspector，获得网页各种元素的加载时间、Javascript函数、Object等信息。
#### html标签与属性
一个网页，实质就是一个html文件，在我们输入一个网址，网址被送到DNS服务器解析成IP地址，然后我们的客户端根据这个IP地址，连接到网址对应的实体服务器/云服务器，一个html文件就从服务器端传输到我们的客户端，经过浏览器的渲染，成为了我们能看见的网页。
**子节点，父节点，孙节点和兄弟节点：**

### 静态网页爬虫

### html解析
#### 正则表达式处理
#### Xpath
#### Beautiful Soup



---
## <font color="red">三、高级功能</font>
### 登陆功能
### 长间隔
### 动态网页爬虫
### 异步XHR爬取
### 反爬虫
### 多代理解析

---
## <font color="red">四、实战</font>

### 小说下载
#### 目的
#### 分析
#### 代码整合
#### 结合

### 表格数据爬取
#### 目的
#### 分析
#### 代码整合
#### 结果

---
## <font color="red">Reference</font>


1. [CSDN博客][4]
2. 
<To be continue>

  [1]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
  [2]: http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
  [3]: https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711?fr=aladdin&fromid=22046949&fromtitle=%E7%88%AC%E8%99%AB
  [4]: http://blog.csdn.net/c406495762
