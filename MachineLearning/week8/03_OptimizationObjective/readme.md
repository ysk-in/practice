# Optimization Objective
https://www.coursera.org/learn/machine-learning/lecture/G6QWt/optimization-objective  
K-Meansの OptimizationObjective(=CostFunction?)について扱う  

OptimizationObjectiveを知ることで以下に役立つ
## K-MeansのOptimizationObjectiveの考え方
* デバッグ  
* なぜ局所的最小値が回避できるのか理解する(こっちが大事 詳しくは後ほど教えてくれる?)  

OptimizationObjectiveで利用する変数は以下  
* <img src="https://latex.codecogs.com/gif.latex?c^{(i)}" title="c^{(i)}" /> : <img src="https://latex.codecogs.com/gif.latex?x^{(i)}" title="x^{(i)}" />がどのクラスタに割り当たっているかトラックするための変数(μのindex)  
* <img src="https://latex.codecogs.com/gif.latex?\mu_{k}" title="\mu_{k}" /> : index=kのClusterCentroidの場所  
* <img src="https://latex.codecogs.com/gif.latex?\mu_{c^{(i)}}" title="\mu_{c^{(i)}}" /> : <img src="https://latex.codecogs.com/gif.latex?x^{(i)}" title="x^{(i)}" />に割り当たっているクラスタの場所  
  <img src="https://latex.codecogs.com/gif.latex?c^{(i)}" title="c^{(i)}" /><img src="https://latex.codecogs.com/gif.latex?x^{(i)}" title="x^{(i)}" />は割り当たっているクラスタμのindexのため  

OptimizationObjectiveは以下  
<img src="../../img/08_03_kmeans_optimization_objective.png" >  
<img src="https://latex.codecogs.com/gif.latex?x^{(i)}" title="x^{(i)}" />と<img src="https://latex.codecogs.com/gif.latex?\mu_{c^{(i)}}" title="\mu_{c^{(i)}}" />間の距離を最小化することが目的  
DistortionFunctionとも呼ぶ  

## K-MeansのOptimizationObjectiveのAlgorithm
Alogirthmは以下  
<img src="../../img/08_03_kmeans_algorithm.png" >  
1. K個のClusterCentroidをランダム初期化する  
1. (収束するまで?)以下を繰り返す  
	1. <img src="https://latex.codecogs.com/gif.latex?\mu_{k}" title="\mu_{k}" />は固定したまま Costを最小化する<img src="https://latex.codecogs.com/gif.latex?c^{(1)}" title="c^{(1)}" />, <img src="https://latex.codecogs.com/gif.latex?c^{(2)}" title="c^{(2)}" />, ..., <img src="https://latex.codecogs.com/gif.latex?c^{(m)}" title="c^{(m)}" />を求める  
	つまり index=iのDataに最も近い ClusterCentroidのindexを<img src="https://latex.codecogs.com/gif.latex?c^{(i)}" title="c^{(i)}" />に設定  
	これを全Dataについて求める  
	1. 全ClusterCentroid(μ)について 当該Clusterに割り当たっているDataの平均を設定する  
	// ClusterCentroid(<img src="https://latex.codecogs.com/gif.latex?\mu_{k}" title="\mu_{k}" />)を移動する  
