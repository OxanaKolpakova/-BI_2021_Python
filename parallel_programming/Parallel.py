import time
from multiprocessing import Process, Manager #, Queue
import itertools
import argparse


def fasta_reader(fasta_name):
    with open(fasta_name, "r") as file:
        seq = []
        for line in file:
            if line.startswith(">"):
                contig = line.split()[0][1:]
            else:
                seq = line.replace("\n", "")
                unique = dict(zip(list(seq), [list(seq).count(i) for i in list(seq)]))
                yield contig, unique


def do_work(in_queue, out_list):
    while True:
        entry = in_queue.get()
        if entry:
            contig, count_dict = entry
            result = (contig, count_dict)
            out_list.append(result)
        else:
            return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        usage="\n%(prog)s <path to the fasta file> <number of threads to use>"
    )
    parser.add_argument("--fasta", type=str)
    parser.add_argument("--threads", type=str)
    args = parser.parse_args()
    threads = int(args.threads)
    fasta_name = args.fasta
    start_time = time.time()
    struct = time.localtime(start_time)
    time.strftime("%d.%m.%Y %H:%M", struct)
    print("Job started at:", time.strftime("%d.%m.%Y %H:%M", struct))
    start_time = time.time()
    threads = 2
    manager = Manager()
    results = manager.list()
    work = manager.Queue(threads)
    pool = []
    for i in range(threads):
        p = Process(target=do_work, args=(work, results))
        p.start()
        pool.append(p)
    reader_chain = itertools.chain(fasta_reader(fasta_name), (None,) * threads)
    for line in reader_chain:
        work.put(line)
    for p in pool:
        p.join()
    for contig, count_dict in results:
        print("Contig", contig, end=": ")
        print(", ".join("%s: %s" % (k, count_dict[k]) for k in count_dict.keys()))
    total_time = time.time() - start_time
    print("Total time:", total_time, "sec")
  
