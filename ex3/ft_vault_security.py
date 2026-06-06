def secure_archive(file_name: str, action: str = "r",
                   content: str = "") -> tuple[bool, str]:
    try:
        if action == "r":
            with open(file_name, action) as file:
                return (True, file.read())
        elif action == "w":
            with open(file_name, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
        return (False, "Invalid action")
    except Exception as e:
        return (False, f"{e}")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    file_name = "/not/existing/file"
    ret_tuple = secure_archive(file_name, "r")
    print(f"{ret_tuple}")
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    file_name = "/etc/shadow"
    ret_tuple = secure_archive(file_name, "r")
    print(f"{ret_tuple}")
    print("\nUsing 'secure_archive' to read from a regular file:")
    file_name = "ancient_fragment.txt"
    ret_tuple = secure_archive(file_name, "r")
    print(f"{ret_tuple}")
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    file_name = "new_file.txt"
    ret_tuple = secure_archive(file_name, "w", ret_tuple[1])
    print(f"{ret_tuple}")


if __name__ == "__main__":
    main()
