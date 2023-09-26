from state import State, Membro, Adulto


class Rule:
    def is_valid(state: State) -> bool:
        # Fazer as verificações das regras

        # Não posso mover dois adultos para o outro lado
        if state.left.count(Adulto) == 2:
            return False
