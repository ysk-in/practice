#ifndef TESTPROJECT_VECTOR_TEMPLATE_H
#define TESTPROJECT_VECTOR_TEMPLATE_H

#include <stdexcept>
#include <string>
#include <iostream>
#include <array>

template<typename T>
class vector_template {

private:
    T* elem = nullptr;
    int sz;
public:
    // templateを利用する場合、実装はヘッダに書くのが楽。
    // 宣言を.hに、実装を.cppにしたい場合は以下参照。
    // https://qiita.com/i153/items/38f9688a9c80b2cb7da7
    vector_template(int s) {
        if (s < 0)
            throw std::length_error{"Construct(Vector) was failed."};
        elem = new T[s]{};
        sz = s;
    }

    ~vector_template() {
        if (elem != nullptr) {
            delete[] elem;
            elem = nullptr;
        }
    }

    void add_elem(std::string str) {
        if (elem == nullptr || sz <= 0) {
            std::cout << "add_elem was failed. elem length error." << std::endl;
            return;
        }
        for (int i = 0; i < sz; i++) {
            if (elem[i].empty()) {
                elem[i] = str;
                return;
            }
        }
        std::cout << "add_elem was failed. there is no empty elem." << std::endl;
        return;
    }

    void add_elem(int val) {
        if (elem == nullptr || sz <= 0) {
            std::cout << "add_elem was failed. elem length error." << std::endl;
            return;
        }
        for (int i = 0; i < sz; i++) {
            if (elem[i] == 0) {
                elem[i] = val;
                return;
            }
        }
        std::cout << "add_elem was failed. there is no empty elem." << std::endl;
        return;
    }

    T& operator[](int i);

    const T& operator[](int i) const;

    int size() const { return sz; }

    // 範囲forループをサポートするための関数定義(begin/end)
    T* begin() const {
        return sz ? &elem[0] : nullptr;
    }

    T* end() const {
        return &elem[sz];
    }

};

void print_vector_template(const vector_template<std::string>& v);

template<typename Container, typename Value>
Value vector_template_sum(const Container* c, Value v) {
    for (auto x : *c)
        v += x;
    return v;
}

//void vector_template_f2(vector_template<std::string>& vs) {
//    for (auto& s : vs)
//        std::cout << s << std::endl;
//}


#endif //TESTPROJECT_VECTOR_TEMPLATE_H
