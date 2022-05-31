# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
{
    'name': 'Odoo WooCommerce Customization',
    'version': '14.0.2.0.6',
    'category': 'Sales',
    'summary': 'Odoo Woocommerce Connector helps you automate your vital business processes at Odoo by enabling '
               'bi-directional data exchange between WooCommerce & Odoo.',

    'author': 'SmartTekSas',
    'website': "http://smartteksas.com",
    'maintainer': 'SmartTekSas',
    'depends': [
        'woo_commerce_ept',
    ],
    'data': [
        'data/ir_actions_server_data.xml',
        'data/ir_config_parameter_data.xml',
        'data/mail_activity.xml',
        'data/product_data.xml',
        'views/product_category_view.xml',
        'views/product_template_view.xml',
        'views/product.xml',
        'views/sale_order_views.xml',
        'views/product_pricelist_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
