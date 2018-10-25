# Kernels I
SVMで複雑な非線形の分類するときに用いられているKernelsの考え方について扱う  

## Kernelsの考え方
以下DataSetを分類するDicisionBoundryは  
イメージでは左のグラフの通りで 式は右にある通りとなる  
<img src="../../img/07_04_non_linear_decision_boundry.png" width=50% >  
ここからFeature f1, f2, f3, ...を用いる  
これは今回の式ではそれぞれx1, x2, x1x2, ...を指すFeature  

以下のようなLandmark l(1), l(2), l(3)が与えられたとき  
f1, f2, f3 を xとそれぞれのLandmarkとのSimilarity(類似度)で求めることを考える  
// なぜそういう発想になっているのか理解できていない...  
ここで Similarityを求める関数は GaussianKernelと呼ばれるもの  
<img src="../../img/07_04_kernel.png" width=50% >  

Similarityで求めている値は2つの点(f1だったらxとl(1))がどれだけ類似しているか  
<img src="../../img/07_04_kernels_and_similarity.png" width=50% >  
つまり xがl(1)とほぼ同じ点を指すとき 上記の通り f1は ほぼほぼ1となる  
逆に xとl(1)が全然異なる点を指すとき 上記の通り f1は ほぼほぼ0となる  

パラメタσは以下の通り作用する  
<img src="../../img/07_04_sigma_example.png" width=50% >  
つまり Similarity(f1)が1(同じ点を指す)になるときのl(1)が`点[3; 5]`であることは  
どのσでも同じだが この点から離れるとき  
σが小さいと急激に0に近づき σが大きいと緩やかに0に近付く  

以下の関数について パラメタ(θ)を以下の通り定めているとき  
一番l(1)に近い青点についてf1, f2, f3を求めると それぞれおよそ1, 0, 0となる  
// l(1)には類似度が高い点なのでf1は1 それ以外のl(2), l(3)からは遠いので0  
<img src="../../img/07_04_example.png" width=50% >  
当該の青点について仮説関数にf1, f2, f3を与えたとき 値は0.5で0以上のため1に分類される  

このような考え方でSVMは考える  
(らしい...? Similarityは分かったけど SVMは未だよく分からない)  
