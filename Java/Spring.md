### 控制反转IOC★★★

在Spring中把每一个需要管理的对象称为Spring Bean（简称Bean），而Spring管理这些Bean的容器，被我们称为Spring IoC容器（或者简称IoC容器）

Spring的控制反转指一个对象依赖的其他对象将会在容器的初始化完成后**主动将其依赖的对象传递给它**，而不需要这个对象自己创建或者查找其依赖的对象。

spring通过一个配置文件描述bean和bean之间的依赖关系，**利用java的反射功能实例化bean**，并建立bean之间的依赖关系。



### 面向切面编程AOP★★★

面向切面编程技术通过**分离系统逻辑**和**业务逻辑**来提高系统的**内聚性**。

是通过**预编译方式**和**运行期动态代理**实现程序功能的统一维护的一种技术。

利用AOP可以**对业务逻辑的各个部分进行隔离**，从而使得业务逻辑各部分之间的耦合度降低，提高程序的可重用性，同时提高了开发效率。

作用：在程序运行期间，在不修改源码的情况下对方法进行功能增强。

优势：减少重复代码，提高开发效率，方便维护。

常用代理技术

- JDK：基于接口
- CGLib：基于父类

Spring提供了**JDK和CGLib** 2种方式来生成代理对象，具体生成代理对象的方式由AopProxyFactory根据AdvisedSupport对象的配置来决定。

Spring默认的代理对象生成策略为：如果是**目标类接口**，则使用**JDK动态代理技术**，否则使用**CGLib动态代理方式**。



### Spring Bean的作用域★★

- **Singleton 单例(默认)**

- **Prototype 原型**

- Request 请求级别

- Session 会话级别

- Global Session 全局会话



### Spring Bean的生命周期
- 实例化Bean
- Bean配置
- 执行setBeanName(String)

### AOP的通知类型
- 前置通知 @before
- 后置通知 @after_returning
- 最终通知 @after 无论是否异常都执行
- 异常通知 @after_throwing
- 环绕通知 @around

### 依赖注入
- 构造器注入
- set方法注入
- 静态工厂注入
- 实例工厂注入

### 自动装配的方式
- no
- byName
- byType
- constructor
- autodetect



### 常用注解
  ```java
  @Configuration:声明一个类作为配置类，代替xml文件
  @Bean：声明在方法上，将方法的返回值加入Bean容器，代替<bean>标签
  @Value：属性注入
  @PropertySource：指定外部属性文件
  @AutoWired：它可以对类成员变量、方法及构造函数进行标注，完成自动装配的工作。 通过 @Autowired的使用来消除 set ，get方法。
  @ConfigurationProperties(prefix="jdbc")：读取资源配置类 通过实现setter进行配置
  @EnableConfigurationProperties(JDBC.class) 启用资源配置读取类
  ```
### maven依赖冲突

- 锁定版本：dependencyManagement + dependency
- 排除依赖：exclusions
- 依赖调节原则：第一声明优先，路径近者优先（直接依赖>间接依赖）