#include "vector_template.h"
#include <stdexcept>


template<typename T>
const T& vector_template<T>::operator[](int i) const {
    if (i < 0 || size() <= i) {
        std::cout << "error!" << std::endl;
        throw std::length_error{"Construct(Vector) was failed."};
    }
    return elem[i];
}

void print_vector_template(const vector_template<std::string>& v) {
    for (int i = 0; i < v.size(); i++) {
        if (!v[i].empty())
            std::cout << v[i] << std::endl;
    }
}
