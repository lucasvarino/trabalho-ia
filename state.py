# Classe para representar os estados do problema da travessia da familia do rio
from member import Membro


class State:
    def __init__(self) -> None:
        self.left = [Membro.PAI, Membro.MAE,
                     Membro.FILHO, Membro.FILHO, Membro.BARCO]
        self.right = []
        self.history = []

    def __str__(self) -> str:
        return f'Left: {self.left}\nRight: {self.right}'

    def apply_rule(self, rule) -> 'State':
        if rule.is_valid(self) and self._is_valid(rule):
            new_state = State()
            new_state.left = self.left[:]
            new_state.right = self.right[:]
            rule.apply(new_state)
            # Substituir o estado atual pelo novo estado
            return new_state
        return None

    def is_complete(self) -> bool:
        return self.left == [] and sum(1 for valor in self.right) == 5

    def _is_valid(self, rule) -> bool:
        # Se a regra tiver duas crianças e o lado do barco tiver uma criança, não é valido
        boat_num = sum(1 for valor in rule.boat if valor in {Membro.FILHO})
        state_num_left = sum(
            1 for valor in self.left if valor in {Membro.FILHO})
        state_num_right = sum(
            1 for valor in self.right if valor in {Membro.FILHO})

        # Verificar se, do lado que o barco estiver, o número é maior
        if Membro.BARCO in self.left:
            return boat_num <= state_num_left
        
        return boat_num <= state_num_right

    def is_valid(self, rule) -> bool:
        return rule.is_valid(self) and self._is_valid(rule)

    def is_in_history(self, rule) -> bool:
        # Check if the current state is in the history list
        newState = State()
        newState.left = self.left[:]
        newState.right = self.right[:]
        # newState.apply_rule(rule)
        # print("Historico: ")
        # print(len(self.history))
        for state in self.history:
            if state.left == newState.left and state.right == newState.right:
                return True

    def tem_mesmo_numero_membros(self, state):
    # Verifica se os arrays left e right têm o mesmo número de membros de cada tipo
        a = self.left.count(Membro.PAI) == state.left.count(Membro.PAI)
        b = self.left.count(Membro.MAE) == state.left.count(Membro.MAE)
        c = self.left.count(Membro.FILHO) == state.left.count(Membro.FILHO)
        d = self.right.count(Membro.PAI) == state.right.count(Membro.PAI)
        e = self.right.count(Membro.MAE) == state.right.count(Membro.MAE)
        f = self.right.count(Membro.FILHO) == state.right.count(Membro.FILHO)

        return (
            a and b and c and d and e and f
        )
    
    def esta_no_historico(self, rule, historico):
        # Verifica se o objeto está no histórico com base na função tem_mesmo_numero_membros
        newState = State()
        newState.left = self.left[:]
        newState.right = self.right[:]
        newState = newState.apply_rule(rule)
        return any(newState.tem_mesmo_numero_membros(state) for state in historico)