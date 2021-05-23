#include <iostream>
#include <math.h>
#include <vector>
#include <fstream>
using namespace std;

class Bungee {


    public:
        vector<float> v;
        vector<float> h;
        vector<float> t;
        vector<float> Ekinetic;
        vector<float> Epotential;
        vector<float> Eelastic;
        vector<float> Etotal;
        float m;
        float k;
        float Cd;
        float A;
        float rho;
        float l;
        float total_time;
        float _h0;

        Bungee(float h0, float len, float mass, float area, float coef, float konst, float _total_time) {

            v.push_back(0);
            h.push_back(h0);
            t.push_back(0);
            Ekinetic.push_back(0);
            Epotential.push_back(m * 9.81 * h0);
            Eelastic.push_back(0);
            Etotal.push_back(Epotential.back());
            m = mass;
            l = len;
            A = area;
            Cd = coef;
            k = konst;
            rho = 1.227;
            total_time = _total_time;
            _h0 = h0;
        }

    public:
        template <typename T>
        int sgn(T val) {

            return (T(0) < val) - (val < T(0));
        } 

    private:
        void __reset() {
            v.clear();
            v.push_back(0);
            h.clear();
            h.push_back(_h0);
            t.clear();
            t.push_back(0);
            Ekinetic.clear();
            Ekinetic.push_back(0);
            Epotential.clear();
            Epotential.push_back(m * 9.81 * _h0);
            Eelastic.clear();
            Eelastic.push_back(0);
            Etotal.clear();
            Etotal.push_back(Epotential.back());

        }
    public:
        float drag_force(float v) {

            float drag = -sgn(v) * 0.5 * pow(v, 2) * rho * Cd * A;

            return drag;
        }

    public:
        float elastic_force(vector<float> h) {

            float x = h.at(0) - h.back() - l;

            if (x > 0) {
                return k * x;
            } else {
                return 0;
            }
        }

    public:
        float accAR(float df, float ef) {

            float a = -9.81 + ((df + ef) / m);

            return a;
        }

    public:
        float EkineticF(float m, float v) {

            float energy = 0.5 * m * pow(v, 2);

            return energy;
        }

    public:
        float EpotentialF(float m, float h) {

            float energy = m * 9.81 * h;

            return energy;
        }

    public:
        float EelasticF(vector<float> h, float l, float k) {

            float x = h.at(0) - h.back() - l;
            if (x > 0) {
                return 0.5 * k * pow(x, 2);  
            } else {
                return 0;
            }
        }

    private:
        void __moveDF(float dt) {
            float a = -9.81 + ((drag_force(v.back()) + elastic_force(h)) / m);
            v.push_back(v.back() + (a * dt));
            h.push_back(h.back() + (v.back() * dt));
            t.push_back(t.back() + dt);
            Ekinetic.push_back(EkineticF(m, v.back()));
            Epotential.push_back(EpotentialF(m, h.back()));
            Eelastic.push_back(EelasticF(h, l, k));
            Etotal.push_back(Ekinetic.back() + Epotential.back() + Eelastic.back());

        }

    private:
        void __move(float dt) {
            float a = -9.81 + (elastic_force(h) / m);
            v.push_back(v.back() + (a * dt));
            h.push_back(h.back() + (v.back() * dt));
            t.push_back(t.back() + dt);
            Ekinetic.push_back(EkineticF(m, v.back()));
            Epotential.push_back(EpotentialF(m, h.back()));
            Eelastic.push_back(EelasticF(h, l, k));
            Etotal.push_back(Ekinetic.back() + Epotential.back() + Eelastic.back());

        }
    public:
        void jump_and_write(float dt) {

            ofstream myfile;

            while (t.back() < total_time) {
                __moveDF(dt);
            };

            myfile.open("t_dataAR.txt");
                for (int j = 0; j < t.size(); j++) {
                    myfile << t.at(j) << " ";
            }
            myfile.close();

            myfile.open("h_dataAR.txt");
                for (int j = 0; j < h.size(); j++) {
                    myfile << h.at(j) << " ";
            }
            myfile.close();

            myfile.open("ekineticAR.txt");
                for (int j = 0; j < Ekinetic.size(); j++) {
                    myfile << Ekinetic.at(j) << " ";
            }
            myfile.close();

            myfile.open("epotentialAR.txt");
                for (int j = 0; j < Epotential.size(); j++) {
                    myfile << Epotential.at(j) << " ";
            }
            myfile.close();

            myfile.open("eelasticAR.txt");
                for (int j = 0; j < Eelastic.size(); j++) {
                    myfile << Eelastic.at(j) << " ";
            }
            myfile.close();

            myfile.open("etotalAR.txt");
                for (int j = 0; j < Etotal.size(); j++) {
                    myfile << Etotal.at(j) << " ";
            }
            myfile.close();

            __reset();

            while (t.back() < total_time) {
                __move(dt);
            };
            myfile.open("t_data.txt");
                for (int j = 0; j < t.size(); j++) {
                    myfile << t.at(j) << " ";
            }
            myfile.close();

            myfile.open("h_data.txt");
                for (int j = 0; j < h.size(); j++) {
                    myfile << h.at(j) << " ";
            }
            myfile.close();

            myfile.open("ekinetic.txt");
                for (int j = 0; j < Ekinetic.size(); j++) {
                    myfile << Ekinetic.at(j) << " ";
            }
            myfile.close();

            myfile.open("epotential.txt");
                for (int j = 0; j < Epotential.size(); j++) {
                    myfile << Epotential.at(j) << " ";
            }
            myfile.close();

            myfile.open("eelastic.txt");
                for (int j = 0; j < Eelastic.size(); j++) {
                    myfile << Eelastic.at(j) << " ";
            }
            myfile.close();

            myfile.open("etotal.txt");
                for (int j = 0; j < Etotal.size(); j++) {
                    myfile << Etotal.at(j) << " ";
            }
            myfile.close();

            __reset();
        }
};

int main() {

    Bungee r1 (100, 50, 60, 0.1, 2, 50, 100);
    //          h    l   m   a    c    k   tt
    r1.jump_and_write(0.001);
}