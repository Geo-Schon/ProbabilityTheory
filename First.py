# Задача 1. Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все 4 карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.


from Combi import combinations

a = combinations(13, 4)
b = combinations(52, 4)
# print(f'm = {a}, n = {b}')

club = a / b
print(f'Вероятность, что все 4 карты крести = {round(club, 4)*100}%')

# club = 13 / 52 * 12 / 51 * 11 / 50 * 10 / 49


ace = 1 - combinations(48, 4) / combinations(52, 4)
print(f'Вероятность, что есть 1 туз = {round(ace, 4)*100}%')


# с = sum([combinations(4, 1) * combinations(48, 3), combinations(4, 2) * combinations(48, 2),
#          combinations(4, 3) * combinations(48, 1), 1])

