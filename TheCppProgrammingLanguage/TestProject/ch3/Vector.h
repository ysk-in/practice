#pragma once
#ifndef TESTPROJECT_VECTOR_H
#define TESTPROJECT_VECTOR_H

#include <iostream>
#include <stdexcept>
#include <string>
#include <initializer_list>
#include <istream>

class Vector {
private:
    double* elem = nullptr;
    int sz = -1;

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
        std::copy(list.begin(), list.end(), elem);
    }

    Vector(const Vector& a);

    // ムーブコンストラクタ(Move Constructor)。&&は右辺値参照を意味する。
    // std::move(Obj)やreturn Obj時などで、このコンストラクタは呼ばれる。
    // これにより、右辺のVectorの要素を左辺に(Copyするのでなく)Moveできる。
    Vector(Vector&& a) :
            elem{a.elem}, sz{a.sz} {
        // ↑でelem, sz の参照先として引数aのメンバを指すようにする。
        // ↓でaのメンバからは参照しなくする。これでMoveが実現できる。
        std::cout << "Move Constructor of Vector was called." << std::endl;
        a.elem = nullptr;
        a.sz = 0;
    }

    ~Vector() {
        if (elem != nullptr)
            delete[] elem;
    }

    // Vectorのコピー代入を正しく行うためのOverride
    Vector& operator=(const Vector& a);

    double& operator[](int i);

    // ちゃんと理解できていないけど、以下から実行されるっぽい。
    // operator+(const Vector& a, const Vector& b);
    // res[i] = a[i] + b[i]; ってすると戻り値の型がconstのが呼ばれるっぽい?
    const double& operator[](int i) const;

    int size() const;

    double read_and_sum(int s);

    double sqrt(double);

    void push_back(double);

    void print_elem();
};

Vector vector_f(Vector v, Vector& rv, Vector* pv);

void fct(int n);

Vector vector_read(std::istream& is);

struct Vector_size_mismatch : public std::exception {
};

Vector operator+(const Vector& a, const Vector& b);

#endif //TESTPROJECT_VECTOR_H
