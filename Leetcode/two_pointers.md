# Two Pointers
- another name is sliding window.
## 10
```c
class Solution {
public:
    int maxArea(vector<int>& h) {
        // greedy + two pointers
        int l = 0, r = h.size() - 1;
        int n = h.size();
        int res = 0;
        while(l < r){
            // choosing the lowest side and moving it closer another side
            res = max(res, (r - l )* min(h[l], h[r]));
            if(h[l] > h[r]){
                r--;
            }else{
                l++;
            }
        }
        return res;
    }
};
```
## 3
```c
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // must keep array consective
        // use hash table record the repeat value 
        // If a char is repeat, we will move the start position until there is no repeat char
        int hashtable[256];
        memset(hashtable, 0, sizeof(hashtable));
        int start = 0, len = 0;
        int start_pos = 0;
        int i = 0;
        for(auto c: s){
            hashtable[c ]++;
            while(hashtable[c] > 1){
                hashtable[s[start_pos]] --;
                start_pos++;
            }
            // If code arrive here, keep no repeat
            if(i - start_pos + 1 > len) {
                start =  start_pos;
                len =  i - start_pos + 1;
            }
            i++;
        }
        return len;
        
    }
};
```
## 438
- sliding window has some property.
- the sub_array length is fixed.
- we only need to do two things: add new element and delete old element.
```c
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        // 1. same char type 
        // 2. same appear times 
        int valid_type = 0;
        unordered_map<int, int> mp, smp;
        for(auto c: p){
            mp[c]++;
        }
        
        vector<int> res;
        // length must keep the same
        // check every sub array that length equals p's length
        int m = p.size();
        int n = s.size();
        int valid = mp.size();
        for(int i = 0; i < n; i++) {
            // length is constant variable
            // add new char
            smp[s[i]]++;
            if(smp[s[i]] == mp[s[i]]) {
                valid_type++;
            }
            // delete old char
            if(i >= m){
                if(smp[s[i-m]] == mp[s[i-m]]){
                    valid_type--;
                }
                smp[s[i-m]]--;
            }
            if(valid_type == valid){
                res.push_back(i-m+1);
            }
            // cout<<i<<" valid = "<<valid_type<<endl;
        }
        return res;
    }
};
```