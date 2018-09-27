# Regularized Logistic Regression
LogisticRegressionをRegularizedする方法について扱う  

## LogisticRegressionのRegularization
LinearRegressionと同様 LogisticRegressionでもOverfittingが発生し得る  
以下の青線がOverfittingな状態  
LinerRegression同様 CostFunctionをRegularizedし Overfittingを解消する    
<img src="../../img/03_11_intuition_of_normalized_logistic_regression.png"  >  
<img src="https://latex.codecogs.com/gif.latex?&plus;&space;\frac{\lambda}{2m}\sum_{j=1}^{n}\theta_{j}^{2}" title="+ \frac{\lambda}{2m}\sum_{j=1}^{n}\theta_{j}^{2}" /> がRegularizedするための項  

前出の通り LogisticRegressionのCostFunctionは(≠Regularized)以下
<img src="../../img/03_11_cost_function_of_logistic_regression.png"  >  

Regularizedすると以下
<img src="../../img/03_11_regularized_cost_function_of_logistic_regression.png"  >

このLogisticRegressionのCostFunctionは  
(LinearRegressionと同様) 以下のGradientDescentに適用できる  
<img src="../../img/03_11_regularized_gradient_descent_of_logistic_regression.png"  >  
<img src="https://latex.codecogs.com/gif.latex?h_{\theta}(x^{(i)})" title="h_{\theta}(x^{(i)})" />がLogisticRegressionの式 <img src="https://latex.codecogs.com/gif.latex?\frac{1}{1&plus;e^{-\theta^{T}}x}" title="\frac{1}{1+e^{-\theta^{T}}x}" /> となる  

## AdvancedOptimazationのRegularization
LogisticRegressionのより洗練されたCostFunctionについて  
Regularizationすると以下の通り  
<img src="../../img/03_11_regularized_advanced_optimazation_of_logistic_regression.png" width=50% >  
