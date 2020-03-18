# 예제
def hanoi(n, from_pos, to_pos, temp_pos):
    if n==1:
        print(from_pos, '->' , to_pos)
        return
    
    hanoi(n-1,from_pos, temp_pos, to_pos)
    print(from_pos, '->', to_pos)

    hanoi(n-1, temp_pos, to_pos, from_pos)

hanoi(2, 1, 3, 2)