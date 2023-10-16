kms = int(input())
stallTime = int(input())

# fare because of dist
dist_fare = 0

if kms<=10:
    dist_fare= kms*10 # first 10 kms have the same rate of 10
elif kms<=10+40:
    dist_fare= 10*10 # first 10 kms have the same rate of 10
    remaining_kms = kms-10
    dist_fare=dist_fare+remaining_kms*9 # 11th km to 50th km fare is Rs 9 per Km
elif kms<=10+40+100:
    dist_fare= 10*10 # first 10 kms have the same rate of 10
    remaining_kms = kms-10
    dist_fare=dist_fare+40*9 # 11th km to 50th km fare is Rs 9 per Km
    remaining_kms = remaining_kms-40
    dist_fare=dist_fare+remaining_kms*8 # 50th km to 150th km fare is Rs 8 per Km
else:
    dist_fare= 10*10 # first 10 kms have the same rate of 10
    remaining_kms = kms-10
    dist_fare=dist_fare+40*9 # 11th km to 50th km fare is Rs 9 per Km
    remaining_kms = remaining_kms-40
    dist_fare=dist_fare+100*8 # 50th km to 150th km fare is Rs 8 per Km
    remaining_kms = remaining_kms-100
    dist_fare=dist_fare+remaining_kms*6 ## Any leftover km count - Rs. 6 per Km

# fare because of stall
stall_fare = 0
stall_fare = stallTime*5

# final fare
print('dist_fare:', dist_fare)
print('stall_fare:', stall_fare)
print('Total fare:', dist_fare+stall_fare)
