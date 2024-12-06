def __init__(self, total, used):
        self.total = total
        self.used = used

@property
def free(self):
        return self.total - self.used

@property
def usedperc(self):
        return self.used / self.total

def __str__(self):
        return f"{self.total} Gb, utilisé : {self.used} Gb]"

def __lt__(self, other):
        return self.usedperc < other.usedperc


if __name__ == '__main__':
    disk1 = Disk(total=10, used=2)
    disk2 = Disk(total=20, used=5)

    print(f"{disk1.free} ")
    print(f"{disk2.free} ")
    print(f"{disk1.usedperc:.2%}")
    print(f"U {disk2.usedperc:.2%}")


    print( disk1)
    print( disk2)


    disks = [disk1, disk2]

    
    disks_sorted = sorted(disks)

    
    for disk in disks_sorted:
        print(disk)
