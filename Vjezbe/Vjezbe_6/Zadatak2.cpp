#include <iostream>
using namespace std;
#include <math.h>

void point_circle(double ox, double oy, double r, double x, double y) {

    double d = sqrt(pow((x-ox), 2) + pow((y-oy), 2));

    if (d > r) {

        cout << "tocka je van kruznice" << endl;
    }

    else {

        cout << "tocka je unutar kruznice" << endl;
    }

}


int main() {

    point_circle(3, 3, 10, 5, 6);
    return 0;
}