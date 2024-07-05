import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'An_ka_Wosso.settings')
django.setup()

from main.models import Product

products = [
    {
        'name': 'Chips Épicées',
        'label': 'Chips de Patate Douce Épicées',
        'description': 'Croquantes et savoureuses, nos chips de patate douce épicées sont préparées avec un mélange d\'épices exotiques qui raviront vos papilles. Parfaites pour les amateurs de sensations fortes, ces chips apportent une touche piquante à vos collations.',
        'price': 500.00,
        'weight': '100 g',
        'categorie': 'chips'
    },
    {
        'name': 'Chips Non Épicées',
        'label': 'Chips de Patate Douce Nature',
        'description': 'Nos chips de patate douce nature sont idéales pour ceux qui préfèrent la simplicité et la pureté des ingrédients naturels. Avec leur goût légèrement sucré et leur texture croquante, elles constituent une collation saine et délicieuse.',
        'price': 500.00,
        'weight': '100 g',
        'categorie': 'chips'
    },
    {
        'name': 'Farine de Patate Douce Naturelle',
        'label': 'Farine de Patate Douce Naturelle',
        'description': 'Obtenue à partir de patates douces rigoureusement sélectionnées, notre farine de patate douce naturelle est riche en fibres et en nutriments. Elle est parfaite pour toutes vos recettes de pain, pâtisseries et autres préparations culinaires.',
        'price': 700.00,
        'weight': '500 g',
        'categorie': 'farine'
    },
   
]

for product in products:
    Product.objects.create(**product)

print("Products have been added to the database.")
