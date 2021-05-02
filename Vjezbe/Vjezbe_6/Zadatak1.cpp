#include <iostream>
using namespace std;

void coordinates(double x1, double x2, double y1, double y2) {
    
    float k = (y2 - y1) / (x2 - x1);
    float l = y1 - (k * x1);
    
    cout << "y=" << k << "x+" << l << endl;
}

int main() {
    coordinates(3, 2, 3, 4);
    return 0;
}