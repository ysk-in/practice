#pragma once


class Vector
{
public:
	Vector(int s);
	~Vector();
	double& operator[](int i);

	int size();
	double read_and_sum(int s);
	static void f(Vector v, Vector& rv, Vector* pv);
	double sqrt(double);

private:
	double* elem;
	int sz;
};

