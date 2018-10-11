# Backpropagation Algorithm
NeuralNetworkのCostFunctionを最小化する  
BackpropagationAlgorithmについて扱う  

## NeuralNetworkで最適なパラメタ(θ)を求めるには
最適なパラメタ(θ)を求めるためにはNeuralNetworkでも  
LinearRegressionやLogisticRegressionと同様 J(Θ)を最小化すれば良い  
<img src="../../img/05_02_gradient_computation_of_neural_network.png" width=50% >  
J(Θ)を最小化するためには LinearRegressionやLogisticRegression同様  
<img src="https://latex.codecogs.com/gif.latex?\frac{\partial}{\partial\Theta^{(l)}_{ij}}&space;J(\Theta)" title="\frac{\partial}{\partial\Theta^{(l)}_{ij}} J(\Theta)" />を求める必要がある  
これを求めるためにBackpropagationを用いる

## Backpropagationの考え方
Backpropagationの手順を把握するため  
簡単な例としてトレーニングセットが1件の場合で考える  

まずはForwardPropagationで 各レイヤのActivationNodesを求めて行き  
<img src="https://latex.codecogs.com/gif.latex?a^{L}" title="a^{L}" />(仮説関数)を求める(以下の例ではL=4のため a(4)を求める)  
<img src="../../img/05_02_forward_propagation.png" width=50% >  

次に 求めた<img src="https://latex.codecogs.com/gif.latex?a^{L}" title="a^{L}" />と y(トレーニングセットの実測値=答え) を用いて  
<img src="https://latex.codecogs.com/gif.latex?\delta^{(L)}_{j}" title="\delta^{(L)}_{j}" />つまりOutputLayerの予測値と実測値の差異を求める  
<img src="../../img/05_02_backpropagation_algorithm_simple.png" width=50% >  
同様に<img src="https://latex.codecogs.com/gif.latex?\delta^{(L-1)}_{j},&space;\delta^{(L-2)}_{j},&space;...,&space;\delta^{(2)}_{j}" title="\delta^{(L-1)}_{j}, \delta^{(L-2)}_{j}, ..., \delta^{(2)}_{j}" />と求める  
// <img src="https://latex.codecogs.com/gif.latex?\delta^{(1)}_{j}" title="\delta^{(1)}_{j}" />はInputLayerで予測値は無いため求めない  

δを求めるには以下の式を用いる(らしい よく分かってない)  
<img src="../../img/05_02_function_of_delta.png" >  

g(z)の微分は以下になる(らしい よく分かってない)  
<img src="../../img/05_02_gprime_derivative_terms.png" >  

## Backpropagationの式
m個のトレーニングセットについて考える場合は  
1番目のトレーニングセット, 2番目の, ...と各トレーニングセットについて考える  
<img src="../../img/05_02_backpropagation_algorithm.png" width=50% >  
この結果の<img src="https://latex.codecogs.com/gif.latex?D^{(l)}_{ij}" title="D^{(l)}_{ij}" />が<img src="https://latex.codecogs.com/gif.latex?\frac{\partial}{\partial\Theta^{(l)}_{ij}}&space;J(\Theta)" title="\frac{\partial}{\partial\Theta^{(l)}_{ij}} J(\Theta)" />  
(らしい よく分かってない...)  
