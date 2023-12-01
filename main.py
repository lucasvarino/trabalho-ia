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


def heuristic(state: State) -> int:
    # Exemplo de heurística: número de membros no lado direito do rio
    return len(state.right)


def main():
    state = State()
    history = []
    history.append(state)
    # print(state)
    state = backtracking(state, 0, history)

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
    print(state);


if __name__ == "__main__":
    main()
