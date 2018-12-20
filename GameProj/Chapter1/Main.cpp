#include "DxLib.h"
#include <string>
#include <iostream>
#include <vector>

constexpr int FUNC_SUCCESS = 0;
constexpr int FUNC_ERROR = -1;

//class Character {
//private:
//	bool is_right_slide = true;
//	std::string name{};
//	int slide_speed = 0;
//public:
//	int x = 0;
//	int y = 0;
//
//	Character(bool b, int xx, int yy, int s, std::string n) :
//		is_right_slide{ b }, x{ xx }, y{ yy }, slide_speed{ s }, name{ n } {}
//	~Character() {}
//
//	void slide() {
//		x += slide_speed;
//	}
//};
//
//std::vector<Character> characters{};

int draw_image(int x, int y, std::string& image_path) {
	// ファイルパスを指定し，ディスク上のファイルを表示する。
	// ディスクからreadして表示するため低速，テストのみで使う関数とのこと。
	//LoadGraphScreen(50, 100, img_path.c_str(), TRUE);

	// 一般的に使われる画像表示手法。まず画像をメモリに載せ，ハンドラを取得。
	// ゲーム中のいわゆるNowLoading...のときとかにやってるとのこと。
	int img_handler = LoadGraph(image_path.c_str());
	if (img_handler == -1) {
		std::cerr << "LoadGraph error. image_path = " << image_path << std::endl;
		return FUNC_ERROR;
	}

	//for (auto& c : characters) {
	//	if (DrawGraph(c.x, c.y, img_handler, TRUE)) {
	//		std::cerr << "DrawGraph error" << std::endl;
	//		return FUNC_ERROR;
	//	}
	//	c.slide();
	//}

	// 取得したハンドラを指定し描画。
	if (DrawGraph(x, y, img_handler, TRUE)) {
		std::cerr << "DrawGraph error" << std::endl;
		return FUNC_ERROR;
	}

	if (DrawGraph(x / 2, y + 100, img_handler, TRUE)) {
		std::cerr << "DrawGraph error" << std::endl;
		return FUNC_ERROR;
	}

	if (DrawGraph(x / 4, y + 200, img_handler, TRUE)) {
		std::cerr << "DrawGraph error" << std::endl;
		return FUNC_ERROR;
	}

	// 裏画面に描画した画像を表画面に反映。
	if (ScreenFlip()) {
		std::cerr << "ScreenFlip error" << std::endl;
		return FUNC_ERROR;
	}
	// 画面をクリアする。ScreenFlip仕様書に，実行後Clearしろとあるので，ここで実行。
	if (ClearDrawScreen()) {
		std::cerr << "ClearDrawScreen error" << std::endl;
		return FUNC_ERROR;
	}
	return FUNC_SUCCESS;
}

bool is_exit_requested() {
	// ESCキーが入力されたら終了
	if (CheckHitKey(KEY_INPUT_ESCAPE)) {
		return TRUE;
	}
	// ProcessMessageはちゃんと理解できていない。
	// ウィンドウの×が押されたら終了させたい，ための処理。
	// 詳細は次を参照 http://dxlib.o.oo7.jp/dxfunc.html#R1N3
	if (ProcessMessage()) {
		return TRUE;
	}
	return FALSE;
}

//void init_characters() {
//	characters.push_back(Character{ true, 0, 0, 2, std::string{"character1"} });
//	characters.push_back(Character{ true, 0, 100, 4, std::string{"character2"} });
//	characters.push_back(Character{ true, 0, 200, 8, std::string{"character3"} });
//}

int exec_main() {
	std::string img_path = "../画像/キャラクタ01.png";
	//draw_image(50, 100, img_path);

	//init_characters();s

	int x = 100;
	constexpr int sleep_msec = 7;
	while (!is_exit_requested()) {
		if (draw_image(x, 100, img_path))
			break;
		x += 2;
	}
	return FUNC_SUCCESS;
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
	// ウィンドウモードに設定
	ChangeWindowMode(TRUE);

	// DXライブラリの初期化
	if (DxLib_Init() == -1) {
		return -1;
	}

	// 描画先を裏画面に設定する(描画途中の画像が表示されてしまうことなどを防止するため)
	// 詳細は次を参照 http://dxlib.o.oo7.jp/function/dxfunc_graph3.html#R4N6
	SetDrawScreen(DX_SCREEN_BACK);

	// 点を打つ
	//DrawPixel(320, 240, GetColor(255, 255, 255));

	exec_main();

	// キー入力待ち
	//WaitKey();

	// DXライブラリ使用の終了
	DxLib_End();

	return 0;
}
