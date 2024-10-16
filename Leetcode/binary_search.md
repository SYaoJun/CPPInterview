# binary search
- This algorithm very fast. It can reach O(logN).
- If you want to use this algorithm, you need to find some monotonic trait.
- One side can satisfy the condition, another side cannot.
- In most situation the array is sorted or we need to sorted firstly.
## 35. Search Insert Position
```c
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        // binary search
        if(nums.empty() || nums.back() < target) return nums.size();
        int n = nums.size();
        int l = 0, r = n-1;
        while(l < r){
            int mid = (l + r)/2;
           // we need to find the first position which greater than or equals target
           // so we use this template
           // but we can not deal with the value bigger than the maximum value of the array
            if(nums[mid] >= target) {
                r = mid;
            }else{
                l = mid + 1;
            }

        }
        return l;
    }
};
```
## 875. Koko Eating Bananas

```c
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // from k all bananas can finish eating under h hours
        //[ xxxxxyyyyyy] find the position of the first y
        int n = piles.size();
        int l = 1, r = 1e9;
        while(l < r){
            int mid = l + (r - l)/2;
            if(check(mid, piles) <= h) { //  satisfy our condition
                r = mid; 
            }else{
                l = mid + 1;
            }
        }
        return l;
    }
    int check(int m, vector<int> &piles) {
        int total_hours = 0;
        for(auto x: piles){
            total_hours += (x + m - 1)/m;
        }
        return total_hours;
    }
};
```