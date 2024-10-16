## 239. Sliding Window Maximum
- tips: monotonic decrease stack
- if I want get the result of sliding window minimum, how do you resolve it?
```
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        // keep all the window elements in a stack
        // maintain this stack to monotonic decrease
        // after move the window 
        // all the maximum element still in the head
        deque<int> dq;
        int n = nums.size();
        vector<int> res;
        for(int i = 0; i < n; i++) {

            // 1. pop outdated data
            if(!dq.empty() && dq.front() <= i-k){
                dq.pop_front();
            }
            // 2. check insert position
            while(!dq.empty() && nums[dq.back()] <= nums[i]){
                dq.pop_back();
            }
            // why we need to insert index rather than value?
            // because we need to decide which element could evict based on the index
            dq.push_back(i);

            // 3. if there are k elements
            if(i >= k - 1) {
                res.push_back(nums[dq.front()]);
            }
            
        }
        return res;
    }
};
```
## 739. Daily Temperatures
```c
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& t) {
        // right to left maintain a stack monotonic decrease
        stack<int> stk;
        int n = t.size();
        vector<int> res(n);
        for(int i = n - 1; i >= 0; i -- ) {
            // insert new value
            while (!stk.empty() && t[stk.top()] <= t[i]){
                stk.pop();
            }
            // get value
            if(stk.empty()) res[i] = 0;
            else res[i] = stk.top() - i;
            // insert value
            stk.push(i);
        }
        return res;
    }
};
```