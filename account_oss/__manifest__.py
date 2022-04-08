################################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2021 SmartTek (<https://smartteksas.com>).
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

{
    'name': "Account OSS",
    'version': '14.0.1.0.1',
    'category': 'Accounting/Accounting',
    'author': 'Smart Tek Solutions and Services',
    'website': "https://smartteksas.com/",
    'depends': [
        'account',
        'woo_commerce_magnety',
    ],
    'data': [
        'views/account_move_views.xml',
        'views/woo_payment_gateway_views.xml',
    ],
    'license': "AGPL-3",
    'installable': True,
    'application': False,
}
