import random
import threading
import time

class MaxThread(threading.Thread):
    def __init__(self,lo,hi,list_nums):
        threading.Thread.__init__(self)
        self.lo = lo
        self.hi = hi
        self.list_nums = list_nums
        self.Max = 0
    
    def run(self):
        self.set_Max()
    def set_Max(self):
        i = self.lo
        while i < self.hi:
            self.Max = self.list_nums[i]
            i += 1
        return
    
    def get_sum(self):
        return self.sum
    
    def print_list(self):
        str_list = ''
        i = self.lo
        while i < self.hi:
            str_list += str(self.list_nums[i]) + '; '
            i += 1
        return str_list
    
def tinh_tong(list_numbers, n_threads):
    tong = 0
    so_pt = len(list_numbers)
    list_threads = []

    i = 0
    while i < n_threads:
        lo = int((i*so_pt)/n_threads)
        hi = int((i+1)*so_pt/n_threads)
        thread = SumThread(lo, hi, list_numbers)
        list_threads.append(thread)
        list_threads[i].start()
        i += 1
        
    j = 0
    while j < n_threads:
        list_threads[j].join()
        tong += list_threads[j].get_sum()
        print("Thread", j+1, ":", list_threads[j].print_list())
        j += 1

    return tong

if __name__ == "__main__":
    list_numbers = []
    n = int(input("Nhap vao so phan tu: "))
    i = 0
    while i < n:
        list_numbers.append(random.randrange(10))
        i += 1
    
    print("List:",list_numbers)
    n_threads = int(input("Nhap vao so thread: "))
    sum = tinh_tong(list_numbers, n_threads);
    print("Tong list=",sum)