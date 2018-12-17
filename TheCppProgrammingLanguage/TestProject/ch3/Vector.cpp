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

const double& Vector::operator[](int i) const {
    double& v = elem[i] ;
    return v;
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

Vector vector_f(Vector v, Vector& rv, Vector* pv) {
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

Vector vector_read(std::istream& is) {
    Vector v = {1};
    for (double d; is >> d;) {
        v.push_back(d);
    }
    return v;
}

Vector::Vector(const Vector& a) :
        elem{new double[a.sz]}, sz{a.sz} {
    for (int i = 0; i < sz; i++) {
        elem[i] = a.elem[i];
    }
}

void Vector::print_elem() {
    if (elem == nullptr)
        return;
    for (int i = 0; i < sz; i++) {
        std::cout << "elem[" << i << "]=" << elem[i] << ", ";
    }
    std::cout << std::endl;
}

Vector& Vector::operator=(const Vector& a) {
    auto* p = new double[a.sz];
    for (int i = 0; i < a.sz; i++)
        p[i] = a.elem[i];
    // 古い要素を削除
    delete[] elem;
    elem = p;
    sz = a.sz;
    return *this;
}

Vector operator+(const Vector& a, const Vector& b) {
    if (a.size() != b.size())
        throw Vector_size_mismatch{};
    Vector res(a.size());
    for (int i = 0; i < a.size(); i++) {
        res[i] = a[i] + b[i];
    }
    // 戻り値の型はVector(実体・コピー)なので、ここで定義したresを
    // 呼びもとで参照可能な場所にコピーし、呼び元では参照する。
    return res;
}
