# Dicionário para mapear caracteres para código Morse
dicionario_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.'
}

# Função para converter texto para código Morse
def texto_morse(texto):
    cod_morse = []
    for char in texto.upper():
        if char in dicionario_morse:
            cod_morse.append(dicionario_morse[char])
        elif char == ' ':
            cod_morse.append(' ')
        else:
            cod_morse.append('')
    return ' '.join(cod_morse)

# Função para converter código Morse para texto
def morse_texto(cod_morse):
    cod_morse = cod_morse.split(' ')
    texto = []
    for code in cod_morse:
        if code in dicionario_morse.values():
            texto.append(list(dicionario_morse.keys())[list(dicionario_morse.values()).index(code)])
        elif code == '':
            texto.append(' ')
    return ''.join(texto)

# Função principal para interação com o usuário
def main():
    while True:
        print("Escolha a operação:")
        print("1. Texto para Código Morse")
        print("2. Código Morse para Texto")
        print("3. Sair")
        
        choice = input("Digite sua escolha (1/2/3): ")
        
        if choice == '1':
            texto = input("Digite o texto para converter em código Morse: ")
            cod_morse = texto_morse(texto)
            print(f"O código Morse correspondente é: {cod_morse}")
        elif choice == '2':
            cod_morse = input("Digite o código Morse para converter em texto: ")
            texto = morse_texto(cod_morse)
            print(f"O texto correspondente é: {texto}")
        elif choice == '3':
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()
