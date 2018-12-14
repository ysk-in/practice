#pragma once

#include <iostream>
#include <stdexcept>
#include <string>
#include <initializer_list>
#include <istream>

class Vector {
public:
//    Vector::Vector(int s) :
//    	elem{ new double[s] },
//    	sz{ s }
//    {
//    }

    Vector(int s) {
        if (s < 0)
            throw std::length_error{"Construct(Vector) was failed."};
        elem = new double[s];
        sz = s;
    }

    Vector(std::initializer_list<double> list) :
            elem{new double[(list.size())]},
            sz{static_cast<int>(list.size())} {
        copy(list.begin(), list.end(), elem);
    }

    ~Vector() {
        if (elem != nullptr)
            delete[] elem;
    }

    double& operator[](int i);

    int size() const;

    double read_and_sum(int s);

    double sqrt(double);

    void push_back(double);

private:
    double *elem = nullptr;
    int sz = -1;
};

Vector vector_f(Vector v, Vector& rv, Vector *pv);

void fct(int n);

Vector vector_read(istream& is);
