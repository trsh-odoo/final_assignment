# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields, models

class FleetVehicleModelCategory(models.Model):
    
    _inherit = "fleet.vehicle.model.category" 
    _description = "extended fleet vehicle model category"
    
    max_weight = fields.Float(string= "Max Weight (Kg)")
    max_volume = fields.Float(string="Max Volume (m³)")
    
    @api.depends('name','max_weight','max_volume')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name}({record.max_weight}kg {record.max_volume}m³)"
        
    
    
    
    
    
    

