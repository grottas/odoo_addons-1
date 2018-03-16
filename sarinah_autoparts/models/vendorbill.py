from odoo import models, fields, api

class EfakturPurchaseOrder(models.Model):
    _inherit = 'account.invoice'

    vendor_efaktur = fields.Char("No. E-Faktur")