import os
import django

# Configurer l'environnement Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'An_ka_Wosso.settings')
django.setup()

from main.models import Product

# Fonction pour peupler la base de données
def populate():
    products = [
        {
        'name': 'Chips Épicées',
        'description': 'Croquantes et savoureuses, nos chips de patate douce épicées sont préparées avec un mélange d\'épices exotiques qui raviront vos papilles. Parfaites pour les amateurs de sensations fortes, ces chips apportent une touche piquante à vos collations.',
        'price': 2000,
        'weight': '200g',
        'categorie': 'Herbe'
    },
    {
        'name': 'Chips Non Épicées',
        'description': 'Nos chips de patate douce nature sont idéales pour ceux qui préfèrent la simplicité et la pureté des ingrédients naturels. Avec leur goût légèrement sucré et leur texture croquante, elles constituent une collation saine et délicieuse.',
        'price': 1500,
        'weight': '200g',
        'categorie': 'Herbe'
    },
    {
        'name': 'Farine de Patate Douce Naturelle',
        'description': 'Obtenue à partir de patates douces rigoureusement sélectionnées, notre farine de patate douce naturelle est riche en fibres et en nutriments. Elle est parfaite pour toutes vos recettes de pain, pâtisseries et autres préparations culinaires.',
        'price': 3000,
        'weight': '1kg',
        'categorie': 'Aliment'
    },
    {
        'name': 'Farine de Patate Douce Sucrée',
        'description': 'Pour ajouter une note sucrée à vos préparations, notre farine de patate douce sucrée est l\'ingrédient idéal. Enrichie avec du sucre naturel, elle est parfaite pour les desserts, les gâteaux et autres douceurs maison.',
        'price': 2500,
        'weight': '1kg',
        'categorie': 'Aliment'
        }
    ]

    for product_data in products:
        product, created = Product.objects.get_or_create(**product_data)
        if created:
            print(f"Produit {product.name} créé.")
        else:
            print(f"Produit {product.name} déjà existant.")

if __name__ == '__main__':
    populate()
