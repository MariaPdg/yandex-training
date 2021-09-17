#include <iostream>

using namespace std;

int main()
{
    /*  Input: n = number of students, coord = coordinates of students' houses.
        Find the coordinate of the school to minimize the sum of distances 
        from houses to the school of all students. */

    int n;
    cin >> n;
    int coord[n];
    for (int i = 0; i < n; i++){
		cin >> coord[i];
	}
    int res =  n / 2;
    cout << coord[res] << endl;
    return 0;
}