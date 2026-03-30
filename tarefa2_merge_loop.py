import re
import copy
from tarefa1_get_stats import get_stats, vocab as vocab_inicial


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
    print("=" * 50)
    print("Tarefa 2: Loop de Fusao (K=5 iteracoes)")
    print("=" * 50)

    vocab = copy.deepcopy(vocab_inicial)

    print("\nVocabulario inicial:")
    for palavra, freq in vocab.items():
        print(f"  '{palavra}': {freq}")

    K = 5
    for i in range(1, K + 1):
        stats = get_stats(vocab)
        best_pair = max(stats, key=lambda x: stats[x])
        vocab = merge_vocab(best_pair, vocab)

        print(f"\n--- Iteracao {i} ---")
        print(f"Par fundido: {best_pair}")
        print("Vocabulario atualizado:")
        for palavra, freq in vocab.items():
            print(f"  '{palavra}': {freq}")

    print("\n" + "=" * 50)
    print("Treinamento concluido!")
    print("Observe a formacao de tokens morfologicos como 'est</w>'.")
    print("=" * 50)