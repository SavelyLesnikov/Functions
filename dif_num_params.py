def test(*dif_params):
    print(*dif_params)


test(573, '* Развернул кортеж - так красивее *', True)


def rec_factor(n):
    if n == 1:
        return 1
    else:
        return n * rec_factor(n-1)


print(rec_factor(7))
