# -*- coding: utf-8 -*-
{
    'name': "vladislavpb_test",

    'summary': """
        Upgraded version of Sale module with added TEST field
        """,

    'description': """
        Upgraded version of Sale module with added TEST field
    """,

    'author': "VladislavPb",
    'website': "https://github.com/VladislavPb",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/test.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ]
}
