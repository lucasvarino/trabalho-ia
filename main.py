from rule import Rule
from state import State
from member import Membro

rules = [Rule(Membro.FILHO, Membro.FILHO), Rule(Membro.FILHO), Rule(Membro.FILHO, Membro.PAI), Rule(Membro.FILHO, Membro.MAE)]

def backtracking(state: State, i, history=[], historico2=[]):
    if state.is_complete():
        # print(state)
        return True

    if i >= len(rules):
        return False

    if state.is_valid(rules[i]):
        # Caso seja um estado que já aconteceu, não é valido
        # Verificar se a quantidade de pais e filhos de cada lado está no historico
        if state.esta_no_historico(rules[i], history):
            return backtracking(state, i+1, history)
        else:
            history.append(state)
            newState = state.apply_rule(rules[i])
            historico2.append(i)
            history.append(newState)
            return backtracking(newState, 0, history)

    else:
        return backtracking(state, i+1, history)



def main():
    state = State()
    history = []
    # print(state)
    backtracking(state, 0, history, [])

    # state = state.apply_rule(rules[0])
    # print(state.is_in_history(rules[0]))
    # print(state.is_complete())
    print(state);


if __name__ == "__main__":
    main()
