#include<iostream>
#include<memory>
#include<string>
using namespace std;
class User{
    public:
        int age;
        string name;
    User(int age_, string name_): age(age_), name(name_){}
    ~User(){}
};
int main() {
    auto ptr = make_shared<User>(18, "Jack");
    auto ptr2 = ptr;
    cout<<ptr2.get()->age<<endl;
    cout<<ptr2.use_count()<<endl;
    /*
    output:
    18
    2
    */
    return 0;
}