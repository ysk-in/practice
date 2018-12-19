#include <iostream>
#include <string>
#include <list>
#include <istream>
#include <vector>
#include <stdexcept>
#include <map>
#include <algorithm>
#include <set>
#include <fstream>

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
    std::string str_line, str_line2;
    // std::cinは，直前で変数strへの入力を読み取った状態。
    // (getlineでなく，>>により入力を読み取ったため)区切り文字の改行文字の前までがstrには入り
    // 改行文字がcinには残っている。そのため，このcinのままgetlineを実行すると，
    // 先頭に残った改行文字を読み取り，それをstr_lineへ設定してしまう。
    // そのため，ignoreを実行し，cinに残っている(先頭1文字)改行文字を無視する。
    // 参考 http://torus711.hatenablog.com/entry/20131205/p1
    std::cin.ignore();
    std::getline(std::cin, str_line);
    // getlineでcinの入力を読み取ったときは，行末の改行文字が読み捨てられるため，
    // ignoreせずともgetlineが意図通りに動作する。4.3.2の末尾に記載あり。
    std::cout << "Please enter your second name(line) : ";
    std::getline(std::cin, str_line2);

    std::cout << "i = " << i << ", d = " << d << ", str = " << str
              << ", str_line = " << str_line
              << ", str_line2 = " << str_line2
              << std::endl;
}

void test_str_vec() {
    std::vector<std::string> str_vec;
    std::cout << "Input the string to add to str_vec : ";
    // cin >> sで取得しているため，sにはスペース区切りで入力が来る。
    for (std::string s; std::cin >> s;) {
        // 改行だけをcinに入力された場合，"sが空でここに制御が戻る"とはならず，
        // こっちに制御が戻ってこないっぽい。なので，ここに制御戻したかったら
        // \sでない入力をして貰わないと駄目っぽい(?)
//        if (s.empty()) {
//            break;
//        }
        if (s == "!end") {
            break;
        }
        str_vec.push_back(s);
    }
    for (auto& s : str_vec) {
        std::cout << s << std::endl;
    }
}

struct TestEntry {
    std::string name;
    int number;
};

std::ostream& operator<<(std::ostream& os, const TestEntry& e) {
    return os << "{\"" << e.name << "\", " << e.number << "}" << std::endl;
}

std::istream& _get_failed(std::istream& is) {
    std::cerr << "Read TestEntry failed." << std::endl;
    is.setstate(std::ios_base::failbit);
    return is;
}

// InputStream(is)から，TestEntry{"name", number}を読み取る。
// isには以下形式でname, numberが入っていること。
// {"<name>",<number>} nameはchar配列, numberはint配列であること。
std::istream& operator>>(std::istream& is, TestEntry& e) {
    char c, c2;
    // "is >> c"は，isからcへの読み取りが成功したかを返す。
    // "is >> c"は，空白文字を読み飛ばす。
    if (!(is >> c) || c == '\n') {
        // 終了
        is.setstate(std::ios_base::failbit);
        return is;
    }
    if (c != '{'
        || !(is >> c2) || c2 != '"') {
        // {"から始まらない場合はエラー
        return _get_failed(is);
    }
    std::string name;
    // name部分の情報を読み取る。
    // is.get(c)は空白文字を読み飛ばさない。
    while (is.get(c) && c != '"') {
        // '"'が来ずに改行文字が来てしまったらエラー
        if (c == '\n')
            return _get_failed(is);
        name += c;
    }
    // <name>"直後にカンマが来なかったらエラー
    if (!(is >> c) || c != ',') {
        return _get_failed(is);
    }
    int number = 0;
    // isの先頭からintで読み取れるところまで読み取った後，}が来なかったらエラー
    if (!(is >> number >> c) && c != '}') {
        return _get_failed(is);
    }
    std::cout << "Read TestEntry succeeded." << std::endl;
    e = {name, number};
    return is;
}

void test_stream_operator() {
    for (TestEntry ee; std::cin >> ee;)
        std::cout << ee << std::endl;
}

void print_phone_book() {
    std::vector<TestEntry> phone_book = {
            {"David Hume",                      123456},
            {"Karl Popper",                     234567},
            {"Bertrand Arthur William Russell", 345678}
    };

//    for (int i = 0; i < phone_book.size(); i++) {
//        std::cout << phone_book[i];
//    }

    for (const auto& x : phone_book) {
        std::cout << x;
    }

    // vectorは要素数と初期値を明示的に与えて生成することも可能
    std::vector<TestEntry> test_vec(3, {"", 000000});
    for (const auto& x : test_vec) {
        std::cout << x;
    }

    std::cout << "Input the TestEntry to add to the phone_book : ";
    for (TestEntry e{}; std::cin >> e;) {
        if (e.name.empty()) {
            break;
        }
        phone_book.push_back(e);
    }
    for (const auto& x : phone_book) {
        std::cout << x;
    }

    // 以下ではコピーコンストラクタ(高コスト)が呼ばれ
    std::vector<TestEntry> book2 = phone_book;
    // 以下ではムーブコンストラクタ(低コスト)が呼ばれる
    book2 = std::move(phone_book);
    // book2にphone_bookにあった要素が正しく入っていることが確認できる
    std::cout << "print book2 start." << std::endl;
    for (const auto& x : book2) {
        std::cout << x;
    }
    // phone_bookの要素はbook2にmove済のため無くなっている
    std::cout << "print phone_book start." << std::endl;
    for (const auto& x : phone_book) {
        std::cout << x;
    }
}

template<typename T>
class CheckedVec : public std::vector<T> {
public:
    using std::vector<T>::vector;

    T& operator[](int i) {
        return std::vector<T>::at(i);
    }

    const T& operator[](int i) const {
        return std::vector<T>::at(i);
    }
};

void test_vec_out_of_range() {
    std::vector<TestEntry> vec = {
            {"David",    123456},
            {"Karl",     234567},
            {"Bertrand", 345678}
    };
    // size()は3で範囲外だけど，エラーとはならず以下は不定値が取れてしまう。
    int i = vec[vec.size()].number;
    std::cout << "i = " << i << std::endl;

    // 自作のCheckedVecでは，operator[]をオーバーライドし
    // vector::at()を実行することにより対象の要素を取り出す。
    // atの詳細は右記参照 https://cpprefjp.github.io/reference/vector/vector/at.html
    // atは範囲外の要素にアクセスする場合，out_of_rangeの例外を発生させるため，
    // 範囲外の要素を不当に参照する恐れがない。
    // そのため，著者さんはよくこのカスタムvectorを使うらしい。
    CheckedVec<TestEntry> checked_ved = {
            {"David",    123456},
            {"Karl",     234567},
            {"Bertrand", 345678}
    };
    try {
//        throw new std::length_error{"test"};
        i = checked_ved[checked_ved.size()].number;
        std::cout << "i = " << i << std::endl;
    } catch (std::out_of_range) {
        std::cout << "out_of_range error." << std::endl;
    } catch (...) {
        // ...指定で全Exception対象にできるっぽい 4.4.1.2の末尾で出てくる
        std::cout << "unknown exception thrown." << std::endl;
    }
}

void _test_list_iterator(std::vector<TestEntry>& vec, std::string& target_name) {
    for (const auto& x : vec) {
        if (x.name == target_name) {
            std::cout << "_test_list_iterator: Found number of \"" + target_name
                      << "\". The number is " << x.number << std::endl;
            return;
        }
    }
    std::cout << "_test_list_iterator: The target \""
              << target_name << "\" was not found." << std::endl;
}

void _test_list_for_loop(std::vector<TestEntry>& vec, std::string& target_name) {
    for (auto p = vec.begin(); p != vec.end(); p++) {
        if (p->name == target_name) {
            std::cout << "_test_list_for_loop: Found number of \"" + target_name
                      << "\". The number is " << p->number << std::endl;
            return;
        }
    }
    std::cout << "_test_list_for_loop: The target \""
              << target_name << "\" was not found." << std::endl;
}

std::vector<TestEntry>::iterator _get_iterator(std::vector<TestEntry>& vec, std::string& target_name) {
    for (auto p = vec.begin(); p != vec.end(); p++) {
        if (p->name == target_name) {
            std::cout << "_test_list_for_loop: Found number of \"" + target_name
                      << "\". The number is " << p->number << std::endl;
            return p;
        }
    }
    std::cout << "_test_list_for_loop: The target \""
              << target_name << "\" was not found." << std::endl;
    return vec.end();
}

void test_list() {
    std::vector<TestEntry> vec = {
            {"David",    123456},
            {"Karl",     234567},
            {"Bertrand", 345678}
    };
    std::string target_name = "Karl";
//    _test_list_iterator(vec, target_name);
//    _test_list_for_loop(vec, target_name);

    // target_nameの要素を指すイテレータを取得
    std::vector<TestEntry>::iterator it = _get_iterator(vec, target_name);
    // 取得したイテレータ(target_nameのnameを持つ要素)の前にTestEntryを追加
    vec.insert(it, TestEntry{"Person1", 999999});
    // 取得したイテレータ(target_nameのnameを持つ要素)を削除
    target_name = "Bertrand";
    it = _get_iterator(vec, target_name);
    vec.erase(it);

    for (auto& v : vec)
        std::cout << v;
}

void test_map() {
    std::map<std::string, int> phone_book = {
            {"David",    123456},
            {"Karl",     234567},
            {"Bertrand", 345678},
    };
}

// TestEntryに対しstd::sortを実行可能にするためのオーバーライド
bool operator<(const TestEntry& x, const TestEntry& y) {
    if (x.name == y.name)
        return x.number < y.number;
    return x.name < y.name;
}

// TestEntryに対しstd::unique_copyを実行可能にするためのオーバーライド
bool operator==(const TestEntry& x, const TestEntry& y) {
    if (x.name == y.name && x.number == y.number)
        return true;
    return false;
}

void test_vec_sort() {
    std::vector<TestEntry> vec = {
            {"AAA", 999999},
            {"ZZZ", 123456},
            {"AAA", 234567},
            {"OOO", 345678},
            {"AAA", 234567},
    };

    for (auto& v: vec) {
        std::cout << v;
    }

    std::sort(vec.begin(), vec.end());
    std::cout << "After std::sort executed" << std::endl;
    for (auto& v: vec) {
        std::cout << v;
    }

    // std::unique_copyの第3引数には出力先の先頭要素を指定する。
    // 先頭要素からイテレータを++しながら，要素を追加していく感じだと思う。
    // 出力したい要素分の領域を確保しておく必要がある。
//    std::vector<TestEntry> vec_unique(vec.size());
//    std::unique_copy(vec.begin(), vec.end(), vec_unique.begin());

    // std::back_inserterを使用することで，コンテナの領域を拡張しながら末尾に追加できる。
    // 右記ドキュメント内でも使われている https://cpprefjp.github.io/reference/algorithm/unique_copy.html
    std::vector<TestEntry> vec_unique;
    std::unique_copy(vec.begin(), vec.end(), vec_unique.begin());
    std::unique_copy(vec.begin(), vec.end(), std::back_inserter(vec_unique));
    std::cout << "Print vec_unique" << std::endl;
    for (auto& v: vec_unique) {
        std::cout << v;
    }
}

void test_find() {
    std::string str = "string aaa bbb ccc";
    auto p = std::find(str.begin(), str.end(), 'b');
    if (p != str.end())
        std::cout << "found char" << std::endl;
    else
        std::cout << "not found" << std::endl;

    std::vector<std::string::iterator> res;
    for (auto p = str.begin(); p != str.end(); p++)
        if (*p == 'b')
            // resに見つかったイテレータを追加する
            res.push_back(p);
    int i = 0;
    // 見つかったイテレータでループ
    for (auto p : res) {
        std::cout << "p = " << *p << ", i = " << i++ << std::endl;
        // 見つかったイテレータを書き換えれば，元の値が書き換えられる。
        *p = 'B';
    }
    std::cout << str << std::endl;
}

void test_ostream_iterator() {
    std::ostream_iterator<std::string> oo{std::cout};
    *oo = "Hello, ";
    oo++;
    *oo = "world!";

    std::string from, to;
    std::cout << "Please input the file path(from and to)" << std::endl;
    std::cin >> from >> to;

    std::ifstream is{from};
    std::ofstream os{to};

    std::set<std::string> b{std::istream_iterator<std::string>{is},
                            std::istream_iterator<std::string>{}};
    std::copy(b.begin(), b.end(), std::ostream_iterator<std::string>{os, "¥n"});

    std::cout << "eof or os = " << (!is.eof() || !os) << std::endl;
}

struct Greater_than {
    int val;

    Greater_than(int v) : val{v} {}

    bool operator()(const std::pair<std::string, int>& r) {
        return r.second > val;
    }
};

void print_greater_than() {
    std::map<std::string, int> m = {
            {std::string{"AAA"}, 999999},
            {std::string{"ZZZ"}, 123456},
    };
    // predicateを使う場合は以下
//    auto p = std::find_if(m.begin(), m.end(), Greater_than(1999999));
    // Lambda式を使う場合は以下
    auto p = std::find_if(m.begin(), m.end(),
            [](const std::pair<std::string, int>& r) { return r.second > 100; });
    if (p != m.end())
        std::cout << "Found" << std::endl;
    else
        std::cerr << "Not Found" << std::endl;
}


int main() {
    std::cout << "ch4main" << std::endl;

//    test_string();
//    test_iostream();
//    test_istream();
//    test_stream_operator();
//    print_phone_book();
//    test_str_vec();
//    test_vec_out_of_range();
//    test_list();
//    test_map();
//    test_vec_sort();
//    test_find();
//    test_ostream_iterator();
    print_greater_than();
}
