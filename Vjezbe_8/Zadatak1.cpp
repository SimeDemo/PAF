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
        template <typename T>
        int sgn(T val) {

            return (T(0) < val) - (val < T(0));
        } 
    
    // public:

    //     int dragForce(float vel) {

    //         float force = (pow(vel, 2) * density * coef * area) / 2;

    //         if (vel >= 0) {
                
    //             return force;
    //         } else {

    //             return -force;
    //         }
    //     }

    // public:

    //     int acc_x(float x_vel) {

    //         return dragForce(x_vel) * (1/mass);
    //     }

    // public:

    //     int acc_y(float y_vel) {

    //         return -9.81 - (dragForce(y_vel) * (1/mass));
    //     }

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

        int acc_x_RK(float velocity, float knx) {
            
            float acc = -sgn(velocity) * ((pow(velocity + (0.5*knx), 2) * density * coef * area) / (2*mass));

            return acc;
        }

    public:

        int acc_y_RK(float velocity, float kny) {

            float acc =  -9.81 - ((sgn(velocity) * ((pow(velocity + (0.5*kny), 2) * density * coef * area) / (2*mass))));

            return acc;
        }

    private:
        
        void __moveRK(float dt) {

            k1vx = acc_x_RK(vx.back(), 0) * dt;
            k1x = vx.back() * dt;
            k2vx = acc_x_RK(vx.back(), k1vx) * dt;
            k2x = (vx.back() + (0.5 * k1vx)) * dt;
            k3vx = acc_x_RK(vx.back(), k2vx) * dt;
            k3x = (vx.back() + (0.5 * k2vx)) * dt;
            k4vx = (vx.back() + k3vx) * dt;
            k4x = (vx.back() + k3vx) * dt;
            vx.push_back(vx.back() + ((k1vx + (2 * k2vx) + (2 * k3vx) + k4vx) / 6));
            x.push_back(x.back() + ((k1x + (2 * k2x) + (2 * k3x) + k4x) / 6));

            k1vy = acc_y_RK(vy.back(), 0) * dt;
            k1y = vy.back() * dt;
            k2vy = acc_y_RK(vy.back(), k1vy) * dt;
            k2y = (vy.back() + (0.5 * k1vy)) * dt;
            k3vy = acc_x_RK(vy.back(), k2vy) * dt;
            k3y = (vy.back() + (0.5 * k2vy)) * dt;
            k4vy = (vy.back() + k3vy) * dt;
            k4y = (vy.back() + k3vy) * dt;
            vy.push_back(vy.back() + ((k1vy + (2 * k2vy) + (2 * k3vy) + k4vy) / 6));
            y.push_back(y.back() + ((k1y + (2 * k2y) + (2 * k3y) + k4y) / 6));
        }

    public:

        void shoot(float _dt) {

            while (y.back() >= 0) {
                __move(_dt);
            };
            cout << x.back() << endl;
        }

    public:

        void shootRK(float _dt) {

            while (y.back() >= 0) {
                __moveRK(_dt);
            };
            cout << "RK " << x.back() << endl;
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
                myfile << endl;
                for (int j = 0; j < y.size(); j++) {
                    myfile << y.at(j) << " ";
                }
                myfile.close();
        }
};


int main() {
    Projectile p1 (10, 30, 1.227, 0.5, 0.1, 5, 0, 0);
    //              v  th  rho    C   A   m  x0 y0
    p1.shootRK(0.01);  // za svaki dt, graf izgleda normalno, osim ako nesto visoko
    p1.write_dataRK();
    return 0;
}
