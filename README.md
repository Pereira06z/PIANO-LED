# PIANO-LED 🎹​

## Descrição do Projeto

Este projeto consiste na criação de um efeito visual inspirado no funcionamento das teclas de um piano, utilizando uma placa ESP32-S2 e três LEDs coloridos. O sistema executa uma sequência automática de iluminação em que os LEDs são acionados individualmente em ordem, simulando o movimento das notas musicais em um teclado.

A programação foi desenvolvida em MicroPython, permitindo o controle preciso do tempo de acionamento de cada LED. Durante a execução, os LEDs acendem de forma sequencial, criando um efeito dinâmico e agradável visualmente.

Cada LED permanece aceso por um intervalo de **0,5 segundo**, sendo desligado antes do acionamento do próximo LED da sequência. Após o último LED ser ativado, o ciclo reinicia automaticamente, mantendo o padrão de iluminação contínuo.

O projeto tem como objetivo demonstrar conceitos fundamentais de programação embarcada, controle de saídas digitais e temporização em microcontroladores. Além disso, serve como uma atividade introdutória para o estudo de sistemas embarcados utilizando a plataforma ESP32-S2.

## Componentes Utilizados

* 1 ESP32-S2 DevKitM-1;
* 3 LEDs (Vermelho, Verde e Azul);
* 3 Resistores para limitação de corrente;
* Protoboard;
* Fios de conexão;
* MicroPython;
* Simulador Wokwi.
* ![imagem](https://github.com/Pereira06z/PIANO-LED/blob/main/PIANO.png)

## Funcionamento

O sistema executa uma sequência repetitiva em que:

1. O LED Azul acende por 0,5 segundo;
2. O LED Azul apaga e o LED Vermelho acende por 0,5 segundo;
3. O LED Vermelho apaga e o LED Amarelo acende por 0,5 segundo;
4. Após o último LED, a sequência reinicia automaticamente.

O resultado é um efeito visual semelhante às teclas de um piano sendo pressionadas em sequência, proporcionando uma animação simples e intuitiva para demonstração de temporização e controle de LEDs.
