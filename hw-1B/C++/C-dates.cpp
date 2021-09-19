#include <iostream>

using namespace std;

int checkDate(int x, int y){

    // Tricky case: e.g. 3 3 2056 is also correct

    if (x <= 12 and y <= 12){
        if (x != y)
            return 0;
    }
    return 1;

}

int main()
{
    // Check whether the date is uniquely determined 

    int x; int y; int z;
    cin >> x >> y >> z;
    int res = checkDate(x, y);
    cout << res << endl;
    return 0;
}
