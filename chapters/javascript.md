Javascript现在已经无处不在了，也许你正打开的某个网站，他便可能是node.js+json+javascript+mustache.js完成的，虽然你还没理解上面那些是什么，也正是因为你不理解才需要去学习更多的东西。但是你只要知道Javascript已经无处不在了，它可能就在你手机上的某个app里，就在你浏览的网页里，就运行在你IDE中的某个进程里。

##Javascript的Hello,world##

这里我们还需要有一个helloworld.html，Javascript是专为网页交互而设计的脚本语言，所以我们一点点来开始这部分的旅途，先写一个符合标准的helloworld.html

``` html
<!DOCTYPE html>
<html>
	<head></head>
	<body></body>
</html>
```

然后开始融入我们的javascript，向HTML中插入Javascript的方法，就需要用到html中的\<script>标签，我们先用页面嵌入的方法来写helloworld。

``` html
<!DOCTYPE html>
<html>
	<head>
		<script>
			document.write('hello,world');
		</script>
	</head>
	<body></body>
</html>
```

按照标准的写法，我们还需要声明这个脚本的类型

``` html
<!DOCTYPE html>
<html>
	<head>
		<script type="text/javascript">
			document.write('hello,world');
		</script>
	</head>
	<body></body>
</html>
```

没有显示hello,world?试试下面的代码

``` html
<!DOCTYPE html>
<html>
	<head>
		<script type="text/javascript">
			document.write('hello,world');
		</script>
	</head>
	<body>
		<noscript>
			disable Javascript
		</noscript>
	</body>
</html>
```

##更js一点###
我们需要让我们的代码看上去更像是js，同时是以js结尾。就像C语言的源码是以C结尾的，我们也同样需要让我们的代码看上去更正式一点。于是我们需要在helloworld.html的同一文件夹下创建一个app.js文件，在里面写着

``` javascript
document.write('hello,world');
```

同时我们的helloworld.html还需要告诉我们的浏览器js代码在哪里

``` html
<!DOCTYPE html>
<html>
	<head>
		<script type="text/javascript" src="app.js"></script>
	</head>
	<body>
		<noscript>
			disable Javascript
		</noscript>
	</body>
</html>
```
	
###从数学出发###
让我们回到第一章讲述的小明的问题，<strong>从实际问题下手编程，更容易学会编程</strong>。小学时代的数学题最喜欢这样子了——某商店里的糖一个5块钱，小明买了3个糖，小明一共花了多少钱。在编程方面，也许我们还算是小学生。最直接的方法就是直接计算3x5=?

``` javascript
document.write(3*5);
```

document.write实际也我们可以理解为输出，也就是往页面里写入3*5的结果，在有双引号的情况下会输出字符串。我们便会在浏览器上看到15，这便是一个好的开始，也是一个糟糕的开始。

##设计和编程###
对于实际问题，如果我们只是止于所要得到的结果，很多年之后，我们就成为了code monkey。对这个问题进行再一次设计，所谓的设计有些时候会把简单的问题复杂化，有些时候会使以后的扩展更加简单。这一天因为这家商店的糖价格太高了，于是店长将价格降为了4块钱。

``` javascript
document.write(3*4);
```

于是我们又得到了我们的结果，但是下次我们看到这些代码的时候没有分清楚哪个是糖的数量，哪个是价格，于是我们重新设计了程序

``` javascript
tang=4;
num=3;
document.write(tang*num);
```

这才能叫得上是程序设计，或许你注意到了";"这个符号的存在，我想说的是这是另外一个标准，我们不得不去遵守，也不得不去fuck。

###函数###
记得刚开始学三角函数的时候，我们会写
  
    sin 30=0.5
    
而我们的函数也是类似于此，换句话说，因为很多搞计算机的先驱都学好了数学，都把数学世界的规律带到了计算机世界，所以我们的函数也是类似于此，让我们做一个简单的开始。

``` javascript
function hello(){
	return document.write("hello,world");
}
hello();
```

当我第一次看到函数的时候，有些小激动终于出现了。我们写了一个叫hello的函数，它返回了往页面中写入hello,world的方法，然后我们调用了hello这个函数，于是页面上有了hello,world。

``` javascript
function sin(degree){
	return document.write(Math.sin(degree));
}
sin(30);
```

在这里degree就称之为变量。
于是输出了-0.9880316240928602，而不是0.5，因为这里用的是弧度制，而不是角度制。

    sin(30)
    
的输出结果有点类似于sin 30。写括号的目的在于，括号是为了方便解析，这个在不同的语言中可能是不一样的，比如在ruby中我们可以直接用类似于数学中的表达:

``` ruby
2.0.0-p353 :004 > Math.sin 30
=> -0.9880316240928618
2.0.0-p353 :005 >
```

我们可以在函数中传入多个变量，于是我们再回到小明的问题，就会这样去编写代码。

``` javascript
function calc(tang,num){
	result=tang*num;
	document.write(result);
}
calc(3,4);
```

但是从某种程度上来说，我们的calc做了计算的事又做了输出的事，总的来说设计上有些不好。

###重新设计###
我们将输出的工作移到函数的外面，

``` javascript
function calc(tang,num){
	return tang*num;
}
document.write(calc(3,4));
```

接着我们用一种更有意思的方法来写这个问题的解决方案

``` javascript
function calc(tang,num){
	return tang*num;
}
function printResult(tang,num){
	document.write(calc(tang,num));
}
printResult(3, 4)
```

看上去更专业了一点点，如果我们只需要计算的时候我们只需要调用calc，如果我们需要输出的时候我们就调用printResult的方法。

###object和函数###
我们还没有说清楚之前我们遇到过的document.write以及Math.sin的语法为什么看上去很奇怪，所以让我们看看他们到底是什么，修改app.js为以下内容

``` javascript
document.write(typeof document);
document.write(typeof Math);
```

typeof document会返回document的数据类型，就会发现输出的结果是

``` javascript
object object
```

所以我们需要去弄清楚什么是object。对象的定义是

<blockquote>无序属性的集合，其属性可以包含基本值、对象或者函数。</blockquote>

创建一个object，然后观察这便是我们接下来要做的 

``` javascript
store={};
store.tang=4;
store.num=3;
document.write(store.tang*store.num);
```

我们就有了和document.write一样的用法，这也是对象的美妙之处，只是这里的对象只是包含着基本值，因为
  
    typeof story.tang="number"
    
一个包含对象的对象应该是这样子的。

``` javascript
store={};
store.tang=4;
store.num=3;
document.writeln(store.tang*store.num);

var wall=new Object();
wall.store=store;
document.write(typeof wall.store);
```
	
而我们用到的document.write和上面用到的document.writeln都是属于这个无序属性集合中的函数。

下面代码说的就是这个无序属性集中中的函数。

``` javascript
var IO=new Object();
function print(result){
	document.write(result);
};
IO.print=print;
IO.print("a obejct with function");
IO.print(typeof IO.print);
```

我们定义了一个叫IO的对象，声明对象可以用

    var store={};
   
又或者是    
   
    var store=new Object{};

两者是等价的，但是用后者的可读性会更好一点，我们定义了一个叫print的函数，他的作用也就是document.write，IO中的print函数是等价于print()函数，这也就是对象和函数之间的一些区别，对象可以包含函数，对象是无序属性的集合，其属性可以包含基本值、对象或者函数。

复杂一点的对象应该是下面这样的一种情况。

``` javascript
var Person={name:"phodal",weight:50,height:166};
function dream(){
	future;
};
Person.future=dream;
document.write(typeof Person);
document.write(Person.future);
```

而这些会在我们未来的实际编程过程中用得更多。

###面向对象###

开始之前先让我们简化上面的代码，

``` javascript
Person.future=function dream(){
	future;
}
```

看上去比上面的简单多了，不过我们还可以简化为下面的代码。。。

``` javascript
var Person=function(){
	this.name="phodal";
	this.weight=50;
	this.height=166;
	this.future=function dream(){
		return "future";
	};
};
var person=new Person();
document.write(person.name+"<br>");
document.write(typeof person+"<br>");
document.write(typeof person.future+"<br>");
document.write(person.future()+"<br>");
```

只是在这个时候Person是一个函数，但是我们声明的person却变成了一个对象<strong>一个Javascript函数也是一个对象，并且，所有的对象从技术上讲也只不过是函数。</strong>这里的"\<br\>"是HTML中的元素，称之为DOM，在这里起的是换行的作用，我们会在稍后介绍它，这里我们先关心下this。this关键字表示函数的所有者或作用域，也就是这里的Person。

上面的方法显得有点不可取，换句话说和一开始的
 
    document.write(3*4);
    
一样，不具有灵活性，因此在我们完成功能之后，我们需要对其进行优化，这就是程序设计的真谛——解决完实际问题后，我们需要开始真正的设计，而不是解决问题时的编程。

``` javascript
var Person=function(name,weight,height){
	this.name=name;
	this.weight=weight;
	this.height=height;	
	this.future=function(){
		return "future";
	};
};
var phodal=new Person("phodal",50,166);
document.write(phodal.name+"<br>");
document.write(phodal.weight+"<br>");
document.write(phodal.height+"<br>");
document.write(phodal.future()+"<br>");
```

于是，产生了这样一个可重用的Javascript对象,this关键字确立了属性的所有者。

##其他

Javascript还有一个很强大的特性，也就是原型继承，不过这里我们先不考虑这些部分，用尽量少的代码及关键字来实际我们所要表达的核心功能，这才是这里的核心，其他的东西我们可以从其他书本上学到。

所谓的继承，

``` javascript
var Chinese=function(){
	this.country="China";
}

var Person=function(name,weight,height){
	this.name=name;
	this.weight=weight;
	this.height=height;	
	this.futrue=function(){
		return "future";
	}
}
Chinese.prototype=new Person();

var phodal=new Chinese("phodal",50,166);
document.write(phodal.country);
```	
	
完整的Javascript应该由下列三个部分组成:

 - 核心(ECMAScript)——核心语言功能
 - 文档对象模型(DOM)——访问和操作网页内容的方法和接口
 - 浏览器对象模型(BOM)——与浏览器交互的方法和接口
 
我们在上面讲的都是ECMAScript，也就是语法相关的，但是JS真正强大的，或者说我们最需要的可能就是对DOM的操作，这也就是为什么jQuery等库可以流行的原因之一，而核心语言功能才是真正在哪里都适用的，至于BOM，真正用到的机会很少，因为没有完善的统一的标准。

一个简单的DOM示例,

``` html
<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<noscript>
		disable Javascript
	</noscript>
	<p id="para" style="color:red">Red</p>
</body>
	<script type="text/javascript" src="app.js"></script>
</html>
```
	
我们需要修改一下helloworld.html添加	

```HTML
<p id="para" style="color:red">Red</p>
```

同时还需要将script标签移到body下面，如果没有意外的话我们会看到页面上用红色的字体显示Red，修改app.js。

``` javascript
var para=document.getElementById("para");
para.style.color="blue";
```
	
接着，字体就变成了蓝色，有了DOM我们就可以对页面进行操作，可以说我们看到的绝大部分的页面效果都是通过DOM操作实现的。

##美妙之处##
这里说到的Javascript仅仅只是其中的一小小部分，忽略掉的东西很多，只关心的是如何去设计一个实用的app，作为一门编程语言，他还有其他强大的内制函数，要学好需要一本有价值的参考书。这里提到的只是其中的不到20%的东西，其他的80%或者更多会在你解决问题的时候出现。

 - 我们可以创建一个对象或者函数，它可以包含基本值、对象或者函数。
 - 我们可以用Javascript修改页面的属性，虽然只是简单的示例。
 - 我们还可以去解决实际的编程问题。