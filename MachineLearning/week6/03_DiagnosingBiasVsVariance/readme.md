# Diagnosing Bias vs. Variance
仮説が良い予測をできないとき Under/Over Fitting が発生していると考えられる  
Costを使い どちらか判別する方法について扱う  

## UnderFitting, OverFittingの見分け方
x軸を仮説の次数 y軸をCostとする2次元グラフに 以下をプロット  
* <img src="https://latex.codecogs.com/gif.latex?J_{training}(\Theta)" title="J_{training}(\Theta)" /> : TrainingSetのCost  
* <img src="https://latex.codecogs.com/gif.latex?J_{cross-validation}(\Theta)" title="J_{cross-validation}(\Theta)" /> : CrossValidationのCost  

<img src="../../img/06_03_diagnosing_bias_vs_variance.png" >  
このグラフから以下の通り判別できる  

* TrainingSetのCostが高く CrossValidationのCostも高い場合 UnderFitting  
  予測値と実測値の差異が大きいので フィットできていない  
* TrainingSetのCostが低く CrossValidationのCostが高い場合 OverFitting  
  学習データに対しての予測は ほぼ誤差がないのに  
  未知データに対しての予測は 大きな誤差がある これはOverFitting  
