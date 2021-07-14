### 起因
一句话，懒得扣js，因为某些网站又臭又长，时不时会更新某些参数
这个项目比自动化快点，省点资源，但是相同条件下是不会超过算法还原的，
### 想法
在渣总的sekiro框架的启发下，友情链接https://github.com/virjar/sekiro，具体介绍可以看官方文档
主要思路就是使用sekiro可以对浏览器进行执行js的操作，比如直接执行document.cookie就能拿到目标网站的
cookie，前提可以配置好相关的配置，具体配置服务可以参考本项目中的sekiro.js，搭建服务的话，自己看官方文档就行，
，通过sekiro可以拿到那个cookie，但是我们需要注入js，
在群里的大佬推荐下，发现了ichrome这个库，这个相对selenium等自动化工具来说轻便了很好，没有特别多的特征
正好符合我们的需求，而且api非常的人性化，也比较简单，然后我们执行js就能进行一个简单的注入。
然后我们通过sekiro就行拿到数据，假如我们拿cooKie话，在cookie失效的时候，直接进行一个页面的刷新
然后就能拿到一个新的cookie，这样的话比直接使用自动化工具快了很多，而且检测力度较小，
### 项目目录：
chrom 对浏览器的一个操作
port_fd是对浏览器端口的一个转发
sekiro是远程调用浏览器的一个操作