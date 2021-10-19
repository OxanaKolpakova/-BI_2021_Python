def main():  # главная
    input_fastq = input("Input the fastq file name ->")
    output_file_prefix = input("Input the output file prefix ->")
    yfilename = output_file_prefix + '_passed.fastq'
    zfilename = output_file_prefix + '_failed.fastq'
    leng_min = 0
    leng_max = 2**32
    gc_bounds_min = 0
    gc_bounds_max = 100
    quality_threshold = 0
    save_filtered = False

    prog(input_fastq, yfilename, zfilename, leng_min, leng_max, gc_bounds_min, gc_bounds_max, quality_threshold, save_filtered)


def prog(input_fastq, yfilename, zfilename, leng_min, leng_max, gc_bounds_min, gc_bounds_max, quality_threshold, save_filtered):  # меню
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
            start(input_fastq, yfilename, zfilename, leng_min, leng_max, gc_bounds_min, gc_bounds_max, quality_threshold, save_filtered)
        elif menu == 2:
            GC(input_fastq, yfilename, zfilename, leng_min, leng_max, gc_bounds_min, gc_bounds_max, quality_threshold, save_filtered)
        elif menu == 3:
            leng(input_fastq, yfilename, zfilename, leng_min, leng_max, gc_bounds_min, gc_bounds_max, quality_threshold, save_filtered)
        elif menu == 4:
            quality(input_fastq, yfilename, zfilename, leng_min, leng_max, gc_bounds_min, gc_bounds_max, quality_threshold, save_filtered)
        elif menu == 5:
            save(input_fastq, yfilename, zfilename, leng_min, leng_max, gc_bounds_min, gc_bounds_max, quality_threshold, save_filtered)
        elif menu == 0:
            exit()


def start(input_fastq, yfilename, zfilename, leng_min, leng_max, gc_bounds_min, gc_bounds_max, quality_threshold, save_filtered):
    print('Start')
    print('fastq file name =', input_fastq)
    print('sorted file name =', yfilename)
    print('trash file name =', zfilename)
    print('leng_min =', leng_min)
    print('leng_max =', leng_max)
    print('gc_bounds_min =', gc_bounds_min)
    print('gc_bounds_max =', gc_bounds_max)
    print('quality_threshold =', quality_threshold)
    print('save_filtered =', save_filtered)
    pause = input("Press enter to continue ->")
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
        num_G = all_fastq[i].count('G')
        num_C = all_fastq[i].count('G')
        num_GC = num_G + num_C
        len_str = len(all_fastq[i])
        GC_content = num_GC / len_str * 100
        print('len_str=', len_str)
        print('GC_content=', GC_content)
        quality = all_fastq[i+2]
        print(quality)
        sum_ord = 0
        len_quality = len(quality)
        for j in range(len_quality): # подсчет качества
            sum_ord = sum_ord + ord(quality[j])
            quality_sum = sum_ord / len_quality
        print('quality_sum=', quality_sum)
        if len_str > leng_min and len_str < leng_max and GC_content > gc_bounds_min and GC_content < gc_bounds_max and quality_sum > quality_threshold:
            y = open(yfilename, 'r+')
            y.seek(0, 2)
            y.write(all_fastq[i-1])
            y.write(all_fastq[i])
            y.write(all_fastq[i+1])
            y.write(all_fastq[i+2])
        elif save_filtered == True:
            z = open(zfilename, 'r+')
            z.seek(0, 2)
            z.write(all_fastq[i - 1])
            z.write(all_fastq[i])
            z.write(all_fastq[i + 1])
            z.write(all_fastq[i + 2])

    prog(input_fastq, yfilename, zfilename, leng_min, leng_max, gc_bounds_min, gc_bounds_max, quality_threshold, save_filtered)


def GC(input_fastq, yfilename, zfilename, leng_min, leng_max, gc_bounds_min, gc_bounds_max, quality_threshold, save_filtered):
    print('gc_bounds_min =', gc_bounds_min)
    print('gc_bounds_max =', gc_bounds_max)
    e_check = str(input("Input the gc_bounds_min ->"))  # проверка на пустоту
    if len(e_check) != 0:
        gc_bounds_min = float(e_check)
    e_check = input("Input the gc_bounds_max ->")
    if len(e_check) != 0:
        gc_bounds_max = float(e_check)
    print('gc_bounds_min =', gc_bounds_min)
    print('gc_bounds_max =', gc_bounds_max)
    #   gc_bounds_min, gc_bounds_max = map(int, input("Enter the range of GC with a space ->").split())
    #    gc_bounds = input("Enter the gc_bounds ->")
    #    output_file_prefix = input("Enter the prefix ->")
    #    length_bounds = input("Enter the length_bounds ->")
    #    quality_threshold  = input("Enter the quality_threshold  ->")
    #    save_filtered = input("Enter the save_filtered ->")
    prog(input_fastq, yfilename, zfilename, leng_min, leng_max, gc_bounds_min, gc_bounds_max, quality_threshold, save_filtered)


def leng(input_fastq, yfilename, zfilename, leng_min, leng_max, gc_bounds_min, gc_bounds_max, quality_threshold, save_filtered):
    print('leng_min =', leng_min)
    print('leng_max =', leng_max)
    e_check = input("Enter the leng_min ->")  # проверка на пустоту
    if len(e_check) != 0:
        leng_min = int(e_check)
    e_check = input("Enter the leng_max ->")
    if len(e_check) != 0:
        leng_max = int(e_check)
    print('leng_min =', leng_min)
    print('leng_max =', leng_max)
    prog(input_fastq, yfilename, zfilename, leng_min, leng_max, gc_bounds_min, gc_bounds_max, quality_threshold, save_filtered)


def quality(input_fastq, yfilename, zfilename, leng_min, leng_max, gc_bounds_min, gc_bounds_max, quality_threshold, save_filtered):
    print('quality_threshold =', quality_threshold)
    e_check = input("Enter the quality_threshold ->")  # проверка на пустоту
    if len(e_check) != 0:
        quality_threshold = int(e_check)
    print('quality_threshold =', quality_threshold)
    prog(input_fastq, yfilename, zfilename, leng_min, leng_max, gc_bounds_min, gc_bounds_max, quality_threshold, save_filtered)


def save(input_fastq, yfilename, zfilename, leng_min, leng_max, gc_bounds_min, gc_bounds_max, quality_threshold, save_filtered):
    print('save_filtered =', save_filtered)
    e_check = input("Enter the quality_threshold ->")  # проверка на пустоту
    if len(e_check) != 0:
        save_filtered = e_check
    print('save_filtered =', save_filtered)
    prog(input_fastq, yfilename, zfilename, leng_min, leng_max, gc_bounds_min, gc_bounds_max, quality_threshold, save_filtered)


main()
