# Classe para representar os estados do problema da travessia da familia do rio
from member import Membro, Adulto


class State:
    def __init__(self) -> None:
        self.left = [Adulto.PAI, Adulto.MAE,
                     Membro.FILHO, Membro.FILHO, Membro.BARCO]
        self.right = [0, 0, 0, 0, 0]

    def __str__(self) -> str:
        return f'Left: {self.left}\nRight: {self.right}'

    def apply_rule(self, rule) -> 'State':
        if rule.is_valid(self):
            new_state = State()
            new_state.left = self.left[:]
            new_state.right = self.right[:]
            rule.apply(new_state)
            return new_state
        return None

    def is_complete(self) -> bool:
        return self.left == [0, 0, 0, 0, 0] & self.right == [Adulto.PAI, Adulto.MAE, Membro.FILHO, Membro.FILHO, Membro.BARCO]
