#include <iostream>

using namespace std;

typedef unsigned long ulg;

int main(){

    /* Person 1: A = the number of trees to cut in each day, each Kth day is holiday.
       Person 2: B = the number of trees to cut in each day, each Mth day is holiday.
       X = the number of trees.
       How many day are required to cut aul trees? */
 
    ulg a, b, k, m, x;
    cin >> a >> k >> b >> m >> x;
    ulg l = 0;
    ulg r = x * 2 / a + 1;
    ulg days, hd1, hd2;
    while (l < r){
        days = l + (r - l) / 2;
        hd1 = days / k;
        hd2 = days / m;
        if ((days - hd1) * a + (days - hd2) * b < x)
            l = days + 1;
        else
            r = days;
    }
    cout << l << "\n";

    return 0;
}