vocab = {
    'l o w </w>': 5,
    'l o w e r </w>': 2,
    'n e w e s t </w>': 6,
    'w i d e s t </w>': 3
}


def get_stats(vocab):
    pairs = {}

    for word, freq in vocab.items():
        symbols = word.split()

        for i in range(len(symbols) - 1):
            pair = (symbols[i], symbols[i + 1])
            if pair in pairs:
                pairs[pair] += freq
            else:
                pairs[pair] = freq

    return pairs


if __name__ == '__main__':
    print("=" * 50)
    print("Tarefa 1: Motor de Frequencias")
    print("=" * 50)

    print("\nVocabulario inicial:")
    for palavra, freq in vocab.items():
        print(f"  '{palavra}': {freq}")

    stats = get_stats(vocab)

    print("\nFrequencia de todos os pares adjacentes:")
    for par, contagem in sorted(stats.items(), key=lambda x: x[1], reverse=True):
        print(f"  {par}: {contagem}")

    par_es = ('e', 's')
    print(f"\nValidacao: frequencia do par {par_es} = {stats.get(par_es, 0)}")

    assert stats[par_es] == 9, f"ERRO: esperado 9, obtido {stats[par_es]}"
    print("Validacao OK: par ('e', 's') retornou contagem maxima de 9.")