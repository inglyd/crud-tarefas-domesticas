from crud import *

# Inserir novos membros
inserir_membro('Carlos Silva', 'carlos.silva@familia.com', '1970-07-10', '2024-08-09')
inserir_membro('Maria Silva', 'maria.silva@familia.com', '1975-09-15', '2024-08-09')
inserir_membro('João Silva', 'joao.silva@familia.com', '2005-12-01', '2024-08-09')

# Listar membros
print("Membros:")
membros = listar_membros()
for membro in membros:
    print(membro)

# Atualizar um membro
atualizar_membro(1, 'Carlos da Silva', 'carlos.silva@familia.com', '1970-07-10')
# Listar membros após atualização
print("\nMembros após atualização:")
membros = listar_membros()
for membro in membros:
    print(membro)

# Deletar um membro
deletar_membro(2)

# Listar membros após exclusão
print("\nMembros após exclusão:")
membros = listar_membros()
for membro in membros:
    print(membro)

# Fechar a conexão ao terminar
fechar_conexao()
