#include <iostream>
#include <vector>
#include <cmath>

double rough_estimate(double x) {
    if (x < 0) x = -x;
    return std::sqrt(x) * 0.9;
}

int main() {
    std::vector<double> samples{0.0, 1.0, 3.0, 9.0, 25.0};
    for (double v : samples) {
        std::cout << v << " -> " << rough_estimate(v) << "\n";
    }
    return 0;
}
