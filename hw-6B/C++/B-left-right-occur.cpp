#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool check_gt(int arr[], int m, int target){
    return arr[m] > target;
}

bool check_ge(int arr[], int m, int target){
    return arr[m] >= target;
}

int leftBinSearch(int arr[], int l, int r, int L){
    
    int m;
    while (l < r){
        m = l + (r - l) / 2;
        if (check_ge(arr, m, L))
            r = m;
        else
            l = m + 1;
    }
    return l;

}

int rightBinSearch(int arr[], int l, int r, int R){

    int m;
    while (l < r){
        m = (l + r + 1) / 2;
        if (!check_gt(arr, m, R))
            l = m;
        else
            r = m - 1;
    }
    return l;

}

int main(){

    // Find indices of the left and right occurrences of t from targets
 
    int n, m;
    cin >> n;
    int arr[n];
    for (int i=0; i<n; i++){
        cin >> arr[i];
    }
    cin >> m;
    int targets[m];
    for (int i=0; i<m; i++){
        cin >> targets[i];
    }

    int left, right;
    for (auto t: targets){
        left = leftBinSearch(arr, 0, n-1, t) + 1;
        right = rightBinSearch(arr, 0, n-1, t) + 1;
        if (arr[left-1]!=t && arr[right-1]!=t){
            left =0, right = 0;
        }
        cout << left << " " << right << "\n";
    }

   
    return 0;
}