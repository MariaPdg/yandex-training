#include <iostream>
#include <vector>
#include <fstream>
#include <unordered_map>

using namespace std;

void isSeenBefore(vector <int> arr){

    unordered_map <int, int> dct;
    for (auto item: arr){
        if (!dct.count(item)){
            dct[item] = 0;
            cout << "NO" << '\n';
        }
        dct[item] ++;
        if (dct[item] > 1)
            cout << "YES" << '\n';
    }
}

int main(){

    // Print whether the number is seen before

    ifstream fin("input.txt");
    int x;
    vector <int> nums;
    while (fin >> x) {
        nums.push_back(x);
    }
    fin.close();

    isSeenBefore(nums);

    return 0;
}