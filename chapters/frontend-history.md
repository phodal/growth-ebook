细细整理了过去接触过的那些前端技术，发现前端演进是段特别有意思的历史。人们总是在过去就做出未来需要的框架，而现在流行的是过去的过去发明过的。如，响应式设计不得不提到的一个缺点是：**他只是将原本在模板层做的事，放到了样式（CSS）层来完成**。

复杂度同力一样不会消失，也不会凭空产生，它总是从一个物体转移到另一个物体或一种形式转为另一种形式。

如果六、七年前的移动网络速度和今天一样快，那么直接上的技术就是响应式设计，APP、SPA就不会流行得这么快。尽管我们可以预见未来这些领域会变得更好，但是更需要的是改变现状。改变现状的同时也需要预见未来的需求。

###什么是前端？

维基百科是这样说的：前端Front-end和后端Back-end是描述进程开始和结束的通用词汇。前端作用于采集输入信息，后端进行处理。计算机程序的界面样式，视觉呈现属于前端。

这种说法给人一种很模糊的感觉，但是他说得又很对，它负责视觉展示。在MVC结构或者MVP中，负责视觉显示的部分只有View层，而今天大多数所谓的View层已经超越了View层。前端是一个很神奇的概念，但是而今的前端已经发生了很大的变化。

你引入了Backbone、Angular，你的架构变成了MVP、MVVM。尽管发生了一些架构上的变化，但是项目的开发并没有因此而发生变化。这其中涉及到了一些职责的问题，如果某一个层级中有太多的职责，那么它是不是加重了一些人的负担？

##前端演进史

过去一直想整理一篇文章来说说前端发展的历史，但是想着这些历史已经被人们所熟知。后来发现并非如此，大抵是幸存者偏见——关注到的都知道这些历史。

###数据-模板-样式混合

在有限的前端经验里，我还是经历了那段用Table来作样式的年代。大学期间曾经有偿帮一些公司或者个人开发、维护一些CMS，而Table是当时帮某个网站更新样式接触到的——ASP.Net（maybe)。当时，我们启动这个CMS用的是一个名为``aspweb.exe``的程序。于是，在我的移动硬盘里找到了下面的代码。

```html
<TABLE cellSpacing=0 cellPadding=0 width=910 align=center border=0>
  <TBODY>
  <TR>
    <TD vAlign=top width=188><TABLE cellSpacing=0 cellPadding=0 width=184 align=center border=0>
        <TBODY>
        <TR>
          <TD><IMG src="Images/xxx.gif" width=184></TD></TR>
        <TR>
          <TD>
            <TABLE cellSpacing=0 cellPadding=0 width=184 align=center 
            background=Images/xxx.gif border=0>
```            

虽然，我也已经在HEAD里找到了现代的雏形——DIV + CSS，然而这仍然是一个Table的年代。

```html
<LINK href="img/xxx.css" type=text/css rel=stylesheet>
```

**人们一直在说前端很难，问题是你学过么？？？**

**人们一直在说前端很难，问题是你学过么？？？**

**人们一直在说前端很难，问题是你学过么？？？**

也许，你也一直在说CSS不好写，但是CSS真的不好写么？人们总在说JS很难用，但是你学过么？只在需要的时候才去学，那肯定很难。**你不曾花时间去学习一门语言，但是却能直接写出可以work的代码，说明他们容易上手**。如果你看过一些有经验的Ruby、Scala、Emacs Lisp开发者写出来的代码，我想会得到相同的结论。有一些语言可以让写程序的人Happy，但是看的人可能就不Happy了。做事的方法不止一种，但是不是所有的人都要用那种方法去做。

过去的那些程序员都是**真正的全栈程序员**，这些程序员不仅仅做了前端的活，还做了数据库的工作。

```sql
Set rs = Server.CreateObject("ADODB.Recordset")
sql = "select id,title,username,email,qq,adddate,content,Re_content,home,face,sex from Fl_Book where ispassed=1 order by id desc"
rs.open sql, Conn, 1, 1
fl.SqlQueryNum = fl.SqlQueryNum + 1
```

在这个ASP文件里，它从数据库里查找出了数据，然后Render出HTML。如果可以看到历史版本，那么我想我会看到有一个作者将style=""的代码一个个放到css文件中。

在这里的代码里也免不了有动态生成JavaScript代码的方法：

```javascript
show_other = "<SCRIPT language=javascript>"
show_other = show_other & "function checkform()"
show_other = show_other & "{"
show_other = show_other & "if (document.add.title.value=='')"
show_other = show_other & "{"
```

请尽情嘲笑，然后再看一段代码：

```javascript
import React from "react";
import { getData } from "../../common/request";
import styles from "./style.css";


export default class HomePage extends React.Component {
  componentWillMount() {
    console.log("[HomePage] will mount with server response: ", this.props.data.home);
  }

  render() {
    let { title } = this.props.data.home;

    return (
      <div className={styles.content}>
        <h1>{title}</h1>
        <p className={styles.welcomeText}>Thanks for joining!</p>
      </div>
    );
  }

  static fetchData = function(params) {
    return getData("/home");
  }
}
```

10年前和10年后的代码，似乎没有太多的变化。有所不同的是数据层已经被独立出去了，如果你的component也混合了数据层，即直接查询数据库而不是调用数据层接口，那么你就需要好好思考下这个问题。你只是在追随潮流，还是在改变。用一个View层更换一个View层，用一个Router换一个Router的意义在哪？

###Model-View-Controller

人们在不断地反思这其中复杂的过程，整理了一些好的架构模式，其中不得不提到的是我司Martin Folwer的《企业应用架构模式》。该书中文译版出版的时候是2004年，那时对于系统的分层是

层次	   | 职责
-------| -----
表现层  | 	提供服务、显示信息、用户请求、HTTP请求和命令行调用。
领域层  | 	逻辑处理，系统中真正的核心。
数据层  | 	与数据库、消息系统、事物管理器和其他软件包通讯。

化身于当时最流行的Spring，就是MVC。人们有了iBatis这样的数据持久层框架，即ORM，对象关系映射。于是，你的package就会有这样的几个文件夹：

```
|____mappers
|____model
|____service
|____utils
|____controller
```

在mappers这一层，我们所做的莫过于如下所示的数据库相关查询：

```java
@Insert(
        "INSERT INTO users(username, password, enabled) " +
                "VALUES (#{userName}, #{passwordHash}, #{enabled})"
)
@Options(keyProperty = "id", keyColumn = "id", useGeneratedKeys = true)
void insert(User user);
```    

model文件夹和mappers文件夹都是数据层的一部分，只是两者间的职责不同，如：

```java
public String getUserName() {
    return userName;
}

public void setUserName(String userName) {
    this.userName = userName;
}
```

而他们最后都需要在Controller，又或者称为ModelAndView中处理：

```java
@RequestMapping(value = {"/disableUser"}, method = RequestMethod.POST)
public ModelAndView processUserDisable(HttpServletRequest request, ModelMap model) {
    String userName = request.getParameter("userName");
    User user = userService.getByUsername(userName);
    userService.disable(user);
    Map<String,User> map = new HashMap<String,User>();
    Map <User,String> usersWithRoles= userService.getAllUsersWithRole();
    model.put("usersWithRoles",usersWithRoles);
    return new ModelAndView("redirect:users",map);
}
```

在多数时候，Controller不应该直接与数据层的一部分，而将业务逻辑放在Controller层又是一种错误，这时就有了Service层，如下图：

![Service MVC](./assets/article/images/frontend/service-mvc.png)

然而对于Domain相关的Service应该放在哪一层，总会有不同的意见：

![MVC Player](./assets/article/images/frontend/mvcplayer.gif)

![MS MVC](./assets/article/images/frontend/ms-mvc.png)

Domain（业务）是一个相当复杂的层级，这里是业务的核心。一个合理的Controller只应该做自己应该做的事，它不应该处理业务相关的代码：

```java
if (isNewnameEmpty == false && newuser == null){
    user.setUserName(newUsername);
    List<Post> myPosts = postService.findMainPostByAuthorNameSortedByCreateTime(principal.getName());

    for (int k = 0;k < myPosts.size();k++){
        Post post = myPosts.get(k);
        post.setAuthorName(newUsername);
        postService.save(post);
    }
    userService.update(user);
    Authentication oldAuthentication = SecurityContextHolder.getContext().getAuthentication();
    Authentication authentication = null;
    if(oldAuthentication == null){
        authentication = new UsernamePasswordAuthenticationToken(newUsername,user.getPasswordHash());
    }else{
        authentication = new UsernamePasswordAuthenticationToken(newUsername,user.getPasswordHash(),oldAuthentication.getAuthorities());
    }
    SecurityContextHolder.getContext().setAuthentication(authentication);
    map.clear();
    map.put("user",user);
    model.addAttribute("myPosts", myPosts);
    model.addAttribute("namesuccess", "User Profile updated successfully");
    return new ModelAndView("user/profile", map);
}
```

我们在Controller层应该做的事是：

1. 处理请求的参数
2. 渲染和重定向
3. 选择Model和Service
4. 处理Session和Cookies

业务是善变的，昨天我们可能还在和对手竞争谁先推出新功能，但是今天可能已经合并了。我们很难预见业务变化，但是我们应该能预见Controller是不容易变化的。在一些设计里面，这种模式就是Command模式。

View层是一直在变化的层级，人们的品味一直在更新，有时甚至可能因为竞争对手而产生变化。在已经取得一定市场的情况下，Model-Service-Controller通常都不太会变动，甚至不敢变动。企业意识到创新的两面性，要么带来死亡，要么占领更大的市场。但是对手通常都比你想象中的更聪明一些，所以这时**开创新的业务是一个更好的选择**。

高速发展期的企业和发展初期的企业相比，更需要前端开发人员。在用户基数不够、业务待定的情形中，View只要可用并美观就行了，这时可能就会有大量的业务代码放在View层：

```jsp
<c:choose>
    <c:when test="${ hasError }">
    <p class="prompt-error">
        ${errors.username} ${errors.password}
    </p>
    </c:when>
    <c:otherwise>
    <p class="prompt">
        Woohoo, User <span class="username">${user.userName}</span> has been created successfully!
    </p>
    </c:otherwise>
</c:choose>	
```

不同的情形下，人们都会对此有所争议，但只要符合当前的业务便是最好的选择。作为一个前端开发人员，在过去我需要修改JSP、PHP文件，这期间我需要去了解这些Template：

```php
{foreach $lists as $v}
<li itemprop="breadcrumb"><span{if(newest($v['addtime'],24))} style="color:red"{/if}>[{fun date('Y-m-d',$v['addtime'])}]</span><a href="{$v['url']}" style="{$v['style']}" target="_blank">{$v['title']}</a></li>
{/foreach}
```       

有时像Django这一类，自称为Model-Template-View的框架，更容易让人理解其意图：

```html
{% for blog_post in blog_posts.object_list %}
{% block blog_post_list_post_title %}
<section class="section--center mdl-grid mdl-grid--no-spacing mdl-shadow--2dp mdl-cell--11-col blog-list">
{% editable blog_post.title %}
<div class="mdl-card__title mdl-card--border mdl-card--expand">
    <h2 class="mdl-card__title-text">
        <a href="{{ blog_post.get_absolute_url }}"  itemprop="headline">{{ blog_post.title }} › </a>
    </h2>
</div>
{% endeditable %}
{% endblock %}
```

作为一个前端人员，我们真正在接触的是View层和Template层，但是MVC并没有说明这些。

###从桌面版到移动版

Wap出现了，并带来了更多的挑战。随后，分辨率从1024x768变成了176×208，开发人员不得不面临这些挑战。当时所需要做的仅仅是修改View层，而View层随着iPhone的出现又发生了变化。

![WAP 网站](./assets/article/images/frontend/wap.gif)

这是一个短暂的历史，PO还需要为手机用户制作一个怎样的网站？于是他们把桌面版的网站搬了过去变成了移动版。由于网络的原因，每次都需要重新加载页面，这带来了不佳的用户体验。

幸运的是，人们很快意识到了这个问题，于是就有了SPA。**如果当时的移动网络速度可以更快的话，我想很多SPA框架就不存在了**。

先说说jQuery Mobile，在那之前，先让我们来看看两个不同版本的代码，下面是一个手机版本的blog详情页：

```html
<ul data-role="listview" data-inset="true" data-splittheme="a">
    {% for blog_post in blog_posts.object_list %}
		<li>
        {% editable blog_post.title blog_post.publish_date %}
        <h2 class="blog-post-title"><a href="{% url "blog_post_detail" blog_post.slug %}">{{ blog_post.title }}</a></h2>
        <em class="since">{% blocktrans with sometime=blog_post.publish_date|timesince %}{{ sometime }} ago{% endblocktrans %}</em>
        {% endeditable %}
        </li>
    {% endfor %}
</ul>
```

而下面是桌面版本的片段：

```html
{% for blog_post in blog_posts.object_list %}
{% block blog_post_list_post_title %}
{% editable blog_post.title %}
<h2>
    <a href="{{ blog_post.get_absolute_url }}">{{ blog_post.title }}</a>
</h2>
{% endeditable %}
{% endblock %}
{% block blog_post_list_post_metainfo %}
{% editable blog_post.publish_date %}
<h6 class="post-meta">
    {% trans "Posted by" %}:
    {% with blog_post.user as author %}
    <a href="{% url "blog_post_list_author" author %}">{{ author.get_full_name|default:author.username }}</a>
    {% endwith %}
    {% with blog_post.categories.all as categories %}
    {% if categories %}
    {% trans "in" %}
    {% for category in categories %}
    <a href="{% url "blog_post_list_category" category.slug %}">{{ category }}</a>{% if not forloop.last %}, {% endif %}
    {% endfor %}
    {% endif %}
    {% endwith %}
    {% blocktrans with sometime=blog_post.publish_date|timesince %}{{ sometime }} ago{% endblocktrans %}
</h6>
{% endeditable %}
{% endblock %}
```

人们所做的只是**重载View层**。这也是一个有效的SEO策略，上面这些代码是我博客过去的代码。对于桌面版和移动版都是不同的模板和不同的JS、CSS。

![移动版网页](./assets/article/images/frontend/mobile-web.png)

在这一时期，桌面版和移动版的代码可能在同一个代码库中。他们使用相同的代码，调用相同的逻辑，只是View层不同了。但是，每次改动我们都要维护两份代码。

随后，人们发现了一种更友好的移动版应用——APP。

###APP与过渡期API

这是一个艰难的时刻，过去我们的很多API都是在原来的代码库中构建的，即桌面版和移动版一起。我们已经在这个代码库中开发了越来越多的功能，系统开发变得臃肿。如《Linux/Unix设计思想》中所说，这是一个伟大的系统，但是它臃肿而又缓慢。

我们是选择重新开发一个结合第一和第二系统的最佳特性的第三个系统，还是继续臃肿下去。我想你已经有答案了。随后我们就有了APP API，构建出了博客的APP。

![应用](./assets/article/images/frontend/mobile-app.jpg)

最开始，人们越来越喜欢用APP，因为与移动版网页相比，其响应速度更快，而且更流畅。对于服务器来说，也是一件好事，因为请求变少了。

但是并非所有的人都会下载APP——**有时只想看看上面有没有需要的东西**。对于刚需不强的应用，人们并不会下载，只会访问网站。

有了APP API之后，我们可以向网页提供API，我们就开始设想要有一个好好的移动版。

###过渡期SPA

Backbone诞生于2010年，和响应式设计出现在同一个年代里，但他们似乎在同一个时代里火了起来。如果CSS3早点流行开来，似乎就没有Backbone啥事了。不过移动网络还是限制了响应式的流行，只是在今天这些都有所变化。

我们用Ajax向后台请求API，然后Mustache Render出来。因为JavaScript在模块化上的缺陷，所以我们就用Require.JS来进行模块化。

下面的代码就是我在尝试对我的博客进行SPA设计时的代码：

```javascript
define([
    'zepto',
    'underscore',
    'mustache',
    'js/ProductsView',
    'json!/configure.json',
    'text!/templates/blog_details.html',
    'js/renderBlog'
],function($, _, Mustache, ProductsView, configure, blogDetailsTemplate, GetBlog){

    var BlogDetailsView = Backbone.View.extend ({
        el: $("#content"),

        initialize: function () {
            this.params = '#content';
        },

        getBlog: function(slug) {
            var getblog = new GetBlog(this.params, configure['blogPostUrl'] + slug, blogDetailsTemplate);
            getblog.renderBlog();
        }
    });

    return BlogDetailsView;
});
```

从API获取数据，结合Template来Render出Page。但是这无法改变我们需要Client Side Render和Server Side Render的两种Render方式，除非我们可以像淘宝一样不需要考虑SEO——因为它不那么依靠搜索引擎带来流量。

这时，我们还是基于类MVC模式。只是数据的获取方式变成了Ajax，我们就犯了一个错误——将大量的业务逻辑放在前端。这时候我们已经不能再从View层直接访问Model层，从安全的角度来说有点危险。

如果你的View层还可以直接访问Model层，那么说明你的架构还是MVC模式。之前我在Github上构建一个Side Project的时候直接用View层访问了Model层，由于Model层是一个ElasticSearch的搜索引擎，它提供了JSON API，这使得我要在View层处理数据——即业务逻辑。将上述的JSON API放入Controller，尽管会加重这一层的复杂度，但是业务逻辑就不再放置于View层。

如果你在你的View层和Model层总有一层接口，那么你采用的就是MVP模式——MVC模式的衍生（PS：为了区别别的事情，总会有人取个表意的名称）。

一夜之前，我们又回到了过去。我们离开了JSP，将View层变成了Template与Controller。而原有的Services层并不是只承担其原来的责任，这些Services开始向ViewModel改变。

一些团队便将Services抽成多个Services，美其名为微服务。传统架构下的API从下图

![API Gateway](./assets/article/images/frontend/api-gateway.png)

变成了直接调用的微服务：

![Micro Services](./assets/article/images/frontend/microservices.png)

对于后台开发者来说，这是一件大快人心的大好事，但是对于应用端/前端来说并非如此。调用的服务变多了，在应用程序端进行功能测试变得更复杂，需要Mock的API变多了。

###Hybird与ViewModel

这时候遇到问题的不仅仅只在前端，而在App端，小的团队已经无法承受开发成本。人们更多的注意力放到了Hybird应用上。Hybird应用解决了一些小团队在开发初期遇到的问题，这部分应用便交给了前端开发者。

前端开发人员先熟悉了单纯的JS + CSS + HTML，又熟悉了Router + PageView + API的结构，现在他们又需要做手机APP。这时候只好用熟悉的jQuer Mobile + Cordova。

随后，人们先从Cordova + jQuery Mobile，变成了Cordova + Angular的 Ionic。在那之前，一些团队可能已经用Angular代换了Backbone。他们需要更好的交互，需要data binding。

接着，我们可以直接将我们的Angular代码从前端移到APP，比如下面这种博客APP的代码：

```javascript
  .controller('BlogCtrl', function ($scope, Blog) {
    $scope.blogs = null;
    $scope.blogOffset = 0;
    //
    $scope.doRefresh = function () {
      Blog.async('https://www.phodal.com/api/v1/app/?format=json').then(function (results) {
        $scope.blogs = results.objects;
      });
      $scope.$broadcast('scroll.refreshComplete');
      $scope.$apply()
    };

    Blog.async('https://www.phodal.com/api/v1/app/?format=json').then(function (results) {
      $scope.blogs = results.objects;
    });

    $scope.loadMore = function() {
      $scope.blogOffset = $scope.blogOffset + 1;
      Blog.async('https://www.phodal.com/api/v1/app/?limit=10&offset='+ $scope.blogOffset * 20 +  '&format=json').then(function (results) {
        Array.prototype.push.apply($scope.blogs, results.objects);
        $scope.$broadcast('scroll.infiniteScrollComplete');
      })
    };
  })
```  

结果**时间轴又错了**，人们总是**超前一个时期做错了一个在未来是正确的决定**。人们遇到了网页版的用户授权问题，于是发明了JWT——Json Web Token。

然而，由于WebView在一些早期的Android手机上出现了性能问题，人们开始考虑替换方案。接着出现了两个不同的解决方案：

1. React Native
2. 新的WebView——Crosswalk

开发人员开始欢呼React Native这样的框架。但是，他们并没有预见到**人们正在厌恶APP**，APP在我们的迭代里更新着，可能是一星期，可能是两星期，又或者是一个月。谁说APP内自更新不是一件坏事，但是APP的提醒无时无刻不在干扰着人们的生活，噪声越来越多。**不要和用户争夺他们手机的使用权**

###一次构建，跨平台运行

在我们需要学习C语言的时候，GCC就有了这样的跨平台编译。

在我们开发桌面应用的时候，QT就有了这样的跨平台能力。

在我们构建Web应用的时候，Java就有了这样的跨平台能力。

在我们需要开发跨平台应用的时候，Cordova就有了这样的跨平台能力。

现在，React这样的跨平台框架又出现了，而响应式设计也是跨平台式的设计。

响应式设计不得不提到的一个缺点是：**他只是将原本在模板层做的事，放到了样式（CSS）层**。你还是在针对着不同的设备进行设计，两种没有什么多大的不同。复杂度不会消失，也不会凭空产生，它只会从一个物体转移到另一个物体或一种形式转为另一种形式。

React，将一小部分复杂度交由人来消化，将另外一部分交给了React自己来消化。在用Spring MVC之前，也许我们还在用CGI编程，而Spring降低了这部分复杂度，但是这和React一样降低的只是新手的复杂度。在我们不能以某种语言的方式写某相关的代码时，这会带来诸多麻烦。

##RePractise

如果你是一只辛勤的蜜蜂，那么我想你应该都玩过上面那些技术。你是在练习前端的技术，还是在RePractise？如果你不花点时间整理一下过去，顺便预测一下未来，那么你就是在白搭。

前端的演进在这一年特别快，Ruby On Rails也在一个合适的年代里出现，在那个年代里也流行得特别快。RoR开发效率高的优势已然不再突显，语法灵活性的副作用就是运行效率降低，同时后期维护难——每个人元编程了自己。

如果不能把Controller、Model Mapper变成ViewModel，又或者是Micro Services来解耦，那么ES6 + React只是在现在带来更高的开发效率。而所谓的高效率，只是相比较而意淫出来的，因为他只是一层View层。将Model和Controller再加回View层，以后再拆分出来？

现有的结构只是将View层做了View层应该做的事。

首先，你应该考虑的是一种可以让View层解耦于Domain或者Service层。今天，桌面、平板、手机并不是唯一用户设备，虽然你可能在明年统一了这三个平台，现在新的设备的出现又将设备分成两种类型——桌面版和手机版。一开始桌面版和手机版是不同的版本，后来你又需要合并这两个设备。

其次，你可以考虑用混合Micro Services优势的Monolithic Service来分解业务。如果可以举一个成功的例子，那么就是Linux，一个混合内核的“Service”。

最后，Keep Learning。我们总需要在适当的时候做出改变，尽管我们觉得一个Web应用代码库中含桌面版和移动版代码会很不错，但是在那个时候需要做出改变。

对于复杂的应用来说，其架构肯定不是只有纯MVP或者纯MVVM这么简单的。如果一个应用混合了MVVM、MVP和MVC，那么他也变成了MVC——因为他直接访问了Model层。但是如果细分来看，只有访问了Model层的那一部分才是MVC模式。

模式，是人们对于某个解决方案的描述。在一段代码中可能有各种各样的设计模式，更何况是架构。


