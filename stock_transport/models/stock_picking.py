# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from collections import defaultdict


class FleetStockPicking(models.Model):
    _inherit = "stock.picking"

    
    volume = fields.Float(string="Volume", compute='_compute_shipping_volume')
    weight = fields.Float(string="Weight", compute='_compute_shipping_weight')
    
    
    @api.depends('move_ids')
    def _compute_shipping_volume(self):
        for record in self:
            for product in record.move_ids:
                record.volume += product.product_id.volume*product.product_uom_qty
                
    @api.depends('move_ids')
    def _compute_shipping_weight(self):
        for record in self:
            for product in record.move_ids:
                record.weight += product.product_id.weight*product.product_uom_qty
    