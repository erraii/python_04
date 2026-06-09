import sys
import typing


def main() -> None:
    total_arguments = len(sys.argv)
    if (total_arguments != 2):
        print("Usage: ft_ancient_text.py <file>\n")
        return
    print("=== Cyber Archives Recovery ===")
    file_name = sys.argv[1]
    f: typing.IO[str] | None = None
    try:
        print(f"Accessing file '{file_name}'")
        f = open(file_name)
        print(f.encoding)
        print(type(f))
        print("---\n")
        print(f.read())
        print("---")
    except Exception as e:
        print(f"Error opening file '{file_name}': {e}\n")
        return
    finally:
        if f is not None:
            f.close()
            print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
