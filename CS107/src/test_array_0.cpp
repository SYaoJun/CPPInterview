#include <iostream>
using namespace std;
struct Node{
    int a;
    int arr[0];
};
int main() {
    Node* node = new Node();
    node->arr[0] = 1;
    node->arr[1] = 2;
    node->arr[2] = 3;
    node->arr[3] = 4;

    cout<<sizeof(Node)<<endl;
    for(int i = 0; i < 3; i++) {
        cout<<node->arr[i]<<" ";
    }
    cout<<endl;

    return 0;
}