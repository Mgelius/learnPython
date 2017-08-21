# -*- coding: utf-8 -*-
# Georgian (ქართული ენა tr. kartuli ena) is a Kartvelian language
# spoken by Georgians.

# Georgian alphabet has 33 letters. Some sounds do not exist in English as well
# as some English sounds are not present in Georgian.

# Georgia is a very beautiful country and I recommend everyone to visit it.

# I thank my sister Lizi Guchua for help.

# And big sorry some names are done completely wrong when this simple/stupid method is used.

yourname = input()
yournameLower = yourname.lower()
new = list(yournameLower)

new = [w.replace('a', 'ა') for w in new]
new = [w.replace('b', 'ბ') for w in new]
new = [w.replace('c', 'ც') for w in new]
new = [w.replace('d', 'დ') for w in new]
new = [w.replace('e', 'ე') for w in new]
new = [w.replace('f', 'ფ') for w in new]
new = [w.replace('g', 'გ') for w in new]
new = [w.replace('h', 'ჱ') for w in new]
new = [w.replace('i', 'ი') for w in new]
new = [w.replace('j', 'ჟ') for w in new]
new = [w.replace('k', 'კ') for w in new]
new = [w.replace('l', 'ლ') for w in new]
new = [w.replace('m', 'მ') for w in new]
new = [w.replace('n', 'ნ') for w in new]
new = [w.replace('o', 'ო') for w in new]
new = [w.replace('p', 'პ') for w in new]
new = [w.replace('q', 'ქ') for w in new]
new = [w.replace('r', 'რ') for w in new]
new = [w.replace('s', 'ს') for w in new]
new = [w.replace('t', 'თ') for w in new]
new = [w.replace('u', 'უ') for w in new]
new = [w.replace('v', 'ვ') for w in new]
new = [w.replace('w', 'ვ') for w in new]
new = [w.replace('x', 'ხ') for w in new]
new = [w.replace('y', 'ყ') for w in new]
new = [w.replace('z', 'ზ') for w in new]

print(*new, sep='')
