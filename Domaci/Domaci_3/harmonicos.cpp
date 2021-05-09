#include <iostream>
#include <math.h>
#include <vector>
#include <fstream>
using namespace std;

class HarmonicOscillator {

    public:
        float m;
        float k;
        float x0;
        vector<float> x;
        float v0;
        vector<float> v;
        vector<float> a;
        vector<float> t_list;
        float t;

        HarmonicOscillator(float _m, float _k, float _x0, float _v0, float _t) {

            m = _m;
            k = _k;
            x.push_back(_x0);
            v.push_back(_v0);
            a.push_back((-_k * _m) * x.back());
            t = _t;
            t_list.push_back(0);

        }
    
    private:

        void __reset() {  // for plotting
            x.clear();
            x.push_back(x0);
            v.clear();
            v.push_back(v0);
            a.clear();
            a.push_back((k * m) * x.back());
            t_list.clear();
            t_list.push_back(0);
        }

    public:

        void oscillate(int dt) {

            for (int i = 0; i < (t / dt); i++) {
                t_list.push_back(t_list.back() * dt);
                a.push_back((-k / m) * x.back());
                v.push_back(v.back() + (a.back() * dt));
                x.push_back(x.back() + (v.back() * dt));
            }
        }
    
    public:

        void write() {
            
            ofstream myfile;
                myfile.open("plot_data.txt");
                for (int i = 0; i < a.size(); i++) {
                    myfile << "acceleration" << a.at(i) << " ";
                    myfile << "velocity " << v.at(i) << " ";
                    myfile << "xcoord " << x.at(i) << " ";
                    myfile << "time " << t_list.at(i) << " ";
                }
                myfile.close();
        }
    
};

int main() {

    HarmonicOscillator HarmonicOscillator (10, 5, 5, 5, 50);
    HarmonicOscillator.oscillate(0.01);
    HarmonicOscillator.write();
}