#include <iostream>
using namespace std;
#include <math.h>

void print_interval(int list[]) {

    int size = sizeof(list);

    for (int i = 0; i < size; i++) {

        cout << list[i] << endl;
    }     
}




int main() {

    int set_wn[5] = {0, 1, 2, 3, 4};

    print_interval(set_wn); // ovdje imam error za koji ne znam rjesenje pa bi volio to prouciti s vama na satu, ne znam dalje s time...

    return 0;
}