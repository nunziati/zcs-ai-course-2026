# Prerequisiti

Il corso dà per noti gli argomenti elencati qui sotto e non li rispiega. Sono cinque
gruppi; per ciascuno trovi il materiale con cui recuperarlo, gratuito e con la lingua
indicata.

## Python e PyTorch

Python letto correntemente, e PyTorch a livello di lettura del codice: capire cosa
fanno un `Dataset`, un `DataLoader`, un `nn.Module` e un ciclo di training scritti da
altri. Non serve saperli scrivere da zero.

Recupero: [PyTorch, *Learn the Basics*](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)
(inglese) — sette capitoli brevi, ognuno apribile direttamente in Colab.

## Addestramento e generalizzazione

Divisione train/validation/test, k-fold, overfitting e generalizzazione.

Recupero: [Google, *Set di dati, generalizzazione e overfitting*](https://developers.google.com/machine-learning/crash-course/overfitting?hl=it)
(italiano). Il k-fold non c'è: sta in
[scikit-learn, *Cross-validation*](https://scikit-learn.org/stable/modules/cross_validation.html)
(inglese).

## Come si addestra una rete

Backpropagation, learning rate, batch size, epoche, normalizzazione, dropout,
early stopping.

Recupero, in italiano, dal corso di Google:
[*Reti neurali*](https://developers.google.com/machine-learning/crash-course/neural-networks?hl=it)
per la backpropagation,
[*Iperparametri*](https://developers.google.com/machine-learning/crash-course/linear-regression/hyperparameters?hl=it)
per learning rate, batch size ed epoche,
[*Normalizzazione*](https://developers.google.com/machine-learning/crash-course/numerical-data/normalization?hl=it)
per la normalizzazione. L'early stopping è nel modulo *Set di dati, generalizzazione e
overfitting* linkato sopra. Il dropout non c'è in nessuno dei due: sta in
[*Dive into Deep Learning*, cap. 5.6](https://d2l.ai/chapter_multilayer-perceptrons/dropout.html)
(inglese), con il codice PyTorch eseguibile.

## CNN e transfer learning

Convoluzione, pooling e architetture convoluzionali; partire da un modello
preaddestrato, congelarne una parte e riaddestrare il resto.

Recupero: [Stanford CS231n, *Convolutional Neural Networks*](https://cs231n.github.io/convolutional-networks/)
(inglese) per le CNN, e
[PyTorch, *Transfer Learning for Computer Vision*](https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)
(inglese) per il transfer learning.

## Metriche di classificazione

Matrice di confusione, accuratezza, precisione, richiamo, ROC e AUC.

Recupero: [Google, *Classificazione*](https://developers.google.com/machine-learning/crash-course/classification?hl=it)
(italiano).
