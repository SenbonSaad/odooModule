# -*- coding: utf-8 -*-
# from odoo import http


# class TransportMarchandise(http.Controller):
#     @http.route('/transport_marchandise/transport_marchandise', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/transport_marchandise/transport_marchandise/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('transport_marchandise.listing', {
#             'root': '/transport_marchandise/transport_marchandise',
#             'objects': http.request.env['transport_marchandise.transport_marchandise'].search([]),
#         })

#     @http.route('/transport_marchandise/transport_marchandise/objects/<model("transport_marchandise.transport_marchandise"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('transport_marchandise.object', {
#             'object': obj
#         })
