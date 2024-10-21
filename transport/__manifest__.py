{
    'name': 'transport',
    'version': '1.0',
    'depends': ['base', 'hr'],
    'author': 'Yechi',
    'version': '1.0',
    'data': [
        'security/ir.model.access.csv',
        'views/ticket_view.xml',
        'wizards/chan_chaffeur.xml',
        'views/voiture_view.xml',
        'views/voyage_view.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
