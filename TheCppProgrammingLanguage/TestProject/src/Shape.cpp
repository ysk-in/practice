#include "Shape.h"

void Smiley::draw() const {
    std::cout << "Smiley::draw() was called." << std::endl;
    Circle::draw();
    for (auto p : eyes)
        p->draw();
    mouth->draw();
}

void shape_rotate_all(std::vector<Shape*>& v, int angle) {
    for (auto p : v) {
        p->rotate(angle);
    }
}

Kind get_kind() {
    return Kind::smiley;
}

//Shape* read_shape(std::istream& is) {
std::unique_ptr<Shape> read_shape(std::istream& is) {
    // ... shapeの先頭部をisから読み込んでKind kを判断する処理。
    // 今回はkに固定値Kind::circleを入れる。
    Kind k = get_kind();
    Point p = Point{};
    Shape* s = nullptr;
    switch (k) {
        case Kind::circle:
            std::cout << "read_shape will return circle." << std::endl;
            s = new Circle{p, 1};
//            return s;
            return std::unique_ptr<Shape>{s};
        case Kind::triangle:
            std::cout << "read_shape will return triangle." << std::endl;
//            return new Circle{p, 1};
            s = new Circle{p, 1};
            return std::unique_ptr<Shape>{s};
        case Kind::smiley:
            std::cout << "read_shape will return smiley." << std::endl;
//            return new Smiley{p, 1};
            s = new Smiley{p, 1};
            return std::unique_ptr<Shape>{s};
        default:
            return nullptr;
    }
}
