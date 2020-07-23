from modulos.eh_primo import eh_primo


def gerar_primos(n: int) -> list:
    return [x for x in range(n) if eh_primo(x)]
