#include <iostream>
using namespace std;
#include <math.h>

void print_interval(int lista) {

    for (int item : lista) {
        
        cout << item << " ";
    }
}




int main() {

    int set_wn[5] = {0, 1, 2, 3, 4};

    print_interval(set_wn[5]);

    return 0;
}