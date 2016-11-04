#Typescript

标签:sublime-text3 windows
---

- [下载](#下载)
- [使用](#使用)
- [接口](#接口)
- [类](#类)
- [阶段小结](#阶段小结)


###下载

>npm install -g typescript

####扩展

>sublime-text ``扩展``

```
cd "%APPDATA%\Sublime Text 3\Packages"
git clone --depth 1 https://github.com/Microsoft/TypeScript-Sublime-Plugin.git TypeScript
```

>cd 到sublime的包文件夹

>git 一下 重启sublime-text3

typescript的文件格式与编译系统就具有了

###使用

**tsc** 命令行

```
tsc lizi.ts
```

>就会生成同名的js文件 lizi.js


###接口

>似乎是对象类型结构相同，的方便使用

```
interface Person{
	firstName: string;
	lastName: string;
}
//接口类型定义

function geen(person: Person) {
	// body...
	return "hello, " + person.firstName + " " +
	person.lastName;
}

var user1 = {
	firstName:"jane",lastName:"user"
};
//变量类型定义

document.body.innerHTML = geen(user1);
//参数的类型与变量类型相同，即可食用
```

###类

>Ts支持Js新特性,像基于类的面向对象编程的支持

我们创建一个具有构造函数与一些公共字段的Student类。

>注意: 类和接口的良好配合使用。

此外,在构造函数参数中使用``public``是一种简写形式, 它将自动创建具有该名称的属性 

```
class Studeng {
	fullName: string;
	constructor(public firstName, public middleInitial, public lastName) {
		this.fullName = firstName + " " + middleInitial + " "+ lastName;

		// code...
	}
}
```

#### 官方类示例

hello world

https://github.com/Microsoft/TypeScriptSamples/tree/master/greeter

```
class Greeter {
    constructor(public greeting: string) { }
    greet() {
        return "<h1>" + this.greeting + "</h1>";
    }
};

var greeter = new Greeter("Hello, world!");
    
document.body.innerHTML = greeter.greet();
```



#### 阶段小结

>ts文件

```
class Student {
    fullName: string;
    constructor(public firstName, public middleInitial, public lastName) {
        this.fullName = firstName + " " + middleInitial + " " + lastName;
    }
}

interface Person {
    firstName: string;
    lastName: string;
}

function greeter(person : Person) {
    return "Hello, " + person.firstName + " " + person.lastName;
}

var user = new Student("Jane", "M.", "User");

document.body.innerHTML = greeter(user);
```

> 运行 **tsc**

>js文件

```
var Student = (function () {
    function Student(firstName, middleInitial, lastName) {
        this.firstName = firstName;
        this.middleInitial = middleInitial;
        this.lastName = lastName;
        this.fullName = firstName + " " + middleInitial + " " + lastName;
    }
    return Student;
}());
function greeter(person) {
    return "Hello, " + person.firstName + " " + person.lastName;
}
var user = new Student("Jane", "M.", "User");
document.body.innerHTML = greeter(user);
```

> 以上内容，似乎只是说明些语法

#####html中使用

>其实是没差的

```
<!DOCTYPE html>
<html>
    <head><title>TypeScript Greeter</title></head>
    <body>
        <script src="greeter.js"></script>
    </body>
</html>
```

### 未完待续
