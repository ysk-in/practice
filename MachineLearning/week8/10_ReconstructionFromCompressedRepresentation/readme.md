# Reconstruction from Compressed Representation
https://www.coursera.org/learn/machine-learning/lecture/X8JoQ/reconstruction-from-compressed-representation  
DimensionalityReductionしたzから元のxを復元する方法について扱う  

## 次元を復元する方法
<img src="https://latex.codecogs.com/gif.latex?z^{(i)}&space;=&space;U_{reduce}^{T}&space;\times&space;x^{(i)}" title="z^{(i)} = U_{reduce}^{T} \times x^{(i)}" /> は  
`k*n行列 * n*1行列` により `k*1行列`を求めることで次元削減するのだった  
なので 次元を復元したいのであれば  
`n*k行列 * k*1行列` により `n*1行列`を求めることで元の次元を復元できる つまり  
<img src="https://latex.codecogs.com/gif.latex?x_{approx}^{(i)}&space;=&space;U_{reduce}&space;\times&space;z^{(i)}" title="x_{approx}^{(i)} = U_{reduce} \times z^{(i)}" />で求められる
<img src="../../img/08_10_reconstruction_from_compressed_representation.png" width=50% >  
