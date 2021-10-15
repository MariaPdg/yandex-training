#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

void output(vector <int> arr){

    // Helpful function to print vector

    for (auto a: arr){
        cout << a << " ";
    }
    cout << endl;
}

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


bool cmp(pair<int, int> p1, pair<int, int> p2)
{
    return (p1.first < p2.first);
}


vector<pair<int,int>> enumerate(int size){
    vector <pair<int,int>> res;
    int x;
    for (int i=0; i<size; i++){
        cin>> x;
        res.push_back(make_pair(x, i+1));
    }
    sort(res.begin(), res.end(), cmp);
    return res;
}


int main(){

    // Find class room with y_i computers for student groups where x_i students, such that 
    // x_i + 1 <= y_i (+1 computer for teacher)

    int n,m;
    freopen("input.txt","r",stdin);
    cin>>n>>m;

    vector<pair<int, int>> x = enumerate(n);
    vector<pair<int, int>> y = enumerate(m);

    vector<int> groups(n+1, 0);
    int count = 0;
    int ynum = 0;

    for (auto item: x){
        while (ynum < y.size() && y[ynum].first < item.first + 1)
            ynum ++;
        if (ynum == y.size()) break;
        groups[item.second] = y[ynum].second;
        count ++; ynum ++;
    }
    
    cout << count << "\n";
    for (int i=1; i<groups.size(); i++){
        cout << groups[i] << " ";
    }
    cout << endl;
    fclose (stdin);
    
    return 0;
}