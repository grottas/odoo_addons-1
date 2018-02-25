# -*- coding: utf-8 -*-
{
    'name': "Sarinah Auto Parts System",

    'summary': """
        This module adds new menu called Spare Part. It adds Merk Kendaraan, Model Kendaraan and Merk Spare Part fields to product.""",

    'description': """
        Add 'Merk Kendaraan' and 'Tipe Kendaraan' fields to product. 
        This allows Sarinah Motor to organize their products based on 'Merk Kendaraan' and 'Tipe Kendaraan'.
    """,

    'author': "Budi Hartono",
    'website': "http://www.recoremedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/autopart_spec.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}