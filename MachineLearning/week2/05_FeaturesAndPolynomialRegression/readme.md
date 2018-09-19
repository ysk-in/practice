# Features and Polynomial Regression
多項式回帰について学ぶ  

## Polynomial Regression(多項式回帰)
以下のデータセットにフィットする線(仮説)を考える場合  
<img src="../../img/02_05_polynomial_regression.png" width=50%>  
1次式(直線)よりも2次式・3次式の方が より最適な仮説になると考えられる  

2次式 <img src="https://latex.codecogs.com/gif.latex?\theta_{0}&plus;\theta_{1}x&plus;\theta_{2}x^{2}" title="\theta_{0}+\theta_{1}x+\theta_{2}x^{2}" />の仮説を用いることを考えると  
Size(x)が一定値を超えると Price(y)が減算されてしまい 適切な仮説とは言えない  

3次式 <img src="https://latex.codecogs.com/gif.latex?\theta_{0}&plus;\theta_{1}x&plus;\theta_{2}x^{2}&plus;\theta_{3}x^{3}" title="\theta_{0}+\theta_{1}x+\theta_{2}x^{2}+\theta_{3}x^{3}" />の仮説を用いることを考えると  
Size(x)が一定値を超えても Price(y)が減算されない仮説になり より最適な仮説になる

3次式を用いた場合Size(x)が一定値を超えると Price(y)が大きく増加する  
これが適さない場合は √を用いると より最適な仮説が導き出せることがある    
<img src="../../img/02_05_polynomial_regression_root.png" width=50%>  
// √を含む式は上記図の右下にあるように xが一定値を超えると  
// yが非常に緩やかに増加するような線になる

## 最適な仮説を考えるために
このように 仮説の 次元数を変えたり √を用いたりすることで  
直線/曲線の傾きをコントロールすることが出来る  

どの次元を選択するか また √の導入是非 を考えるのは難しいことだが  
どのように選択すれば良いかは この後で学習できるらしい(プログラムを使う?)

もう1つ ここで覚えておきたいのは 次数を大きくすると  
それに伴い 変数の値が非常に大きくなるため(収束するのに時間がかかる)  
前出のFeature Scalingを適用し 値域を揃える必要があること
