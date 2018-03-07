# -*- coding: utf-8 -*-
{
    'name': "Barcode Scanning",

    'summary': """
        Enable barcode scanning for product input in sale order""",

    'description': """
        Enable barcode scanning for product input in sale order. This module will help you to use barcode scanner in sales.
    """,

    'author': "Recore",
    'website': "http://www.recoremedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.5',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}