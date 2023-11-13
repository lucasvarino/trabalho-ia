from rule import Rule
from state import State
from member import Membro

rules = [Rule(Membro.FILHO, Membro.FILHO), Rule(Membro.FILHO), Rule(Membro.FILHO, Membro.PAI), Rule(Membro.FILHO, Membro.MAE)]


def backtracking(state, i):
    if state.is_complete():
        print(state)
        return True

    if i >= len(rules):
        return False

    if state.is_valid(rules[i]):
        # Caso seja um estado que já aconteceu, não é valido
        if state.is_in_history(rules[i]):
            return backtracking(state, i+1)
        else:
            print(i)
            state.apply_rule(rules[i])

        return backtracking(state, 0)
    else:
        return backtracking(state, i+1)


def main():
    state = State()
    # print("Solving...")
    # backtracking(state, 0)

    print(state.apply_rule(rules[0]))
    # print(state.is_in_history(rules[0]))
    # print(state.is_in_history(rules[0]))
    print(state.apply_rule(rules[1]))
    print(state.apply_rule(rules[2]))
    print(state.apply_rule(rules[1]))
    print(state.apply_rule(rules[3]))

    print()
    print("Histórico final:")
    for i in state.history:
        print(i)
    # print(state.is_complete())
    # print(state);


if __name__ == "__main__":
    main()
