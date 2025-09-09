def format_string(string):
    return ' '.join(string.strip().split())

def right_align(lines):
    max_len = max(len(line) for line in lines)
    return [line.rjust(max_len) for line in lines]

def main():
    first_case = True
    
    while True:
        try:
            line_input = input()
            if not line_input:
                break
            N = int(line_input)
        except (EOFError, ValueError):
            break

        if N == 0:
            break

        if not first_case:
            print()
        
        lines = [format_string(input()) for _ in range(N)]
        align_lines = right_align(lines)
        
        for line in align_lines:
            print(line)
            
        first_case = False

if __name__ == "__main__":
    main()