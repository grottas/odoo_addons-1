# -*- coding: utf-8 -*-
from odoo import http

# class SarinahAutoparts(http.Controller):
#     @http.route('/sarinah_autoparts/sarinah_autoparts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sarinah_autoparts/sarinah_autoparts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sarinah_autoparts.listing', {
#             'root': '/sarinah_autoparts/sarinah_autoparts',
#             'objects': http.request.env['sarinah_autoparts.sarinah_autoparts'].search([]),
#         })

#     @http.route('/sarinah_autoparts/sarinah_autoparts/objects/<model("sarinah_autoparts.sarinah_autoparts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sarinah_autoparts.object', {
#             'object': obj
#         })