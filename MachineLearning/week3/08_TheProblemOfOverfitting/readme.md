# The Problem of Overfitting
オーバーフィットについて扱う

## オーバーフィットとは なにか
LinearRegressionの例を用いた場合 以下の右のケースを指す  
<img src="../../img/03_08_example_of_overfit_for_linear_regression.png" width=50% >  
つまり トレーニングセットに適合し過ぎた仮説を導き出してしまうことで  
未知のデータに対しての予測が適切でなくなってしまった仮説のことを指す  

ちなみに
* 左のケースがUnderFit/HighBiasな状態  
  つまり この例だと  
  データセットは 一定Sizeを越えると Price増加量は緩やかになることを示している  
  しかし 仮説はそれが反映できておらず Sizeが上がれば それに応じてPriceは上がる  
  という バイアスが強くかかり過ぎている状態を指す
* 真ん中のケース は望ましい状態  
  つまり データセットに対して よくフィットできており  
  また 未知のデータに対しての予測も 適切な値を導き出せることが期待できる状態  

同様に LogisticRegressionについては 各状態の仮説は以下のようになる  
<img src="../../img/03_08_example_of_overfit_for_logistic_regression.png" width=50% >  

## オーバーフィットの対策
実際に予測をしようとすると 多くのfeaturesを扱うことになる  
これらのfeaturesをそのまま全て使用するとオーバーフィットが発生し易い(?)
<img src="../../img/03_08_think_about_addressing_overfitting.png" width=50% >  

オーバーフィットの対策として以下が考えられる  
<img src="../../img/03_08_options_for_addressing_overfitting.png" width=50% >  
2.のRegularizationについて 次回以降(?)で詳細を扱ってもらえるらしい  
