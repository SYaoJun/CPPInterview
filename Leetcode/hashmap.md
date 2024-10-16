## 1
```c
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> mp;
        for(int i = 0; i < nums.size(); i++) {
            int t = target - nums[i];
            if(mp.find(t) != mp.end()){
                return {i, mp[t]};
            }
            mp[nums[i]] = i;
        }
        return {-1, -1};
    }
};
```
## 49
```c
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // 排序 + 哈希表
        map<string, vector<string>> mp;
        vector<vector<string>> res;
        for(auto y: strs){
            
                string temp = y;
                sort(y.begin(), y.end());
                mp[y].push_back(temp);
            
        }
        for(auto [k,v]: mp){
            res.push_back(v);
        }
        return res;
    }
};
```

## 128
- Tips: hash table
- Ideas of solving a problem
1. The big obstacle is keep the complexity under O(N).
2. We can store the value in hash table, however we need to loop ever value and find the longest sub_array.
3. There is a way to optimize the inner loop. If we check every start value greater than that queried, we can reduce many no meaningful query.
```c
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        map<int, int> mp;
        for(auto x: nums){
            mp[x]++;
        }
        int res = 0;
        int temp = -1e9;
        for(auto [k, v]: mp){
           if(k < temp) continue;
           temp = k;
            int local_res = 0;
            while(mp.count(temp)){
                temp++;
                local_res++;
            }
            res = max(res, local_res);
        }
        return res;
    }
};
```
## 560. Subarray Sum Equals K
```
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        // by means of hash table 
        // how to caculate the subarray? we always use total sum subtract prefix check if the result equals k
        // if we change our mind to use total sum subtract k and then check the answer whether exist in hashtable
        unordered_map<int, int> mp;
        int prefix_sum = 0;
        int res = 0;
        // 0 is a special prefix
        mp[0] = 1;
        for(auto x: nums){
            prefix_sum += x;
            if(mp.find(prefix_sum - k) != mp.end()){
                res += mp[prefix_sum - k];
            }
            mp[prefix_sum]++;
        }
        return res;
    }
};
```