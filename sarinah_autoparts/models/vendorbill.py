from odoo import models, fields, api

class EfakturPurchaseOrder(models.Model):
    _inherit = 'account.invoice'

    vendor_efaktur = fields.Char("No. E-Faktur")

class GiroPayment(models.Model):
    _inherit = 'account.payment'

    giro_number = fields.Char("No. Giro")
    giro_create_date = fields.Char("Tanggal Buat Giro")
    journal_name = fields.Char(string="Journal Name", related="journal_id.name")