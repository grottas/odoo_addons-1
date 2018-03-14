from odoo import models, fields, api

class EfakturPurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    vendor_efaktur = fields.Char("No. E-Faktur")
