# Análise Comparativa da Proteína vvMLP em Diferentes pHs

Este repositório contém um script em Python para comparar estruturas da proteína **vvMLP** (PDB ID: 5YH4) em diferentes condições de pH. O programa analisa as alterações nos aminoácidos da proteína a partir da comparação de suas estruturas em pH neutro (7,4), ácido (3,0) e original PDB (6,5).

A **vvMLP** é uma proteína similar à Miraculina, extraída da uva (**Vitis vinifera**). [cite_start]Embora não altere o sabor como a Miraculina, ela inibe a tripsina [cite: 5][cite_start], uma proteína digestiva de insetos, contribuindo para a defesa da videira contra a herbivoria. [cite: 5] [cite_start]O objetivo deste projeto é observar o comportamento da **vvMLP** em diferentes pHs, para identificar quais aminoácidos são protonados. [cite: 6]

## Tecnologias Utilizadas

* **Biopython (PDBParser):** Utilizada para ler os arquivos PDB e extrair informações dos aminoácidos.
* **Pandas:** Usada para comparar os dados, organizar as informações em tabelas e exportar os resultados para planilhas do Excel.

## Como o Código Funciona

Este script é uma ferramenta para auxiliar na análise de dados de simulações de dinâmica molecular. [cite_start]O programa usa a biblioteca Biopython para ler três arquivos PDB da proteína **vvMLP** (PDB ID: 5YH4 [cite: 12][cite_start]), correspondentes a diferentes condições: original (6,5), pH neutro (7,4 [cite: 14][cite_start]) e pH ácido (3,0 [cite: 14]). O arquivo da proteína em pH ácido foi gerado usando o site `pdb2pqr` para protonar os aminoácidos. Os aminoácidos e suas respectivas posições são armazenados em dicionários.

O usuário pode escolher entre três opções de comparação:

1.  Original vs. Neutro
2.  Original vs. Ácido
3.  Neutro vs. Ácido

Após a escolha, o programa usa a biblioteca Pandas para criar uma tabela comparativa e identificar as diferenças entre os aminoácidos. Os resultados são exportados para um arquivo `.xlsx` e exibidos no terminal.

## Resultados Obtidos

As análises mostraram que a mudança de pH resultou na protonação de muitos aminoácidos. [cite_start]As comparações evidenciam as alterações mais significativas no ambiente ácido, o que contrasta com a Miraculina comum, que sofre uma grande alteração estrutural em pH ácido. [cite: 62] [cite_start]Acredita-se que a **vvMLP** é mais resiliente a variações de pH por ser monomérica, enquanto a miraculina ativa é funcional apenas na forma dimérica. [cite: 63]

Abaixo estão os resultados das comparações:

### Comparação: Original - Ácido

| resíduo | Original | pH ácido | Diferente |
|---------|----------|----------|-----------|
| 9       | ASP      | ASH      | VERDADEIRO|
| 11      | GLU      | GLH      | VERDADEIRO|
| 20      | ASP      | ASH      | VERDADEIRO|
| ...     | ...      | ...      | ...       |

* **Resíduos alterados:** 28

### Comparação: Neutro - Ácido

| resíduo | pH neutro| pH ácido | Diferente |
|---------|----------|----------|-----------|
| 9       | ASP      | ASH      | VERDADEIRO|
| 11      | GLU      | GLH      | VERDADEIRO|
| 20      | ASP      | ASH      | VERDADEIRO|
| ...     | ...      | ...      | ...       |

* **Resíduos alterados:** 22

### Comparação: Original - Neutro

| resíduo | Original | pH neutro| Diferente |
|---------|----------|----------|-----------|
| 44      | CYS      | CYX      | VERDADEIRO|
| 53      | HIS      | HID      | VERDADEIRO|
| 79      | HIS      | HIE      | VERDADEIRO|
| ...     | ...      | ...      | ...       |

* **Resíduos alterados:** 8

---

## Análise

A alteração dos aminoácidos em ambientes ácidos, como observado nas tabelas de comparação, ocorre devido à protonação dos resíduos. A relação entre pH e concentração de H⁺ demonstra que quanto menor o pH, maior a concentração de H⁺, influenciando diretamente as alterações observadas.

Os aminoácidos que foram alterados durante as mudanças de pH seguem um padrão específico, conforme a tabela abaixo:

| Aminoácido | Alterado      | Grupo         |
|------------|---------------|---------------|
| HIS        | HIP, HID, HIE | Carregados +  |
| CYS        | CYX           | Não carregados|
| GLU        | GLH           | Carregados -  |
| ASP        | ASH           | Carregados -  |

## Próximos Passos

A próxima etapa do projeto é implementar essa ferramenta em um site, utilizando a biblioteca Streamlit. O objetivo é disponibilizar a ferramenta para que outras pessoas possam utilizá-la e, ao mesmo tempo, aprofundar a lógica de programação.
