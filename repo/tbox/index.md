---
title: TBox
description: Caixa térmica de incubação microcontrolada
published: True
date: 2025-08-14 18:51:03.505000+00:00
tags: None
editor: markdown
dateCreated: 2025-08-13 17:42:04.656000+00:00
---

***Laboratório Experimental de Ciência Cidadã, Cultura Oceânica e Tecnologia***


## Introdução

O objetivo da Therminator Box (TBox) é manter uma incubadora para cultura de bactérias com temperatura controlada. Quando ligada, a caixa porcura se regular automaticamente com a temperatura selecionada pelo botão angular (potenciômetro) desde que a temperatura desejada seja maior que a do ambiente. Caso deseje resfriar o ar da incubadora o lado da pastilha peltier deverá ser invertido ao desta montagem.

## Materiais

- [1 Arduino UNO](https://www.arduino.cc/en/Main/ArduinoBoardUno) atualizado com firmware [therminator-box](https://github.com/guimasan/T-box);
- 1 [Mini BreadBoard](https://www.sparkfun.com/breadboard-mini-modular-white.html);
- 1 [Transistor NPN TIP122](https://cdn-shop.adafruit.com/datasheets/TIP120.pdf) 
- 1 Fonte 12Volts 5A (no mínimo);
- Fios para eletrônica ;
- 1 [Pastilha peltier 12V ~ 40W](http://peltiermodules.com/peltier.datasheet/TEC1-12705.pdf);
![tbox1.png]({{ '/assets/media/tbox1.png' | relative_url }})
- 1 Dissipador com relevo do tamanho da pastilha:
![tbox2.png]({{ '/assets/media/tbox2.png' | relative_url }})
- 1 Dissipador do tamanho da pastila peltier:
![tbox3.png]({{ '/assets/media/tbox3.png' | relative_url }})
- 1 Caixa plástica (Incubadoras que fiquem com temperatura de até 60⁰C):
![tbox4.png]({{ '/assets/media/tbox4.png' | relative_url }})
- 1 [Sensor de temperatura](https://wiki.seeedstudio.com/Grove-Temperature_Sensor/):
![tbox5.png]({{ '/assets/media/tbox5.png' | relative_url }})
- 1 Display [LCD](https://wiki.seeedstudio.com/Grove-LCD_RGB_Backlight/),e [também](https://wiki.seeedstudio.com/Grove-LCD_RGB_Backlight/)

## Como fazer

Marque o tamanho do relevo do dissipador escolhido, para que apenas essa área fique em contato com a parte interna da incubadora. Faça um corte na caixa plástica:
![tbox6.png]({{ '/assets/media/tbox6.png' | relative_url }})

Acople o dissipador, se necessário pode ser colada a parte de baixo na caixa plástica com silicone de alta temperatura:
![tbox7.png]({{ '/assets/media/tbox7.png' | relative_url }})

Passe pasta térmica no dissipador e na pastilha peltier. Coloque o lado que resfria da pastilha com o dissipador externo da caixa:
![tbox71.png]({{ '/assets/media/tbox71.png' | relative_url }})
Adicione um dissipador menor que fará o papel de aquecer o ar interno da incubadora:
![tbox81.png]({{ '/assets/media/tbox81.png' | relative_url }})
![tbox9.png]({{ '/assets/media/tbox9.png' | relative_url }})
Coloque o sensor de temperatura próximo de onde ficará a amostra incubada:
![tbox10.png]({{ '/assets/media/tbox10.png' | relative_url }})

A amostra não deve ficar sobre o dissipador interno pois o mesmo ficará com temperatura superior enquanto mantém o ar a caixa em temperatura controlada.

Conecte um [Transistor NPN Darlington TIP122 na protoboard](https://cdn-shop.adafruit.com/datasheets/TIP120.pdf):
![tbox11.png]({{ '/assets/media/tbox11.png' | relative_url }})

Conecte o fio negativo (preto) da pastilha peltier no pino 2 do transistor TIP122 e o fio positivo (vermelho) da pastilha conecte na saída Vin do arduino
![tbox12.png]({{ '/assets/media/tbox12.png' | relative_url }})

Conecte o sensor de temperatura na entrada A0 do Arduino (Neste exemplo o Arduino está com um shield de conexão (Groove Seeedstudio)
![tbox13.png]({{ '/assets/media/tbox13.png' | relative_url }})

Conecte um potenciômetro (sensor angular resistivo) na entrada A1 do Arduino
![tbox14.png]({{ '/assets/media/tbox14.png' | relative_url }})

Conecte o pino 3 do transistor TIP122 no GND do Arduino
![tbox15.png]({{ '/assets/media/tbox15.png' | relative_url }})

Faça um dissipador de calor para o transistor TIP122. Passe pasta térmica na carcaça de junção dos metais
![tbox16.png]({{ '/assets/media/tbox16.png' | relative_url }})

Conecte o pino 1 do transistor TIP122 na saída digital 3 ~ PWM do Arduino
![tbox17.png]({{ '/assets/media/tbox17.png' | relative_url }})
![tbox18.png]({{ '/assets/media/tbox18.png' | relative_url }})

Tampe a caixa e adicione o Display LCD
![tbox19.png]({{ '/assets/media/tbox19.png' | relative_url }})
![tbox20.png]({{ '/assets/media/tbox20.png' | relative_url }})

Conecte a fonte 12V 5A no Arduino e ajuste no potênciometro a temperatura na qual o dissipador deverá chegar e manter o ar da caixa aquecido
![tbox21.png]({{ '/assets/media/tbox21.png' | relative_url }})

> Esta estufa ainda não é capaz de trabalhar com temperaturas maiores que 60⁰C por muito tempo por conta de uma limitação no tip122.
> 
> Pensando em acessibilidade e facilidade de replicação, uma versão simples (SV) foi desenvolvida:
{.is-info}


## Therminator Box SV (Small Version)

![tboxsmall.png]({{ '/assets/media/tboxsmall.png' | relative_url }})

[Firmware](https://github.com/guimasan/therminator-box/blob/master/therminatorBoxSV.ino): 

Edite no código a temperatura (em graus Celsius) desejada, ex.: [ ] define TEMP 37 (37 é a temperatura desejada);

Proceda a montagem como no tutorial acima, substituindo o termistor sensor de temperatura da Grove Kit pelo lm35 e a fiação necessária.

Substitua o LCD Display pelo LED RGB Anôdo comum. O TherminatorBox SV ligará:

LED Azul quando a temperatura estiver abaixo do desejado;

LED Verde quando a temperatura estiver equilibrada com o desejado;

LED Vermelho quando a temperatura estiver acima do dejesado;

Pode ser comum o LED Vermelho ligar quando a estufa estiver se equilibrando com a temperatura, por causa do delay entre o aquecimento do ar e o da pastilha.

Espere aproximadamente 10min para que a incubadora fique em temperatura equilibrada.
