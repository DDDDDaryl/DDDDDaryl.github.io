---
title: TPLINK笔试复盘
date: 2020-06-17 00:51:52
categories:
- 真题
tags:
- Algorithm
- TPLINK
---



```c++
/*第一题*/
    vector<int> longestSubsequence(vector<int>& seq) {
        if(seq.size() < 2) return seq;
        vector<vector<int>> dp(seq.size()+1);
        dp[1] = {seq[0]};
        unsigned global_max_idx = 0;
        for(int idx=2; idx<=seq.size(); ++idx) {
            unsigned max_idx = 0, max_size = 0;
            for(int i=0; i<=idx; ++i) {
                if(seq[idx-1] > seq[i-1] && dp[i].size() > max_size) {
                    max_size = dp[i].size();
                    max_idx = i;
                }
            }
            dp[idx] = dp[max_idx];
            dp[idx].emplace_back(seq[idx-1]);
            if(dp[idx].size() > global_max_idx) {
                global_max_idx = idx;
            }
        }
        return dp[global_max_idx];
    }
```



```c++
    /*第二题*/
    string minimumSplicedNumber(vector<unsigned>& nums) {
        vector<string> buckets(nums.size());
        string ret{};
        for(int i=0; i<nums.size(); ++i) {
            buckets[i] = to_string(nums[i]);
        }
        auto my_less = [](string str1, string str2)->bool{
            if(str1.length() == str2.length()) return str1 < str2;
            while (str1.length() > str2.length()) {
                str2 += str2[0];
            }
            while (str1.length() < str2.length()) {
                str1 += str1[0];
            }
            return str1 < str2;
        };
        sort(buckets.begin(), buckets.end(), my_less);
        for(const auto& str:buckets) {
            ret += str;
        }
        cout << ret <<endl;
        return ret;
    }
```

