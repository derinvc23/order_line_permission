# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def write(self, values):
        res = super(SaleOrder, self).write(values)
        if 'order_line' in values:
            self.message_post(body="Changes made in Order Line by {}".format(self.env.user.name))
        return res
