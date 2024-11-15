#include <iostream>
#include "logisticRegression.hpp"
#include <vector>
#include <stdexcept>

int LogisticRegression::fit(const std::vector<std::vector<int>>& X_Train, const std::vector<int>& Y_Train) {

    std::size_t YSize = Y_Train.size();
    std::size_t XDim = X_Train.size();

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

    // Print dimensions of X_Train
    std::cout << "X_Train dimensions: " << X_Train.size() << "x" << (X_Train.empty() ? 0 : X_Train[0].size()) << std::endl;
    
    // Print number of elements in Y_Train
    std::cout << "Y_Train size: " << Y_Train.size() << std::endl;

    return 0;
}
