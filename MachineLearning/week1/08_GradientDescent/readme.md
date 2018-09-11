# Gradient Descent(最急降下法)
目的関数を最小化するためのアルゴリズム Gradient Descent(最急降下法)について学ぶ  

## Gradient Descentの特徴
Gradient Descentは以下の特徴がある
* 線形回帰以外にも適用可能な より汎用的な関数
* Θ0, Θ1だけでなく任意(Θn)のパラメタを求めるのに適用可能

## Gradient Descentの考え方
Gradient Descentの考え方は以下の通り  
以降 考えやすいようにΘ0, Θ1についてのみ考える
1. まず任意のΘ0, Θ1を決める
1. J(Θ0, Θ1)を減少させられるΘ0, Θ1を求める  
   これをJが最小値になるまで続ける  

## Gradient Descentの考え方 図で考える
これは図にしてみると以下のような考え方  
<img src="../../img/01_08_gradient_descent_graph.png" width=50%>  
まず任意のΘ0, Θ1を決めると 赤丸で囲まれた×(ここでは2つある右側の×で考える)が決まる  
Jが最も減少する(つまり 高さを最も減らせる)方向に移動する  
これを繰り返して Jが最小になる場所まで移動を続ける のような考え方  

## Gradient Descentの考え方 関数で考える
Gradient Descentの考え方を関数で表現すると以下  
<img src="../../img/01_08_gradient_descent_algorithm.png" width=50%>  
* := は代入を示す
* α は学習率 どれだけ大きな降下ステップを採るか制御  
  大きければ急降下し 小さければ小刻みに降下
* αにかけている項(導関数項) ここでは理解できなくてOK 後で説明

この関数は "Θj := xxx (for j=0 and j1)" とある通りΘ0, Θ1を更新していく  
Gradient DescentではΘ0とΘ1を同時に更新する必要がある  
<img src="../../img/01_08_gradient_descent_algorithm_simultaneous.png" width=50%>  
左の順序でΘjを求める必要があり 右の順序では駄目だよ ということ
