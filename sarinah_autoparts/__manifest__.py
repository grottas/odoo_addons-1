# -*- coding: utf-8 -*-
{
    'name': "Sarinah Autoparts Module",

    'summary': """
        This module adds new menu called Spare Part. It adds Tipe Kendaraan and Merk Spare Part fields to product.""",

    'description': """
        This module adds new menu called Spare Part and modify some views and reports in Odoo. This module is developed
        to adapt Sarinah Motor Semarang business.

        This module is developed by Recore.
    """,

    'author': "Budi Hartono",
    'website': "http://www.recoremedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/autopart.xml',
        'views/product.xml',
        'views/vendorbill.xml',
        'views/customerinvoice.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}