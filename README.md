spider
======

a spider for picture

python spider.py -h查看帮助

试例一：
python spider.py -u "http://www.22mm.cc/" -o "g:\mm" -n 20 -ad "meimei22.com" -c "utf-8" -l 100

试例二：
python spider.py -u "http://girl-atlas.com/" -o "g:\meitu" -n 500 -r 2 -ae "jpg!mid" -ae "jpg!pre" -ae "jog!prev" -ad "upaiyun.com" -t 0.001

一、设计思路

1、访问页面

2、解析结果

3、将图片存到本地

二、工具选择

1、用pycurl进行网络访问

2、用lxml解析

3、用磁盘存放图片文件

三、简单接口实现

1、网络访问接口request()

2、页面解析接口start_parse()

3、图片存储接口store_picture()


四、Demo

访问"http://www.22mm.cc/"页面，并将该页面中的图片存到磁盘中

五、功能完善

1、增加消重功能

2、增加url提取功能，将解析出来的url继续爬取

六、功能包装

1、设计Dispatcher线程类，用于包装访问页面，解析结果功能

2、设计Collector线程类，用于包装页面消重，图片存储功能

3、设计Task类，用于存放任务相关信息

4、设计Config类，用于存放配置信息

七、功能完善

1、Dispatch类中加入图片数限制功能

2、在Dispatch与Collect类中加入多线程策略

3、增加最大线程数限制功能
 
八、测试，功能完善

1、增加自定义编码功能

2、增加自定义文件类型功能

3、增加自定义爬取域名功能

4、增加外链爬取功能

九、测试，性能调优

1、增加自动加速策略
