#include <iostream>
#include "logisticRegression.hpp"
#include <vector>
#include <stdexcept>
#include <cmath>

int checks(const std::vector<std::vector<double> >& X_Train, const std::vector<int>& Y_Train) {

    std::size_t YSize = Y_Train.size();
    std::size_t XDim = X_Train.size();

    // Initial dimentionality and binomial checks
    for (std::size_t i=0; i < XDim; ++i) {
        if (YSize != X_Train[i].size()){
            throw std::runtime_error("Error : Input and Output Features are of different sizes");
        }
    }

    for (std::size_t target_val : Y_Train) {
        if (target_val != 0 && target_val != 1) {
            throw std::runtime_error("Error : Target variable can only be binary (0 or 1)");
        }
    }
    
    return 0;
}

std::vector<double> calculate_linear_output (const std::vector<std::vector<double> >& X_Train, const std::vector<double>& W) {
    std::size_t RecordSize = X_Train[0].size();
    std::size_t FieldSize = X_Train.size();

    // Declaring the output variable where the output gets saved to
    std::vector<double> Z(RecordSize, 0.0);

    for (std::double_t records = 0; records < RecordSize; ++records) {
        for (std::double_t fields = 0; fields < FieldSize; ++fields) {
            Z[records] += X_Train[fields][records] * W[fields];
        }

    }

    return Z;
}


int LogisticRegression::fit(const std::vector<std::vector<double> >& X_Train, const std::vector<int>& Y_Train) {

    std::size_t YSize = Y_Train.size();
    std::size_t XDim = X_Train.size();

    // Initial dimentionality and binomial checks
    checks(X_Train,Y_Train);
    // Print dimensions of X_Train
    std::cout << "X_Train dimensions: " << XDim << "x" << (X_Train.empty() ? 0 : X_Train[0].size()) << std::endl;
    // Print number of elements in Y_Train
    std::cout << "Y_Train size: " << YSize << std::endl;

    
    // Initializing the weights for linear function
    std::vector<double> w(XDim, 0.5);

    // Calculate the linear estimator value (z = summation(x*w))
    std::vector<double> Z(YSize, 0.0);
    Z = calculate_linear_output(X_Train,w);

    for (double out:Z) {
        std::cout << out << " ";
    }
    std::cout << std::endl;

    return 0;
}
