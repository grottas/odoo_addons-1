# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class sarinah_autoparts(models.Model):
#     _name = 'sarinah_autoparts.sarinah_autoparts'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class AutopartBrand(models.Model):
    _name = 'autopart.brand'

    name = fields.Char('Merk Part', required=True)
    product_ids = fields.One2many(
        'product.template', 'autopart_brand_id', string='Produk Spare Part'
    )

class AutopartVehicleBrand(models.Model):
    _name = 'autopart.vehiclebrand'

    name = fields.Char('Merk Kendaraan', required=True)
    vehiclemodel_ids = fields.One2many(
        'product.template', 'autopart_vehiclebrand_id', string='Model Kendaraan'
    )

class AutopartVehicleModel(models.Model):
    _name = 'autopart.vehiclemodel'

    name = fields.Char('Model Kendaraan', required=True)
    vehiclebrand_id = fields.Many2one(
        'autopart.vehiclebrand', string='Merk Kendaraan',
        ondelete='cascade'
    )
    autopart_vehiclebrand_id = fields.Char('Merk Kendaraan', related='vehiclebrand_id.name')
    product_ids = fields.One2many(
        'product.template', 'autopart_vehiclemodel_id', string='Produk Spare Part'
    )

class ProductPartBrand(models.Model):
    _inherit = 'product.template'

    autopart_brand_id = fields.Many2one(
        'autopart.brand', string='Merk Part',
        ondelete='set null'
    )
    autopart_vehiclemodel_id = fields.Many2one(
        'autopart.vehiclemodel', string='Model Kendaraan',
        ondelete='set null'
    )
    autopart_vehiclebrand_id = fields.Char( 
        'Merk Kendaraan', 
        related='autopart_vehiclemodel_id.autopart_vehiclebrand_id', # Retrieve from Vehicle Model instead of directly access the Vehicle Brand Table
        readonly=True
    )

    # Sementara tidak diperlukan field Tahun Pembuatan terpisah
    # autopart_vehiclemodel_year = fields.Char( 
    #     'Tahun Pembuatan', 
    #     related='autopart_vehiclemodel_id.model_year',
    #     readonly=True
    # )

    # How to do it:
    # https://www.odoo.com/forum/help-1/question/showing-many2one-fields-in-other-modules-102434