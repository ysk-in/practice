#ifndef TESTPROJECT_LESS_THAN_H
#define TESTPROJECT_LESS_THAN_H

#include <iostream>

template<typename T>
class Less_than {
    const T val;
public:
    Less_than(const T& v) :
            val(v) {
    }

    bool operator()(const T& x) const {
        return x < val;
    }
};

template<typename C, typename P>
int less_than_count(const C& c, P predicate) {
    int cnt = 0;
    for (const auto& x : c)
        if (predicate(x))
            cnt++;
    return cnt;
}

template<typename T>
void less_than_f(T x) {
    std::cout << x << " ";
}

// templateを利用し可変長引数tailを受け取る
template<typename T, typename... Tail>
void less_than_f(T head, Tail... tail) {
    // 引数の先頭要素を対象にした処理を行なう
    less_than_f(head);
    // 残りの要素をアンパックし，本関数を再起呼び出し。
    less_than_f(tail...);
}


#endif //TESTPROJECT_LESS_THAN_H
