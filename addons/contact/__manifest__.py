{
    'name': "Contacts",
    'version': '1.0',
    'summary': 'Contact Management',
    'sequence': 1,
    'depends': ['base'],
    'author': "Dao Hai Long",
    'category': 'Tools',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/info_views.xml',
    ],
    # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}