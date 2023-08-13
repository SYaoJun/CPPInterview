# 数据结构
- 链表
- 队列
- 树
- 图
- 查找
- 排序
- 哈希表

## 平衡树和红黑树的区别
- 平衡树是严格的左右子树高度差不超过1
- 红黑树在平衡性上做了妥协，自定义了四条规则
    - 所有的根节点都是黑色
    - 红色的孩子是黑色
    - 任意节点到叶子节点的路径上黑色节点的数目相同
    - 所有叶子节点都是黑色
- 红黑树牺牲查找的效率，换取了插入和删除的效率，但是平均时间复杂度还是log(N)
## 单例模式

```c
class A{
	public:
		static A* getInstance();
		static A* instance;
	private:
		A();
	    ~A();
};
A* A::instance = nullptr;
//内存读写reorder不安全 导致双检查锁失效
//先分配内存 再执行构造器 最后返回给实例
//编译器的优化 
A* A::getInstance(){
	//读没有问题 写就有问题 
	//锁前检查 锁的粒度过大 锁后检查安全性 
	if(instance==nullptr){
		mutex.lock();
		if(instance==nullptr) instance = new A();
		mutex.unlock();
	}
	return instance; 
}

```



## 快排 归并 堆排

```c
#include <iostream>
#include <cstdio>
using namespace std;

//快排 时间复杂度 平均nlogn 空间复杂度O(1) 
void quick_sort(int arr[], int l, int r){
	if(l >= r) return;
	int x = arr[l+r >> 1];
	int i = l-1, j = r+1;
	while(i < j){
		while(arr[++i] < x);
		while(arr[--j] > x);
		if(i < j) swap(arr[i], arr[j]);
	}
	quick_sort(arr, l, j);
	quick_sort(arr, j+1, r);
}
//归并
//时间复杂度NlongN  空间复杂度N
 
int tmp[105];
void merge_sort(int arr[], int l, int r){
	if(l >= r) return;
	int mid = (l + r)>>1;
	merge_sort(arr, l, mid); merge_sort(arr, mid+1, r);
	//合并
	int i = l, j = mid+1, k = 0;
	while(i <= mid && j <= r){ //i和j注意了
		if(arr[i] < arr[j]) tmp[k++] = arr[i++];
		else tmp[k++] = arr[j++];
	} 
	while(i <= mid) tmp[k++] = arr[i++];
	while(j <= r) tmp[k++] = arr[j++];
	for(int i = 0; i < k; i++){
		arr[l+i] = tmp[i];
	}
} 

//大根堆 把大交换上去
void heapify(int arr[], int r, int n){
    int i = 2*r+1, j = 2*r+2;
    int mx = r;
    if(i < n && arr[i] > arr[mx]) mx = i;
    if(j < n && arr[j] > arr[mx]) mx = j;
    if(mx != r) {
        swap(arr[mx], arr[r]);
        heapify(arr, mx, n);
    }
}

//堆排序 堆化 堆顶取出交换到末尾去
void heap_sort(int arr[], int n){
	for(int i = n; i >= 0; i--){
        heapify(arr, i, n); //当前的点 总共的点
    }
    //交换完成
    for(int i = n-1; i >= 0; i--){
        swap(arr[0], arr[i]);
        heapify(arr, 0, i); //总量减1
    }
} 

int main(){
    int arr[]{1,93,6,45,2,7,8,45,2123,239,0,3};
	int n = 12;
	// merge_sort(arr, 0, n-1);
    //如果从0编号 那么儿子节点为2i+1 2i+2
    //最后一个节点是啥
    heap_sort(arr, n);
	for(int i = 0; i < n; i++) printf("%d ", arr[i]);
	puts("");
	
	return 0;
} 
```

## kmp算法

```c
#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
int Next[105];
void getNext(string p){
    //按照左神讲的 考查的是当前位置的前一个字符串的最长前后缀
    Next[0] = -1;
    Next[1] = 0;
    int cn = 0, i = 2;
    int n = p.size();
    while(i < n){
        if(p[cn] == p[i-1]) Next[i++] = ++cn;
        else if(cn) cn = Next[cn];
        else Next[i++] = 0; //前后缀为0
    }
}
void kmp(string p, string s){
    //首先求next数组
    getNext(p);
    int i = 0, j = 0;
    int m = s.size();
    int n = p.size();
    while(i < m && j < n){
        if(s[i] == p[j]) i++, j++;
        else if(Next[j] == -1) i++; //开头不匹配
        else j = Next[j];
        if(j==n){
            cout<<i-n<<endl; //起始位置
            j = Next[j-1];
            i--;
        }
    }
}
int main(){
    string text = "helloworldllo";
    string pattern = "llo";
    kmp(pattern, text);
    return 0;
}

```

## LRU算法

## strcpy和memcpy

```c
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;
//内存拷贝函数 按字节拷贝
void* my_memcpy(void* dest, void* src, size_t count){
    if(dest == NULL || src == NULL) return NULL;
    char* pdest = (char*) dest;
    char* psrc = (char*) src;
    while(count--){
        *pdest++ = *psrc++;
    }
    return dest;
}
//字符串拷贝函数 仅用来拷贝字符串
char* my_strcpy(char* dest, const char* src){
    if(dest == NULL || src ==NULL) return NULL;
    char* pdest = dest;
    while((*dest++ = *src++) != '\0');
    return pdest;
}
int main(){
    char src[] ="hello";
    char dest[100];
   
    //my_memcpy(dest, src, strlen(src));
    my_strcpy(dest, src);
    printf("%s\n", src);
    return 0;
}
```

## string类

```c
class String{
public:
    String(const char* str = NULL); //通用构造函数
    String(const String& str); //拷贝构造函数
    ~String();
    String& operator+(const String &str);
    String& operator+=(const String &str);
    char& operator[](const int n) const;
    String operator=(const String &str) const;
    bool operator==(const String &str)const;
    bool operator<(const String &str) const;
    bool operator<(const String &str) const;
    size_t size const; //获取长度
    //流运算符>> <<
private:
    char* data; //字符串
    size_t length; //长度
}
String::String(const char* str){ //通用构造函数
    if(!str){
        length = 0;
        data = new char[1];
        *data='\0';
    }else{
        length = strlen(str); //对空指针调用strlen会导致内存错误
        data = new char[length+1];
        strcpy(data, str);
    }
}
String::String(const String& str){ //拷贝构造
    length = str.length;
    data = new char[length+1];
    strcpy(data, str.data);
}
//析构
String::~String(){
    delete []data;
    length = 0;
}
//赋值重载
String& String::operator=(const String &str){
    delete []data;
    length = str.length;
    data = new char[length+1];
    strcpy(data, str.data);
    return *this;
}
```

## 智能指针shared_ptr

```c
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
template <typename T>
class SmartPtr{
private:
    T * ptr;
    int* use_count();
    SmartPtr(T* p);
    SmartPtr(const SmartPtr<T> & orig);//拷贝
    SmartPtr<T>& operator=(const SmartPtr<T>& orig);
    ~SmartPtr();
}
SmartPtr::SmartPtr(T* p){
    ptr = p;
    *use_count = 1;
}
SmartPtr::~SmartPtr(){  //析构
    delete ptr;
    ptr = nullptr;
    delete use_count;
    use_count = nullptr;
}
int main(){
    return 0;
}
```

## 写一个函数在main函数执行前先运行

```c++
#include <iostream>
using namespace std;
class Hello{
public:
	Hello(){
		cout<<"before main!"<<endl;
	}
};
Hello w; //全局变量在main之前执行 
int main(){
	cout<<"I am main"<<endl;
	return 0;
}
```

## 匿名管道pipe

```c
#include <unistd.h>
#include <stdio.h>
#include <string.h>
int main(){
    pid_t fd[2];
    pipe(fd); //创建管道
    int ret = fork();
    if(ret > 0){ //父进程 父写 fd[0]读 fd[1]写
        close(fd[0]);
        char *str ="hello world\n";
        write(fd[1], str, strlen(str));
        sleep(1);
    }else if(ret == 0){ //子进程 子读 fd[1]关闭
        close(fd[1]);
        char buf[1024];
        int n = read(fd[0], buf, sizeof(buf));
        //写到显示器上
        write(1, buf, n);
    }
    return 0;
}
```

## rand7产生rand10

[leetcode470](https://leetcode-cn.com/problems/implement-rand10-using-rand7/) 左程云BAT精讲 牛课堂系列算法讲座2.1

```c
class Solution {
public:
    int rand10() {
        int t;
        while(true){
            t = rand7() + (rand7()-1) * 7;
            if(t <= 40) return t%10 +1;
        };
        return 0;
    }
};
```

## 反转二叉树

```c
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        //遍历所有点 然后交换左右孩子
        dfs(root);
        return root;
    }
    void dfs(TreeNode* root){
        if(!root) return;
        dfs(root->left);
        dfs(root->right);
        swap(root->left, root->right); 
    }
};
```
```c++
#include <iostream>
using namespace std;
class Person{
public:
	Person(int age, int height){
		this->age = age;
		this->height = new int(height);
	}
	Person(const Person& p){
		this->age = p.age;
		this->height = new int(*p.height); 
	}
	~Person(){
		cout<<"析构"<<endl;
		delete height;
		height = nullptr;
	}
	int age;
	int* height;
};
int main(){
	Person p1(18,190);
	Person p2(p1);
	cout<<p2.age<<" "<<*p2.height<<endl;
	return 0;
}
```




## partition函数

- 快排中的partition函数在algorithm库中有实现

```c
#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    //按照关键字划分 返回不满足条件的首个位置下标
    vector<int> v{19,8,7,3,5,1,0};
    int key = 6;
    auto t = partition(v.begin(), v.end(), [key](int a){
        return a < key;
    }) - v.begin();
    cout<<t<<endl;
    for(auto x: v) cout<<x<<" ";
    return 0;
}
```

## bind函数

- 参数绑定。通用的函数适配器。接受一个可调用对象，生成一个新的可调用对象。

```c
#include <iostream>
#include <algorithm>
#include <functional>
#include <queue>
using namespace std;
using std::placeholders::_1;
using std::placeholders::_2;
bool cmp( int a,  int b){
    return a > b;
}
int main(){
    //使用bind()将函数转换为仿函数
    //从大到小
    vector<int> v{1,0,99,3,4,12,2};
    sort(v.begin(), v.end(), bind(cmp, _1, _2));
    for(auto x: v) cout<<x<<" ";
    cout<<endl;
    return 0;
}
```

## lambda表达式

- 未命名的内联函数。一般来说应该减少捕获的数据量，避免捕获指针和引用。捕获列表和函数体是必不可少的。

```c
#include <iostream>
#include <algorithm>
#include <functional>
#include <queue>
using namespace std;
int main(){
    //lambda表达式 匿名函数对象
    auto f = [](const int &a){
        return a*a;
    };
    cout<<f(5)<<endl;
    return 0;
}
```

## function函数

- 函数指针

```c
#include <iostream>
#include <algorithm>
#include <functional>
#include <queue>
using namespace std;
int f(int a){
    return a*a;
}
int main(){
    //function是一个模板 相当于函数指针 function<return(args)> ff = func;
    function<int(int)> ff = f;
    cout<<ff(55)<<endl;
    return 0;
}
```

## 生成随机数

- 线性同余算法

```c++
#include<iostream>
using namespace std;
//x_{n+1} = a*x_n + c mod m
//a = 48271 
int main(){
	long long a = 48271, c = 0, x = 1;
	long long m = INT_MAX;
	for(long long i = 0; i < 10; i++){
		x = (a*x+c) % m;
		cout<<x<<endl;
	}
	return 0;
} 
```

## string转char*

```c++
char *str = const_cast<char*>(str.c_str());
```

