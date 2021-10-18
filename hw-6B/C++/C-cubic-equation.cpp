#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

double equation(int coef[], double x){
    return coef[0] * pow(x, 3) + coef[1] * pow(x, 2) + coef[2] * x + coef[3];
}

bool checkPos(int coef[], double m){
    return equation(coef, m) > 0;
}

bool checkNeg(int coef[], double m){
    return equation(coef, m) < 0;
}

double leftBinSearch(bool (*check)(int[], double), int coef[], double l, double r, double eps){
    
    double m;
    while (l + eps < r){
        m = (l + r) / 2.0;
        if (check(coef, m))
            r = m;
        else
            l = m;
    }
    return l;

}

int main(){

    // Solve cubic equation
 
    int coef[4];
    double ans;
    for (int i=0; i<4; i++){
        cin >> coef[i];
    }
    double eps = 1e-6;
    if (coef[0] > 0)
        ans = leftBinSearch(&checkPos, coef, -1001., 1001., eps);
    else
        ans = leftBinSearch(&checkNeg, coef, -1001., 1001., eps);
    
    cout << setprecision(15) << ans << "\n";
   
    return 0;
}