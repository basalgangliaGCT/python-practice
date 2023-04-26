import os
import time

def follow(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)
            continue
        yield line

def filematch(lines,substr):
    for line in lines:
        if substr in line:
            yield line


def main(argv):
    import report
    portfolio = report.read_portfolio(argv[2])

    for line in follow(argv[1]):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
        
if __name__ == '__main__':
    import sys
    main(sys.argv)

# f = open('Data/stocklog.csv')
# f.seek(0, os.SEEK_END) # Move file pointer 0 bytes from end of file

# while True:
#     line = f.readline()
#     if line == '':
#         time.sleep(0.1) # Sleep briefly and retry
#         continue
#     fields = line.split(',')
#     name = fields[0].strip('"')
#     price = float(fields[1])
#     change = float(fields[4])
#     if change < 0:
#         print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
