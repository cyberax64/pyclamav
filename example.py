from concurrent.futures import ThreadPoolExecutor, as_completed
import pyclamav
import glob


print("Version: ", pyclamav.get_version())


print("load_database")
print(pyclamav.load_database('database'))
print("Signatures: ", pyclamav.get_numsig())
print("OK")


def scan(file):
    try:
        print(pyclamav.scanfile(file))
    except:
        pass



threads= []
with ThreadPoolExecutor(max_workers=24) as executor:
    for file in glob.glob('*.*', recursive=True):
        threads.append(executor.submit(scan, file))