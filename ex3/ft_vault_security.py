def secure_archive(file_name: str, *options: str) -> tuple[bool, str]:
    try:
        with open(file_name, options[0]) as file:
            if options[0] == "r":
                return (True, file.read())
            elif options[0] == "w":
                file.write(options[1])
                return (True, "Content successfully written to file")
    except Exception as e:
        return (False, f"{e}")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    file_name = "/not/existing/file"
    ret_tuple = secure_archive(file_name, "r")
    print(f"{ret_tuple}\n")
    print("Using 'secure_archive' to read from an inaccessible file:")
    file_name = "/etc/shadow"
    ret_tuple = secure_archive(file_name, "r")
    print(f"{ret_tuple}\n")
    print("Using 'secure_archive' to read from a regular file:")
    file_name = "ancient_fragment.txt"
    ret_tuple = secure_archive(file_name, "r")
    print(f"{ret_tuple}\n")
    print("Using 'secure_archive' to write previous content to a new file:")
    file_name = "new_file.txt"
    ret_tuple = secure_archive(file_name, "w", ret_tuple[1])
    print(f"{ret_tuple}\n")


if __name__ == "__main__":
    main()
