#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

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

    // Calculate prefix sums for segments [l, r] of the array

    long n, k;
    long l, r;
    ll x;
    vector <ll> arr, prefixsum;
    cin >> n >> k;
    for (long i=0; i<n; i++){
        cin >> x;
        arr.push_back(x);
    }
    prefixsum = buildPrefixSum(arr);
    for (long i=0; i<k; i++){
        cin >> l >> r;
        cout << prefixsum[r] - prefixsum[l-1] << endl;
    }
    
    return 0;
}