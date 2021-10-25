# <img src="./Images/Inter.png" width="25"> INTER - INterative Transistor calculatER

<a href="LICENSE">![Badge](https://img.shields.io/badge/license-BeerWare-yellow?style=for-the-badge)</a>

Software que calcula informações de circuitos amplificadores TBJ e FET, feito para a matéria de "Dispositivos e Circuitos Eletrônicos II" do curso de "Engenharia Elétrica" da Universidade Federal de Santa Maria Campus Cachoeira do Sul (UFSM-CS).

## Autor:
- Arthur Cordeiro Andrade

## Dependências
- PyGame - https://www.pygame.org
```
pip install pygame
```

# Compilar
## Dependências:
- Pyinstaller - https://www.pyinstaller.org
```
pip install pyinstaller
```

## Comando Compilar
```
pyinstaller --noconfirm --onefile --windowed --icon "Images/Inter.ico" --add-data "Images;Images/" --add-data "Sounds;Sounds/" "./INTER.py"
```