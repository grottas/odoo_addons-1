# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BarcodeScanningSalesOrder(models.Model):
    _inherit = 'sale.order.line'

    barcode_scan = fields.Char(string='Barcode', help='Here you can provide the barcode for the product')

    @api.onchange('barcode_scan')
    def _onchange_barcode_scan(self):
        product_rec = self.env['product.product']
        if self.barcode_scan:
            product = product_rec.search([('barcode', '=', self.barcode_scan)])
            self.product_id = product.id