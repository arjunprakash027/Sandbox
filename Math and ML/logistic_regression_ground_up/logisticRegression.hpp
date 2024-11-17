#ifndef ARRAY_UTILITIES_HPP
#define ARRAY_UTILITIES_HPP

#include <string>
#include <vector>

class LogisticRegression {
    public:
        static int fit(const std::vector<std::vector<double> >& X_Train, const std::vector<double>& Y_Train);
};

int checks(const std::vector<std::vector<double> >& X_Train, const std::vector<double>& Y_Train);
std::vector<double> calculate_linear_output (const std::vector<std::vector<double> >& X_Train, const std::vector<double>& W);
int sigmoid_function (std::vector<double>& Z);
std::vector<double> log_loss (const std::vector<double> Z, const std::vector<double> Actual);

#endif