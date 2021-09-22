#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int prepPalindrome(string word){

    // if the word is already palindrome
    string wordReversed = word;
    reverse(wordReversed.begin(), wordReversed.end());
    if (word == wordReversed)
        return 0;
    
    int ans = 0;
    int r, l;
    if (word.size() % 2 == 0){
        r = word.size() / 2;
        l = r - 1;  
    }
    else{
        r = word.size() / 2 + 1;
        l = r - 2;
    }
    while (l >= 0){
        if (word[l] != word[r])
            ans ++;
        l--; r++;
    }
    return ans;
}

int main(){

    // Calculate the cost of palindrome preparing from word: 
    // we can change 1 letter in the word with the cost 1

    string word;
    cin >> word;
    int res = prepPalindrome(word);
    cout << res << "\n";

    return 0;

}