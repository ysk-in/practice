# Large Margin Intuition
https://www.coursera.org/learn/machine-learning/lecture/wrjaS/large-margin-intuition  
ClassifierのMarginについて扱う  

## Marginとはなにか
前回の通りSVMのCostは以下の通り扱う  
<img src="../../img/07_02_svm_margin.png" width=50% >  
上記にある通り `z>=0` や `z<0` を満たす時点で`Cost=0`にするのでなく  
`z>=1` や `z<=-1` を満たす時点で`Cost=0`として扱う  

これは仮説のパラメタにMargin(余裕)を持たせるために有効  

パラメタにMarginを持たせると言うのは以下を指す  
<img src="../../img/07_02_large_margin_classifier.png" width=50% >  
つまり DicisionBoundryの線が いかに余裕(データと距離)を持てているか  
上記のどの線も現状のデータに対しては妥当なDicisionBoundry  
しかし 緑線はMarginが少なく 既存データと少し傾向が異なるだけで分類を誤る  
対して 黒線はMarginが大きく取れており より妥当な分類が可能  

パラメタCは以下のように作用する  
<img src="../../img/07_02_comparison_c_value.png" width=50% >  
Cにとても大きな値を与えると 左下にある赤×のような無視すべきか悩ましいデータについても  
実測値通り分類しようとする つまり OverFitting傾向になる  
