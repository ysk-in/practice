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
すべての商品や映画について Feature=xをLearnすることができたなら  
商品や映画iに似た性質を持つjを探すためには 以下の通り考えれば良い
<img src="../../img/09_13_finding_related_movies.png" width=50% >  
つまり <img src="https://latex.codecogs.com/gif.latex?x^{(i)}" title="x^{(i)}" /> と似た成分を持つ(距離の近い) <img src="https://latex.codecogs.com/gif.latex?x^{(j)}" title="x^{(j)}" />を採れば良い  

ちなみに CollaborativeFilterでFittingするFeature x を求めることができ
このxは対象の重要なFeatureを補足する傾向はあるのだが  
このxが何を意味する(何のFeatureを捉えたもの)か を 人間が可視化するのは難しい  
