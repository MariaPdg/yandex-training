#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main(){

    // Calculate the sum of numbers i with the color d

    typedef long long ll;
    unordered_map <ll, ll> dct;
    vector <ll> A;
    ll n, d, k;
    cin >> n;
    for (ll i=0; i<n; i++){
        cin >> d >> k;
        if (!dct.count(d)) {
            dct[d] = k;
            A.push_back(d);
        }
        else dct[d] += k;
    }

    sort(A.begin(), A.end());

    for (auto a: A){
        cout << a << " " << dct[a] << "\n";
    }

    return 0;
}