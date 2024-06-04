def split_tsv(input_file, output_file, num_lines):
    with open(input_file, 'r', encoding='utf-8') as infile:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for _ in range(num_lines):
                line = infile.readline()
                if not line:
                    break
                outfile.write(line)

split_tsv('data.tsv', 'small_data.tsv', 10000)  # 只读取前10000行
