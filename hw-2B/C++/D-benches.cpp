#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

void output(vector <int> arr){

    // Helpful function to print vector

    for (auto a: arr){
        cout << a << " ";
    }
    cout << endl;
}

vector <int> benchLegsToLeave(int length, vector <int> coord){

    if (length % 2 != 0 and find(coord.begin(), coord.end(), length / 2) != coord.end()){
        return {length/2};
    }
    int l = length / 2 - 1;
    int r = l + 1;
    vector <int> res{};
    while (l >= 0){
        if (find(coord.begin(), coord.end(), l) != coord.end()){
            res.push_back(l);
            break;
        }
        l --;
    }
    while (r < length){
        if (find(coord.begin(), coord.end(), r) != coord.end()){
            res.push_back(r);
            break;
        }
        r ++;
    }
    return res;
}

int main(){

    // Input: l = length of a bench, k = number of legs, coord = location of legs.
    // Output: location of legs, which should be left.
    // Condition: at least one leg in the left and right sides from the bench center.


    int l, k, x;
    cin >> l >> k;
    vector <int> coord;
    vector <int> res;
    for (int i = 0; i < k; i++){
		cin >> x;
        coord.push_back(x);
	}
    
    res = benchLegsToLeave(l, coord);
    output(res);

    return 0;

}