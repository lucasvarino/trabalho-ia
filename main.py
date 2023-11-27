from rule import Rule
from state import State
from member import Membro

rules = [Rule(Membro.FILHO, Membro.FILHO), Rule(Membro.FILHO), Rule(Membro.PAI), Rule(Membro.MAE)]

def backtracking(state: State, i, history=[]):
    if state.is_complete():
        # print(state)
        return state

    if i >= len(rules):
        state = history.pop()
        return backtracking(state, 0, history)

    if state.is_valid(rules[i]):
        # Caso seja um estado que já aconteceu, não é valido
        # Verificar se a quantidade de pais e filhos de cada lado está no historico
        if state.is_in_history(rules[i], history):
            return backtracking(state, i+1, history)
        else:
            newState = state.apply_rule(rules[i])
            history.append(newState)
            return backtracking(newState, 0, history)

    else:
        return backtracking(state, i+1, history)

def largura():
    abertos = [] # Lista de Estados
    state = State() # Cria Estado inicial
    fracasso = False # Variável de Controle em caso de Falha na busca
    sucesso = False # Variável de Controle em caso de Sucesso na busca
    abertos.append(state) # Insere o estado inicial na fila de abertos
    fechados = [] # Lista de estados já visitados

    while(not (sucesso or fracasso)):
        print(f'Tamanho do ABERTOS: {len(abertos)}')

        if len(abertos) == 0: # Verifica se a fila de abertos está vazia
            fracasso = True # Retorna fracasso por não ter mais estados possíveis
            print('ABERTOS FICOU VAZIO - FRACASSO!')
        else:
            state = abertos.pop(0)
            print(f'State atual: {state}')
            if state.is_complete():
                sucesso = True
                print('STATE ATUAL É SOLUÇÃO - SUCESSO!')
            else:
                for rule in rules:
                    new_state = state.apply_rule(rule)
                    if new_state is not None:
                        abertos.append(new_state)
                        print('ADICIONOU AOS ABERTOS')
                    else:
                        print('NÃO ADICIONOU AO ABERTOS')
                fechados.append(state)
        print('-' * 20)
    if fracasso:
        return None
    else:
        return state

def main():
    state = State()
    history = []
    history.append(state)
    # print(state)
    #backtracking(state, 0, history)
    state = largura()
    #state = backtracking(state, 0, history)

    # state = state.apply_rule(rules[0])
    # state = state.apply_rule(rules[1])
    # state = state.apply_rule(rules[2])
    # state = state.apply_rule(rules[1])
    # state = state.apply_rule(rules[0])
    # state = state.apply_rule(rules[1])
    # state = state.apply_rule(rules[3])
    # state = state.apply_rule(rules[1])
    # state = state.apply_rule(rules[0])
    # print(state.is_complete())
    print('AQUI')
    print(state)


if __name__ == "__main__":
    main()
