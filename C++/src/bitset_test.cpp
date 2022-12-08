#include<iostream>
#include<memory>
#include<string>
using namespace std;
int main() {
    int n = 32;
    string s = bitset<32>(n).to_string();
    reverse(s.begin(), s.end());
    cout<<bitset<32>(s).to_ulong()<<endl;
    return 0;
}