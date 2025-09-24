from Bio.PDB import PDBParser
import pandas as pd

dic_original = {}
dic_neutro = {}
dic_acido = {}

parser = PDBParser(QUIET=True)

estrutura_original = parser.get_structure("Original", "5yh4.pdb")
estrutura_neutra = parser.get_structure("pH Neutro", "5yh4_pH_7.pdb")
estrutura_acida = parser.get_structure("pH Ácido", "5yh4_pH_3.pdb")

for model in estrutura_original:
    for chain in model:
        for residue in chain:
            numero_residuo = residue.id[1]
            if 1 <= numero_residuo <= 179:
                nome = residue.resname 
                dic_original[residue.id[1]] = nome

for model in estrutura_neutra:
    for chain in model:
        for residue in chain:
            residuo_neutro = residue.id[1]
            if 1 <= residuo_neutro <= 179:
                nome = residue.resname
                dic_neutro[residue.id[1]] = nome

for model in estrutura_acida:
    for chain in model:
        for residue in chain:
            residuo_acido = residue.id[1]
            if 1 <= residuo_acido <= 179:
                nome = residue.resname
                dic_acido[residue.id[1]] = nome

seletor = int(input("Sistema para comparar PDB, selecione a opção desejada: \n1 - Comparação: Original | Neutro\n2 - Comparação: Original | Ácida\n3 - Comparação: Neutra   | Ácida\nSeleção: "))

match seletor: 

    case 1:
        df_ori_neu = pd.DataFrame({
            "Original": dic_original,
            "pH neutro": dic_neutro,
            #"pH ácido": dic_acido
        })

        df_ori_neu["Diferente"] = df_ori_neu["Original"] != df_ori_neu["pH neutro"]

        #df = df_ori_neu.transpose()
        df_ori_neu.to_excel("compracao_neutro_original.xlsx", index_label="resideuo", engine='openpyxl')

        print(df_ori_neu)
    
    case 2:
        df_ori_aci = pd.DataFrame({
            "Original": dic_original,
            #"pH neutro": dic_neutro,
            "pH ácido": dic_acido
        })

        df_ori_aci["Diferente"] = df_ori_aci["Original"] != df_ori_aci["pH ácido"]

        #df = df_ori_neu.transpose()
        df_ori_aci.to_excel("compracao_acido_original.xlsx", index_label="resideuo", engine='openpyxl')

        print(df_ori_aci)
    
    case 3: 
        df_neu_aci = pd.DataFrame({
            #"Original": dic_original,
            "pH neutro": dic_neutro,
            "pH ácido": dic_acido
        })

        df_neu_aci["Diferente"] = df_neu_aci["pH neutro"] != df_neu_aci["pH ácido"]

        #df = df_ori_neu.transpose()
        df_neu_aci.to_excel("compracao_neutro_acido.xlsx", index_label="resideuo", engine='openpyxl')

        print(df_neu_aci)