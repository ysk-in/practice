# Multivariate Gaussian Distribution
https://www.coursera.org/learn/machine-learning/lecture/Cf8DF/multivariate-gaussian-distribution  
MultivariateGaussianDistributionを用いたAnomalyDetection拡張について扱う  
MultivariateGaussianDistributionを用いることで Feature間の相関を考慮できる  

## MultivariateGaussianDistributionが必要になる理由
Datacenterのモニタリングで AnomalyDetectionを適用することを考える  
以下で 赤×のプロットがTrainingSet 緑×がTestSetを表している  
<img src="../../img/09_07_motivating_example.png" width=50% >  
Computerで作業が行われれば Cpu使用量が増えれば Memory使用量も増えるのがNormalなため  
青線が囲む範囲をNormalと分類し これから外れるものをAnomalyと扱いたい  
しかし AnomalyDetectionは 紫線で囲む範囲をNormalとして扱ってしまう  
// 内側ほど高い値を示す x1, x2それぞれが平均値(に近い値)を最もNormalとみなすため  

例えば左上にある緑×はCpuLoad(x1)が低いのにMemoryUsage(x2)が高いため  
Anomalyと分類することを期待するが AnomalyDetectionは上記の右側にある通り  
x1, x2 それぞれを参照し それ程TrainingSetのFeatureから離れていないためNormalと扱う  

Feature間(x1, x2)の相関を考慮し AnomalyDetectionしたい場合  
MultivariateGaussianDistributionを用いることで実現できる  

## MultivariateGaussianDistributionを用いた式
AnomalyDetectionにMultivariateGaussianDistributionを用いることで  
Feature各々からAnomaly判定するのでなく Feature間の相関関係を反映しAnomaly判定できる  

式は以下の通り ConvarianceMatrix(Sigma)を利用する この式も覚える必要は無いとのこと   
<img src="../../img/09_07_multivariate_gaussian_distribution.png" width=50% >  

## MultivariateGaussianのパラメタがどう影響するか
パラメタのConvarianceMatrix(Sigma)の対角成分を変えると以下のように作用する  
<img src="../../img/09_07_multivariate_gaussian_example.png" width=50% >  
対角成分は x1, x2, ... の分散(<img src="https://latex.codecogs.com/gif.latex?\sigma_{1}^{2},&space;\sigma_{2}^{2},&space;..." title="\sigma_{1}^{2}, \sigma_{2}^{2}, ..." />)を指す成分であるため  
小さくなると分布が集中(コブの幅が 狭くなり高くなる)し 大きくなると分散する  

x1, x2 それぞれの分散のみが変わると それぞれ以下のように作用する  
<img src="../../img/09_07_multivariate_gaussian_example_x1.png" width=40% >
<img src="../../img/09_07_multivariate_gaussian_example_x2.png" width=40% >  

非対角成分はそれぞれの共分散 変わると以下のように作用する  
<img src="../../img/09_07_multivariate_gaussian_correlation_positive.png" width=40% >
<img src="../../img/09_07_multivariate_gaussian_example_correlation_negative.png" width=40% >  
共分散: ちゃんと理解できていないけれど Feature間の関係のこと  
各成分で2つのFeature間の関係を示す 今回はx1, x2しかないので これらについてだけ    
つまり今回は右上と左下ともに<img src="https://latex.codecogs.com/gif.latex?\sigma_{x1x2},&space;\sigma_{x1x2}" title="\sigma_{x1x2}, \sigma_{x1x2}" />で同値(と思う...)  
1から-1の値をとる 0は相関関係なし 1/-1に近いほど相関関係が強い  
正の値なら正の相関関係(x1が増えるとき x2も増える)  
負の値なら負の相関関係(x1が増えるとき x2は減る)  

パラメタμを変えると 以下の通り ピーク・中心(分布全体の中心)がシフトできる  
<img src="../../img/09_07_multivariate_gaussian_example_mu.png" width=50% >  
