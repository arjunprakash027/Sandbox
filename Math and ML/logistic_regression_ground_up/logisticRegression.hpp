#ifndef ARRAY_UTILITIES_HPP
#define ARRAY_UTILITIES_HPP

#include <string>
#include <vector>

class LogisticRegression {
    public:
        static int fit(const std::vector<std::vector<int>>& X_Train, const std::vector<int>& Y_Train);
};

#endif