#ifndef TESTPROJECT_LESS_THAN_H
#define TESTPROJECT_LESS_THAN_H

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

template <typename C, typename P>
int less_than_count(const C& c, P predicate) {
    int cnt = 0;
    for (const auto& x : c)
        if (predicate(x))
            cnt++;
        return cnt;
}

#endif //TESTPROJECT_LESS_THAN_H
