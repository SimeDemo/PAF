#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

class Particle {

    public:
        float angle;
        vector<float> v;
        vector<float> x;
        vector<float> y;
        float v0x;
        vector<float> v0y;
        
        Particle(float v0, float theta, float x0, float y0) {

            angle = theta;
            v.push_back(v0);
            x.push_back(x0);
            y.push_back(y0);
            v0x = v0 * cos((theta/360) * 2 * acos(-1));
            v0y.push_back(v0 * sin((theta/360) * 2 * acos(-1)));
        }

    private:

        void __move(float dt) {
            
            v0y.push_back(v0y.back() - (9.81 * dt));
            x.push_back(x.back() + (v0x * dt));
            y.push_back(y.back() + (v0y.back() * dt));
        }

    public:

        void range(float dt) {

            while (y.back() >= 0) {
                __move(dt);
            }

            for (int j = 0; j < y.size(); j++) {
                if (y.at(j) < 0) {
                    break;
                }
            }
            cout << "range is equal to " << x.back() - x.at(0) << "m" << endl ;
        }
    
    public:

        void time_of_flight(float dt) {

            cout << "time of flight is equal to " << y.size() * dt << "s" << endl;
        }
};

int main() {
    Particle p1 (10, 30, 0, 0);
    p1.range(0.01);
    p1.time_of_flight(0.01);
}