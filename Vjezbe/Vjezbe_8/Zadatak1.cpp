#include <iostream>
using namespace std;
#include <math.h>
#include <vector>
#include <fstream>

class Projectile {

    public:
        float angle, density, coef, area, mass;
        float x0, y0;
        float v0x, v0y;
        vector<float> x, y;
        vector<float> vx, vy;
        float ax, ay;
        float k1vx, k2vx, k3vx, k4vx;
        float k1vy, k2vy, k3vy, k4vy;
        float k1x, k2x, k3x, k4x;
        float k1y, k2y, k3y, k4y;

        Projectile(float v, float theta, float rho, float C, float A, float m, float _x0, float _y0) {

            x0 = _x0;
            y0 = _y0;
            angle = (theta/360) * 2 * acos(-1);
            v0x = v * cos(angle);
            v0y = v * sin(angle);
            vx.push_back(v0x);
            vy.push_back(v0y);
            density = rho;
            coef = C;
            area = A;
            mass = m;
            x.push_back(_x0);
            y.push_back(_y0);
        }

    public:

        void reset() {

            vx.clear();
            vx.push_back(v0x);
            vy.clear();
            vy.push_back(v0y);
            x.clear();
            x.push_back(x0);
            y.clear();
            y.push_back(y0);
        }
    
    public:
        template <typename T>
        int sgn(T val) {

            return (T(0) < val) - (val < T(0));
        } 

    private:

        void __move(float dt) {
            
            ax = - sgn(vx.back()) * (pow(vx.back(), 2) * density * coef * area)/(2*mass);
            vx.push_back(vx.back() + (ax * dt));
            x.push_back(x.back() + (vx.back() * dt));
            
            ay = - 9.81 - (sgn(vy.back()) * (pow(vy.back(), 2) * density * coef * area)/(2*mass));
            vy.push_back(vy.back() + (ay * dt));
            y.push_back(y.back() + (vy.back() * dt));
            // cout << "vy je " << vy.back() << ", vx je " << vx.back() << endl;
            }

    public:

        float acc_x_RK(float velocity, float knx) {

            float acc = -sgn(velocity) * (pow(velocity + knx, 2) * density * coef * area) / (2*mass);

            return acc;
        }

    public:

        float acc_y_RK(float velocity, float kny) {

            float acc =  -9.81 - (sgn(velocity) * (pow(velocity + kny, 2) * density * coef * area) / (2*mass));
    
            return acc;
        }

    private:
        
        void __moveRK(float dt) {

            k1vx = acc_x_RK(vx.back(), 0) * dt;
            k1x = vx.back() * dt;
            k2vx = acc_x_RK(vx.back(), k1vx / 2) * dt;
            k2x = (vx.back() + (0.5 * k1vx)) * dt;
            k3vx = acc_x_RK(vx.back(), k2vx / 2) * dt;
            k3x = (vx.back() + (0.5 * k2vx)) * dt;
            k4vx = acc_x_RK(vx.back(), k3vx) * dt;
            k4x = (vx.back() + k3vx) * dt;
            vx.push_back(vx.back() + ((k1vx + (2 * k2vx) + (2 * k3vx) + k4vx) / 6));
            x.push_back(x.back() + ((k1x + (2 * k2x) + (2 * k3x) + k4x) / 6));

            k1vy = acc_y_RK(vy.back(), 0) * dt;
            k1y = vy.back() * dt;
            k2vy = acc_y_RK(vy.back(), k1vy / 2) * dt;
            k2y = (vy.back() + (0.5 * k1vy)) * dt;
            k3vy = acc_y_RK(vy.back(), k2vy / 2) * dt;
            k3y = (vy.back() + (0.5 * k2vy)) * dt;
            k4vy = acc_y_RK(vy.back(), k3vy) * dt;
            k4y = (vy.back() + k3vy) * dt;
            vy.push_back(vy.back() + ((k1vy + (2 * k2vy) + (2 * k3vy) + k4vy) / 6));
            y.push_back(y.back() + ((k1y + (2 * k2y) + (2 * k3y) + k4y) / 6));
        }

    public:

        void shoot(float _dt) {

            while (y.back() >= 0) {
                __move(_dt);
            };
        }

    public:

        void shootRK(float _dt) {

            while (y.back() >= 0) {
                __moveRK(_dt);
            };
        }

    public:

        void write_data() {

            ofstream myfile;
            myfile.open("x_data.txt");
                for (int i = 0; i < x.size(); i++) {
                    myfile << x.at(i) << " ";

                }
                myfile.close();

            myfile.open("y_data.txt");
                myfile << endl;
                for (int j = 0; j < y.size(); j++) {
                    myfile << y.at(j) << " ";
                }
                myfile.close();
        }

    public:

        void write_dataRK() {

            ofstream myfile;
            myfile.open("x_dataRK.txt");
                for (int i = 0; i < x.size(); i++) {
                    myfile << x.at(i) << " ";

                }
                myfile.close();

            myfile.open("y_dataRK.txt");
                for (int j = 0; j < y.size(); j++) {
                    myfile << y.at(j) << " ";
                }
                myfile.close();
        }
    
    public:

        float range(float dt) {

            shootRK(dt);
            float r = x.back() - x0;
            reset();
            return r;
        }
};

void range_vs(float dt) {

    vector<float> cds;
    vector<float> masses;
    vector<float> ranges_cd;
    vector<float> ranges_m;

    for (float cd = 0.0; cd < 100; cd = cd + 0.001) { // cd nek ide od 0 do 1

        cds.push_back(cd);
    }

    for (float m = 0.01; m < 7.3; m = m + 0.001) { // masa neka ide od 0.01 do 7.3 (tezine muske kugle u atletici :) )
    
        masses.push_back(m);
    }

    for (int j = 0; j < cds.size(); j++) {

        Projectile p1 (10, 30, 1.227, cds.at(j), 0.1, 5, 0, 0);

        ranges_cd.push_back(p1.range(0.01));
    }

    for (int l = 0; l < masses.size(); l++) {

        Projectile p1 (10, 30, 1.227, 0.5, 0.1, masses.at(l), 0, 0);

        ranges_m.push_back(p1.range(0.01));
    }

    ofstream myfile;
    myfile.open("cds.txt");
        for (int n = 0; n < cds.size(); n++) {
            myfile << cds.at(n) << " ";
        }
        myfile.close();

    myfile.open("masses.txt");
        for (int j = 0; j < masses.size(); j++) {
            myfile << masses.at(j) << " ";
        }
        myfile.close();

    myfile.open("ranges_cd.txt");   
        for (int n = 0; n < ranges_cd.size(); n++) {
            myfile << ranges_cd.at(n) << " ";
        }
        myfile.close();

    myfile.open("ranges_m.txt");
        for (int j = 0; j < ranges_m.size(); j++) {
            myfile << ranges_m.at(j) << " ";
        }
        myfile.close();

}


int main() {
    Projectile p1 (10, 30, 1.227, 0.5, 0.1, 5, 0, 0);
    //              v  th  rho    C     A   m  x0 y0
    p1.shootRK(0.01);
    p1.write_dataRK();
    p1.reset();
    p1.shoot(0.01);  // ako se stavi veci dt onda graf samo ima manje koraka, neam ne fizikalnog gibanja
    p1.write_data();
    range_vs(0.01);
    return 0;
}
