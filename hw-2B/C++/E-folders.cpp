#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int minTime(vector <int> arr){

    sort(arr.begin(), arr.end());
    int res = 0;
    for (int i = 0; i < arr.size() - 1; i++){
        res += arr[i];
    }

    return res;
}

int main(){

    // Calculate the minimum time required to find the diploma in folders in the worst case (1 sec per diploma).
    // Input: n = number of folders, arr = number of diplomas in each folder. 

    int n, x, res;
    cin >> n;
    vector <int> arr;
    for (int i = 0; i < n; i++){
		cin >> x;
        arr.push_back(x);
	}
    
    res = minTime(arr);
    cout << res << "\n";
    
    return 0;
    
}