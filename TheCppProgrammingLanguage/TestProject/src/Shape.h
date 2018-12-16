#pragma once
#ifndef TESTPROJECT_SHAPE_H
#define TESTPROJECT_SHAPE_H

#include <iostream>
#include <vector>
#include <istream>

class Point {
public:
    Point() {}

    ~Point() {}
};

class Shape {
public:
    // 引数ありコンストラクタのdelete追加でコンパイルエラー出るようになった。
    // 引数ありコンストラクタのdelete定義だけでも、デフォルトコンストラクタは自動生成されなくなる？
    // コンパイルエラー抑止のためにデフォルトコンストラクタくを明示的に定義する。
    Shape() {}

    virtual Point center() const = 0;

    virtual void move(Point to) = 0;

    virtual void draw() const {
        std::cout << "Shape::draw() was called." << std::endl;
    }

    virtual void rotate(int angle) = 0;

    virtual ~Shape() {}

    // 基底クラスであるShapeからは、派生クラスのメンバが分からない(例えばCircle.x)。
    // そのため、適切なCopyやMoveを行うことは難しい。
    // delete指定することで、関数定義を削除できる。
    // これにより、基底クラスを利用したCopy/Moveの呼び出しをコンパイラで検出することができる。
    Shape(const Shape&) = delete;

    // ちなみに、CopyとMoveは明示的にdeleteしなくても実害は発生しない。
    // なぜなら、明示的にデストラクタを宣言したクラスに対しては、Moveが暗黙裏には生成されないから。
    Shape& operator=(const Shape&) = delete;

    Shape(Shape&&) = delete;

    Shape& operator=(Shape&&) = delete;
};

class Circle : public Shape {
public:
    Circle(Point p, int rr) :
            x{p}, r{rr} {}

    Point center() const { return x; }

    void move(Point to) { x = to; }

    void draw() const {
        std::cout << "Circle::draw was called." << std::endl;
    };

    void rotate(int) {
        std::cout << "Circle::rotate was called." << std::endl;
    }

    ~Circle() {}

private:
    Point x;
    int r;
};

class Smiley : public Circle {
public:
    Smiley(Point p, int r) :
            Circle{p, r}, mouth{nullptr} {}

    Point center() const {
        return Circle::center();
    }

    void move(Point to) {
        Circle::move(to);
    }

    void draw() const;

    void rotate(int) {
        std::cout << "Smiley::rotate was called." << std::endl;
    }

    void add_eye(Shape* s) {
        eyes.push_back(s);
    }

    void set_mouth(Shape* s) {
        std::cout << "Smiley::set_mouth was called." << std::endl;
        mouth = s;
    }

    virtual void wink(int i) {
        std::cout << "Smiley::wink was called." << std::endl;
    }

    ~Smiley() {
        delete mouth;
        for (auto p : eyes) {
            delete p;
        }
    }

private:
    std::vector<Shape*> eyes;
    Shape* mouth;
};

void shape_rotate_all(std::vector<Shape*>& v, int angle);

enum class Kind {
    circle,
    triangle,
    smiley
};

// Shape* read_shape(std::istream& is);
std::unique_ptr<Shape> read_shape(std::istream& is);


#endif //TESTPROJECT_SHAPE_H
