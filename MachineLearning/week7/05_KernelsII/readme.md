# Kernels II
続けてKernelsについて扱う  
今回は特に実践でどのように使用するかと Bias-VarianceのTradeOffについて扱う  
// 日本語字幕がないため理解があやしい...  

## Landmarkの決め方
Landmarkはトレーニングセットのxをそのまま使用すれば良い  
上記の左下グラフの通りDataSetがあるときは 右のようにLandmarkを設定すれば良い  
<img src="../../img/07_05_choosing_the_landmark.png" >  

例えば <img src="https://latex.codecogs.com/gif.latex?l^{(1)}&space;=&space;x&space;^{(1)}&space;=&space;[x^{(1)}_{1};&space;...;&space;x^{(1)}_{n}]" title="l^{(1)} = x ^{(1)} = [x^{(1)}_{1}; ...; x^{(1)}_{n}]" /> のように設定するということ  
<img src="../../img/07_05_svm_with_kernels.png" >  
i番目のDataSet(<img src="https://latex.codecogs.com/gif.latex?x^{(i)}" title="x^{(i)}" />)から<img src="https://latex.codecogs.com/gif.latex?f^{(i)}" title="f^{(i)}" />ベクトルのFeatureが求められる  
ちなみに このFeatureは<img src="https://latex.codecogs.com/gif.latex?f^{(i)}_{i}" title="f^{(i)}_{i}" />が1となる(<img src="https://latex.codecogs.com/gif.latex?l^{(i)}&space;=&space;x^{(i)}" title="l^{(i)} = x^{(i)}" />のため)

## チューニングパラメタ Cとσ について
前出の通りSVMのCostFunctionは以下  
<img src="../../img/07_01_cost_function_of_svm.png" >  
SVMでもパラメタを調節することで  
OverFitting(HighVariance)とUnderFitting(HighBias)のTradeOffが実現可能  
<img src="../../img/07_05_svm_parameters.png" >  

係数Cは1/λのようなもので  
* Cを大きくすると LowerBias, HigherVariance になる  
  // まだちゃんとイメージ掴めていないけど  
  // Regularization項の影響が Cost和の項より小さくなるから そんな気はする  
  // Regularization項=Featureの総和 を最小化しようとする影響が小さくなるから  
* Cを小さくすると HigherBias, LowerVariance になる

σ^2については
* σ^2を大きくすると HigherBias, LowerVariance になる  
  // こっちもまだイメージ掴めていないけれど  
  // それぞれのFeatureが緩やかに影響を与えあいそう(各f_i間の差が急激でないため)  
  // 各パラメタに急激に引っ張られた変化はしなそうでOverFittingしづらいイメージ  
* σ^2を小さくすると LowerBias, HigherVariance になる  
