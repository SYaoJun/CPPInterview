#include <algorithm>
#include <vector>
#include <iostream>
#include <numeric>

int main() {
    std::vector<int> vec = {112, 32, 877, 99, 19};
    auto res = std::accumulate(vec.begin(), vec.end(), 0);
    std::cout<<res<<std::endl;
    return 0;
}