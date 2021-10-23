#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

bool cmp(pair<int, int> p1, pair<int, int> p2)
{
    return (p1.first < p2.first);
}

int paintedSegments(vector <pair<int, int>> segments){

    sort(segments.begin(), segments.end(), cmp);
    int paintedLen = 0;
    int online = 0;
    for (int i=0; i<segments.size(); i++){
        if (online > 0){
            paintedLen += segments[i].first - segments[i-1].first;
        }
        if (segments[i].second == -1){
            online ++;
        }
        else{
            online --;
        }
    }
    return paintedLen; 
}

int main(){

    int n, x, y;
    cin >> n;
    int start = -1, end = 1;
    vector <pair<int, int>> segments;
    for (int i=0; i<n; i++){
        cin >> x >> y;
        segments.push_back(make_pair(x, start));
        segments.push_back(make_pair(y, end));
    }
    int res = paintedSegments(segments);
    cout << res << "\n";
    return 0;
}