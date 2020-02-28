from argparse import ArgumentParser
import json
import re


def parse_args():
    ap = ArgumentParser()

    ap.add_argument(
        '--documentos',
        type=str,
        required=True,
        help='Caminho para o arquivo .jl com os documentos para efetuar a busca'
    )

    ap.add_argument(
        '--n-resultados',
        type=int,
        required=False,
        default=10,
        help='Quantidade máxima de resultados (10 padrão) para retornar na busca.'
    )

    return ap.parse_args()


def main(args):
    print('Bem-vindo ao sistema de busca de livros.')
    print('> Para pesquisar, digite palavras separadas por um "AND"')
    print('> Pressione ENTER sem nenhuma palavras para sair')
    print('> Montando o índice para acelerar as consultas')
    documentos = list(ler_documentos(args.documentos))
    indice_invertido = construir_indice_invertido(documentos)
    indice_k_grams = construir_indice_k_grams(indice_invertido, k=3)
    while True:
        print('=' * 80)
        print('=' * 80)
        consulta = input('Qual é a sua consulta? ')
        consulta = consulta.strip()
        if not consulta:
            print('Saindo...')
            break

        termos = normalizar_tokens(consulta.split('AND'))
        termos_ = aplicar_correcao_ortografica(termos, indice_invertido, indice_k_grams)
        if termos_ != termos:
            termos = termos_
            print(f'Você quis dizer "{" AND ".join(termos)}"?')
        else:
            print(f'Resultados para {consulta}')

        print()
        resultados = consultar(termos, indice_invertido, documentos)
        for (documento, i) in zip(resultados, range(args.n_resultados)):
            print(f'{i + 1}. {documento["titulo"]}')
            print(documento["url"])
            print('>', documento['descricao'][:100], '...')
            print()


def ler_documentos(caminho_documentos):
    with open(caminho_documentos, 'r') as f:
        for line in f:
            documento = json.loads(line)
            if documento['descricao']:
                yield documento


def construir_indice_invertido(documentos):
    '''
    Essa função constrói e retorna um índice invertido.
    Entrada: Lista de documentos (strings)
    Saída: Dicionário de termos para lista de documentos
    '''
    # Exercício 1
    indice_invertido = {}
    # Seu código aqui
    for i in range(len(documentos)):
        documento = documentos[i]
        tokens = obter_tokens(documento['descricao'])

        for token in tokens:
            if token not in indice_invertido:
                indice_invertido[token] = [i]
            elif i != indice_invertido[token][-1]:
                indice_invertido[token].append(i)
    
    return indice_invertido


def construir_indice_k_grams(indice_invertido, k=3):
    '''
    Constrói um índice que mapeia de k-grams para termos
    '''
    indice_k_grams = {}
    # Exercício 3
    for token in indice_invertido:
        for k_gram in obter_k_grams(token):
            if k_gram not in indice_k_grams:
                indice_k_grams[k_gram] = {token}
            else:
                indice_k_grams[k_gram].add(token)
    return indice_k_grams


def obter_k_grams(termo, k=3):
    '''Retorna as substrings de tamanho k de termo.
    São adicionados k - 1 sinais especiais ($) no início e fim do termo.
    '''
    pad = k - 1
    termo_pad = ('$' * pad) + termo + ('$' * pad)
    return {termo_pad[i:i + k] for i in range(len(termo_pad) - pad)}


def obter_tokens(documento):
    '''Quebra um texto em sequências de palavras normalizadas em lower case'''
    tokens = re.findall(r'(?:\b(\w+)\b)', documento)
    return normalizar_tokens(tokens)


def normalizar_tokens(tokens):
    '''Coloca os tokens em lower case e remove espaços no começo/final'''
    return [t.strip().lower() for t in tokens]


def aplicar_correcao_ortografica(termos, indice_invertido, indice_k_grams):
    '''Retorna termos com correção ortográfica.
    Se o termo existe no índice inverto, mantém.
    Se não existe, encontra a melhor correção ortográfica.
    '''
    termos_corrigidos = []
    for termo in termos:
        if termo in indice_invertido:
            termos_corrigidos.append(termo)
        else:
            correcao = obter_termo_corrigido(termo, indice_k_grams)
            termos_corrigidos.append(correcao)

    return termos_corrigidos


def obter_termo_corrigido(termo, indice_k_grams):
    '''
    Encontra a melhor correção ortográfica de um determinado termo utilizando
    o índice k-grams.
    '''
    # Exercício 4
    possible_tokens = set()
    termo_k_grams = obter_k_grams(termo)
    for termo_k_gram in termo_k_grams:
        k_gram_tokens = indice_k_grams.get(termo_k_gram, set())
        possible_tokens = possible_tokens.union(k_gram_tokens)

    max_jaccard = 0
    max_jaccard_token = None

    for possible_token in possible_tokens:
        possible_token_k_grams = obter_k_grams(possible_token)
        total_k_grams_count = len(termo_k_grams.union(possible_token_k_grams)) # poderia fazer o union usando |
        intersection_count = len(termo_k_grams.intersection(possible_token_k_grams)) # poderia fazer intersection usando &
        jaccard = intersection_count / total_k_grams_count
        if jaccard > max_jaccard:
            max_jaccard = jaccard
            max_jaccard_token = possible_token

    return max_jaccard_token

def consultar(termos_consulta, indice_invertido, documentos):
    '''
    Retorna todos os documentos que contém todos os termos de consulta.
    Como seria essa rotina se usássemos set() do python como estrutura de dados ao invés de list()?
    Como seriam as operações OR e NOT?
    '''
    p1 = termos_consulta.pop(0)
    resultados = indice_invertido.get(p1, [])
    while termos_consulta:
        p2 = termos_consulta.pop(0)
        resultadosP2 = indice_invertido.get(p2, [])
        resultados = intersect(resultadosP2, resultados)
    
    for i in resultados:
        yield documentos[i]


def intersect(p1, p2):
    '''
    Implementar o algoritmo INTERSECT do Livro Introduction to Information Retrieval
    '''
    # Exercício 2
    # Seu código aqui
    p1 = p1 + [] # para nao alterar os indices do mapa original
    p2 = p2 + [] # para nao alterar os indices do mapa original
    p3 = []
    while p1 and p2:
        if p1[0] == p2[0]:
            p3.append(p1[0])
            del p1[0]
            del p2[0]
        elif p1[0] < p2[0]:
            del p1[0]
        else:
            del p2[0]
    return p3

if __name__ == '__main__':
    main(parse_args())
