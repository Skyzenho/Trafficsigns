# Trafficsigns
Repositório referente ao desafio técnico de reconhecimento de placas de transito.  

<h4 align="center">
  Traffic signs - Reconhecimento de placas de trânsito
</h4>

---
## Tabela de Conteúdo
- [Tabela de Conteúdo](#tabela-de-conte%C3%BAdo)
- [Sobre o desafio](#sobre-o-desafio)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Instalação](#instala%C3%A7%C3%A3o)
- [Contribuição](#contribui%C3%A7%C3%A3o)
## 📖 Sobre o desafio

O desafio consiste de reconhecer 43 placas de transito com diferentes qualidade de aquisição.
A solução proposta utiliza redes neurais convolucionais.

## ⚙ Tecnologias utilizadas

- Framework deep learning: TensorFlow
- Principais bibliotecas utilizadas: Numpy, Pandas

## ⚙ Instalação
1. Abra o terminal na pasta desejada.
2. Clone or download the project (`git clone https://github.com/Skyzenho/Trafficsigns.git`)
3. Download o conjunto de dados e descompacte na pasta desejada. (https://www.kaggle.com/venkateshroshan/traffic-signs)
4. Crie o ambiente virtual(`conda myenv create -f environment.yml`)
5. Ative o ambiente (`conda activate myenv`)
6. Entre na pasta(`cd nome_pasta`)
7. Execute o comando(`python main.py -I imagem.png -P 9001`) I= Imagem a ser analisada

## Contribuição
1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/Feature`)
3. Adicione suas mudanças (`git add .`)
4. Comite suas mudanças (`git commit -m 'Adicionando uma Feature!`)
5. Faça o Push da Branch (`git push origin feature/Feature`)
6. Abra um Pull Request