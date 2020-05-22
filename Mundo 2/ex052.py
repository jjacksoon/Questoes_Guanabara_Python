s = 0
n = int(input('\nEntre com o número: '))
for c in range(1,n+1):
    if(n % c == 0):
        s += 1
if (s == 2):
    print('\nPRIMO!')
else:
    print('\nNÃO É PRIMO!')
print('\nFIM')
