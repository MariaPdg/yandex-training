#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <fstream>

using namespace std;

int main(){

    // Calculate the election results

    ifstream fin("input.txt");
    int n;
    string name;
    unordered_map <string, int> dct;
    vector  <string> candidates;
    while (fin >> name >> n) {
        if (!dct.count(name)){
            dct[name] = n;
            candidates.push_back(name);
        }
        else{
            dct[name] += n;
        }
    }
    fin.close();
    sort(candidates.begin(), candidates.end());
    for (auto c: candidates){
        cout << c << " "<< dct[c] << "\n";
    }

    return 0;
}