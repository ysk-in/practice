# Random Initialization
https://www.coursera.org/learn/machine-learning/lecture/ND5G5/random-initialization  
NeuralNetworkのInitialThetaについて扱う  

## NeuralNetworkのInitialTheta
GradientDescentやAdvancedOptimizationではInitialThetaを指定する必要がある  
例えばAdvancedOptimizationのfminuncは以下  
<img src="../../img/03_06_call_fminunc.png" >    
LinearRegressionやLogisticRegressionではこれを0初期化してきた  

NeuralNetworkで0初期化したInitialThetaを使用すると  
<img src="https://latex.codecogs.com/gif.latex?a^{(2)}" title="a^{(2)}" />以降のNodesが同値になり 適切にパラメタが求められない  
<img src="../../img/05_06_zero_initialization_in_neural_network.png" width=60% >    
これを回避するため NeuralNetworkのInitialThetaはランダム値を指定する  

# Random Initializationのやり方
[-ε, ε] (値域が-εからε)のランダム値を生成する方法として以下がある  
<img src="../../img/05_06_random_initialization.png" >
Theta1はランダム([-ε, ε])な10*11行列  

Octaveでは以下実装  
<img src="../../img/05_06_random_initialization_in_octave.png" >  
Octaveでrand関数は0から1の実数(0.31728とか)  
