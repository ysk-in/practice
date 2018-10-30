# K-Means Algorithm
https://www.coursera.org/learn/machine-learning/lecture/93VPG/k-means-algorithm  
ClusteringアルゴリズムのK-Meansについて扱う  

## K-MeansのClusteringの考え方
K-Meansアルゴリズムは以下2つのステップでClusteringする  
1. Cluster assignment ステップ
1. Centroid(重心)を動かす ステップ

最初のステップとして まず 適当なクラスタCentroidを決め(以下 赤× と 青×)  
DataSet(緑点)がどちらのCentroidに近いか求める  
<img src="../../img/08_02_k-means_1.png" width=50% >  
近いものを同色で表すと以下になる  
<img src="../../img/08_02_k-means_2.png" width=50% >  

次のステップとして Centroidを動かす  
同色でグルーピングされたDataSetの平均点を求め Centroidをそこへ動かす  
<img src="../../img/08_02_k-means_3.png" width=50% >  

Centroidが動くと DataSetの近いもの(同色として扱うべきもの)が変わるので  
グルーピングし直し その後で再度Centroidを動かす これを繰り返す  
<img src="../../img/08_02_k-means_4.png" width=30% >
<img src="../../img/08_02_k-means_5.png" width=30% >
<img src="../../img/08_02_k-means_6.png" width=30% >  

繰り返していると やがて収束する  
<img src="../../img/08_02_k-means_7.png" width=50% >  
K-Meansでは このようにしてClusteringする  

## K-Meansの入力(パラメタ)
K-Meansは2つの入力を取る
* K: データの中から見つけだしたいClusterの数  
  この数をどのように決めたら良いかは 後ほど教えてくれるらしい  
* TrainingSet: 教師なし学習なので{<img src="https://latex.codecogs.com/gif.latex?x^{(1)},&space;x^{(2)},&space;...,&space;x^{(n)}" title="x^{(1)}, x^{(2)}, ..., x^{(n)}" />} yはなくxだけ  

## K-Meansのアルゴリズム
K-Meansのアルゴリズムは以下の通り  
<img src="../../img/08_02_k-means_algorithm.png" width=50% >  
1. K個のClusterCentroidsをランダム値で初期化(μとする)  
1. 以下を収束するまで繰り返す  
	1. 各TrainingSet(<img src="https://latex.codecogs.com/gif.latex?x^{(i)}" title="x^{(i)}" />)の最も近いClusterCentroid(<img src="https://latex.codecogs.com/gif.latex?\mu^{(i)}" title="\mu^{(i)}" />)を求め  
	<img src="https://latex.codecogs.com/gif.latex?c^{(i)}" title="c^{(i)}" />に<img src="https://latex.codecogs.com/gif.latex?\mu_{k}" title="\mu_{k}" />のIndex(k)を設定する    
	1. 各ClusterCentroidについて 同種としたTrainingSetの平均点を求め
	<img src="https://latex.codecogs.com/gif.latex?\mu_{k}" title="\mu_{k}" />に覚える  
	1. (μが変わっているため 収束するまで繰り返す)
