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
    _inherit = 'account.move'

    kros_classifier = fields.Char(
        string='Classifier',
        copy=False,
    )

    @api.depends('posted_before', 'state', 'journal_id', 'date')
    def _compute_name(self):
        res = super()._compute_name()

        for move in self.filtered(lambda m: m.name != '/' and m.kros_classifier):
            move.name = move.kros_classifier

        return res

    def _get_last_sequence_domain(self, relaxed=False):
        """Get the sql domain to retreive the previous sequence number.
        :param relaxed: see _get_last_sequence.

        :returns: tuple(where_string, where_params): with
            where_string: the entire SQL WHERE clause as a string.
            where_params: a dictionary containing the parameters to substitute
                at the execution of the query.
        """
        where_string, param = super()._get_last_sequence_domain(relaxed)
        where_string += " AND kros_classifier IS NULL"
        return where_string, param
