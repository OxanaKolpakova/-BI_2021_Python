import matplotlib.pyplot as plt
class my_class(object):

    
    def __init__(self, path):
        self.path = path


    def num_seq(self):
        with open(self.path) as f:
            count = 0
            while(True):
                line = f.readline()
                if line.find(">") != -1:
                    count += 1
                if not line:
                    break
        return(count)

    def hist(self):
        seq_length = []
        with open(self.path) as f:
            count = 0
            while(True): 
                line = f.readline()
                if line.find(">") == -1:
                    count += len(line)                   
                else:
                    print(count)
                    seq_length.append(count)
                    count = 0             
                if not line:
                    break
        seq_length.append(count)
        plt.plot(seq_length[1:])
        plt.show()
        return(seq_length[1:])

    def GC(self):
        with open(self.path) as f:
            count_all = 0
            count_GC = 0
            while(True):
                line = f.readline()
                if line.find(">") == -1:
                    count_all += len(line)
                    count_GC += line.count("G")+line.count("C")
                if not line:
                    break
        return(count_GC/count_all)
    
