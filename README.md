# Jogo da Velha em Python (Terminal) - UNINASSAU

Trabalho Avaliativo da 2ª Avaliação da disciplina de **Coding** do Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas da **UNINASSAU**.

**Alunos (Dupla):**
* **Gustavo Mateus Santana Ferreira** (Matrícula: 01936445)
* **Miguel Lucas Mendes do Monte** (Matrícula: 01924050)
* **Professor:** M.Sc. Tiago Martins Ribeiro

---

## 📋 Sobre o Projeto
Este projeto consiste em um **Jogo da Velha** interativo desenvolvido em **Python puro**, executado inteiramente via terminal. O tabuleiro é representado por uma matriz bidimensional (lista de listas 3x3) percorrida com laços de repetição aninhados (`for` aninhado), cumprindo rigorosamente todas as restrições da disciplina (sem funções `def`/`lambda`, sem dicionários, tuplas ou conjuntos, sem métodos avançados como `isdigit()` ou `append()`, sem bibliotecas externas e sem blocos `try/except`).

---

## 🚀 Como Executar a Aplicação

### Pré-requisitos
* Ter o **Python 3** instalado no computador.

### Passo a passo:
1. Abra o terminal (Prompt de Comando, PowerShell ou Terminal do VS Code) na pasta onde está o arquivo `jogo.py`.
2. Execute o seguinte comando:
   ```bash
   py jogo.py
   ```
3. Utilize o menu interativo no terminal escolhendo os números de 1 a 4 para navegar entre as opções de jogo, placar, regras e saída.

---

## 🕹️ Funcionalidades Implementadas
* **Menu Interativo:** Controlado por laço `while`, com opções para jogar, visualizar placar, consultar regras e sair.
* **Tabuleiro em Matriz 3x3:** Exibido dinamicamente a cada rodada com a numeração clara das linhas e colunas (0 a 2).
* **Validação Robusta de Entradas:** Impede o encerramento abrupto (*crash*) do programa ao digitar letras, símbolos, campos vazios, números fora do intervalo ou casas já ocupadas.
* **Verificação Automática de Vitória e Empate:** Percorre linhas, colunas e diagonais utilizando laços `for` para detectar vencedores ou verificar o esvaziamento de casas (empate).
* **Placar Acumulado:** Mantém contagem contínua das vitórias dos Jogadores X e O, além dos empates ao longo da sessão.
* **Reinício Automático:** Permite reiniciar a partida limpando a matriz do tabuleiro sem precisar fechar o programa.

---

## 📂 Estrutura da Pasta Organizada
* `jogo.py`: Código-fonte principal da aplicação em Python.
* `relatorio_tecnico.pdf`: Relatório técnico completo formatado segundo as normas da ABNT e o template da UNINASSAU.
* `README.md`: Documentação de orientações de uso e arquitetura.
