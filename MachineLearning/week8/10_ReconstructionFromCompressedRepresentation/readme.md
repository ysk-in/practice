# Reconstruction from Compressed Representation
https://www.coursera.org/learn/machine-learning/lecture/X8JoQ/reconstruction-from-compressed-representation  
DimensionalityReductionしたzから元のxを復元する方法について扱う  

## 次元を復元する方法
<img src="https://latex.codecogs.com/gif.latex?z^{(i)}&space;=&space;U_{reduce}^{T}&space;\times&space;x^{(i)}" title="z^{(i)} = U_{reduce}^{T} \times x^{(i)}" /> は  
`k*1行列`にするため`k*n行列 * n*1行列`により 次元削減するのだった  
なので 次元を復元したいのであれば  
`n*1行列`にするため`n*k行列 * k*1行列`により次元を復元すれば良い つまり  
<img src="https://latex.codecogs.com/gif.latex?x_{approx}^{(i)}&space;=&space;U_{reduce}&space;\times&space;z^{(i)}" title="x_{approx}^{(i)} = U_{reduce} \times z^{(i)}" />すれば良い  
<img src="../../img/08_10_reconstruction_from_compressed_representation.png" width=50% >  
