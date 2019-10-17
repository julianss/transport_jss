# -*- coding: utf-8 -*-

from odoo import fields, models

class PickingRoute(models.Model):
    _name = 'picking.route'
    _rec_name = 'source_location'

    transport_info_id = fields.Many2one("picking.route.info", string="Transport Info", required=True)
    cliente = fields.Many2one("res.partner", string="Cliente")
    product_id = fields.Many2one("product.product", string="Producto", required=True)
    source_location = fields.Many2one('route.location',string='Origen', required=True)
    destination_location = fields.Many2one('route.location',string='Destino',required=True)
    distance = fields.Float('KMS')
    cap_carga = fields.Float("Cap. Carga")
    maniobras = fields.Char("Maniobras")
    repartos = fields.Char("Repartos")
    recoleccion = fields.Char("Recolección")
    fecha_carga = fields.Datetime("Fecha carga")
    fecha_entrega = fields.Datetime("Fecha entrega")
    state = fields.Selection([
        ('start','Salida'),
        ('onroute','En ruta'),
        ('halt','Detenido'),
        ('reach','Llegada'),
    ], string="Estatus")
    

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
