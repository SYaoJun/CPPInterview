# Dynamic Programming

## 62. Unique Paths
```c
class Solution {
public:
    int dp[110][110];
    int uniquePaths(int m, int n) {
        memset(dp, 0, sizeof(dp));
        // first column
        for(int i = 0; i < m; i++) dp[i][0] = 1;
        // first row
        for(int j = 0; j < n; j++) dp[0][j] = 1;

        for(int i = 1; i < m; i++) {
            for(int j = 1; j < n; j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
};
```