# Vectorization: Low Rank Matrix Factorization
https://www.coursera.org/learn/machine-learning/lecture/CEXN0/vectorization-low-rank-matrix-factorization  
CollaborativeFilterAlgorithmのベクトル化について扱う  
// LowRankMatrixFactorizationはCollaborativeFilterAlgorithmの別名らしい  

また ある映画・商品(など)と似た特徴を持つと予想されるものを見付ける方法についても扱う  

## CollaborativeFilterAlgorithmのベクトル化
5つのMovie 4人のUser が居るとき YはMatrixで以下の通り表現できる  
<img src="../../img/09_13_collaborative_filtering.png" width=50% >  
Ratedで無い箇所は Yには?を入れとく  
<img src="https://latex.codecogs.com/gif.latex?y^{(i,j)}" title="y^{(i,j)}" />Yの特定成分を指す変数  

Yの各成分はθとxから以下の通り求めることができる  
<img src="../../img/09_13_collaborative_filtering2.png" width=50% >  
そのため XとΘに上記の通りFeatureとParamterを持つことができていれば  
<img src="https://latex.codecogs.com/gif.latex?Y=X\Theta^{T}" title="Y=X\Theta^{T}" /> で求められる  
ちなみに マゼンタ グリーンで囲った箇所がそれぞれPredictedRatngとYで対応する  
// マゼンタの<img src="https://latex.codecogs.com/gif.latex?(\theta^{(1)})^{T}(x^{(1)})" title="(\theta^{(1)})^{T}(x^{(1)})" /> はユーザ1のMovie1のRateで5に対応  

## 似たFeatureを持つものを探す方法

<img src="../../img/09_13_finding_related_movies.png" width=100% >  
