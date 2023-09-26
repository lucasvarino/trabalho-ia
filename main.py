from rule import Rule
from state import State
from member import Membro, Adulto


def main():
    rule = Rule(Membro.FILHO, Adulto.MAE)
    print(rule.is_valid(State()))


if __name__ == "__main__":
    main()
