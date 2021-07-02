
# 수온 계산기
depth = int(input('수심: '))
waTemp = 20 - (depth / 10) * 0.7
print(f'수온: {waTemp:.1f}')

