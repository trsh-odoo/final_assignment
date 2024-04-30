# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class StockPickingBatchInherit(models.Model):

    # using inheritance to inherit stock.picking.batch to our module and add custom fields Extension inheritance
#When using _inherit but leaving out _name, the new model replaces the existing one, essentially extending it in place
    _inherit = "stock.picking.batch"
    
# Many2one -> for many record of this model there is one record related in comodel), have _id suffix ,column is created in current model
    dock_id = fields.Many2one('dock', string="Dock")
    vehicle = fields.Many2one('fleet.vehicle', required=False)
    vehicle_category = fields.Many2one('fleet.vehicle.model.category')
    package_batch_id = fields.Many2one('stock.picking')
    weight = fields.Float(readonly=True)
    volume = fields.Float(readonly=True)
    
    # compute fields :
    # only computes at run time no data stored in table if wants to store data set store=True
    number_of_line = fields.Integer(compute='_compute_number_of_lines',store=True)
    number_of_transfers = fields.Integer(compute='_compute_number_of_lines',store=True)
    weight_percent = fields.Float( compute='_compute_weight_percent', string="weight")
    volume_percent = fields.Float(compute='_compute_volume_percent', string="volume")
    
#computing total volume in a given batch line
    @api.depends('picking_ids', 'vehicle_category')
    def _compute_volume_percent(self):
        for record in self:
            total_volume = sum(picking.volume for picking in record.picking_ids)
            self.volume = total_volume
            if record.vehicle_category.max_volume>0:
                record.volume_percent = ( total_volume / record.vehicle_category.max_volume)*100
            else:
                record.volume_percent = 0.0

# computing total weight in a given batch line
    def _compute_weight_percent(self):
        for record in self:
            total_weight = sum( picking.weight for picking in record.picking_ids)
            self.weight = total_weight
            if record.vehicle_category.max_weight>0:
                record.weight_percent = (total_weight / record.vehicle_category.max_weight)*100
            else:
                record.weight_percent = 0.0
    
# computing number of lines and transfers in a given batch
    @api.depends('picking_ids', 'move_line_ids')
    def _compute_number_of_lines(self):
        for batch in self:
            batch.number_of_transfers = len(batch.picking_ids)
            batch.number_of_line = sum(len(picking.move_line_ids) for picking in batch.picking_ids)

