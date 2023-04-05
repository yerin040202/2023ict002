A, B = map(int, input() .split())
C = int(input())
print(A+(B+C)//60, (B+C)%60) if A+(B+C)//60<=23 and (B+C) else print(A+(B+C)//60-24, (B+C)%60)