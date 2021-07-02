import os, sys

if len(sys.argv) < 2:
    os.system(f"ls")
elif len(sys.argv) == 2:
    os.system(f"ls {sys.argv[1]}")
elif len(sys.argv) == 3:
    if '-' in sys.argv[1]:
        os.system(f"ls {sys.argv[1]} {sys.argv[2]}")
    else:
        os.system(f"ls {sys.argv[2]} {sys.argv[1]}")
