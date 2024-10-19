def copy_file(file_name_s: str, file_name_d: str) -> None:
    with open (file = file_name_s, mode = 'r', encoding='utf-8') as file_s:
        with open (file = file_name_d, mode = 'w', encoding = 'utf-8') as file_d:
            for line in file_s:
                file_d.write(line)


copy_file ('4/source.txt', '4/destination.txt')
