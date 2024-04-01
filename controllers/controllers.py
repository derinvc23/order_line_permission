# -*- coding: utf-8 -*-
from odoo import http

# class OrderLinePermission(http.Controller):
#     @http.route('/order_line_permission/order_line_permission/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/order_line_permission/order_line_permission/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('order_line_permission.listing', {
#             'root': '/order_line_permission/order_line_permission',
#             'objects': http.request.env['order_line_permission.order_line_permission'].search([]),
#         })

#     @http.route('/order_line_permission/order_line_permission/objects/<model("order_line_permission.order_line_permission"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('order_line_permission.object', {
#             'object': obj
#         })