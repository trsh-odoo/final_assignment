# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Inventory',
    'version': '1.1',
    'summary': 'Manage your stock and logistics activities',
    'website': 'https://www.odoo.com/app/inventory',
    'depends': ['product', 'barcodes_gs1_nomenclature', 'digest','stock'],
    'category': 'Inventory/Inventory',
    'data': [
        
        'views/res_config_settings_views.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
