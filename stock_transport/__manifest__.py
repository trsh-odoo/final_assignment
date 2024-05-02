# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Transport Management System',
    'version': '1.0',
    'summary': 'Treansport Management System',
    'category': 'Transport Management / fleet picking batch',
    'depends': ['stock_picking_batch','fleet'],
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_model_category_view.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_picking_views.xml'
    ],
    'installable':True,
    'application': True,
    'license': "LGPL-3",

}
