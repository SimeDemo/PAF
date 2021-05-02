#include <iostream>
using namespace std;
#include <math.h>

void solve_equation(double a1, double b1, double c1, double a2, double b2, double c2) {

    int x; 
    int y;

    if ((a1 * b2) - (b1 * a2) == 0) {

    cout << "No result" << endl;
    }   

    else{

    x = ((c1 * b2) - (b1 * c2)) / ((a1 * b2) - (b1 * a2));
    y = ((a1 * c2) - (c1 * a2)) / ((a1 * b2) - (b1 * a2));

    cout << "x=" << x << " y=" << y << endl;
    }
}


int main() {

    solve_equation(3, 4, 61, 7, 3, 2);
    
    return 0;
}