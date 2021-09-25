#include <iostream>
#include <vector>
#include <fstream>
#include <map>

using namespace std;

vector <int> isUnique(vector <int> arr){

    map <int, int> dct;
    vector <int> res;
    for (auto item: arr){
        if (!dct.count(item)){
            dct[item] = 0;
        }
        dct[item] ++;
    }

    for (auto item: arr){
        if (dct[item] == 1)
            res.push_back(item);
    }
    return res;
}

void output(vector <int> arr){

    // Helpful function to print vector

    for (auto a: arr){
        cout << a << " ";
    }
    cout << endl;
}

int main(){

    // Print whether the number is unique

    ifstream fin("input.txt");
    int x;
    vector <int> nums, res;
    while (fin >> x) {
        nums.push_back(x);
    }
    fin.close();

    res = isUnique(nums);
    output(res);

    return 0;
}