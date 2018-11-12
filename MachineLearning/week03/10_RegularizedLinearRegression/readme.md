# Regularized Linear Regression
https://www.coursera.org/learn/machine-learning/lecture/QrMXd/regularized-linear-regression  
LinearRegressionをRegularizedするための考え方について扱う  

## LinearRegressionをGradientDescentでFittingするときのRegularization
GradientDescentにRegularizationするための式を加え以下となる  
<img src="../../img/03_10_normalized_gradient_descent.png" width=50% >  
前出の通り<img src="https://latex.codecogs.com/gif.latex?\theta_{0}" title="\theta_{0}" />はNormalizedする必要がないため式がわかれる  
<img src="https://latex.codecogs.com/gif.latex?\frac{\lambda}{m}\theta_{j}" title="\frac{\lambda}{m}\theta_{j}" />がNormalizedのための項  

また <img src="https://latex.codecogs.com/gif.latex?\theta_{j}" title="\theta_{j}" />のための式は以下に変形できる  
<img src="../../img/03_10_manupulated_normalized_gradient_descent.png" >    

## LinearRegressionをNormalEquationでFittingするときのRegularization
同様に RegularizedなNormalEquationの式は以下  
<img src="../../img/03_10_normalized_normal_equation.png" width=30%>  
λ*Lの項がNormalizationのための項  
Lは上記の通り diag=(0, 1, 1, ..., 1)の単位行列 (用語間違ってるかも...)
