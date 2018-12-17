#pragma once

namespace my_complex {

    class complex {
        double re, im;

    public:
        // クラス内で定義することで関数をインライン化する

        complex(double r, double i) :
                re{r}, im{i} {
        }

        complex(double r) :
                re{r}, im{0} {
        }

        // デフォルトコンストラクタ(引数なし)
        complex() :
                re{0}, im{0} {
        }

        ~complex() {
        }

        // const指定子により オブジェクトを変更しないことを指定
        double real() const {
            // re++; // const指定子によりエラーとなる
            return re;
        }

        void real(double d) {
            re = d;
        }

        double imag() const {
            return im;
        }

        void imag(double d) {
            im = d;
        }

        complex& operator+=(complex z) {
            re += z.re;
            im += z.im;
            return *this;
        }

        complex& operator-=(complex z) {
            re -= z.re;
            im -= z.im;
            return *this;
        }

        complex& operator*=(complex z);

        complex& operator/=(complex z);
    };

    void f(complex z);
}

