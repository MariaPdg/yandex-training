#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int equalToMax(vector <int> arr){

    unordered_map <int, int> cnt;
    for (auto item: arr)
        cnt[item] ++;
    
    vector <int>::iterator idx;
    idx = max_element(arr.begin(), arr.end()); 
    // return iterator => use *idx 
    return cnt[*idx];
}

int main(){

    // Calculate the number of values in a sequence, which are equal to the maximum value

    vector <int> nums;
    int x;
    while (true){
        cin >> x;
        if (x != 0)
            nums.push_back(x);
        else
            break;
    }

    int res = equalToMax(nums);
    cout << res << endl;

}