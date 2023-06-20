# -*- coding: utf-8 -*-
{
    'name': "transport_marchandise",

    'summary': """
       management of the marchandise transportation""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Nouhaila-etu",
    'website': "https://www.transport.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/commande.xml',
        'views/vehicule.xml',
        'views/facture.xml',
        'views/paiement.xml',
        'security/ir.model.access.csv'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
