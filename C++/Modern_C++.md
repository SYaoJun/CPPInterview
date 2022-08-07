## 现代C++
### tuple

优势在于传输一次性的一组数据，如果要大量使用，实际上不及结构体清晰明了。

可以将tuple用在map中作为多索引值。可以用来比较两个tuple类型的字典序大小。

**tuple可以存引用**

```c
#include <iostream>
#include <algorithm>
#include <functional>
#include <queue>
#include <tuple>
#include <map>
#include <string>
using namespace std;

int main(){
    //usage
    std::tuple<int, string, char> t(32, "Penny", 'A');
    //output
    cout<<get<0>(t)<<endl; //32
    get<1>(t) = "Alex"; //reference
    //assignment 
    tuple<int, string, char> t2;
    t2 = tuple<int, string, char>(24, "Alex", 'B');
    t2 = make_tuple(17, "Jun", 'C');
    //tuple can store reference 
    string st = "In for a penny";
    tupel<string&> t3(st);
    t3 = make_tuple(ref(st));
    int x;
    string y;
    char z;
    make_tuple(ref(x), ref(y), ref(z)) = t2;
    tie(x, y, z) = t2; // doing the same thing
    tie(x, std::ignore, z) = t2;
    auto t4 = tuple_cat(t2, t3); //concatenate two string
    //tuple traits
    cout<<tuple_size<decltype(t4)>::value<<endl;
    tuple_element<1, decltype(t4)>::type d;
    cout<<d<<endl;
    //Advantage
    //comparison of tuples 
    tuple<int, int , int > time1, time2; //hours mintues seconds
    if(time1 > time2) cout<<"time1 is a later time"<<endl;
    //multi index map
    map<tuple<int, char, float>, string> mp;
    mp[make_tuple(18, 'A', 3.14)] = "Curiosity kills the cat";
    //fast change value
    int a, b, c;
    tie(c, b, a) = make_tuple(a, b, c);
    return 0;
}
```
### variant