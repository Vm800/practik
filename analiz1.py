import os
def get_size(path):
    total_size = 0
    if os.path.isdir(path):
        for dp, _, fn in os.walk(path):
            for f in fn:
                try:
                    total_size += os.path.getsize(os.path.join(dp, f))
                except FileNotFoundError:
                    pass
    else:
        try:
            total_size = os.path.getsize(path)
        except FileNotFoundError:
            pass
    return total_size
def main():
    items = [(item, get_size(item)) for item in os.listdir() if os.path.isfile(item) or os.path.isdir(item)]
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    for item, size in sorted_items:
        print(f"{item:<30}{size:>15} байт")
if __name__ == "__main__":
    main()

