# Simplified Cost Function and Gradient Descent
LogisticRegressionのCostFunctionをシンプルに表現する方法と  
LogisticRegressionのCostFunctionにGradientDescentを適用する方法について扱う  

## Simplified Cost Function of Logistic Regression
前出の通り LogisticRegressionでは以下のCostFunctionを使用する  
<img src="../../img/03_04_cost_function_for_logistic_function.png" width=40% >  
yは常に0または1のため この2つの式は以下1つの式にまとめられる  
<img src="https://latex.codecogs.com/gif.latex?Cost(h_{\theta}(x),&space;y)&space;=&space;-y\log(h_{\theta}(x))&space;-&space;(1&space;-y)log(1&space;-&space;h_{\theta}(x))" title="Cost(h_{\theta}(x), y) = -y\log(h_{\theta}(x)) - (1 -y)log(1 - h_{\theta}(x))" />  
yが1のときは2項目が消え 1項目のみが残り  
yが0のときは1項目が消え 2項目のみが残る そのため元の式と内容は同じ  

このCostFunctionの全体を式にすると以下  
<img src="../../img/03_05_full_cost_function.png" width=50% >  
またこの式をベクトル化すると以下  
<img src="../../img/03_05_vectorized_cost_function.png" width=40% >  

## Gradient Descent of Logistic Regression
GradientDescent(前出の以下)を  
<img src="../../img/03_05_gradient_descent.png" width=20% >  
をLogisticRegressionのCostFunctionに適用すると以下の通り  
<img src="../../img/03_05_gradient_descent_of_logistic_regression.png" width=30% >  
LinearRegressionのときと同様 各<img src="https://latex.codecogs.com/gif.latex?\theta_{j}" title="\theta_{j}" />は同時に更新する必要がある  

また ベクトル化すると以下  
<img src="../../img/03_05_vectorized_gradient_descent_of_logistic_regression.png" >  
