A, B, C = map(int, input() .split())
max=A if A>B else B
max=C if C>max else max
if A==B==C :
  print(10000+A*1000)
elif A==B or B==C or A==C :
  if A==B or B==C :
    print(1000+B*100)
  else :
    print(1000+C*100)
else :
  print(max*100)