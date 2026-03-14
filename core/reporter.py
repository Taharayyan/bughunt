import os

def generate():
    print("\nScan Summary\n")

    for file in os.listdir("results"):
        path = os.path.join("results", file)

        if os.path.isfile(path):
            with open(path, "r", errors="ignore") as f:
                count = len(f.readlines())

            print(f"{file}: {count} entries")
