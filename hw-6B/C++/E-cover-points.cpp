#include <iostream>
#include <algorithm>

using namespace std;


int main(){

    // n = number of points, k = number of segments
    // Calculate the minimum l such that each point is covered by a segment of length l

    int n, k;
    cin >> n >> k;
    int points[n];
    for (int i = 0; i<n; i++){
        cin >> points[i];
    }
    sort(points, points + n);
    int left = 0, right = points[n-1] - points[0];
    while (left < right){
        int l = left + (right - left) / 2;
        int max_right = points[0] - 1;
        int count = 0;
        for (auto p: points){
            if (p > max_right){
                count ++;
                max_right = p + l;
            }
        }
        if (count > k){
            left = l + 1;
        }
        else{
            right = l;
        }
    }
    cout << left << "\n";
    return 0;

}