import sys
import typing


def main() -> None:
    total_arguments = len(sys.argv)
    if (total_arguments != 2):
        print("Usage: ft_archive_creation.py <file>")
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
        print(f"Error opening file '{file_name}': {e}")
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
        print(f"Error opening file '{file_name}': {e}")
        return
    finally:
        if f is not None:
            f.close()
    new_file = input("Enter new file name (or empty): ")
    if new_file:
        print(f"Saving data to '{new_file}'")
        try:
            f = open(new_file, "w")
            f.write(data)
        except Exception as e:
            print(f"Error opening file '{new_file}': {e}")
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
