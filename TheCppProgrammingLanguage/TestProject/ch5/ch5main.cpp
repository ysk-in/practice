#include <iostream>
#include <mutex>
#include <memory>
#include <fstream>
#include <string>
#include <ios>

std::mutex m;

void test_mutex() {
    std::unique_lock<std::mutex> lock{m};
    // これだけでmが有効な間(デストラクタによって解放されるまで)、
    // 排他とるって動きしてくれるらしい。
}

void test_open_file() {
    std::string file_name = "aaa.txt";

    std::shared_ptr<std::fstream> fp{new std::fstream(file_name, std::ios_base::in)};
    if (!*fp) {
        std::cerr << "Open error" << std::endl;
    }
    std::string str;
    while(!(*fp).eof()) {
        std::getline((*fp), str);
        std::cout << str << std::endl;
    }
}

int main() {
    std::cout << "ch5main" << std::endl;
    test_open_file();
}
