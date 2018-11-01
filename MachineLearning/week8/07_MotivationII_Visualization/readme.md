# Motivation II: Visualization
https://www.coursera.org/learn/machine-learning/lecture/t6pYD/motivation-ii-visualization  
DimensionalityReductionの利用目的として DataのVisualizationについて扱う  

## Visualizationの方法
Features数が50など多い場合  
グラフで表現できるのは2D/3Dのため Dataの可視化(グラフにプロット)が出来ない  
<img src="../../img/08_07_many_features.png" width=50% >  

DimensionalityReductionを用いてFeatures数を 2 or 3 に削減することで  
Visualization(グラフへのプロット)が可能になる 今回は以下の通り2次元(z1, z2)にする  
<img src="../../img/08_07_dimensionality_reduction.png" width=50% >  

2次元Data(z1, z2)のため 以下の通り 2次元グラフへDataをプロットできる  
<img src="../../img/08_07_data_visualization.png" width=50% >  
z1, z2が持つ情報は上記の通りのため  
右上のDataは GDP および 1人あたりのGDPが高い国であることが 視覚的に分かる  
