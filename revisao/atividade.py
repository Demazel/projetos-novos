import pandas as pd
 
# =========================
# DataFrame de Funcionários
# =========================
funcionarios = pd.DataFrame({
    "id_funcionario": [1, 2, 3, 4, 5, 6],
    "nome_funcionario": ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda"],
    "departamento_id": [10, 20, 10, 30, 20, 10],
    "cidade": ["São Paulo", "Rio de Janeiro", "São Paulo", "Curitiba", "Rio de Janeiro", "São Paulo"]
})
 
# =========================
# DataFrame de Departamentos
# =========================
departamentos = pd.DataFrame({
    "departamento_id": [10, 20, 30],
    "nome_departamento": ["Vendas", "Marketing", "TI"]
})
 
# =========================
# DataFrame de Vendas
# =========================
vendas = pd.DataFrame({
    "id_venda": [101, 102, 103, 104, 105, 106, 107, 108],
    "id_funcionario": [1, 2, 1, 3, 4, 5, 6, 1],
    "valor_venda": [500, 300, 700, 200, 900, 400, 650, 800],
    "mes": ["Jan", "Jan", "Fev", "Fev", "Mar", "Mar", "Fev", "Mar"]
})





funcionariosDepartamento = pd.merge(funcionarios, departamentos, on="departamento_id")
funcionariosDepartamentosVendas = pd.merge(funcionariosDepartamento, vendas, on="id_funcionario")

print("\nJunção:")
print(funcionariosDepartamentosVendas)

print("\nVendas em SP:")
print(funcionariosDepartamentosVendas[funcionariosDepartamentosVendas["cidade"] == "São Paulo"])

# filtro com multiplas condições
print("\nMultiplas Condicoes:")
print(funcionariosDepartamentosVendas[
    (funcionariosDepartamentosVendas["cidade"] == "São Paulo") &
    (funcionariosDepartamentosVendas["valor_venda"] > 300)
    ])

# agrupamento simples
# vendas x cidade

print(funcionariosDepartamentosVendas.groupby("cidade")["valor_venda"].sum())

# venda x cidade - soma - media - contagem
# agrupamento de argumentos
print(funcionariosDepartamentosVendas.groupby("cidade").agg(
    {"valor_venda":["sum","mean","count","min","max"]}
))