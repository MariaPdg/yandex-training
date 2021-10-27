#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

bool cmp(pair<int, int> p1, pair<int, int> p2){
       
    if (p1.first == p2.first)
        return p1.second < p2.second;
    return (p1.first < p2.first);
}

int arrivedGoods(vector <pair<int, int>> events){

    sort(events.begin(), events.end(), cmp);
    int arrived = 0, maxArrived = 0;
    for (int i=0; i<events.size(); i++){
        if (events[i].second == 1){
            arrived++;
        }
        else {
            arrived--;
        }
        maxArrived = max(maxArrived, arrived);
    }
    return maxArrived; 
}

int main(){

    // Define a minimum of machines required for preprocessing all goods after their arrival

    int n, x, y;
    cin >> n;
    int start = 1, end = -1;
    vector <pair<int, int>> events;
    for (int i=0; i<n; i++){
        cin >> x >> y;
        events.push_back(make_pair(x, start));
        events.push_back(make_pair(x + y, end));
    }
    int res = arrivedGoods(events);
    cout << res << "\n";
    return 0;
}