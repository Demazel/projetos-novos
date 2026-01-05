import pandas as pd
# estamos importando a biblioteca pandas no nosso sistema e apelidando ela de pd
# se é a primeira vez que voce usa, devemos usar no terminal o comando: pip install pandas

funcionarios = pd.DataFrame({
    "id_funcionario":[1,2,3,4],
    "nome_funcionario":["Aline","André","Paulo","Luiz"],
    "departamento_id":[100,200,300,400]
})

departamento = pd.DataFrame({
    "departamento_id":[100,200,300,400],
    "nome_departamento":["TI", "RH","Manutenção","Financeiro"]
})

# unir dados
# o comando merge() vai unir tabelas
# ele precisa de tres atributos - tabela principal - tabela com os outros dados - campo referencia
funcionariosDepartamento = pd.merge(funcionarios, departamento, on="departamento_id")
print(funcionariosDepartamento)
# o comando on = "join"

# vamos filtar

print(funcionariosDepartamento[funcionariosDepartamento["nome_departamento"] == "TI"])

