# Classe para representar os estados do problema da travessia da familia do rio
from member import Membro


class State:
    def __init__(self) -> None:
        self.left = [Membro.PAI, Membro.MAE,
                     Membro.FILHO, Membro.FILHO, Membro.BARCO]
        self.right = []
        self.history = []
        self.previous: State = None
        self.cost = 0  # Adicionando a propriedade para rastrear o custo acumulado

    def imprime(self) -> None:
        print('Está funcionando')

    def __str__(self) -> str:
        return f'Left: {self.left}\nRight: {self.right}'

    def apply_rule(self, rule) -> 'State':
        if rule.is_valid(self) and self._is_valid(rule):
            new_state = State()
            new_state.left = self.left[:]
            new_state.right = self.right[:]
            rule.apply(new_state)
            new_state.left = State.ordenar_membros(new_state.left)
            new_state.right = State.ordenar_membros(new_state.right)
            new_state.history = self.history[:]
            new_state.history.append(self)
            new_state.cost = self.cost + 1  # Incrementa o custo g
            if not new_state.is_antecedent():
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
            a = boat_num <= state_num_left
            b = True
            for membro in rule.boat:
                if membro not in self.left:
                    b = False

            return a and b
        
        cond2 = True
        for membro in rule.boat:
            if membro not in self.right:
                cond2 = False
        return boat_num <= state_num_right and cond2

    def is_valid(self, rule) -> bool:
        return rule.is_valid(self) and self._is_valid(rule)
    
    def is_antecedent(self) -> bool:
        for state in self.history:
            if state.left == self.left and state.right == self.right:
                return True
        return False

    def is_in_history(self, rule, history) -> bool:
        # Check if the current state is in the history list
        newState = State()
        newState.left = self.left[:]
        newState.right = self.right[:]
        newState = newState.apply_rule(rule)
        # print("Historico: ")
        # print(len(self.history))
        for state in history:
            if state.left == newState.left and state.right == newState.right:
                return True
            
    def ordenar_membros(membros):
        # Definir uma função de chave para a ordenação
        def chave_ordenacao(membro):
            # Atribuir um valor numérico a cada tipo de membro
            ordem = {Membro.PAI: 0, Membro.MAE: 1, Membro.FILHO: 2, Membro.BARCO: 3}
            # Usar o valor atribuído como chave de ordenação
            return ordem.get(membro, float('inf'))

        # Ordenar a lista de membros usando a chave de ordenação
        membros_ordenados = sorted(membros, key=chave_ordenacao)

        return membros_ordenados