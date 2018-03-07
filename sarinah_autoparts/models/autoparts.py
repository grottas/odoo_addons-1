# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductPartBrand(models.Model):
    _inherit = 'product.template'

    autopart_brand_id = fields.Many2one(
        'autopart.brand', string='Merk Part',
        ondelete='set null'
    )
    autopart_part_number = fields.Char('Part Number')
    # autopart_vehicletype_id = fields.Many2one(
    #     'autopart.vehicletype', string='Tipe Kendaraan',
    #     ondelete='set null'
    # )
    autopart_vehicletype_ids = fields.Many2many(
        'autopart.vehicletype', string='Tipe Kendaraan',
    )

class AutopartBrand(models.Model):
    _name = 'autopart.brand'

    name = fields.Char('Merk Part', required=True)
    product_ids = fields.One2many(
        'product.template', 'autopart_brand_id', string='Produk Spare Part'
    )

class AutopartVehicleBrand(models.Model):
    _name = 'autopart.vehiclebrand'

    name = fields.Char('Merk Kendaraan', required=True)
    
class AutopartVehicleType(models.Model):
    _name = 'autopart.vehicletype'

    name = fields.Char('Model Kendaraan', required=True)
    vehiclebrand_id = fields.Many2one(
        'autopart.vehiclebrand', string='Merk Kendaraan',
        ondelete='cascade',
        required=True
    )
    autopart_vehiclebrand_id = fields.Char('Merk Kendaraan', related='vehiclebrand_id.name')

    # product_ids = fields.One2many(
    #     'product.template', 'autopart_vehicletype_id', string='Produk Spare Part'
    # )