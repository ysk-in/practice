#include "complex.h"

using namespace my_complex;

complex & complex::operator*=(complex z)
{
	re *= z.re;
	im *= z.im;
	return *this;
}

complex & complex::operator/=(complex z)
{
	re /= z.re;
	im /= z.im;
	return *this;
}


// complexの内部データ表現に直接アクセスする必要がないため,クラス定義とは分離して記述する。
// 以下で定義する関数の引数は値渡し(コピー)のため，値を変更しても，呼び出し側の値には影響を与えない。

complex operator+(complex a, complex b)
{
	return a += b;
}

complex operator-(complex a, complex b)
{
	return a -= b;
}

complex operator-(complex a)
{
	// 関数の戻り値の型をcomplexと指定しているため以下でコンストラクタが呼ばれる。
	return { -a.real(), -a.imag() };
	// complex z = { -a.real(), -a.imag() }; と書いているようなもの。
}

complex operator*(complex a, complex b)
{
	return a *= b;
}

complex operator/(complex a, complex b)
{
	return a /= b;
}

bool operator==(complex a, complex b)
{
	return a.real() == b.real() && a.imag() == b.imag();
}

bool operator!=(complex a, complex b)
{
	return a.real() == b.real() && a.imag() == b.imag();
}

void my_complex::f(complex z)
{
	complex a{ 2, 3 };
	complex b{ 1 / a };
	complex c{ a + z * complex{1, 2.3} };
	if (c != b)
		c = -(b / a) + 2 * b;
}
