#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cmath>

using namespace std;

typedef long long ll;

vector <ll> buildPrefixSum(vector <ll> nums){
    vector <ll> prefixsum(nums.size()+1, 0);
    for (int i=1; i<nums.size()+1; i++){
        prefixsum[i] = prefixsum[i-1] + nums[i-1];
    }
    return prefixsum;
}


int main(){

    // Find the segment with maximum sum and output max sum

    long n, k;
    long l, r;
    ll x;
    vector <ll> arr, prefixsum;
    cin >> n;
    for (long i=0; i<n; i++){
        cin >> x;
        arr.push_back(x);
    }
    prefixsum = buildPrefixSum(arr);
    
    ll min_elem = pow(10, 9);
    ll max_sum = prefixsum[1];

    for (int i=0; i<prefixsum.size();i++){ 
        if (prefixsum[i] < min_elem)
            min_elem = prefixsum[i];
        else if (prefixsum[i] - min_elem > max_sum)
            max_sum = prefixsum[i] - min_elem;
    }
    cout << max_sum << '\n';

    return 0;
}