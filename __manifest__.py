{
    'name': 'DGII Reports',
    'version': '1.0.0',
    'summary': 'Reportes DGII para República Dominicana',
    'description': 'Módulo para generación de reportes DGII (606, 607, 608, etc.)',
    'author': 'Miguel Angel Mateo Collado',
    'category': 'Accounting',
    'depends': [
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/dgii_report_views.xml',
        'data/dgii_data.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
