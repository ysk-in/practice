# Deciding What to Do Next Revisited
仮説を改善するための方法についてまとめる  

## 仮説の改善方法 まとめ
HighVariance(OverFitting)のとき有効  
* 仮説のFeatureを減らす  
* TrainingSetの数を増やす(week6_05にある通り)  
* λを増加させる(パラメタのペナルティを強くしフィッティングを緩和)  

HighBias(UnderFitting)のとき有効  
* 仮説のFeatureを増やす  
* 仮説のPolynomialFeatureを増やす  
* λを減少させる(パラメタへのペナルティ効き過ぎを緩和)  

## 仮説の改善方法 まとめ NeruralNetworkの場合
NeuralNetworkでは以下の傾向がある  
* パラメタが少なかったり 小さなNeuralNetwork(レイヤ数やユニット数が少ない)は  
  UnderFittingしやすい また計算量は少なくなる
* パラメタが多かったり 大きなNeuralNetwork(レイヤ数やユニット数が多い)は  
  OverFittingしやすい また計算量は大きくなる  
  OverFittingには Regularization適用 や λを大きくすることで 改善が見込める  

1つのHiddenLayerから始めて CVを使いながらHiddenLayerを増やして行く方法が良い  

## 仮説の複雑さ(モデル)について まとめ
* シンプルなモデルは あまりFitできない
* 複雑なモデル(高次多項式)は TrainingDataにはFitしやすいが TestDataにはFitしづらい  
* 一般的なデータ(TrainingData以外)にも適度にFitできるモデルを選ぶのが望ましいが  
  過度にFitするモデルを選択することもできる  
