# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# Не очень понял, где тут надо использовать цикл и для чего

s = abs(int(input('Введите число S: ')))
p = abs(int(input('Введите число P: ')))
print(s - (p // 2), p // 2)