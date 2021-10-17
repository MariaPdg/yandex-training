#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int leftBinSearch(int arr[], int L, int l, int r){
    
    int m;
    while (l < r){
        m = l + (r - l) / 2;
        if (arr[m] >= L)
            r = m;
        else
            l = m + 1;
    }
    return l;

}

int rightBinSearch(int arr[], int R, int l, int r){

    int m;
    while (l < r){
        m = (l + r + 1) / 2;
        if (arr[m] <= R)
            l = m;
        else
            r = m - 1;
    }
    return l;

}


int main(){

    // How many numbers in a range [L, R]?
    
    // freopen("input.txt", "r", stdin);

    int n, k;
    int x, L, R;
    // vector<int> arr;
    cin >> n;
    int array[n];
    for (int i = 0; i<n; i++){
        cin >> x;
        array[i] = x;
    }
    sort(array, array + n);
    cin >> k;
    for (int i=0; i<k; i++){
        cin >> L >> R;
        int left = leftBinSearch(array, L, 0, n-1);
        int right = rightBinSearch(array, R, left, n-1);
        if (array[left] >= L && array[right] <= R){
            cout << right - left + 1 << " ";
        }
        else
            cout << 0 << " ";
    }
    return 0;
}