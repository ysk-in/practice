# Gradient Descent For Linear Regression
https://www.coursera.org/learn/machine-learning/lecture/kCvQc/gradient-descent-for-linear-regression  
LinearRegression(線形回帰)の場合  
GradientDescent(最急降下法)の新しい方程式が導き出される  

## 線形回帰においての最急降下法
前出の通り 最急降下法の式は以下  
<img src="../../img/01_08_gradient_descent_algorithm.png" width=50%>  

また 前出の通り Squared error function(二乗誤差関数/最小二乗法)の式は以下  
<img src="../../img/01_05_cost_function_formula.png">  

これらを組み合わせると (最急降下法のJ(Θ0, Θ1)を最小二乗法の式で置き換えると)  
以下の式を導き出すことができる(式の変換過程の詳細は以降の参考項目を参照)  
<img src="../../img/01_10_gradient_descent_for_linear_regression_algorithm.png" width=50%>  

この式を用いることで  
最急降下法 のみを用いてJ(Θ0, Θ1, ..., Θn)を最小化するときに発生する  
局所的最小値が取得される ということがなくなり 必ず最小値を取得することができる  

ということを言っているっぽいが 日本語字幕が不正確なこともあり  
理解が正しいか怪しい...

## (参考) 式の変換過程
J(Θ0, Θ1)を展開すると以下の通り  
<img src="https://latex.codecogs.com/gif.latex?\frac{\partial}{\partial\theta_{j}}J(\theta_{0},&space;\theta_{1})&space;\\&space;=&space;\frac{\partial}{\partial\theta_{j}}&space;\cdot&space;\frac{1}{2m}&space;\sum_{i=1}^{m}(h_{\theta}(x^{(i)})&space;-&space;y^{(i)})^{2}&space;\\&space;=&space;\frac{\partial}{\partial\theta_{j}}&space;\cdot&space;\frac{1}{2m}&space;\sum_{i=1}^{m}(\theta_{0}&space;&plus;&space;\theta_{1}x^{(i)}&space;-&space;y^{(i)})^{2}&space;\\&space;=&space;\frac{\partial}{\partial\theta_{j}}&space;\cdot&space;\frac{1}{2m}&space;\sum_{i=1}^{m}(&space;\theta_{0}^{2}&space;&plus;&space;\theta_{1}^{2}x^{(i)^{2}}&space;&plus;&space;y^{(i)^{2}}&space;&plus;&space;2\theta_{0}\theta_{1}x^{(i)}&space;-&space;2\theta_{1}x^{(i)}y^{(i)}&space;-&space;2y^{(i)}\theta_{0}&space;)" width=50%>   

この式について j = 0 の場合 を考えると以下の通り展開できる  
<img src="https://latex.codecogs.com/gif.latex?j%20%3D%200%20%3A%20%5Cfrac%7B%5Cpartial%7D%7B%5Cpartial%5Ctheta_%7Bj%7D%7DJ%28%5Ctheta_%7B0%7D%2C%20%5Ctheta_%7B1%7D%29%20%5C%5C%20%3D%20%5Cfrac%7B%5Cpartial%7D%7B%5Cpartial%5Ctheta_%7B0%7D%7D%20%5Ccdot%20%5Cfrac%7B1%7D%7B2m%7D%20%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28%20%5Ctheta_%7B0%7D%5E%7B2%7D%20&plus;%20%5Ctheta_%7B1%7D%5E%7B2%7Dx%5E%7B%28i%29%5E%7B2%7D%7D%20&plus;%20y%5E%7B%28i%29%5E%7B2%7D%7D%20&plus;%202%5Ctheta_%7B0%7D%5Ctheta_%7B1%7Dx%5E%7B%28i%29%7D%20-%202%5Ctheta_%7B1%7Dx%5E%7B%28i%29%7Dy%5E%7B%28i%29%7D%20-%202y%5E%7B%28i%29%7D%5Ctheta_%7B0%7D%20%29%20%5C%5C%20%3D%20%5Cfrac%7B1%7D%7B2m%7D%20%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28%202%5Ctheta_%7B0%7D%20&plus;%202%5Ctheta_%7B1%7Dx%5E%7B%28i%29%7D%20-%202y%5E%7B%28i%29%7D%20%29%20%5C%5C%20%3D%20%5Cfrac%7B1%7D%7Bm%7D%20%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28%20%5Ctheta_%7B0%7D%20&plus;%20%5Ctheta_%7B1%7Dx%5E%7B%28i%29%7D%20-%20y%5E%7B%28i%29%7D%20%29%20%5C%5C%20%3D%20%5Cfrac%7B1%7D%7Bm%7D%20%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28%20h_%7B%5CTheta%7D%28x%5E%7B%28i%29%7D%29%20-%20y%5E%7B%28i%29%7D%20%29" width=50%>  

同様に j = 1 の場合 を考えると以下の通り展開できる  
<img src="https://latex.codecogs.com/gif.latex?j&space;=&space;1&space;:&space;\frac{\partial}{\partial\theta_{j}}J(\theta_{0},&space;\theta_{1})&space;\\&space;=&space;\frac{\partial}{\partial\theta_{1}}&space;\cdot&space;\frac{1}{2m}&space;\sum_{i=1}^{m}(&space;\theta_{0}^{2}&space;&plus;&space;\theta_{1}^{2}x^{(i)^{2}}&space;&plus;&space;y^{(i)^{2}}&space;&plus;&space;2\theta_{0}\theta_{1}x^{(i)}&space;-&space;2\theta_{1}x^{(i)}y^{(i)}&space;-&space;2y^{(i)}\theta_{0}&space;)&space;\\&space;=&space;\frac{1}{2m}&space;\sum_{i=1}^{m}(&space;2\theta_{1}x^{(i)^{2}}&space;&plus;&space;2\theta_{0}x^{(i)}&space;-&space;2x^{(i)}y^{(i)}&space;)&space;\\&space;=&space;\frac{1}{m}&space;\sum_{i=1}^{m}(&space;\theta_{1}x^{(i)^{2}}&space;&plus;&space;\theta_{0}x^{(i)}&space;-&space;x^{(i)}y^{(i)}&space;)&space;\\&space;=&space;\frac{1}{m}&space;\sum_{i=1}^{m}(&space;\theta_{1}x^{(i)}&space;&plus;&space;\theta_{0}&space;-&space;y^{(i)}&space;)&space;\cdot&space;x^{(i)}&space;\\&space;=&space;\frac{1}{m}&space;\sum_{i=1}^{m}(&space;h_{\theta}(x^{(i)})&space;-&space;y^{(i)}&space;)&space;\cdot&space;x^{(i)}" width=50%>  
