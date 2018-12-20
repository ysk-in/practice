#include <DxLib.h>

inline bool ProcessMessageAndFlipScreen() {
	if (ProcessMessage() == 0 && ScreenFlip() == 0 && ClearDrawScreen() == 0)
		return TRUE;
	return FALSE;
}

void TestDrawString() {
	int x = 0, y = 0;
	int color_green = GetColor(0, 255, 0);
	while (ProcessMessageAndFlipScreen()) {
		DrawFormatString(x, y, color_green, "座標[%d, %d]", x, y);
		x += 2;
		y += 1;
	}
}

void TestSound() {
	int handle = LoadSoundMem("サウンド/1up.wav");
	int count = 0;
	while (ProcessMessageAndFlipScreen()) {
		if (count % 120 == 0) {
			PlaySoundMem(handle, DX_PLAYTYPE_BACK);
		}
		count++;
	}
}

void TestLoadDivGraph() {
	int color_white = GetColor(255, 255, 255);
	constexpr int graphic_num = 16;
	int graphic_handles[graphic_num];
	int handle = LoadDivGraph("../画像/キャラクタ10.png", 16, 4, 4, 32, 32, graphic_handles);
	constexpr DWORD sleep_ms = 1000;
	int i = 0;
	while (ProcessMessageAndFlipScreen()) {
		if (i >= graphic_num) {
			i = 0;
		}
		DrawGraph(0, 0, graphic_handles[i], TRUE);
		DrawFormatString(0, 33, color_white, "i = %d", i);
		Sleep(sleep_ms);
		i++;
	}
}

void TestCheckHitKey() {
	int x = 0;
	while (ProcessMessageAndFlipScreen()) {
		DrawFormatString(x, 0, GetColor(255, 255, 255), "!?");

		if (CheckHitKey(KEY_INPUT_RIGHT) != 0) {
			x += 50;
		}
	}
}

constexpr int KEY_NUM = 256;
int HITTED_KEY_COUNT[KEY_NUM];

//bool UpadteHitKeyCountState() {
//	char tmpKey[KEY_NUM];
//	GetHitKeyStateAll(tmpKey);
//	for (int i = 0; i < KEY_NUM; i++) {
//		if (tmpKey[i])
//			HITTED_KEY[i]++;
//		else
//			HITTED_KEY[i] = 0;
//	}
//	return TRUE;
//}

char HITTED_KEY[KEY_NUM];

bool UpadteHitKeyState() {
	GetHitKeyStateAll(HITTED_KEY);
	return TRUE;
}

void TestGetHitKeyStateAll() {
	int x = 0, y = 0;
	while (ProcessMessageAndFlipScreen() && UpadteHitKeyState()) {
		int slide_size = 2;
		if (HITTED_KEY[KEY_INPUT_LSHIFT] || HITTED_KEY[KEY_INPUT_RSHIFT])
			slide_size *= 2;
		if (HITTED_KEY[KEY_INPUT_LCONTROL] || HITTED_KEY[KEY_INPUT_RCONTROL])
			slide_size /= 2;
		if (HITTED_KEY[KEY_INPUT_RIGHT])
			x += slide_size;
		if (HITTED_KEY[KEY_INPUT_LEFT])
			x -= slide_size;
		if (HITTED_KEY[KEY_INPUT_UP])
			y -= slide_size;
		if (HITTED_KEY[KEY_INPUT_DOWN]) {
			y += slide_size;
		}
		DrawFormatString(x, y, GetColor(255, 255, 255), "*");
	}
}

int WINAPI WinMain(HINSTANCE, HINSTANCE, LPSTR, int) {
	ChangeWindowMode(TRUE), DxLib_Init(), SetDrawScreen(DX_SCREEN_BACK);

	//TestDrawString();
	//TestSound();
	//TestLoadDivGraph();
	//TestCheckHitKey();
	TestGetHitKeyStateAll();

	DxLib_End();
	return 0;
}
