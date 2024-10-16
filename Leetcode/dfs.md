# DFS
## 112. Path Sum
```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool ans;
    bool hasPathSum(TreeNode* root, int targetSum) {
        ans = false;
        dfs(root, targetSum);
        return ans;
    }
    void dfs(TreeNode* root, int t){
        if(!root) return;
        if(!root->left && !root->right && t == root->val){
            ans = true;
            return;
        }
        if(root->left) dfs(root->left, t - root->val);
        if(root->right) dfs(root->right, t - root->val);
    }
};
```
## 200. Number of Islands

```c
class Solution {
public:
    int st[305][305];
    int m, n;
    int dx[4]={0, 0, 1, -1};
    int dy[4]={1, -1, 0, 0};
    void dfs(int i, int j, vector<vector<char>>& g){
        if(i < 0 || j < 0 || i >= m || j >= n) return;
        if(g[i][j] == '0' || st[i][j]) return;
        st[i][j] = 1;
        for(int u = 0; u < 4; u++) {
            int a = i + dx[u];
            int b = j + dy[u];
            dfs(a, b, g);
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        // attention: the matrix is not int but char
        // time complexity O(M*N*M*N)
        memset(st, 0, sizeof(st));
        m = grid.size();
        if(!m) return 0;
        n = grid[0].size();
        
        int res = 0;
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j]=='1' && !st[i][j]) {
                    dfs(i, j, grid);
                    res++;
                }
            }
        }
        return res;
    }
};
```