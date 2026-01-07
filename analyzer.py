def analyze_log(filename):
    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    with open(filename, "r") as file:
        for line in file:
            for level in counts:
                if level in line:
                    counts[level] += 1

    return counts


if __name__ == "__main__":
    result = analyze_log("sample.log")

    for level, count in result.items():
        print(f"{level}: {count}")
