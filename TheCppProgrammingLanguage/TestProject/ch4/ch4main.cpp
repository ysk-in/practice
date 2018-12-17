#include <iostream>
#include <string>
#include <list>
#include <istream>

std::string compose(const std::string& name, const std::string& domain) {
    return name + '@' + domain;
}

void test_string() {
    std::string s{"Four legs Good; two legs Bad!"};
    std::cout << "s = " << s << std::endl;

    std::list<std::string> slogans{"War is Peace", "Freedom is Slavery", "Ignorance is Strength"};
    int count_slogans = 0;
    for (auto& slogan : slogans)
        std::cout << "slogan(" << count_slogans++ << ") = " << slogan << std::endl;

    std::cout << compose(std::string{"dmr"}, std::string{"bell-labs.com"}) << std::endl;

    std::string name_niels = "Niels Stroustrup";
    std::cout << "name_niels = " << name_niels << std::endl;
    std::cout << "name_niels.substr(6, 10) = " << name_niels.substr(6, 10) << std::endl;
    std::cout << "name_niels.replace(0, 5, \"nicholas\") = " << name_niels.replace(0, 5, "nicholas") << std::endl;
    name_niels[0] = std::toupper(name_niels[0]);
    std::cout << "std::toupper(name_niels[0]) = " << name_niels << std::endl;
}

void test_iostream() {
    int b = 'b';
    char c = 'c';
    std::cout << 'a' << b << c << std::endl;
}

void test_istream() {
    std::cout << "Please enter int value : ";
    int i;
    std::cin >> i;

    std::cout << "Please enter double value : ";
    double d;
    std::cin >> d;

    std::cout << "Please enter your name : ";
    std::string str;
    std::cin >> str;

    std::cout << "Please enter your name(line) : ";
    std::string str_line;
    std::cin.ignore();
    std::getline(std::cin, str_line);

    std::cout << "i = " << i << ", d = " << d << ", str = " << str
              << ", str_line = " << str_line << std::endl;
}

int main() {
    std::cout << "ch4main" << std::endl;

    test_string();
    test_iostream();
    test_istream();
}

