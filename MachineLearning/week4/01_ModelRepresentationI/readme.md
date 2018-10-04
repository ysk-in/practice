# Model Representation I
ニューラルネットワークについて扱う  
ここではニューラルネットワークの表現について扱う  

## ニューラルネットワークの用語
ニューロンにおいて Input=dendrites Output=axons

ニューラルネットワークにおいてdendrites, axonsは以下に対応  
* dendrites: <img src="https://latex.codecogs.com/gif.latex?x_{1},&space;x_{1},&space;...,&space;x_{n}" title="x_{1}, x_{1}, ..., x_{n}" />などのInputFeatures  
  特に<img src="https://latex.codecogs.com/gif.latex?x_{0}" title="x_{0}" />はBiasUnitと呼ばれ 常に1  
* axons: 結果の仮説関数  

ニューラルネットワークにおいてもClassification(<img src="https://latex.codecogs.com/gif.latex?\frac{1}{1&plus;e^{-\theta^{T}x}}" title="\frac{1}{1+e^{-\theta^{T}x}}" />)を使用  
Sigmoid(Logistic) ActivationFunctionとも呼ぶ  
パラメータθは weights とも呼ぶ  

InputNodesのLayer1はInputLayerとも呼ばれ 別のNode(Layer2)へ入力される  
最終的なOutputは仮説関数でOutputLayerとも呼ばれる  
<img src="../../img/04_01_neural_networks.png" width=50%>  
// <img src="https://latex.codecogs.com/gif.latex?x_{0},&space;a_{0}^{(2)}" title="x_{0}, a_{0}^{(2)}" />は常に1のため書いたり書かなかったりする  
InputLayerとOutputLayerの間にLayers(IntermediateLayers)を持つことができ  
これはHiddenLayersと呼ぶ  
この層のノードは
<img src="https://latex.codecogs.com/gif.latex?a_{0}^{2},&space;a_{1}^{2},&space;...,&space;a_{n}^{2}" title="a_{0}^{2}, a_{1}^{2}, ..., a_{n}^{2}" />とラベリングされActivationUnitsと呼ばれる  
<img src="../../img/04_01_label_of_neural_networks.png" >  

## ニューラルネットワークの表現・関数
例えば1つのHiddenLayerを持つNeuralNetworkは以下で表現できる  
<img src="../../img/04_01_neural_network_with_one_hidden_layer.png" >  
各ActivationNodeの値は以下で求められる  
<img src="../../img/04_01_value_of_activation_nodes.png" >  
また この例では ActivationNodeのパラメタ(Θ)は3*4の行列  
// Rows=3は<img src="https://latex.codecogs.com/gif.latex?\Theta_{10}^{(1)},&space;\Theta_{20}^{(1)},&space;\Theta_{30}^{(1)}" title="\Theta_{10}^{(1)},&space;\Theta_{20}^{(1)},&space;\Theta_{30}^{(1)}" />の各行  
// Columns=4は<img src="https://latex.codecogs.com/gif.latex?\Theta_{10}^{(1)},&space;\Theta_{11}^{(1)},&space;\Theta_{12}^{(1)},&space;\Theta_{13}^{(1)}" title="\Theta_{10}^{(1)},&space;\Theta_{11}^{(1)},&space;\Theta_{12}^{(1)},&space;\Theta_{13}^{(1)}" />の各列  

これを一般化すると jレイヤに<img src="https://latex.codecogs.com/gif.latex?s_{j}" title="s_{j}" />ユニットがあり j+1レイヤに<img src="https://latex.codecogs.com/gif.latex?s_{j+1}" title="s_{j+1}" />ユニットがあるとき  
<img src="https://latex.codecogs.com/gif.latex?\Theta^{j}" title="\Theta^{j}" />の行列は <img src="https://latex.codecogs.com/gif.latex?s_{j+1}" title="s_{j+1}" /> * (<img src="https://latex.codecogs.com/gif.latex?s_{j}" title="s_{j}" />+1) となる ということ  
