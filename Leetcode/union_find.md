# Union-find Data Structure
- A  good example is find friends. If A familiar with B, and B familiar with C, we can say A,B,C are friends.
# 547. Number of Provinces
```c
class Solution {
public:
    int p[205];
    int find(int x){
        if(p[x] != x){
            p[x] = find(p[x]);
        }
        return p[x];
    }
    int findCircleNum(vector<vector<int>>& g) {
        int n = g.size();
        for(int i = 0; i < 205; i++) {
            p[i] = i;
        }
        // set<int> st;
        for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++){
            if(g[i][j] == 0) continue;
            int a = find(i);
            int b = find(j);
            if(a != b) {
                // union
                p[a] = b;
            }
        }
        int res = 0;
        for(int i = 0; i < n; i++){
            if(find(i)==i){
                res++;
            }
        }
        return res;
    }
};
```