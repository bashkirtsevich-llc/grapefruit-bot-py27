def str_escape(string):
    return "".join(
        x for x in string if x.isalpha() or x.isdigit() or x == " "
    )


def is_info_hash(string):
    if string is not None:
        try:
            _ = int(string, 16)
            return len(string) == 40
        except ValueError:
            return False
    else:
        return False


def get_files_size(files):
    return sizeof_fmt(reduce(lambda r, e: r + e["length"], files, 0))


def sizeof_fmt(num, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)

        num /= 1024.0

    return "%.1f %s%s" % (num, "Y", suffix)
