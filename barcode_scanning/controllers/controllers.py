# -*- coding: utf-8 -*-
from odoo import http

# class SarinahBarcodeScanning(http.Controller):
#     @http.route('/sarinah_barcode_scanning/sarinah_barcode_scanning/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sarinah_barcode_scanning/sarinah_barcode_scanning/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sarinah_barcode_scanning.listing', {
#             'root': '/sarinah_barcode_scanning/sarinah_barcode_scanning',
#             'objects': http.request.env['sarinah_barcode_scanning.sarinah_barcode_scanning'].search([]),
#         })

#     @http.route('/sarinah_barcode_scanning/sarinah_barcode_scanning/objects/<model("sarinah_barcode_scanning.sarinah_barcode_scanning"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sarinah_barcode_scanning.object', {
#             'object': obj
#         })