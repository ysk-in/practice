# Model Representation II
https://www.coursera.org/learn/machine-learning/lecture/Hw3VK/model-representation-ii  
ニューラルネットワークのベクトル化について扱う  

## ニューラルネットワークのベクトル化
前回あったように ニューラルネットワークは以下の式で表現できる  
<img src="../../img/04_01_value_of_activation_nodes.png" >  

ベクトル化を考えるために  
新しい変数<img src="https://latex.codecogs.com/gif.latex?z_{k}^{(j)}" title="z_{k}^{(j)}" />を定義し これをシグモイド関数gのパラメタとする  
zを使うと 上記ActivationNodesの式は以下で表現できる  
<img src="../../img/04_02_variable_zk.png" >

zは例えば<img src="https://latex.codecogs.com/gif.latex?z_{k}^{(2)}" title="z_{k}^{(2)}" />のとき つまり2層目のノードkについては以下となる  
<img src="../../img/04_02_example_of_zk.png" >  

xと<img src="https://latex.codecogs.com/gif.latex?z^{(j)}" title="z^{(j)}" />のベクトルは以下なので  
<img src="../../img/04_02_vectors_of_x_and_z.png" >  

jレイヤのzベクトルは以下で表現できる  
<img src="../../img/04_02_vectorized_z.png" >  

このようにベクトル化していく流れをForwardPropagation(順方向伝播?)とも呼ぶ
<img src="../../img/04_02_forward_propagation.png" width=70%>  

仮説関数のベクトルを汎化すると以下  
<img src="../../img/04_02_vectorized_hypothesis.png" >  
Outputへの最後のステップがやっていることはLogisticRegressionと全く同じ  
// と言ってくれているが 未だいまいちピンと来ない...  
