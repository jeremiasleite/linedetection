# linedetection
Algoritmos para detecção da linha do horizonte e da costa em imagens de praia da orla de Recife, utilizando opencv e python.

# Resumo do trabalho
A orla da região metropolitana de Pernambuco tem apresentado vários incidentes com
tubarões e alguns desses casos foram fatais. Visando reduzir os incidentes, este trabalho
propõe uma abordagem para segmentação do mar como parte de um sistema
de monitoramento de banhistas através de câmeras. Uma vez que são identificadas
uma ou mais pessoas dentro da zona de risco, o sistema emitirá um alerta a central
de monitoramento, e o guarda-vida mais próximo seria alertado para se deslocar até
o local. Para que o sistema identifique as pessoas na imagem, o sistema deve ser capaz
de identificar a região de praia na imagem, afim de segmentá-las e identificar os
banhistas. A faixa de água é formada por duas fronteiras, uma com o céu e a outra
com a areia. A fronteira com o céu é uma linha reta horizontal denominada linha do
horizonte, e a fronteira com a areia é um contorno formado pelo limite da água com
a areia que é chamado de linha da costa. Esse trabalho visa propor algoritmos para
detecção das linhas do horizonte e da costa para segmentação do mar, que representa
uma das etapas principais para o sistema de monitoramento de banhista em imagens
de praia. Neste trabalho foram analisados quatro algoritmos de detecção da linha do
horizonte para avaliar quais desses obtém o melhor resultado na detecção. Dois algoritmos
do estado da arte foram analisados: o de Lie et al. e o de Ahmad et al.. Ambos
são trabalhos para detecção de linha do horizonte em imagens de montanhas, outros
dois algoritmos foram contribuições desse trabalho: o Detecção da Linha do horizonte
com Canny Edge Detection e Grafo Multiestágios (DLHCGME) e o Detecção da Linha
do Horizonte com Sobel e transformada de Hough (DLHSTH). Para detecção da linha
da costa foram propostos dois novos algoritmos: o Detecção da Linha da Costa com
Canny Edge Detection e Grafo Multiestágios (DLCCGME) e Detecção da linha da costa
baseado em contornos do canal hue (DLCCCH). Na detecção da linha do horizonte em
imagens sem oclusões os experimentos demostram que o DLHCGME obteve o melhor
resultado com uma taxa de erro de 0,47 e o segundo foi o DLHSTH com 1,11, e para
imagens com oclusões o DLHSTH obteve o melhor resultado com taxa de erro de 1,98
e o DLHCGME foi o segundo melhor resultado com 2,62.
