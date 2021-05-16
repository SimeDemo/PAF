#include <iostream>
using namespace std;
#include <math.h>
#include <vector>
#include <fstream>
template <typename T>


int sgn(T val) {
    return (T(0) < val) - (val < T(0));
};

int main() {

    cout << sgn(3) << endl;
}
