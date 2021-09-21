#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cmath>

using namespace std;

void output(vector <int> arr){

    // Helpful function to print vector

    for (auto a: arr){
        cout << a << " ";
    }
    cout << endl;
}

int max_min_distance(vector <int> arr){

    vector <int> shops;
    vector <int> houses;
    vector <int> res{};

    for (int i = 0; i < arr.size(); i++){
        if (arr[i] == 2)
            shops.push_back(i);
        else if (arr[i] == 1)
            houses.push_back(i);
    }

    for (auto h: houses){
        vector <int> dist{};
        for (auto s: shops){
            dist.push_back(abs(s-h));
        }
        auto min_el = min_element(dist.begin(), dist.end());
        res.push_back(*min_el);
    }
    auto max_el = max_element(res.begin(), res.end());
    return *max_el;
}


int main(){

    // Input of n numbers: e.g. 2 0 1 1 0 1 0 2 1 2, where 0-offices, 1-houses, 2-shops.
    // Define the maximum between the minimum distances from houses to shops 

    // input from the file
    ifstream fin("input.txt");
    int x;
    vector <int> street;
    while (fin >> x) {
        street.push_back(x);
    }
    fin.close();

    int res = max_min_distance(street);
    cout << res << endl;

    return 0;

}
