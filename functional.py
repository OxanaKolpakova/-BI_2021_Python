def sequential_map(seq, *args):
  for func in args:
    seq=list(map(func, seq))
  return(seq)


def consensus_filter(seq, *args):
  list = []
  for i in seq:
    check = 1
    for func in args:
      check = check*func(i)
    if check == 1:
      list.append(i)
  return(list)
  

def conditional_reduce(seq, func_1, func_2):
  sum=0
  for i in seq:
    if func_1(i):
      sum = func_2(sum, i)
  return(sum)
  



