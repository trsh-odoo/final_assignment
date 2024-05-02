# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class StockPickingBatchInherit(models.Model):

    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one('dock', string="Dock")
    vehicle_id = fields.Many2one('fleet.vehicle', required=False)
    vehicle_category_id = fields.Many2one('fleet.vehicle.model.category')
    weight = fields.Float(readonly=True)
    volume = fields.Float(readonly=True)
    
    lines = fields.Integer(string="lines ", compute='_compute_number_of_lines',store=True)
    transfers = fields.Integer( string="Transfers ", compute='_compute_number_of_lines',store=True)
    weight_percent = fields.Float(compute='_compute_weight_percent', string="weight")
    volume_percent = fields.Float(compute='_compute_volume_percent', string="volume")

    @api.depends('picking_ids', 'vehicle_category_id')
    def _compute_volume_percent(self):
        for record in self:
            total_volume = sum(picking.volume for picking in record.picking_ids)
            record.volume = total_volume
            record.volume_percent = (total_volume / record.vehicle_category_id.max_volume) * 100 if record.vehicle_category_id.max_volume > 0 else 0.0

    @api.depends('picking_ids', 'vehicle_category_id')
    def _compute_weight_percent(self):
        for record in self:
            total_weight = sum(picking.weight for picking in record.picking_ids)
            record.weight = total_weight
            record.weight_percent = (total_weight / record.vehicle_category_id.max_weight) * 100 if record.vehicle_category_id.max_weight > 0 else 0.0

    @api.depends('picking_ids', 'move_line_ids')
    def _compute_number_of_lines(self):
        for record in self:
            record.transfers = len(record.picking_ids)
            record.lines = len(record.move_line_ids)
            
            

