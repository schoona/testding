dier = 'hond'
naam = 'Bello'
gewicht = 9.523445

print('Mijn {} heet {} en weegt {} kilo'.format(dier, naam, gewicht))
print(f'Mijn {dier} heet {naam}')
print('{1}, {0}, {1}, {leeftijd}, {2:.2f}'.format(dier, naam, gewicht, leeftijd=5))

for i in range(3,6):
    print("{:<6} {:6d} {:6d}".format(f"label{i}", i*i, i*i*i))