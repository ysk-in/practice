# Optimization Objective
ここから新しいアルゴリズムSupportVectorMachines(SVM)を扱う  
今回は特にCostFunctionを扱う  

## Support Vector Machines(SVM)のCostFunciton
SVMはLogisticRegression同様 分類を行なうための 教師ありアルゴリズムらしい  

CostFunctionの考え方はLogisticRegressionに似ていて  
前出の通り LogisticRegressionのCostは以下の細い曲線で示されたが  
SVMでは以下の手書きの太い直線で示したいらしい  
<img src="../../img/07_01_svm_view.png" width=50%>  
つまり SVMのCostはz(<img src="https://latex.codecogs.com/gif.latex?\theta^{T}x" title="\theta^{T}x" />)が1/-1を超えると常に0とし  
それ以外のzでは LogisticRegressionの傾きに似た変化をする直線としたいらしい  

また 表現するとき y=1に分類するものを<img src="https://latex.codecogs.com/gif.latex?Cost_{1}(z)" title="Cost_{1}(z)" /> 0のものを<img src="https://latex.codecogs.com/gif.latex?Cost_{0}(z)" title="Cost_{0}(z)" />と表すらしい  

SVMのCostFunctionは以下でLogisticRegressionとほぼ同じ  
<img src="../../img/07_01_cost_function_of_svm.png" width=50%>  
LogisticRegressionではReguralized項のペナルティにλ/2mを使ったり  
CostのSummation項に1/mをかけたりしていたのに対し SVMでは異なる値を使用しているが  
これには深い意味はないらしいので 深く考えすぎなくても良いらしい(よく理解できていない)  
