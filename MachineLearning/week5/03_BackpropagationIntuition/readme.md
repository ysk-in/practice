# Backpropagation Intuition
前出の 難しいBackpropagationの理解を進めるための より簡単な説明  
Backpropagationを詳細に理解することは難しいという認識で問題はないっぽい  

## Backpropagationが何をしているか
前出の通りNeuralNetworkのCostFunctionは以下  
<img src="../../img/05_03_cost_function_for_neural_network.png" >  

Backpropagationを考え易くするため CostFunctionを以下シンプルなケースで考える  
　出力ユニット数が1(K=1) かつ Regularization(正規化)を無視  
このとき t番目のトレーニングセットについて考える場合 CostFunctionは以下
<img src="../../img/05_03_simplified_cost_function_for_neural_network.png" >  
このCostFunctionは以下の式(誤差の2乗)と似たような役割    
<img src="https://latex.codecogs.com/gif.latex?cost(t)&space;\approx&space;(h_{\Theta}(x^{(t)})&space;-&space;y^{(t)})^{2}" title="cost(t) \approx (h_{\Theta}(x^{(t)}) - y^{(t)})^{2}" />

前出の通りBackpropagationは以下の図の右から左に流れるように計算する  
<img src="../../img/05_03_backpropagation_intuition.png" width=60% >  
Backpropagationの計算イメージは  
<img src="https://latex.codecogs.com/gif.latex?\delta^{(4)}_{1}" title="\delta^{(4)}_{1}" />は上記の通り<img src="https://latex.codecogs.com/gif.latex?cost(t)&space;\approx&space;(h_{\Theta}(x^{(t)})&space;-&space;y^{(t)})^{2}" title="cost(t) \approx (h_{\Theta}(x^{(t)}) - y^{(t)})^{2}" />みたいなもの  
<img src="https://latex.codecogs.com/gif.latex?\delta^{(3)}_{2}&space;=&space;\Theta^{(3)}_{12}&space;\times&space;\delta^{(4)}_{1}" title="\delta^{(3)}_{2} = \Theta^{(3)}_{12} \times \delta^{(4)}_{1}" />のようなもので  
続けて求めていくと <img src="https://latex.codecogs.com/gif.latex?\delta^{(2)}_{2}&space;=&space;\Theta^{(2)}_{12}&space;*&space;\delta^{(3)}_{1}&space;&plus;&space;\Theta^{(2)}_{22}&space;*&space;\delta^{(3)}_{2}" title="\delta^{(2)}_{2} = \Theta^{(2)}_{12} * \delta^{(3)}_{1} + \Theta^{(2)}_{22} * \delta^{(3)}_{2}" />と求められる のようなイメージ  

δを求める本来の式は以下(らしいけど なんでこうなるかは未だに理解できていない)  
<img src="../../img/05_03_calculate_delta_formally.png" >  
けどまあ 正確に理解できてなくても問題はないらしい  
