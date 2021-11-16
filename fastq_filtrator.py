def main(input_fastq, output_file_prefix, gc_bounds, length_bounds, quality_threshold, save_filtered):  # главная программа
    yfilename = output_file_prefix + '_passed.fastq'
    zfilename = output_file_prefix + '_failed.fastq'
    prog_menu(input_fastq, yfilename, zfilename, length_bounds, gc_bounds, quality_threshold, save_filtered)


def prog_menu(input_fastq, yfilename, zfilename, length_bounds, gc_bounds, quality_threshold, save_filtered):  # меню
    menu = 1
    while menu != 0:
        print('1 - start\n'
              '2 - GC content\n'
              '3 - length\n'
              '4 - quality\n'
              '5 - save\n'
              '0 - exit\n')
        menu = int(input())
        if menu == 1:
            start_filters(input_fastq, yfilename, zfilename, length_bounds, gc_bounds, quality_threshold, save_filtered)
        elif menu == 2:
            GC(input_fastq, yfilename, zfilename, length_bounds, gc_bounds, quality_threshold, save_filtered)
        elif menu == 3:
            length_setup(input_fastq, yfilename, zfilename, length_bounds, gc_bounds, quality_threshold, save_filtered)
        elif menu == 4:
            quality(input_fastq, yfilename, zfilename, length_bounds, gc_bounds, quality_threshold, save_filtered)
        elif menu == 5:
            save(input_fastq, yfilename, zfilename, length_bounds, gc_bounds, quality_threshold, save_filtered)
        elif menu == 0:
            exit()


def start_filters(input_fastq, yfilename, zfilename, length_bounds, gc_bounds, quality_threshold, save_filtered):
    print('Start')
    print('fastq file name =', input_fastq)
    print('sorted file name =', yfilename)
    print('trash file name =', zfilename)
    print('length_bounds  =', length_bounds)
    print('gc_bounds =', gc_bounds)
    print('quality_threshold =', quality_threshold)
    print('save_filtered =', save_filtered)
    # pause = input("Press enter to continue ->")
    x = open(input_fastq, 'r')  # открыть файл чтения
    y = open(yfilename, 'w')    # создать файл для записи
    y.close()
    z = open(zfilename, 'w')    # создать файл для отфильтрованных
    z.close()
    all_fastq = x.readlines()
    num_str = sum(1 for line in all_fastq)
    print('num_str=', num_str)
    for i in range(1, num_str+1, 4):
        print('i=', i)
        print(all_fastq[i], end='')
        num_G = all_fastq[i].upper().count('G')
        num_C = all_fastq[i].upper().count('G')
        num_GC = num_G + num_C
        len_str = len(all_fastq[i])
        GC_content = num_GC / len_str * 100
        print('len_str=', len_str)
        print('GC_content=', GC_content)
        quality = all_fastq[i+2]
        print(quality)
        sum_ord = 0
        len_quality = len(quality)
        for j in range(len_quality):  # подсчет качества
            sum_ord = sum_ord + ord(quality[j])
            quality_sum = sum_ord / len_quality
        print('quality_sum=', quality_sum)
        print(length_bounds[0], length_bounds[1], gc_bounds[0], gc_bounds[1])
        if length_bounds[0] <= len_str <= length_bounds[1] and gc_bounds[0] <= GC_content <= gc_bounds[1] and quality_sum >= quality_threshold:
            y = open(yfilename, 'r+')
            y.seek(0, 2)
            y.write(all_fastq[i-1])
            y.write(all_fastq[i])
            y.write(all_fastq[i+1])
            y.write(all_fastq[i+2])
        elif save_filtered:
            z = open(zfilename, 'r+')
            z.seek(0, 2)
            z.write(all_fastq[i - 1])
            z.write(all_fastq[i])
            z.write(all_fastq[i + 1])
            z.write(all_fastq[i + 2])
    prog_menu(input_fastq, yfilename, zfilename, length_bounds, gc_bounds, quality_threshold, save_filtered)


def GC(input_fastq, yfilename, zfilename, length_bounds, gc_bounds, quality_threshold, save_filtered):
    print('gc_bounds =', gc_bounds)
    gc_bounds = [int(token) for token in input("Input the gc_bounds range separated by a space ->").split()]
    print('gc_bounds =', gc_bounds)
    prog_menu(input_fastq, yfilename, zfilename, length_bounds, gc_bounds, quality_threshold, save_filtered)


def length_setup(input_fastq, yfilename, zfilename, length_bounds, gc_bounds, quality_threshold, save_filtered):
    print('length_bounds =', length_bounds)
    length_bounds = [int(token) for token in input("Input the length_bounds range separated by a space ->").split()]
    print('length_bounds =', length_bounds)
    prog_menu(input_fastq, yfilename, zfilename, length_bounds, gc_bounds, quality_threshold, save_filtered)


def quality(input_fastq, yfilename, zfilename, length_bounds, gc_bounds, quality_threshold, save_filtered):
    print('quality_threshold =', quality_threshold)
    e_check = input("Enter the quality_threshold ->")  # проверка на пустоту
    if len(e_check) != 0:
        quality_threshold = int(e_check)
    print('quality_threshold =', quality_threshold)
    prog_menu(input_fastq, yfilename, zfilename, length_bounds, gc_bounds, quality_threshold, save_filtered)


def save(input_fastq, yfilename, zfilename, length_bounds, gc_bounds, quality_threshold, save_filtered):
    save_filtered = 1
    print('save_filtered =', save_filtered)
    prog_menu(input_fastq, yfilename, zfilename, length_bounds, gc_bounds, quality_threshold, save_filtered)


input_fastq = input("Input the fastq file name ->")
output_file_prefix = input("Input the output file prefix ->")
gc_bounds = (0, 100)
length_bounds = (0, 2**32)
quality_threshold = 0
save_filtered = False
main(input_fastq, output_file_prefix, gc_bounds, length_bounds, quality_threshold, save_filtered)
