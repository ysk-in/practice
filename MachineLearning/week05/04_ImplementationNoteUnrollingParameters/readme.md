# Implementation Note: Unrolling Parameters
https://www.coursera.org/learn/machine-learning/lecture/60Uxp/implementation-note-unrolling-parameters  
NeuralNetworkでAdvancedOptimizationを使用する場合の  
Octave実装について unrollとresphare を扱う  

## Octaveのunrollとresphare
fminunc関数などのAdnvancedOptimizationでは  
引数や戻り値がベクトル(≠行列)形式の必要がある  
<img src="../../img/05_04_advanced_optimization_in_neural_network.png" width=50% >  
NeuralNetworkでは thetaやgradientが上記のような行列形式である  

そのため thetaやgradientはunroll(展開?)し ベクトルにする必要がある  
Octaveでは以下で 行列 -> ベクトル の変換ができる  
<img src="../../img/05_04_matrix_to_vector.png" >  

また 以下で ベクトル -> 行列 の変換ができる  
<img src="../../img/05_04_vector_to_matrix.png" >  

この変換を用いることで NeuralNetworkでAdnvancedOptimizationが使用可能  
<img src="../../img/05_04_learning_algorithm.png" >  
1. fminuncの引数initialThetaに指定する値をunroll(行列->ベクトル)  
1. costFunctionに指定される引数thetaはベクトル化されているため  
  reshape(ベクトル->行列) この行列を用いてgradient(D)を求める  
1. costFunctionの戻り値gradientはベクトルの必要があるためDをunroll  
