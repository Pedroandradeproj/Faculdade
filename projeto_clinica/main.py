# PROJETO INTEGRADO - CLÍNICA VIDA+
# SISTEMA COMPLETO DE GESTÃO
# Aluno: [SEU NOME]
# Data: [DATA]

# =============================================
# ESTRUTURAS DE DADOS GLOBAIS
# =============================================

# Banco de dados da clínica
pacientes = []
fila_atendimento = []
consultas = []
medicos = [
    {"nome": "Dr. Carlos Silva", "especialidade": "Clínico Geral", "disponivel": True},
    {"nome": "Dra. Ana Santos", "especialidade": "Cardiologia", "disponivel": True},
    {"nome": "Dr. Pedro Costa", "especialidade": "Ortopedia", "disponivel": False}
]

# =============================================
# FUNÇÃO PRINCIPAL
# =============================================

def main():
    """Sistema principal da Clínica Vida+"""
    
    # Dados de exemplo para teste
    carregar_dados_exemplo()
    
    while True:
        print("\n" + "="*60)
        print("🏥 CLÍNICA VIDA+ - SISTEMA INTEGRADO DE GESTÃO")
        print("="*60)
        print("1. 📋 PASSO 2 - Cadastro e Estatísticas de Pacientes")
        print("2. 🔐 PASSO 3 - Controle de Acesso e Lógica Booleana")
        print("3. 📊 PASSO 3 - Tabelas Verdade Completas")
        print("4. 🎯 PASSO 4 - Fila de Atendimento (FIFO)")
        print("5. 👥 PASSO 5 - Gestão de Consultas e Médicos")
        print("6. 📈 RELATÓRIO COMPLETO DO SISTEMA")
        print("7. ❌ SAIR")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            passo_2_sistema_pacientes()
        elif opcao == "2":
            passo_3_controle_acesso()
        elif opcao == "3":
            passo_3_tabelas_verdade()
        elif opcao == "4":
            passo_4_fila_atendimento()
        elif opcao == "5":
            passo_5_gestao_consultas()
        elif opcao == "6":
            relatorio_completo()
        elif opcao == "7":
            print("\n✅ Sistema encerrado. Dados salvos!")
            break
        else:
            print("❌ Opção inválida!")

# =============================================
# PASSO 2 - SISTEMA DE PACIENTES
# =============================================

def passo_2_sistema_pacientes():
    """Sistema completo de cadastro e estatísticas de pacientes"""
    
    while True:
        print("\n" + "="*50)
        print("📋 PASSO 2 - SISTEMA DE PACIENTES")
        print("="*50)
        print("1. 👤 Cadastrar novo paciente")
        print("2. 📊 Ver estatísticas completas")
        print("3. 🔍 Buscar paciente por nome")
        print("4. 📄 Listar todos os pacientes")
        print("5. 📝 Cadastrar pacientes de exemplo")
        print("6. ↩️ Voltar ao menu principal")
        
        opcao = input("\nEscolha: ")
        
        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            mostrar_estatisticas()
        elif opcao == "3":
            buscar_paciente()
        elif opcao == "4":
            listar_pacientes()
        elif opcao == "5":
            cadastrar_pacientes_exemplo()
        elif opcao == "6":
            break
        else:
            print("❌ Opção inválida!")

def cadastrar_paciente():
    """Cadastra um novo paciente"""
    print("\n--- CADASTRO DE PACIENTE ---")
    
    try:
        nome = input("Nome completo: ").strip()
        if not nome:
            print("❌ Nome é obrigatório!")
            return
            
        idade = int(input("Idade: "))
        if idade <= 0 or idade > 150:
            print("❌ Idade deve ser entre 1 e 150 anos!")
            return
            
        telefone = input("Telefone: ").strip()
        cpf = input("CPF: ").strip()
        
        paciente = {
            "id": len(pacientes) + 1,
            "nome": nome,
            "idade": idade,
            "telefone": telefone,
            "cpf": cpf,
            "documentos_ok": True,
            "pagamentos_em_dia": True
        }
        
        pacientes.append(paciente)
        print(f"✅ Paciente {nome} cadastrado com sucesso! (ID: {paciente['id']})")
        
    except ValueError:
        print("❌ Erro: Idade deve ser um número!")

def mostrar_estatisticas():
    """Calcula e exibe estatísticas dos pacientes"""
    if not pacientes:
        print("❌ Nenhum paciente cadastrado!")
        return
    
    print("\n--- ESTATÍSTICAS DA CLÍNICA ---")
    
    # Cálculos
    total = len(pacientes)
    idades = [p['idade'] for p in pacientes]
    idade_media = sum(idades) / total
    mais_novo = min(pacientes, key=lambda x: x['idade'])
    mais_velho = max(pacientes, key=lambda x: x['idade'])
    
    # Exibição
    print(f"👥 Total de pacientes: {total}")
    print(f"📊 Idade média: {idade_media:.1f} anos")
    print(f"👶 Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"👴 Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")
    
    # Distribuição por faixa etária
    jovens = len([p for p in pacientes if p['idade'] < 30])
    adultos = len([p for p in pacientes if 30 <= p['idade'] < 60])
    idosos = len([p for p in pacientes if p['idade'] >= 60])
    
    print(f"\n📈 Distribuição por faixa etária:")
    print(f"  Jovens (<30 anos): {jovens} pacientes ({jovens/total*100:.1f}%)")
    print(f"  Adultos (30-59 anos): {adultos} pacientes ({adultos/total*100:.1f}%)")
    print(f"  Idosos (60+ anos): {idosos} pacientes ({idosos/total*100:.1f}%)")

def buscar_paciente():
    """Busca paciente pelo nome"""
    if not pacientes:
        print("❌ Nenhum paciente cadastrado!")
        return
        
    termo = input("\nDigite o nome para buscar: ").lower()
    encontrados = [p for p in pacientes if termo in p['nome'].lower()]
    
    if encontrados:
        print(f"\n🔍 {len(encontrados)} paciente(s) encontrado(s):")
        for paciente in encontrados:
            print(f"  📝 {paciente['nome']} - {paciente['idade']} anos - Tel: {paciente['telefone']}")
    else:
        print("❌ Nenhum paciente encontrado!")

def listar_pacientes():
    """Lista todos os pacientes cadastrados"""
    if not pacientes:
        print("❌ Nenhum paciente cadastrado!")
        return
        
    print("\n--- LISTA COMPLETA DE PACIENTES ---")
    for i, paciente in enumerate(pacientes, 1):
        print(f"{i:2d}. {paciente['nome']:20} | {paciente['idade']:3} anos | {paciente['telefone']:15} | CPF: {paciente['cpf']}")

def cadastrar_pacientes_exemplo():
    """Cadastra pacientes de exemplo para teste"""
    exemplos = [
        {"nome": "João Silva", "idade": 45, "telefone": "(11) 9999-9999", "cpf": "111.222.333-44"},
        {"nome": "Maria Santos", "idade": 32, "telefone": "(11) 8888-8888", "cpf": "222.333.444-55"},
        {"nome": "Pedro Costa", "idade": 67, "telefone": "(11) 7777-7777", "cpf": "333.444.555-66"},
        {"nome": "Ana Oliveira", "idade": 28, "telefone": "(11) 6666-6666", "cpf": "444.555.666-77"},
        {"nome": "Carlos Souza", "idade": 55, "telefone": "(11) 5555-5555", "cpf": "555.666.777-88"}
    ]
    
    for exemplo in exemplos:
        paciente = {
            "id": len(pacientes) + 1,
            **exemplo,
            "documentos_ok": True,
            "pagamentos_em_dia": True
        }
        pacientes.append(paciente)
    
    print(f"✅ {len(exemplos)} pacientes de exemplo cadastrados!")

# =============================================
# PASSO 3 - CONTROLE DE ACESSO (LÓGICA)
# =============================================

def passo_3_controle_acesso():
    """Sistema interativo de controle de acesso"""
    
    while True:
        print("\n" + "="*50)
        print("🔐 PASSO 3 - CONTROLE DE ACESSO")
        print("="*50)
        print("1. 🧠 Expressões Lógicas do Sistema")
        print("2. 🏥 Simular Atendimento (Consulta/Emergência)")
        print("3. 📋 Situação Prática do Enunciado")
        print("4. ↩️ Voltar")
        
        opcao = input("\nEscolha: ")
        
        if opcao == "1":
            mostrar_expressoes_logicas()
        elif opcao == "2":
            simular_atendimento()
        elif opcao == "3":
            situacao_pratica_enunciado()
        elif opcao == "4":
            break
        else:
            print("❌ Opção inválida!")

def consulta_normal(A, B, C, D):
    """Lógica para consulta normal: (A ∧ B ∧ C) ∨ (B ∧ C ∧ D)"""
    return (A and B and C) or (B and C and D)

def emergencia(A, B, C, D):
    """Lógica para emergência: C ∧ (B ∨ D)"""
    return C and (B or D)

def mostrar_expressoes_logicas():
    """Explica as expressões lógicas do sistema"""
    print("\n--- EXPRESSÕES LÓGICAS DO SISTEMA ---")
    print("\nVariáveis booleanas:")
    print("A = Tem agendamento marcado")
    print("B = Documentos em dia (RG/CPF válidos)")
    print("C = Médico disponível no horário")
    print("D = Pagamentos anteriores em dia")
    
    print("\n🔹 CONSULTA NORMAL:")
    print("(A ∧ B ∧ C) ∨ (B ∧ C ∧ D)")
    print("Em Python: (A and B and C) or (B and C and D)")
    
    print("\n🔹 EMERGÊNCIA:")
    print("C ∧ (B ∨ D)")
    print("Em Python: C and (B or D)")
    
    print("\n📖 Regras de negócio:")
    print("Consulta Normal: Agenda + Docs + Médico OU Docs + Médico + Pagamentos")
    print("Emergência: Médico + (Docs OU Pagamentos)")

def simular_atendimento():
    """Simula o controle de acesso para um paciente"""
    print("\n--- SIMULAÇÃO DE ATENDIMENTO ---")
    
    print("\n🎯 Condições do paciente:")
    A = input("Tem agendamento? (s/n): ").lower() == 's'
    B = input("Documentos em dia? (s/n): ").lower() == 's'
    C = input("Médico disponível? (s/n): ").lower() == 's'
    D = input("Pagamentos em dia? (s/n): ").lower() == 's'
    
    print("\n📋 Condições informadas:")
    print(f"Agendamento: {'✅ SIM' if A else '❌ NÃO'}")
    print(f"Documentos: {'✅ OK' if B else '❌ PENDENTE'}")
    print(f"Médico: {'✅ DISPONÍVEL' if C else '❌ INDISPONÍVEL'}")
    print(f"Pagamentos: {'✅ EM DIA' if D else '❌ ATRASADOS'}")
    
    # Cálculos
    resultado_normal = consulta_normal(A, B, C, D)
    resultado_emergencia = emergencia(A, B, C, D)
    
    print("\n🎯 RESULTADOS:")
    print(f"CONSULTA NORMAL: {'✅ ATENDIDO' if resultado_normal else '❌ NÃO ATENDIDO'}")
    print(f"EMERGÊNCIA: {'✅ ATENDIDO' if resultado_emergencia else '❌ NÃO ATENDIDO'}")
    
    # Explicação detalhada
    print("\n🧠 CÁLCULO DETALHADO:")
    if resultado_normal:
        if A and B and C:
            print("Consulta Normal: Atendido por ter AGENDAMENTO + DOCUMENTOS + MÉDICO")
        else:
            print("Consulta Normal: Atendido por ter DOCUMENTOS + MÉDICO + PAGAMENTOS")
    else:
        print("Consulta Normal: Não atendido - não cumpre os requisitos mínimos")
    
    if resultado_emergencia:
        print("Emergência: Atendido por ter MÉDICO + (DOCUMENTOS OU PAGAMENTOS)")
    else:
        print("Emergência: Não atendido - médico indisponível ou sem docs/pagamentos")

def situacao_pratica_enunciado():
    """Resolve a situação prática específica do enunciado"""
    print("\n--- SITUAÇÃO PRÁTICA DO ENUNCIADO ---")
    print("Condições do paciente:")
    print("A = F (Sem agendamento)")
    print("B = V (Documentos OK)")
    print("C = V (Médico disponível)")
    print("D = F (Pagamentos atrasados)")
    
    A, B, C, D = False, True, True, False
    
    # Cálculos detalhados
    parte1 = A and B and C  # F ∧ V ∧ V = F
    parte2 = B and C and D  # V ∧ V ∧ F = F
    resultado_normal = parte1 or parte2  # F ∨ F = F
    
    parte_emerg = B or D  # V ∨ F = V
    resultado_emergencia = C and parte_emerg  # V ∧ V = V
    
    print("\n🧮 CÁLCULO PASSO A PASSO:")
    print(f"Consulta Normal: (F ∧ V ∧ V) ∨ (V ∧ V ∧ F) = F ∨ F = {resultado_normal}")
    print(f"Emergência: V ∧ (V ∨ F) = V ∧ V = {resultado_emergencia}")
    
    print("\n🎯 RESULTADO FINAL:")
    print(f"Consulta Normal: {'✅ ATENDIDO' if resultado_normal else '❌ NÃO ATENDIDO'}")
    print(f"Emergência: {'✅ ATENDIDO' if resultado_emergencia else '❌ NÃO ATENDIDO'}")

# =============================================
# PASSO 3 - TABELAS VERDADE COMPLETAS
# =============================================

def passo_3_tabelas_verdade():
    """Gera as tabelas verdade completas"""
    
    print("\n" + "="*50)
    print("📊 PASSO 3 - TABELAS VERDADE COMPLETAS")
    print("="*50)
    
    print("🔹 Gerando tabela verdade para CONSULTA NORMAL...")
    tabela_normal = gerar_tabela_verdade(consulta_normal)
    exibir_tabela(tabela_normal, "CONSULTA NORMAL")
    
    print("\n" + "="*50)
    print("🔹 Gerando tabela verdade para EMERGÊNCIA...")
    tabela_emergencia = gerar_tabela_verdade(emergencia)
    exibir_tabela(tabela_emergencia, "EMERGÊNCIA")
    
    # Análise comparativa
    analisar_tabelas(tabela_normal, tabela_emergencia)

def gerar_tabela_verdade(funcao_logica):
    """Gera tabela verdade para uma função lógica"""
    tabela = []
    
    for A in [False, True]:
        for B in [False, True]:
            for C in [False, True]:
                for D in [False, True]:
                    resultado = funcao_logica(A, B, C, D)
                    tabela.append({
                        'A': A, 'B': B, 'C': C, 'D': D,
                        'resultado': resultado
                    })
    
    return tabela

def exibir_tabela(tabela, titulo):
    """Exibe uma tabela verdade formatada"""
    print(f"\n--- TABELA VERDADE - {titulo} ---")
    print(" A | B | C | D | Resultado")
    print("-" * 25)
    
    count_true = 0
    for linha in tabela:
        a = 'V' if linha['A'] else 'F'
        b = 'V' if linha['B'] else 'F'
        c = 'V' if linha['C'] else 'F'
        d = 'V' if linha['D'] else 'F'
        res = 'V' if linha['resultado'] else 'F'
        
        print(f" {a} | {b} | {c} | {d} |     {res}")
        
        if linha['resultado']:
            count_true += 1
    
    print(f"\n📈 Total de situações 'V' (atendido): {count_true}/16")
    return count_true

def analisar_tabelas(tabela_normal, tabela_emergencia):
    """Faz análise comparativa das tabelas"""
    print("\n--- ANÁLISE COMPARATIVA DAS TABELAS ---")
    
    count_normal = sum(1 for linha in tabela_normal if linha['resultado'])
    count_emergencia = sum(1 for linha in tabela_emergencia if linha['resultado'])
    
    # Situações onde ambos são verdadeiros
    count_ambos = 0
    for i in range(16):
        if tabela_normal[i]['resultado'] and tabela_emergencia[i]['resultado']:
            count_ambos += 1
    
    print(f"🔸 Consulta Normal: {count_normal}/16 situações de atendimento")
    print(f"🔸 Emergência: {count_emergencia}/16 situações de atendimento")
    print(f"🔸 Ambas modalidades: {count_ambos}/16 situações")
    print(f"🔸 Apenas Emergência: {count_emergencia - count_ambos}/16 situações")
    print(f"🔸 Apenas Consulta Normal: {count_normal - count_ambos}/16 situações")
    
    print("\n💡 CONCLUSÃO: O sistema de emergência é mais permissivo,")
    print("permitindo atendimento em mais situações que a consulta normal.")

# =============================================
# PASSO 4 - FILA DE ATENDIMENTO (FIFO)
# =============================================

def passo_4_fila_atendimento():
    """Implementa o sistema de fila FIFO"""
    
    print("\n" + "="*50)
    print("🎯 PASSO 4 - FILA DE ATENDIMENTO (FIFO)")
    print("="*50)
    
    # Pseudocódigo explicativo
    print("📝 PSEUDOCÓDIGO IMPLEMENTADO:")
    print("1. INICIAR fila vazia")
    print("2. PARA i = 1 ATÉ 3 FAÇA")
    print("3.   LER nome e CPF do paciente")
    print("4.   INSERIR no FINAL da fila (append)")
    print("5. FIM PARA")
    print("6. REMOVER primeiro paciente (pop(0))")
    print("7. EXIBIR paciente atendido")
    print("8. EXIBIR fila restante")
    
    # Implementação prática
    print("\n--- IMPLEMENTAÇÃO PRÁTICA ---")
    
    fila_local = []  # Fila para esta execução
    
    # 1. Inserir 3 pacientes na fila
    print("\n📥 ADICIONANDO PACIENTES NA FILA:")
    for i in range(3):
        print(f"\nPaciente {i+1}:")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        
        paciente = {"nome": nome, "cpf": cpf, "posicao": i+1}
        fila_local.append(paciente)
        print(f"✅ {nome} adicionado à posição {i+1} da fila")
    
    # Mostrar fila completa
    print(f"\n--- FILA COMPLETA ({len(fila_local)} pacientes) ---")
    for i, paciente in enumerate(fila_local):
        print(f"{i+1}º 🧍 {paciente['nome']} - CPF: {paciente['cpf']}")
    
    # 2. Atender primeiro paciente (FIFO)
    if fila_local:
        print("\n🔔 CHAMANDO PRÓXIMO PACIENTE...")
        paciente_atendido = fila_local.pop(0)  # Remove o primeiro
        print(f"🎯 EM ATENDIMENTO: {paciente_atendido['nome']} - CPF: {paciente_atendido['cpf']}")
        
        # 3. Mostrar fila atualizada
        print(f"\n--- FILA ATUALIZADA ({len(fila_local)} pacientes aguardando) ---")
        if fila_local:
            for i, paciente in enumerate(fila_local):
                print(f"{i+1}º 🕒 {paciente['nome']} - CPF: {paciente['cpf']}")
        else:
            print("📭 Fila vazia! Todos os pacientes foram atendidos.")
    else:
        print("❌ Fila vazia! Nenhum paciente para atender.")

# =============================================
# PASSO 5 - GESTÃO DE CONSULTAS (CASOS DE USO)
# =============================================

def passo_5_gestao_consultas():
    """Sistema de gestão de consultas (casos de uso)"""
    
    while True:
        print("\n" + "="*50)
        print("👥 PASSO 5 - GESTÃO DE CONSULTAS E MÉDICOS")
        print("="*50)
        print("1. 🏥 Visualizar casos de uso do sistema")
        print("2. 👨‍⚕️ Listar médicos disponíveis")
        print("3. 📅 Agendar nova consulta")
        print("4. ✅ Confirmar consulta agendada")
        print("5. ❌ Cancelar consulta (Secretária/Médico)")
        print("6. 💊 Simular geração de receita")
        print("7. ↩️ Voltar")
        
        opcao = input("\nEscolha: ")
        
        if opcao == "1":
            mostrar_casos_uso()
        elif opcao == "2":
            listar_medicos()
        elif opcao == "3":
            agendar_consulta()
        elif opcao == "4":
            confirmar_consulta()
        elif opcao == "5":
            cancelar_consulta()
        elif opcao == "6":
            gerar_receita()
        elif opcao == "7":
            break
        else:
            print("❌ Opção inválida!")

def mostrar_casos_uso():
    """Exibe o diagrama de casos de uso textual"""
    print("\n--- DIAGRAMA DE CASOS DE USO - CLÍNICA VIDA+ ---")
    print("\n🎭 ATORES PRINCIPAIS:")
    print("👤 SECRETÁRIA - Responsável pelo agendamento e cadastro")
    print("👨‍⚕️ MÉDICO - Realiza atendimentos e procedimentos")
    print("👤 PACIENTE - Usuário final do sistema (indireto)")
    
    print("\n📋 CASOS DE USO PRINCIPAIS:")
    print("\n🔹 SECRETÁRIA:")
    print("   • Cadastrar Paciente <<include>> em Agendar/Confirmar")
    print("   • Agendar Consulta")
    print("   • Confirmar Consulta") 
    print("   • Cancelar Consulta")
    
    print("\n🔹 MÉDICO:")
    print("   • Cancelar Consulta <<extend>> da Secretária")
    print("   • Gerar Receita <<include>> Imprimir Receita")
    print("   • Registrar Atendimento")
    
    print("\n🔹 SISTEMA (automático):")
    print("   • Imprimir Receita (automático ao gerar)")
    
    print("\n🔄 RELACIONAMENTOS:")
    print("<<include>>: Uma funcionalidade INCLUI outra obrigatoriamente")
    print("<<extend>>: Uma funcionalidade ESTENDE outra opcionalmente")

def listar_medicos():
    """Lista os médicos cadastrados"""
    print("\n--- CORPO MÉDICO DA CLÍNICA ---")
    for i, medico in enumerate(medicos, 1):
        status = "✅ DISPONÍVEL" if medico['disponivel'] else "❌ INDISPONÍVEL"
        print(f"{i}. {medico['nome']} - {medico['especialidade']} - {status}")

def agendar_consulta():
    """Simula o agendamento de consulta"""
    if not pacientes:
        print("❌ Cadastre pacientes primeiro!")
        return
        
    print("\n--- AGENDAMENTO DE CONSULTA ---")
    
    # Selecionar paciente
    print("Pacientes cadastrados:")
    for i, paciente in enumerate(pacientes, 1):
        print(f"{i}. {paciente['nome']}")
    
    try:
        idx_paciente = int(input("Número do paciente: ")) - 1
        paciente = pacientes[idx_paciente]
        
        # Selecionar médico
        listar_medicos()
        idx_medico = int(input("Número do médico: ")) - 1
        medico = medicos[idx_medico]
        
        if not medico['disponivel']:
            print("❌ Médico indisponível!")
            return
            
        data = input("Data da consulta (DD/MM/AAAA): ")
        horario = input("Horário (HH:MM): ")
        
        consulta = {
            "id": len(consultas) + 1,
            "paciente": paciente['nome'],
            "medico": medico['nome'],
            "data": data,
            "horario": horario,
            "confirmada": False,
            "realizada": False
        }
        
        consultas.append(consulta)
        print(f"✅ Consulta agendada para {paciente['nome']} com {medico['nome']}")
        
    except (ValueError, IndexError):
        print("❌ Seleção inválida!")

# ... (continua com outras funções do Passo 5)
def confirmar_consulta():
    """Confirma uma consulta agendada - Caso de uso da Secretária"""
    if not consultas:
        print("❌ Nenhuma consulta agendada!")
        return
    
    print("\n--- CONFIRMAÇÃO DE CONSULTA ---")
    
    # Mostrar consultas não confirmadas
    consultas_nao_confirmadas = [c for c in consultas if not c['confirmada']]
    
    if not consultas_nao_confirmadas:
        print("✅ Todas as consultas já estão confirmadas!")
        return
    
    print("Consultas pendentes de confirmação:")
    for i, consulta in enumerate(consultas_nao_confirmadas, 1):
        print(f"{i}. {consulta['paciente']} com {consulta['medico']} - {consulta['data']} {consulta['horario']}")
    
    try:
        idx = int(input("Número da consulta a confirmar: ")) - 1
        if 0 <= idx < len(consultas_nao_confirmadas):
            consulta = consultas_nao_confirmadas[idx]
            consulta['confirmada'] = True
            print(f"✅ Consulta de {consulta['paciente']} confirmada com sucesso!")
        else:
            print("❌ Número inválido!")
    except ValueError:
        print("❌ Digite um número válido!")

def cancelar_consulta():
    """Cancela uma consulta - Caso de uso da Secretária (extendido para Médico)"""
    if not consultas:
        print("❌ Nenhuma consulta agendada!")
        return
    
    print("\n--- CANCELAMENTO DE CONSULTA ---")
    
    # Identificar o tipo de usuário
    print("Quem está cancelando a consulta?")
    print("1. Secretária")
    print("2. Médico")
    
    try:
        tipo_usuario = int(input("Opção: "))
        if tipo_usuario not in [1, 2]:
            print("❌ Opção inválida!")
            return
    except ValueError:
        print("❌ Digite um número válido!")
        return
    
    # Listar consultas
    print("\nConsultas agendadas:")
    for i, consulta in enumerate(consultas, 1):
        status = "✅ CONFIRMADA" if consulta['confirmada'] else "🕒 PENDENTE"
        print(f"{i}. {consulta['paciente']} com {consulta['medico']} - {consulta['data']} {consulta['horario']} - {status}")
    
    try:
        idx = int(input("Número da consulta a cancelar: ")) - 1
        if 0 <= idx < len(consultas):
            consulta = consultas[idx]
            
            if tipo_usuario == 1:  # Secretária
                motivo = input("Motivo do cancelamento: ")
                print(f"✅ Consulta cancelada pela secretária. Motivo: {motivo}")
            else:  # Médico
                print("👨‍⚕️ Médico logado: Dr. Carlos Silva")
                motivo = input("Motivo médico do cancelamento: ")
                print(f"✅ Consulta cancelada pelo médico. Motivo: {motivo}")
            
            # Remover consulta da lista
            consulta_cancelada = consultas.pop(idx)
            print(f"❌ Consulta de {consulta_cancelada['paciente']} cancelada!")
        else:
            print("❌ Número inválido!")
    except ValueError:
        print("❌ Digite um número válido!")

def gerar_receita():
    """Gera uma receita médica - Caso de uso do Médico"""
    if not consultas:
        print("❌ Nenhuma consulta realizada!")
        return
    
    print("\n--- GERAÇÃO DE RECEITA MÉDICA ---")
    
    # Consultas confirmadas (consideradas como realizadas)
    consultas_realizadas = [c for c in consultas if c['confirmada'] and not c.get('receita_gerada', False)]
    
    if not consultas_realizadas:
        print("❌ Nenhuma consulta disponível para gerar receita!")
        return
    
    print("Consultas realizadas (para gerar receita):")
    for i, consulta in enumerate(consultas_realizadas, 1):
        print(f"{i}. Paciente: {consulta['paciente']} - Médico: {consulta['medico']}")
    
    try:
        idx = int(input("Número da consulta: ")) - 1
        if 0 <= idx < len(consultas_realizadas):
            consulta = consultas_realizadas[idx]
            
            # Coletar dados da receita
            print(f"\n📝 Gerando receita para: {consulta['paciente']}")
            medicamento = input("Medicamento prescrito: ")
            dosagem = input("Dosagem: ")
            periodo = input("Período de tratamento: ")
            observacoes = input("Observações: ")
            
            # Gerar receita
            receita = {
                "id": len([r for r in consultas if r.get('receita_gerada', False)]) + 1,
                "paciente": consulta['paciente'],
                "medico": consulta['medico'],
                "data": consulta['data'],
                "medicamento": medicamento,
                "dosagem": dosagem,
                "periodo": periodo,
                "observacoes": observacoes
            }
            
            # Marcar consulta como tendo receita gerada
            consulta['receita_gerada'] = True
            consulta['receita'] = receita
            
            # <<include>> Imprimir Receita (automático)
            imprimir_receita(receita)
            
            print(f"✅ Receita gerada e impressa para {consulta['paciente']}!")
        else:
            print("❌ Número inválido!")
    except ValueError:
        print("❌ Digite um número válido!")

def imprimir_receita(receita):
    """Função incluída automaticamente na geração de receita"""
    print("\n" + "="*50)
    print("💊 RECEITA MÉDICA - CLÍNICA VIDA+")
    print("="*50)
    print(f"Paciente: {receita['paciente']}")
    print(f"Médico: {receita['medico']}")
    print(f"Data: {receita['data']}")
    print(f"Medicamento: {receita['medicamento']}")
    print(f"Dosagem: {receita['dosagem']}")
    print(f"Período: {receita['periodo']}")
    print(f"Observações: {receita['observacoes']}")
    print("="*50)
    print("Assinatura do Médico: ___________________")
    print("CRM: ________/________")
    print("\n")

def listar_consultas():
    """Lista todas as consultas do sistema"""
    if not consultas:
        print("❌ Nenhuma consulta agendada!")
        return
    
    print("\n--- LISTA DE CONSULTAS ---")
    for i, consulta in enumerate(consultas, 1):
        status = "✅ CONFIRMADA" if consulta['confirmada'] else "🕒 PENDENTE"
        receita = "💊 COM RECEITA" if consulta.get('receita_gerada', False) else "📄 SEM RECEITA"
        print(f"{i}. {consulta['paciente']}")
        print(f"   Médico: {consulta['medico']}")
        print(f"   Data: {consulta['data']} {consulta['horario']}")
        print(f"   Status: {status} | {receita}")
        print()

def mostrar_casos_uso():
    """Exibe o diagrama de casos de uso textual"""
    print("\n--- DIAGRAMA DE CASOS DE USO - CLÍNICA VIDA+ ---")
    print("\n🎭 ATORES PRINCIPAIS:")
    print("👤 SECRETÁRIA - Responsável pelo agendamento e cadastro")
    print("👨‍⚕️ MÉDICO - Realiza atendimentos e procedimentos")
    print("👤 PACIENTE - Usuário final do sistema (indireto)")
    
    print("\n📋 CASOS DE USO PRINCIPAIS:")
    print("\n🔹 SECRETÁRIA:")
    print("   • Cadastrar Paciente <<include>> em Agendar/Confirmar")
    print("   • Agendar Consulta")
    print("   • Confirmar Consulta") 
    print("   • Cancelar Consulta")
    
    print("\n🔹 MÉDICO:")
    print("   • Cancelar Consulta <<extend>> da Secretária")
    print("   • Gerar Receita <<include>> Imprimir Receita")
    print("   • Registrar Atendimento")
    
    print("\n🔹 SISTEMA (automático):")
    print("   • Imprimir Receita (automático ao gerar)")
    
    print("\n🔄 RELACIONAMENTOS:")
    print("<<include>>: Uma funcionalidade INCLUI outra obrigatoriamente")
    print("<<extend>>: Uma funcionalidade ESTENDE outra opcionalmente")
    
    print("\n💡 EXEMPLO PRÁTICO:")
    print("Quando o médico GERA RECEITA, o sistema automaticamente IMPRIME RECEITA")
    print("Quando a secretária CANCELA CONSULTA, o médico pode estender esta função")

# ... (as outras funções permanecem iguais)

def agendar_consulta():
    """Simula o agendamento de consulta - Caso de uso da Secretária"""
    if not pacientes:
        print("❌ Cadastre pacientes primeiro!")
        return
        
    print("\n--- AGENDAMENTO DE CONSULTA ---")
    
    # Verificar se há paciente cadastrado (<<include>> implícito)
    print("Pacientes cadastrados:")
    for i, paciente in enumerate(pacientes, 1):
        print(f"{i}. {paciente['nome']}")
    
    try:
        idx_paciente = int(input("Número do paciente: ")) - 1
        paciente = pacientes[idx_paciente]
        
        # Selecionar médico
        listar_medicos()
        idx_medico = int(input("Número do médico: ")) - 1
        medico = medicos[idx_medico]
        
        if not medico['disponivel']:
            print("❌ Médico indisponível!")
            return
            
        data = input("Data da consulta (DD/MM/AAAA): ")
        horario = input("Horário (HH:MM): ")
        
        consulta = {
            "id": len(consultas) + 1,
            "paciente": paciente['nome'],
            "medico": medico['nome'],
            "data": data,
            "horario": horario,
            "confirmada": False,
            "realizada": False,
            "receita_gerada": False
        }
        
        consultas.append(consulta)
        print(f"✅ Consulta agendada para {paciente['nome']} com {medico['nome']}")
        print("🕒 Status: Aguardando confirmação")
        
    except (ValueError, IndexError):
        print("❌ Seleção inválida!")
# =============================================
# FUNÇÕES AUXILIARES
# =============================================

def carregar_dados_exemplo():
    """Carrega dados de exemplo para demonstração"""
    if not pacientes:
        cadastrar_pacientes_exemplo()

def relatorio_completo():
    """Gera relatório completo do sistema"""
    print("\n" + "="*60)
    print("📈 RELATÓRIO COMPLETO - CLÍNICA VIDA+")
    print("="*60)
    
    print(f"\n👥 PACIENTES CADASTRADOS: {len(pacientes)}")
    print(f"📅 CONSULTAS AGENDADAS: {len(consultas)}")
    print(f"👨‍⚕️ MÉDICOS CADASTRADOS: {len(medicos)}")
    print(f"🎯 MÉDICOS DISPONÍVEIS: {sum(1 for m in medicos if m['disponivel'])}")
    
    if pacientes:
        idades = [p['idade'] for p in pacientes]
        print(f"📊 IDADE MÉDIA: {sum(idades)/len(idades):.1f} anos")
    
    print("\n✅ SISTEMA OPERACIONAL - TODOS OS MÓDULOS INTEGRADOS")
    print("🎓 PROJETO INTEGRADO CONCLUÍDO COM SUCESSO!")

# =============================================
# EXECUÇÃO DO PROGRAMA
# =============================================

if __name__ == "__main__":
    print("🚀 INICIANDO SISTEMA CLÍNICA VIDA+")
    print("📚 PROJETO INTEGRADO - ANÁLISE E DESENVOLVIMENTO DE SISTEMAS")
    main()