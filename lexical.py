# Library yang digunakan
import string

# Inputan user
sentence = input("Token Input: ")
input = sentence.lower() + "#"

# Inisiasi
list_alphabet = list(string.ascii_lowercase)
list_state = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
              'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20',
              'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30',
              'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40',
              'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47', 'q48', 'q49']

# Tabel transisi
transition_table = {}

for state in list_state:
    for alphabet in list_alphabet:
        transition_table[(state, alphabet)] = "error"
    transition_table[(state, "#")] = "error"
    transition_table[(state, " ")] = "error"

# Spasi sebelum input string
transition_table["q0", " "] = "q0"

# Mengupdate tabel transisi untuk token "flor"
transition_table[("q0", "f")] = "q23"
transition_table[("q23", "l")] = "q24"
transition_table[("q24", "o")] = "q25"
transition_table[("q25", "r")] = "q26"
transition_table[("q26", "#")] = "accept"
transition_table[("q26", " ")] = "q48"
transition_table[("q48", "#")] = "accept"

# Mengupdate tabel transisi untuk token "arroz"
transition_table[("q0", "a")] = "q44"
transition_table[("q44", "r")] = "q45"
transition_table[("q45", "r")] = "q46"
transition_table[("q46", "o")] = "q47"
transition_table[("q47", "z")] = "q26"
transition_table[("q26", "#")] = "accept"
transition_table[("q26", " ")] = "q48"
transition_table[("q48", "#")] = "accept"

# Mengupdate tabel transisi untuk token "zapato"
transition_table[("q0", "z")] = "q40"
transition_table[("q40", "a")] = "q41"
transition_table[("q41", "p")] = "q42"
transition_table[("q42", "a")] = "q43"
transition_table[("q43", "t")] = "q36"
transition_table[("q36", "o")] = "q26"
transition_table[("q26", "#")] = "accept"
transition_table[("q26", " ")] = "q48"
transition_table[("q48", "#")] = "accept"

# Mengupdate tabel transisi untuk token "vestir"
transition_table[("q0", "v")] = "q19"
transition_table[("q19", "e")] = "q20"
transition_table[("q20", "s")] = "q21"
transition_table[("q21", "t")] = "q22"
transition_table[("q22", "i")] = "q25"
transition_table[("q25", "r")] = "q26"
transition_table[("q26", "#")] = "accept"
transition_table[("q26", " ")] = "q48"
transition_table[("q48", "#")] = "accept"

# Mengupdate tabel transisi untuk token "libro"
transition_table[("q0", "l")] = "q37"
transition_table[("q37", "i")] = "q38"
transition_table[("q38", "b")] = "q39"
transition_table[("q39", "r")] = "q36"
transition_table[("q36", "o")] = "q26"
transition_table[("q26", "#")] = "accept"
transition_table[("q26", " ")] = "q48"
transition_table[("q48", "#")] = "accept"

# Mengupdate tabel transisi untuk token "yo"
transition_table[("q0", "y")] = "q36"
transition_table[("q36", "o")] = "q26"
transition_table[("q26", "#")] = "accept"
transition_table[("q26", " ")] = "q48"
transition_table[("q48", "#")] = "accept"

# Mengupdate tabel transisi untuk token "madre"
transition_table[("q0", "m")] = "q15"
transition_table[("q15", "a")] = "q16"
transition_table[("q16", "d")] = "q17"
transition_table[("q17", "r")] = "q18"
transition_table[("q18", "e")] = "q26"
transition_table[("q26", "#")] = "accept"
transition_table[("q26", " ")] = "q48"
transition_table[("q48", "#")] = "accept"

# Mengupdate tabel transisi untuk token "padre"
transition_table[("q0", "p")] = "q10"
transition_table[("q10", "a")] = "q16"
transition_table[("q16", "d")] = "q17"
transition_table[("q17", "r")] = "q18"
transition_table[("q18", "e")] = "q26"
transition_table[("q26", "#")] = "accept"
transition_table[("q26", " ")] = "q48"
transition_table[("q48", "#")] = "accept"

# Mengupdate tabel transisi untuk token "ellos"
transition_table[("q0", "e")] = "q6"
transition_table[("q6", "l")] = "q7"
transition_table[("q7", "l")] = "q8"
transition_table[("q8", "o")] = "q9"
transition_table[("q9", "s")] = "q26"
transition_table[("q26", "#")] = "accept"
transition_table[("q26", " ")] = "q48"
transition_table[("q48", "#")] = "accept"

# Mengupdate tabel transisi untuk token "nosotros"
transition_table[("q0", "n")] = "q1"
transition_table[("q1", "o")] = "q2"
transition_table[("q2", "s")] = "q3"
transition_table[("q3", "o")] = "q4"
transition_table[("q4", "t")] = "q5"
transition_table[("q5", "r")] = "q8"
transition_table[("q8", "o")] = "q9"
transition_table[("q9", "s")] = "q26"
transition_table[("q26", "#")] = "accept"
transition_table[("q26", " ")] = "q48"
transition_table[("q48", "#")] = "accept"

# Mengupdate tabel transisi untuk token "planta"
transition_table[("q0", "p")] = "q10"
transition_table[("q10", "l")] = "q11"
transition_table[("q11", "a")] = "q12"
transition_table[("q12", "n")] = "q13"
transition_table[("q13", "t")] = "q14"
transition_table[("q14", "a")] = "q26"
transition_table[("q26", "#")] = "accept"
transition_table[("q26", " ")] = "q48"
transition_table[("q48", "#")] = "accept"

# Mengupdate tabel transisi untuk token "comer"
transition_table[("q0", "c")] = "q27"
transition_table[("q27", "o")] = "q28"
transition_table[("q28", "m")] = "q29"
transition_table[("q29", "e")] = "q25"
transition_table[("q25", "r")] = "q26"
transition_table[("q26", "#")] = "accept"
transition_table[("q26", " ")] = "q48"
transition_table[("q48", "#")] = "accept"

# Mengupdate tabel transisi untuk token "comprar"
transition_table[("q0", "c")] = "q27"
transition_table[("q27", "o")] = "q28"
transition_table[("q28", "m")] = "q29"
transition_table[("q29", "p")] = "q30"
transition_table[("q30", "r")] = "q31"
transition_table[("q31", "a")] = "q25"
transition_table[("q25", "r")] = "q26"
transition_table[("q26", "#")] = "accept"
transition_table[("q26", " ")] = "q48"
transition_table[("q48", "#")] = "accept"

# Mengupdate tabel transisi untuk token "usar"
transition_table[("q0", "u")] = "q32"
transition_table[("q32", "s")] = "q31"
transition_table[("q31", "a")] = "q25"
transition_table[("q25", "r")] = "q26"
transition_table[("q26", "#")] = "accept"
transition_table[("q26", " ")] = "q48"
transition_table[("q48", "#")] = "accept"

# Mengupdate tabel transisi untuk token "buscar"
transition_table[("q0", "b")] = "q33"
transition_table[("q33", "u")] = "q34"
transition_table[("q34", "s")] = "q35"
transition_table[("q35", "c")] = "q31"
transition_table[("q31", "a")] = "q25"
transition_table[("q25", "r")] = "q26"
transition_table[("q26", "#")] = "accept"
transition_table[("q26", " ")] = "q48"
transition_table[("q48", "#")] = "accept"

# Transisi untuk token baru
transition_table[("q48", "n")] = "q1"
transition_table[("q48", "e")] = "q6"
transition_table[("q48", "p")] = "q10"
transition_table[("q48", "m")] = "q15"
transition_table[("q48", "v")] = "q19"
transition_table[("q48", "f")] = "q23"
transition_table[("q48", "c")] = "q27"
transition_table[("q48", "u")] = "q32"
transition_table[("q48", "b")] = "q33"
transition_table[("q48", "y")] = "q36"
transition_table[("q48", "l")] = "q37"
transition_table[("q48", "z")] = "q40"
transition_table[("q48", "a")] = "q44"

# Program utama Lexical Analyzer
index_character = 0
i = 1
state = "q0"
current_token = ""
while state != "accept":
    current_char = input[index_character]
    current_token += current_char
    state = transition_table[(state, current_char)]
    if state == "q26":
        print("current token ", "[", i, "]" ": ", current_token)
        i += 1
        current_token = ""
    if state == "error":
        print("error, token is [NOT VALID]")
        break
    index_character += 1
    


# Konklusi
if state == "accept":
    print("Hasil token dari: ", sentence, ", [VALID]")
