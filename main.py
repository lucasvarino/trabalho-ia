from rule import Rule
from state import State
from member import Membro

rules = [Rule(Membro.FILHO, Membro.FILHO), Rule(Membro.FILHO), Rule(Membro.FILHO, Membro.PAI), Rule(Membro.FILHO, Membro.MAE)]

def backtracking(state: State, i, history=[]):
    if state.is_complete():
        # print(state)
        return True

    if i >= len(rules):
        return False

    if state.is_valid(rules[i]):
        # Caso seja um estado que já aconteceu, não é valido
        # Verificar se a quantidade de pais e filhos de cada lado está no historico
        if state.is_in_history(rules[i], history):
            return backtracking(state, i+1, history)
        else:
            print(i)
            newState = state.apply_rule(rules[i])
            history.append(newState)
            return backtracking(newState, 0, history)

    else:
        return backtracking(state, i+1, history)

def largura():
    abertos = []
    state = State()
    fracasso = False
    sucesso = False
    abertos.append(state)
    print(f'{abertos=}\n')
    fechados = []

    while(not(fracasso or sucesso)):
        if len(abertos) == 0:
            fracasso = True
            print(f'{fracasso=}\n')
        else:
            n = abertos[0]
            print(f'{n=}\n')
            abertos.pop(0)
            if n.is_complete():
                sucesso = True
                print(f'{sucesso=}\n')
            else:
                for rule in rules:
                    #print('For das regras')
                    new_state = state.apply_rule(rule)     
                    if new_state is not None and not state.is_in_history(rule,fechados):
                        print('Entrou no IF new_state')
                        abertos.append(new_state)
                        print(f'{abertos=}\n')
                fechados.append(n)
        print(new_state)
    
    if sucesso:
        return n
    else:
        return None

def main():
    state = State()
    history = []
    history.append(state)
    # print(state)
    #backtracking(state, 0, history)
    state = largura()

    # state = state.apply_rule(rules[0])
    # state = state.apply_rule(rules[1])
    # state = state.apply_rule(rules[2])
    # state = state.apply_rule(rules[1])
    # state = state.apply_rule(rules[3])
    # print(state.is_complete())
    print(state)


if __name__ == "__main__":
    main()
