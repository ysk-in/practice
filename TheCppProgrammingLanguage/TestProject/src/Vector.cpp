#include "pch.h"
#include "Vector.h"
#include <iostream>
#include <cmath>

double Vector::sqrt(double d) {
    return std::sqrt(d);
}

double& Vector::operator[](int i) {
    if (i < 0 || i >= size())
        throw std::out_of_range{"Vector::operator[]"};
    return elem[i];
}

int Vector::size() const {
    return sz;
}


double Vector::read_and_sum(int s) {
    Vector v(s);
    for (int i = 0; i < v.size(); i++) {
        std::cin >> v[i];
    }

    double sum = 0;
    for (int i = 0; i < v.size(); i++) {
        sum += v[i];
    }

    return sum;
}

Vector vector_f(Vector v, Vector& rv, Vector *pv) {
    std::cout << "size(obj)=" << v.size()
              << ", size(ref)=" << rv.size()
              << ", size(pointer)=" << pv->size()
              << std::endl;
    return v;
}

void Vector::push_back(double d) {
    // push_backの実装は13.6.4.3らしいので後回し
    return;
}

void fct(int n) {
    Vector v(n);
    std::cout << "v1" << std::endl;
    {
        Vector v2(2 * n);
    } // v2はここで解体される(デストラクタが実行される)
} // vはここで解体される

Vector vector_read(istream& is) {
    Vector v = {1};
    for (double d; is >> d;) {
        v.push_back(d);
        return v;
    }
}
