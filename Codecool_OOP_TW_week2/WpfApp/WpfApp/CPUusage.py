import psutil
import sys


p = psutil.Process(int(sys.argv[1]))
print(p.cpu_percent(interval=1.0))

