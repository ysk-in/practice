# Error Metrics for Skewed Classes
https://www.coursera.org/learn/machine-learning/lecture/tKMWX/error-metrics-for-skewed-classes  
前出の通り FeatureやアルゴリズムなどMachineLearningの精度を上げるためには
エラー分析やエラーメトリクス(どれだけ正確に予測できているかの実数値の評価指標)が重要  
ここではエラーメトリクスについて扱う  

## エラーメトリクス
TestSetに対する誤差のみで予測の精度を計ると 精度を上手く計れないことがある  
例えば以下のケース  
<img src="../../img/06_09_canncer_classification_example.png" width=50%>  
つまり Cancer(1と分類すべきSet)が0.5%しか存在しない場合  
仮説が常に0を予測(例えばfeatureを無視し常に0)しても99.5%で予測は正解となってしまう  
この仮説は Cancerであることを全く正しく予測できないが 高いAccuracyとなってしまう  

このようにDataSetのyが0または1の片方に凄く偏っているものをSkewedClassesと呼ぶ  

SkewedClassesのエラーメトリクスは 以下が有効  
<img src="../../img/06_09_precision_recall.png" width=50%>  
RareClassをy=1と置き この方法で計ることで  
常に0を返してしまうような仮説は低い精度として扱える(分子が0となるため)  

Precision, Recall どちらも高い(1.0に近い)方が望ましい  
* Precision: 1として分類(予測)したものが 実際に1だった割合  
  下記表だと 80 / (80 + 20) = 0.8  
  100個を1と予測したけどうち20個は外れてた
* Recall: 1として分類(予測)したものが 実際の1全体をどれだけ捕捉できたかの割合  
  下記表だと 80 / (80 + 80) = 0.5  
  160個の1と分類すべきものがあり 予測はうち80個だけ捉えた  

/|001|000|  
1|080|020|  
0|080|820|  
