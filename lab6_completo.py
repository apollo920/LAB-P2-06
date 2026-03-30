import re
import copy
from transformers import AutoTokenizer


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


def merge_vocab(pair, v_in):
    v_out = {}
    p1, p2 = pair
    bigram = p1 + ' ' + p2
    merged = p1 + p2

    for word, freq in v_in.items():
        new_word = re.sub(r'(?<![^\s])' + re.escape(bigram) + r'(?![^\s])', merged, word)
        v_out[new_word] = freq

    return v_out


if __name__ == '__main__':

    print("=" * 55)
    print("TAREFA 1: Motor de Frequencias")
    print("=" * 55)

    print("\nVocabulario inicial:")
    for palavra, freq in vocab.items():
        print(f"  '{palavra}': {freq}")

    stats = get_stats(vocab)

    print("\nFrequencia de pares adjacentes (ordenado decrescente):")
    for par, contagem in sorted(stats.items(), key=lambda x: x[1], reverse=True):
        print(f"  {par}: {contagem}")

    assert stats[('e', 's')] == 9, "ERRO na validacao do par ('e', 's')"
    print("\nValidacao OK: par ('e', 's') retornou contagem maxima de 9.")

    print("\n" + "=" * 55)
    print("TAREFA 2: Loop de Fusao (K=5 iteracoes)")
    print("=" * 55)

    vocab_treino = copy.deepcopy(vocab)

    K = 5
    for i in range(1, K + 1):
        stats = get_stats(vocab_treino)
        best_pair = max(stats, key=lambda x: stats[x])
        vocab_treino = merge_vocab(best_pair, vocab_treino)

        print(f"\n--- Iteracao {i} ---")
        print(f"Par fundido: {best_pair}")
        print("Vocabulario atualizado:")
        for palavra, freq in vocab_treino.items():
            print(f"  '{palavra}': {freq}")

    print("\nTreinamento concluido!")
    print("Observe tokens como 'est</w>' formados ao longo das iteracoes.")

    print("\n" + "=" * 55)
    print("TAREFA 3: WordPiece com BERT Multilingue")
    print("=" * 55)

    print("\nCarregando tokenizador 'bert-base-multilingual-cased'...")
    tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
    print("Tokenizador carregado!")

    frase = "Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar."
    print(f"\nFrase de teste:\n  \"{frase}\"")

    tokens = tokenizer.tokenize(frase)
    print("\nTokens gerados pelo WordPiece:")
    print(tokens)
    print(f"\nTotal de tokens: {len(tokens)}")

    tokens_com_cerquilha = [t for t in tokens if t.startswith('##')]
    print(f"Tokens com '##': {tokens_com_cerquilha}")