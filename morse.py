# Dicionário de correspondência entre letras/números e código Morse
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'
}

# Função para traduzir texto em código Morse
def texto_para_morse(texto):
    texto = texto.upper()
    morse = []
    for letra in texto:
        if letra in morse_code_dict:
            morse.append(morse_code_dict[letra])
        else:
            morse.append(letra)
    return ' '.join(morse)

# Função para traduzir código Morse em texto
def morse_para_texto(morse):
    morse = morse.split(' ')
    texto = []
    for codigo in morse:
        for letra, codigo_morse in morse_code_dict.items():
            if codigo == codigo_morse:
                texto.append(letra)
                break
        else:
            texto.append(codigo)
    return ''.join(texto)

# Solicitar ao usuário a escolha de conversão
opcao = input("Escolha a conversão (T para Texto -> Morse, M para Morse -> Texto): ").strip()

if opcao.upper() == 'T':
    texto = input("Digite o texto a ser convertido em código Morse: ")
    codigo_morse = texto_para_morse(texto)
    print("Texto em Morse:", codigo_morse)
elif opcao.upper() == 'M':
    morse = input("Digite o código Morse a ser convertido em texto: ")
    texto = morse_para_texto(morse)
    print("Morse em Texto:", texto)
else:
    print("Opção inválida. Use 'T' para Texto -> Morse ou 'M' para Morse -> Texto.")
