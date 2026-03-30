from transformers import AutoTokenizer


if __name__ == '__main__':
    print("=" * 50)
    print("Tarefa 3: WordPiece com BERT Multilingue")
    print("=" * 50)

    print("\nCarregando tokenizador 'bert-base-multilingual-cased'...")
    tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
    print("Tokenizador carregado com sucesso!")

    frase = "Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar."

    print(f"\nFrase de teste:\n  \"{frase}\"")

    tokens = tokenizer.tokenize(frase)

    print("\nTokens gerados pelo WordPiece:")
    print(tokens)

    print(f"\nTotal de tokens: {len(tokens)}")

    tokens_com_cerquilha = [t for t in tokens if t.startswith('##')]
    print(f"\nTokens com prefixo '##': {tokens_com_cerquilha}")