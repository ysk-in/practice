# Cost Function
ニューラルネットワークのパラメタをフィッティングするため  
まずはCostFunctionについて扱う  

## NeuralNetworkのCostFunction 用語
ニューラルネットワークのCostFunctionで使用する変数について定義する  
* L: ネットワークのレイヤ数  
* <img src="https://latex.codecogs.com/gif.latex?S_{l}" title="S_{l}" />: lレイヤのユニット数(バイアスユニットは含めない)  
* K: 出力 ユニット/クラス の数  

例えば 以下ニューラルネットワークにおいては各変数は以下の通り  
<img src="../../img/05_01_vaiables_for_neural_network.png" width=50% >  

## NeuralNetworkのCostFunction 式
LogisticRegressionにおいて 正規化したCostFunctionは以下であった  
<img src="../../img/03_11_regularized_cost_function_of_logistic_regression.png" >  

ニューラルネットワークにおいてはCostFunctionは以下の通り  
<img src="../../img/05_01_cost_function_for_neural_network.png" >  
SquareBrackets("[", "]"で囲まれた式)前の<img src="https://latex.codecogs.com/gif.latex?\sum_{k=1}^{K}" title="\sum_{k=1}^{K}" />は各OutputNodeの総和をとること  
正規化の項は 全Nodeのweight(OutputLayerにはweightは無い)の累乗和をとること(?)  
// 理解が正しいかあやしい 一旦すすめて後で見直す
