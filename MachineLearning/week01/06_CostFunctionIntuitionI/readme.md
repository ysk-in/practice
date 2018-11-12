# Cost Function Ⅰ
https://www.coursera.org/learn/machine-learning/lecture/N09c6/cost-function-intuition-i  
線形回帰の目的関数の詳細説明1(単純な仮説関数について考える)

## 線形回帰の考え方
最適な線形回帰の仮説関数を求めるためには以下の通りパラメタを求める必要がある  
<img src="../../img/01_06_regression_goal.png" width=25%>  

理解し易くするためここでは線形回帰の単純なケース(Θ0⁼0の場合)で具体的に考える  
<img src="../../img/01_06_regression_simplified.png" width=25%>  

## 目的関数の考え方(単純な仮説関数を用いて)
線形回帰の単純なケース(Θ0⁼0の場合)で具体的に考えていく  
TrainingSetとして(1, 1), (2, 2), (3, 3)が与えられた場合を考える  
<img src="../../img/01_06_regression_dataset.png" width=25%>  

Θ1=1を考えるとき 以下の通り考えることができる  
<img src="../../img/01_06_regression_theta1_1.png" width=50%>  
仮説関数にΘ1=1与えたときの直線は 左グラフの通りの線となる  
また このときのJ(Θ1)を 目的関数を利用し求めると(左グラフの下の式)0であることが分かる  
これをプロットすると右グラフの通りとなる

つまり Jが0のとき(Jが0に最も近いとき)に最適なパラメタ(Θ1)となることが分かる  
(最適なパラメタ = TrainingSetのプロット との距離が最短な 仮説関数hΘ(x)のΘ)

同様にΘ1=0.5のとき Θ1=0のときについて考えると 以下の通りとなる  
<img src="../../img/01_06_regression_theta1_05.png" width=40%>　　
<img src="../../img/01_06_regression_theta1_0.png" width=40%>  
Jが0より離れるほど 仮説関数の直線 と TrainingSetのプロット との距離が離れることが分かる  
つまり Jが0より離れるほど パラメタ(Θ1)が最適でなくなることが分かる  
