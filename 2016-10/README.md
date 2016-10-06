* ajax 学习

## 目录
* [创建 XMLHttpRequest 对象](#创建 XMLHttpRequest 对象)
* [向服务器发送请求](#向服务器发送请求)
* [异步等待](#异步等待)
* [获得服务器的响应](#获得服务器的响应)
*

AJAX 
---------

创建 XMLHttpRequest 对象
-----------------------
	XMLHttpRequest 是 AJAX 的基础

	
	var xmlhttp;
	if (window.XMLHttpRequest)
  	{// code for IE7+, Firefox, Chrome, Opera, Safari
 	 xmlhttp=new XMLHttpRequest();
  	}
	else
 	{// code for IE6, IE5
	 xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}

向服务器发送请求
--------------

	xmlhttp.open("GET","ajax_info.txt",true);
	xmlhttp.send();

	open(method,url,async) 	规定请求的类型、URL 以及是否异步处理请求。

    	method：请求的类型；GET 或 POST
    	url：文件在服务器上的位置
   		async：true（异步）或 false（同步）

	send(string) 	将请求发送到服务器。
		string：仅用于 POST 请求
		
	*与 ``POST`` 相比，``GET`` 更简单也更快，并且在大部分情况下都能用。*

	然而，在以下情况中，请使用 POST 请求：

   	 -无法使用缓存文件（更新服务器上的文件或数据库）
   	 -向服务器发送大量数据（POST 没有数据量限制）
   	 -发送包含未知字符的用户输入时，POST 比 GET 更稳定也更可靠
	
如果需要像 HTML 表单那样 POST 数据，请使用 setRequestHeader() 来添加 HTTP 头。然后在 send() 方法中规定您希望发送的数据


	xmlhttp.open("POST","ajax_test.html",true);
	xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	xmlhttp.send("fname=Henry&lname=Ford");

异步等待
---------

-当使用 async=true 时，请规定在响应处于 onreadystatechange 事件中的就绪状态时执行的函数：



	xmlhttp.onreadystatechange=function()
  	{
  	if (xmlhttp.readyState==4 && xmlhttp.status==200)
  	  {
  	  document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
  	  }
  		}
		xmlhttp.open("GET","ajax_info.txt",true);
		xmlhttp.send();

-当然 也有false 的情况， 但.
	我们不推荐使用 async=false，但是对于一些小型的请求，也是可以的。

请记住，JavaScript 会等到服务器响应就绪才继续执行。如果服务器繁忙或缓慢，应用程序会挂起或停止。

注意：当您使用 async=false 时，请不要编写 [onreadystatechange](#onreadystatechange) 函数 - 把代码放到 send() 语句后面即可：

```
	xmlhttp.open("GET","ajax_info.txt",false);
	xmlhttp.send();
	document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
```

获得服务器的响应
--------------

-如需获得来自服务器的响应，请使用 XMLHttpRequest 对象的 responseText 或 responseXML 属性。
	responseText 	获得字符串形式的响应数据。
	responseXML 	获得 XML 形式的响应数据。
	
	-如果来自服务器的响应是 XML，而且需要作为 XML 对象进行解析，请使用 responseXML 属性：
		
		xmlDoc=xmlhttp.responseXML;
		txt="";
		x=xmlDoc.getElementsByTagName("ARTIST");
		for (i=0;i<x.length;i++)
		  {
		  txt=txt + x[i].childNodes[0].nodeValue + "<br>";
		  }
		document.getElementById("myDiv").innerHTML=txt;
		
响应服务器事件``onreadystatechange``
---------------------------------

当请求被发送到服务器时，我们需要执行一些基于响应的任务。

每当 readyState 改变时，就会触发 onreadystatechange 事件。	
	readyState 属性存有 XMLHttpRequest 的状态信息。
		
	下面是 XMLHttpRequest 对象的三个重要的属性：
		onreadystatechange 	存储函数（或函数名），每当 readyState 属性改变时，就会调用该函数。
		readyState 	
			
		存有 XMLHttpRequest 的状态。从 0 到 4 发生变化。
			    0: 请求未初始化
			    1: 服务器连接已建立
			    2: 请求已接收
			    3: 请求处理中
			    4: 请求已完成，且响应已就绪
		status 	200: "OK"
		404: 未找到页面
