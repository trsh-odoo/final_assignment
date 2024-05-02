# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class FleetStockPicking(models.Model):
    _inherit = "stock.picking"
    
    volume = fields.Float(string="Volume", compute='_compute_shipping_volume_weight')
    weight = fields.Float(string="Weight", compute='_compute_shipping_volume_weight')
    
    
    @api.depends('move_ids')
    def _compute_shipping_volume_weight(self):
        for record in self:
            for move in record.move_ids:
                record.volume += move.product_id.volume*move.product_uom_qty
                record.weight += move.product_id.weight*move.product_uom_qty
    