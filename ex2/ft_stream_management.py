import sys
import typing


def main() -> None:
    total_arguments = len(sys.argv)
    if (total_arguments != 2):
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    file_name = sys.argv[1]
    f: typing.IO[str] | None = None
    try:
        print(f"Accessing file '{file_name}'")
        f = open(file_name)
        print("---\n")
        print(f.read())
        print("---")
    except Exception as e:
        print(f"[STDERR] Error opening file '{file_name}': {e}",
              file=sys.stderr)
        return
    finally:
        if f is not None:
            f.close()
            print(f"File '{file_name}' closed.")
    print("\nTransform data:\n---\n")
    try:
        f = open(file_name)
        data = f.read().replace("\n", "#\n")
        print(data)
        print("---")
    except Exception as e:
        print(f"[STDERR] Error opening file '{file_name}': {e}",
              file=sys.stderr)
        return
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file = sys.stdin.readline().strip()
    if new_file:
        print(f"Saving data to '{new_file}'")
        try:
            f = open(new_file, "w")
            f.write(data)
        except Exception as e:
            print(f"[STDERR] Error opening file: {e}",
                  file=sys.stderr)
            print("Data not saved.")
            return
        else:
            print(f"Data saved in file '{new_file}'")
        finally:
            if f is not None:
                f.close()
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
