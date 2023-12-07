from rule import Rule
from state import State
from member import Membro
from typing import Callable
from heapq import heappop, heappush
import time

rules = [Rule(Membro.FILHO, Membro.FILHO), Rule(Membro.FILHO), Rule(Membro.PAI), Rule(Membro.MAE)]
rules[0].name = 'FF'
rules[1].name = 'F'
rules[2].name = 'P'
rules[3].name = 'M'


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


def dfs(state: State, history=[]):

    if(state.is_complete()):
        return state;

    for i in range(len(rules)):
        if(state.is_valid(rules[i]) and not state.is_in_history(rules[i], history)):
            newState = state.apply_rule(rules[i])
            newHistory = history + [newState];
            result = dfs(newState, newHistory);
            if result is not None:
                return result;

    return None;

def largura():
    abertos = [] # Lista de Estados
    state = State() # Cria Estado inicial
    fracasso = False # Variável de Controle em caso de Falha na busca
    sucesso = False # Variável de Controle em caso de Sucesso na busca
    abertos.append(state) # Insere o estado inicial na fila de abertos
    fechados = [] # Lista de estados já visitados
    while(not (sucesso or fracasso)):
        print(f'Tamanho do ABERTOS: {len(abertos)}')

        if len(abertos) == 0: # Verifica se a fila de abertos está vazia
            fracasso = True # Retorna fracasso por não ter mais estados possíveis
            print('ABERTOS FICOU VAZIO - FRACASSO!')
        else:
            state = abertos.pop(0)
            print(f'State atual: {state}')
            if state.is_complete():
                sucesso = True
                print('STATE ATUAL É SOLUÇÃO - SUCESSO!')
            else:
                for rule in rules:
                    new_state = state.apply_rule(rule)
                    if new_state is not None:
                        abertos.append(new_state)
                        print('ADICIONOU AOS ABERTOS')
                    else:
                        print('NÃO ADICIONOU AO ABERTOS')
                fechados.append(state)
        print('-' * 20)
    if fracasso:
        return None
    else:
        return state


def heuristica(state: State) -> int:
    # Calcula a quantidade de filhos no lado left
    custo = 0

    for membro in state.left:
        if membro == Membro.FILHO:
            custo += 1
        elif membro == Membro.PAI:
            custo += 2

    return custo

def Greedy(state: State, heuristica: Callable[[State], int], history=[]) -> State:
    start_time = time.time()  # Registra o tempo inicial
    custo_total = 0

    abertos = [] # Lista de Estados
    fracasso = False # Variável de Controle em caso de Falha na busca
    sucesso = False # Variável de Controle em caso de Sucesso na busca
    abertos.append(state) # Insere o estado inicial na fila de abertos
    fechados = [] # Lista de estados já visitados


    while (sucesso == False and fracasso == False): # Enquanto não for sucesso ou fracasso (ou seja, enquanto a busca não terminar com

        if len(abertos) == 0: # Verifica se a fila de abertos está vazia
            print('ABERTOS FICOU VAZIO - FRACASSO!')
            fracasso = True # Retorna fracasso por não ter mais estados possíveis
        else:
            # Ordena os estados abertos de acordo com o custo da heurística
            abertos.sort(key=lambda state: heuristica(state))
            state = abertos.pop(0)
            history.append(state)
            custo_total += heuristica(state)
            if state.is_complete():
                sucesso = True
            else:
                for rule in rules:
                    new_state = state.apply_rule(rule)
                    if new_state is not None:
                        abertos.append(new_state)
                        # Check if the new state is not None before assigning the previous state
                        if new_state:
                            new_state.previous = state
                fechados.append(state)

    if fracasso:
        return None
    else:
        end_time = time.time()  # Registra o tempo final
        execution_time = (end_time - start_time) * 1000  # Calcula o tempo de execução em milissegundos
        print(f"Tempo de execução: {execution_time:.2f} ms")
        
        print(f'Custo Total: {custo_total}')
        history.pop(0)
        print(f'Tamanho do histórico: {len(history)}')
        caminho = []
        
        while state is not None:
            caminho.append(state)
            state = state.previous
        
        print(f'Tamanho do caminho-solução: {len(caminho)}')
        print('Caminho-solução:') 

        caminho.reverse()
        for state in caminho:
            print(state)
        return caminho

def pesoTransicao(rule: int) -> int:
    return rule + 1
    
def ordenada(state: State, heuristica: Callable[[State], int], history=[]) -> State:
    start_time = time.time()  # Registra o tempo inicial
    custo_total = 0

    abertos = []  # Lista de Estados
    fracasso = False  # Variável de Controle em caso de Falha na busca
    sucesso = False  # Variável de Controle em caso de Sucesso na busca
    abertos.append((state, 0))  # Insere o estado inicial na fila de abertos com custo inicial 0
    fechados = []  # Lista de estados já visitados
    transicoesPossiveis = []
    custo_acumulado = 0

    debug = 0

    while (sucesso == False and fracasso == False):  # Enquanto não for sucesso ou fracasso (ou seja, enquanto a busca não terminar com
        if len(abertos) == 0:  # Verifica se a fila de abertos está vazia
            print('ABERTOS FICOU VAZIO - FRACASSO!')
            fracasso = True  # Retorna fracasso por não ter mais estados possíveis
        else:
            
            abertos.sort(key=lambda x:x[1])
            history.append(state)
            state, custo = abertos.pop(0)
            
            if(state.is_complete()):
                print("Concluido")
                sucesso = True
            else:
                for i, rule in enumerate(rules):
                    new_state = state.apply_rule(rule)
                    if new_state is not None:
                        abertos.append((new_state, custo + i+1))
                        
                        if new_state:
                            new_state.previous = state
                fechados.append(state)
    if (fracasso):
        return None
    else:
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        print(f"Tempo de execução: {execution_time:.2f} ms")
        print(f'Custo Total: {custo}')
        history.pop(0)
        print(f'Tamanho do histórico: {len(history)}')
        caminho = []
        while state is not None:
            caminho.append(state)
            state = state.previous
        print(f'Tamanho do caminho-solução: {len(caminho)}')
        print('Caminho-solução:')
        caminho.reverse()
        for state in caminho:
            print(state)
        return caminho

def Aestrela(state: State, heuristica: Callable[[State], int], history=[]) -> State:
    start_time = time.time()  # Registra o tempo inicial
    custo_total = 0

    abertos = []  # Lista de Estados
    fracasso = False  # Variável de Controle em caso de Falha na busca
    sucesso = False  # Variável de Controle em caso de Sucesso na busca
    abertos.append(state)  # Insere o estado inicial na fila de abertos
    fechados = []  # Lista de estados já visitados
    it = 0

    while (sucesso == False and fracasso == False):  # Enquanto não for sucesso ou fracasso (ou seja, enquanto a busca não terminar com
        if len(abertos) == 0:  # Verifica se a fila de abertos está vazia
            print('ABERTOS FICOU VAZIO - FRACASSO!')
            fracasso = True  # Retorna fracasso por não ter mais estados possíveis
        else:
            # Ordena os estados abertos de acordo com a função de avaliação f(n) = g(n) + h(n)
            abertos.sort(key=lambda state: heuristica(state) + state.cost)
            state = abertos.pop(0)
            history.append(state)
            custo_total = state.cost
            if state.is_complete():
                sucesso = True
            else:
                for rule in rules:
                    new_state = state.apply_rule(rule)
                    if new_state is not None:
                        abertos.append(new_state)
                        if new_state:
                            new_state.previous = state
                            new_state.cost = state.cost + 1  # Incrementa o custo g
                fechados.append(state)

        it += 1

    if fracasso:
        return None
    else:
        end_time = time.time()  # Registra o tempo final
        execution_time = (end_time - start_time) * 1000  # Calcula o tempo de execução em milissegundos
        print(f"Tempo de execução: {execution_time:.2f} ms")

        print(f'Custo Total: {custo_total}')
        history.pop(0)
        print(f'Tamanho do histórico: {len(history)}')
        caminho = []

        while state is not None:
            caminho.append(state)
            state = state.previous

        print(f'Tamanho do caminho-solução: {len(caminho)}')
        print('Caminho-solução:')

        caminho.reverse()
        for state in caminho:
            print(state)

        return caminho
    
def main():
    state = State()
    history = []
    history.append(state)
    caminho = []
    #backtracking(state, 0, history)
    #state = largura()
    #state = backtracking(state, 0, history)
    #caminho = Greedy(state, heuristica, history)
    #caminho = ordenada(state, heuristica, history)
    caminho = Aestrela(state, heuristica, history)

if __name__ == "__main__":
    main()