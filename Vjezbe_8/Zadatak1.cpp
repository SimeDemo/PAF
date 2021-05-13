#include <iostream>
using namespace std;
#include <math.h>
#include <vector>
#include <fstream>


class Projectile {

    public:
        vector<float> velocity;
        int angle;
        int density;
        int coef;
        int area;
        int mass;
        int x0;
        int y0;
        vector<float> x;
        vector<float> y;
        vector<float> a;
        vector<float> t;
        float v0x;
        vector<float> v0y;

        Projectile(int v, int theta, int rho, int C, int A, int m, int _x0, int _y0) {
            // ak bude bug onda checkirati jel u radijanima ili stupnjevima
            angle = (theta/360) * 2 * acos(-1);
            velocity.push_back(v);
            v0x = velocity.back() * cos(theta);
            v0y.push_back(v * sin(theta));
            density = rho;
            coef = C;
            area = A;
            mass = m;
            x.push_back(_x0);
            y.push_back(_y0);
        }
    
    public:

        int dragForce() {

            float force = -((density * coef * area) / 2) * pow(velocity.back(), 2);

            return force;
        }

    public:

        void move(float dt) {

            a.push_back(dragForce() / mass);
            t.push_back(t.back() * dt);
            velocity.push_back(velocity.back() - (9.81 - dragForce()) * dt);
            y.push_back(y.back() + (velocity.back() * dt));
            x.push_back(x.back() + (v0x * dt));
            y.push_back(y.back() + (v0y.back() * dt));
            }

    public:

        void write_data() {

            ofstream myfile;
            myfile.open("plot_data.txt");
                for (int i = 0; i < x.size(); i++) {
                    myfile << x.at(i) << endl;
                }
                myfile.close();
        }
};


int main() {
    Projectile p1 (1, 2, 3, 4, 5, 6, 7, 8);
    p1.move(0.01);
    p1.write_data();
    cout << 1 << endl;
    return 0;
}