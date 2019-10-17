# -*- coding: utf-8 -*-

from odoo import fields, models

class FleetVehicle(models.Model):
    _inherit = "fleet.vehicle"

    transport_driver_id = fields.Many2one("hr.employee", string="Conductor")
