# include <iostream>

using namespace std;

int output(int r, int i, int c){

    if (i == 0){
        if (r != 0)
            return 3;
        return c;
    }
    else if (i == 1){
        return c;
    }
    else if (i == 4){
        if (r != 0)
            return 3;
        return 4;
    }
    else if (i == 6){
        return 0;
    }
    else if (i == 7){
        return 1;
    }
    return i;
}

int main()
{
    //Output the result of the testing system

    int r; int i; int c;
    cin >> r;
    cin >> i;
    cin >> c;
    int res = output(r, i, c);
    cout << res << endl;
    return 0;
}
