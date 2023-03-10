# -*- coding: utf-8 -*-
# from odoo import http


# class TokoHp(http.Controller):
#     @http.route('/toko__hp/toko__hp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/toko__hp/toko__hp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('toko__hp.listing', {
#             'root': '/toko__hp/toko__hp',
#             'objects': http.request.env['toko__hp.toko__hp'].search([]),
#         })

#     @http.route('/toko__hp/toko__hp/objects/<model("toko__hp.toko__hp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('toko__hp.object', {
#             'object': obj
#         })
