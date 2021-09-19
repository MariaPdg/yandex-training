#include <iostream>

using namespace std;

int minStations(int a, int b, int c){

    // Tricky case: e.g. from 3 to 9, choose the minimum between 9-3-1 = 5 and 10-9+3-1=3.
    // I.e. it is better to go via the stations 10, 1, 2  rather than 4,5,6,7,8"""
    int maxN = max(b, c);
    int minN = min(b, c);
    return min(abs(b-c)-1, abs(a - maxN) + minN - 1);
}

int main()
{
    // Find the minimum number of intermediate stations from i to j,
    // n is the total number of stations
    int n, i, j;
    cin >> n >> i >> j;
    int res = minStations(n, i, j);
    cout << res << endl;
    return 0;
}


