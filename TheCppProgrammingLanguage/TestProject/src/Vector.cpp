#include "pch.h"
#include "Vector.h"
#include <iostream>

double Vector::sqrt(double d)
{
	return std::sqrt(d);
}

//Vector::Vector(int s) :
//	elem{ new double[s] },
//	sz{ s }
//{
//}


Vector::Vector(int s)
{
	if (s < 0)
		throw std::length_error{"Construct(Vector) was failed."};
	elem = new double[s];
	sz = s;
}


Vector::~Vector()
{
}

double& Vector::operator[](int i)
{
	if (i < 0 || i >= size())
		throw std::out_of_range{ "Vector::operator[]" };
	return elem[i];
}

int Vector::size()
{
	return sz;
}


double Vector::read_and_sum(int s)
{
	Vector v(2);
	for (int i = 0; i < v.size(); i++)
	{
		std::cin >> v[i];
	}

	double sum = 0;
	for (int i = 0; i < v.size(); i++)
	{
		sum += v[i];
	}

	return sum;
}

void Vector::f(Vector v, Vector& rv, Vector* pv)
{
	std::cout << "size(obj)=" << v.size()
		<< ", size(ref)=" << rv.size()
		<< ", size(pointer)=" << pv->size()
		<< std::endl;
}

