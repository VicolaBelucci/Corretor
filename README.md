# Corretor
Projeto de corretor ortográfico (Reprodução)


  Este projeto foi realizado ao fim de uma formação de Python para Data Science na plataforma de estudos Alura. 
A ideia foi mostrar a lógica utilizada para correção de uma palavra com distância de 1 a 2 erro da palavra 
correta.

  A lógica utilizada foi a de identificar 4 possíveis fontes de erro (falta de uma letra, troca de letras, digitação
equivocada e adição de letras a mais) e trabalhar com métodos já conhecidos de slice e concatenação para gerar 
possíveis palavras corretas a partir da palavra errada.

  Com as palavras geradas, elas são comparadas com um banco criado a partir de artigos (a separação, criação e
normalização do banco de palavras foi feita no mesmo código, nas primeiras funções) com possíveis candidatos
corretos.

Obviamente o projeto possui suas limitações, tanto funcionais quanto gráficas, mas foi interessante por demonstrar
alguma funções e pacotes que antes eram desconhecidas (como nltk, por exemplo) e também por aprofundar conceitos
mais básicos como slice e tratamento de strings.
