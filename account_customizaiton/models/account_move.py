################################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2019 SmartTek (<https://smartteksas.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

from odoo import _, api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move.line'

    product_hs_code = fields.Char(related='product_id.hs_code')
    product_origin_id = fields.Many2one(related='product_id.origin_id')
    total_weight = fields.Float(compute='_compute_total_weight')

    @api.depends('product_id.weight', 'quantity')
    def _compute_total_weight(self):
        for r in self:
            r.total_weight = r.product_id.weight * r.quantity
