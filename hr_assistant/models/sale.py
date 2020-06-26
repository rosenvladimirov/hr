# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    assistant_user_ids = fields.Many2many('hr.employee', string='Sales assistant', track_visibility='onchange')
