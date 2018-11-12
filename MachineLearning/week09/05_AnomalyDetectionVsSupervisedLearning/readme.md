# Anomaly Detection vs. Supervised Learning
https://www.coursera.org/learn/machine-learning/lecture/Rkc5x/anomaly-detection-vs-supervised-learning  
AnomalyDetectionとSupervisedLearningの使い分けについて扱う  

前回扱ったように Dataにラベル(y)があるときでも AnomalyDetectionを用いることがある  
ラベル(y)があるためSupervisedLearningも用いることができる 有効に使い分けるべき  

## AnomalyDetectionとSupervisedLearningの使い分け
基本的には y=1(陽性Data)のDataSetが少ない場合はAnomalyDetectionが有効で  
y=1, 0(陰性Data)のDataSetがともに十分にある場合はSupervisedLearningを使うべき  

もう少し詳細な観点を挙げると 主に以下の特徴に従い使い分ける  

* AnomalyDetectionが有効なケース  
	* y=1のDataが非常に少なく y=0が多い場合  
	* Anomalyの種類が豊富な場合  
		y=1と分類すべきDataSetの種類が豊富でアルゴリズムがその傾向を掴むのが難しそうな場合  
	* 未知(DataSetに含まれない)の種類のAnomalyが多そうな場合  
		これも↑と同じ AnomalyDetectionだとy=0のDataでモデリングするため有効  
* SupervisedLearningが有効なケース  
	* y=1とy=0のDataがどちらも豊富にある場合  
	* y=1に分類すべきDataが過去Data(TrainingSet)と似た傾向を持つ場合  
		過去のケースと似たものであることが分かっている場合はSupervisedLearningが有効  

y=1のDataが少ないとき AnomalyDetectionはy=1のDataを CV/Test Setに残せることが重要  
<img src="../../img/09_05_anomaly_detection_vs_supervised_learning.png" width=50% >  

ちなみに過去取り上げたメールがスパムかどうか分類するケースはSupervisedLearningが有効  
スパムメールと分類すべきメールの種類は豊富だが 十分なスパムメールのDataSetがあるため  

## 使い分けの具体例
具体的なケースでは以下の通り使い分ける  
<img src="../../img/09_05_anomaly_detection_supervised_learning.png" width=50% >  
製造で 様々な種類の欠陥があり 少しのDataSetしかないならAnomalyDetectionが適切  
ただし この場合でもy=1のDataSetがたくさんあればSupervisedLearningの方が適切かも  

変わった動きをするユーザが少ないときにFraud(詐欺)検出したいならAnomalyDetection  

基本的には たくさんのDataSetがあればSupervisedLearningで  
あんまりないならAnomalyDetection y=1,0のDataSetが同数くらいあればSupervisedLearning  
