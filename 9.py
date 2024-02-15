dads_playlist=str(input("Введите плей-лист папы: "))
mums_playlist=[]
for a in range(5):
    mums_playlist.append(input())
print("Плей-лист мамы: ", mums_playlist[::-1])
