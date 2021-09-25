#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

vector<int> input(FILE* file) {
  int n;
  vector<int> array;
	char temp;
	do{
	    fscanf(file,"%d%c", &n, &temp); 
	    array.push_back(n);
	} while(temp!= '\n');
 	return array;
}

int countMatches(vector <int> v1, vector <int> v2){

    std::vector<int> v3;

    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());

    set_intersection(v1.begin(),v1.end(),
                          v2.begin(),v2.end(),
                          back_inserter(v3));
    return v3.size();

}

int main(){

    // Count the number of matches in list1 and list2

    FILE* ptr = fopen("input.txt","r");
    vector<int> arr1 = input(ptr);
    vector<int> arr2 = input(ptr);
    int res = countMatches(arr1, arr2);
    cout << res << '\n';

    return 0;
}