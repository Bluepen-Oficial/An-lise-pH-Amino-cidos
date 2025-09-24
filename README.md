# Análise Comparativa da Proteína vvMLP em Diferentes pHs

Este repositório contém um script em Python para comparar estruturas da proteína **vvMLP** (PDB ID: 5YH4) em diferentes condições de pH. O programa analisa as alterações nos aminoácidos da proteína a partir da comparação de suas estruturas em pH neutro (7,4), ácido (3,0) e original PDB (6,5).

A **vvMLP** é uma proteína similar à Miraculina, extraída da uva (**Vitis vinifera**). Embora não altere o sabor como a Miraculina, ela inibe a tripsina, uma proteína digestiva de insetos, contribuindo para a defesa da videira contra a herbivoria. O objetivo deste projeto é observar o comportamento da **vvMLP** em diferentes pHs, para identificar quais aminoácidos são protonados.

## Tecnologias Utilizadas

* **Biopython (PDBParser):** Utilizada para ler os arquivos PDB e extrair informações dos aminoácidos.
* **Pandas:** Usada para comparar os dados, organizar as informações em tabelas e exportar os resultados para planilhas do Excel.

## Como o Código Funciona

Este script é uma ferramenta para auxiliar na análise de dados de simulações. O programa usa a biblioteca **Biopython** para ler os arquivos PDB da proteína **vvMLP** e armazena os aminoácidos e suas posições em dicionários. O arquivo da proteína em pH ácido foi gerado usando o site `pdb2pqr` para a protonação dos aminoácidos.

O usuário pode escolher entre três opções de comparação:

1. Original vs. Neutro
2. Original vs. Ácido
3. Neutro vs. Ácido

Após a escolha, o programa usa a biblioteca **Pandas** para criar uma tabela comparativa, identificar as diferenças entre os aminoácidos e exportar os resultados para um arquivo `.xlsx`.

## Resultados Obtidos

As análises mostraram que a mudança de pH resultou na protonação de muitos aminoácidos. As comparações evidenciam as alterações mais significativas no ambiente ácido.

Abaixo estão os resultados das comparações obtidas:

### Comparação: Original - Ácido

| resíduo | Original | pH ácido | Diferente |
|---------|----------|----------|-----------|
| 9 | ASP | ASH | VERDADEIRO|
| 11 | GLU | GLH | VERDADEIRO|
| 20 | ASP | ASH | VERDADEIRO|
| 42 | GLU | GLH | VERDADEIRO|
| ... | ... | ... | ... |

* **Resíduos alterados:** 28

### Comparação: Neutro - Ácido

| resíduo | pH neutro| pH ácido | Diferente |
|---------|----------|----------|-----------|
| 9 | ASP | ASH | VERDADEIRO|
| 11 | GLU | GLH | VERDADEIRO|
| 20 | ASP | ASH | VERDADEIRO|
| 42 | GLU | GLH | VERDADEIRO|
| ... | ... | ... | ... |

* **Resíduos alterados:** 22

### Comparação: Original - Neutro

| resíduo | Original | pH neutro| Diferente |
|---------|----------|----------|-----------|
| 44 | CYS | CYX | VERDADEIRO|
| 53 | HIS | HID | VERDADEIRO|
| 79 | HIS | HIE | VERDADEIRO|
| ... | ... | ... | ... |

* **Resíduos alterados:** 8

---

## Análise

Para um sistema ficar ácido, é necessário adicionar H⁺, e é isso que a ferramenta **pdb2pqr** faz. A alteração dos aminoácidos em ambientes ácidos, como observado nas tabelas de comparação, ocorre devido à protonação dos resíduos. A relação entre pH e concentração de H⁺ demonstra que, quanto menor o valor do pH, maior a concentração de H⁺ no sistema.

Os aminoácidos que foram alterados durante as mudanças de pH seguem um padrão, conforme a tabela abaixo:

| Aminoácido | Alterado | Grupo |
|------------|----------|---------------|
| HIS | HIP, HID, HIE | Carregados + |
| CYS | CYX | Não carregados|
| GLU | GLH | Carregados - |
| ASP | ASH | Carregados - |

## Próximos Passos

O próximo passo do projeto é implementar essa ferramenta em um site com a biblioteca **Streamlit**, para treinar a lógica de programação e disponibilizar a ferramenta para uso.
