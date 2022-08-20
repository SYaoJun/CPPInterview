# Modern C++
### C++11
1. move
2. forward
3. lambda
4. tuple
5. array
### C++14
1. std::make_unique
2. std::shared_lock
3. std::shared_timed_mutex
4. std::exchange
5. std::quoted
### C++17
1. std::shared_mutex
2. std::string_view
3. std::optional
4. std::variant
5. std::any
### C++20
1. ranges
2. concepts
3. coroutine
4. import
5. module
### tuple
- 优势在于传输一次性的一组数据，如果要大量使用，实际上不及结构体清晰明了。
- 可以将tuple用在map中作为多索引值。可以用来比较两个tuple类型的字典序大小。
- tuple可以存引用
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