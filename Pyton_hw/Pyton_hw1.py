def check(seq):         #проверка
    global len_seq
    len_seq = len(seq)
    i_len_seq = 0
    i_len_letter = 0
    for i_len_seq in range(len_seq):
        for i_len_letter in range(len_letter):
            if seq[i_len_seq] == letter[i_len_letter]:      #проверка на лишние символы
                break
        else:
            print('It is not nucleotide sequence')
            print('Try again')
            main()
    i_len_seq = 0
    i_len_letter = 0
    l_t = 0
    l_u = 0
    for i_len_seq in range(len_seq):            #проверка на смесь
        if seq[i_len_seq] == 'T' or seq[i_len_seq] == 't':
            l_t = 1
        if seq[i_len_seq] == 'U' or seq[i_len_seq] == 'u':
            l_u = 1
        if l_u == 1 and l_t == 1:
            print('DNA/RNA nucleatide mix')
            print('Try again')
            main()
    prog()
def transcribe():
    print('DNA:  ', seq)
    print('Transcribe: ', end ="")
    complement = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 'u', 'c': 'g', 'g': 'c', 't': 'a'}
    i = 0
    for i in range(len_seq):
        print(complement[seq[i]], end ="")
    print()
def reverse():
    print('DNA:  ', seq)
    print('Reverse:', end=' ')
    rev_seq = seq[::-1]
    print(rev_seq)

def complement():
    print('DNA:  ', seq)
    print('Complement:', end=' ')
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}
    i = 0
    for i in range(len_seq):
        print(complement[seq[i]], end ="")
    print()
def reverse_complement():
    print('DNA:  ', seq)
    print('Reverse complement:', end=' ')
    complement = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 'u', 'c': 'g', 'g': 'c', 't': 'a'}
    i = 0
    rev_seq = seq[::-1]
    for i in range(len_seq):
        print(complement[rev_seq[i]], end ="")
    print()
def prog():         #меню
    menu = 1
    while menu != 0:
        print('1 - transcribe\n'
              '2 - reverse\n'
              '3 - complement\n'
              '4 - reverse complement\n'
              '0 - exit\n')
        menu = int(input())
        if menu == 1:
            transcribe()
        elif menu == 2:
            reverse()
        elif menu == 3:
            complement()
        elif menu == 4:
            reverse_complement()
        elif menu == 0:
            break
def main():             #главная
        global seq
        print('For exit enter: 0')
        seq = input("Enter the sequence ->")        #ввод последовательности
        if seq == '0':
            exit()
        check(seq)      #проверка на символы и смесь
############################## BEGIN ####################################################
letter = 'AaTtGgCcUu'
len_letter = len(letter)
main()