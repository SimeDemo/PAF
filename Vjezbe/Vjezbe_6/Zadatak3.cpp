#include <iostream>
using namespace std;
#include <algorithm>
#include <math.h>

void print_list(int list[]) {

    int size = sizeof(list);

    for (int i = 0; i < 5; i++) {

        cout << list[i] << " ";
    };
    cout << endl;
}

void print_interval(int list[], int lower, int upper) {

    int size = sizeof(list);
    int users_list[] = {};
    int i = 0;
    
    while (i >= lower && i <= upper) {

        cout << list[i] << " ";
        i++;
    };
}

void replace(int list[], int a, int b) {

    int c = list[a];
    list[a] = list[b];
    list[b] = c;
}




int main() {

    int set_wn[5] = {0, 1, 2, 3, 4};

    print_list(set_wn);

    print_interval(set_wn, 0, 2);

    cout << endl;

    replace(set_wn, 0, 4);
    print_list(set_wn);

    sort(begin(set_wn), end(set_wn));
    print_list(set_wn);

    reverse(begin(set_wn), end(set_wn));
    print_list(set_wn);

    return 0;
}