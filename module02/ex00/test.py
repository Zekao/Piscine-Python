from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce

x = [1, 2, 3, 4, 5]

print(ft_map(lambda dum: dum + 1, x))

map_test = iter(x)
print(ft_map(lambda dum: dum + 1, map_test))

filter_test = list(ft_filter(lambda dum: not (dum % 2), x))
print(filter_test)

lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
lst = ft_reduce(lambda u, v: u + v, lst)
print (lst)