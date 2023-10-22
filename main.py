from rule import Rule
from state import State
from member import Membro


def backtracking():
    pass


def main():
    rule = Rule(0, Membro.FILHO, Membro.MAE)
    state = State()

    print(state)
    print()
    print(state.apply_rule(rule))

    rule2 = Rule(1, Membro.FILHO)
    print()
    print(state.apply_rule(rule2))


if __name__ == "__main__":
    main()
