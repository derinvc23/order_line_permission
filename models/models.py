# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    can_edit_so = fields.Html(compute='compute_can_edit_so')

    @api.depends('name', 'state')
    def compute_can_edit_so(self):
        for rec in self:
            if rec.state in ['draft', 'sent'] or rec.env.user.has_group('order_line_permission.group_add_delete_sale_order') or rec.env.user.has_group('sales_team.group_sale_manager'):
                rec.can_edit_so = True
            else:
                rec.can_edit_so = False

    def write(self, values):
        res = super(SaleOrder, self).write(values)
        if 'order_line' in values:
            self.message_post(body="Changes made in Order Line by {}".format(self.env.user.name))
        return res
