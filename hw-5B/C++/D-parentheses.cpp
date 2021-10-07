#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;


int main(){

    // Is there a valid number of parentheses in a given sequence?

    string line;
    getline(cin, line);
    unordered_map <char, int> dct;
    dct['('] = 0;
    for (char s: line){
        if (s == '(')
            dct[s] += 1;
        else
            if (s == ')'){
                dct['('] -= 1;
                if (dct['('] < 0){
                    cout << "NO" << "\n";
                    return 0;
                }
            }
    }
    if (dct['('] == 0) 
        cout << "YES" << "\n";
    else 
        cout << "NO" << "\n";
    return 0;
}