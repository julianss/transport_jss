# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class PickingTransportInfo(models.Model):
    _name = 'picking.transport.info'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    _order= 'id desc'

    name = fields.Char(string='Number',readonly=True)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('cotizado', 'Cotizado'),
        ('cancel', 'Cancel')
    ], default='draft', track_visibility='onchange', copy=False)
    saleorder_id = fields.Many2one('sale.order', string="Pedido de venta")
    vehicle_id = fields.Many2one('fleet.vehicle', string="Vehículo")
    vehicle_driver = fields.Many2one('hr.employee', string="Conductor")
    transport_date = fields.Datetime(string='Fecha', required=True, default=fields.Datetime.now())
    customer_id = fields.Many2one('res.partner', string='Cliente')
    lr_number = fields.Char(string="LR Number", store=True)
    picking_route_ids = fields.One2many('picking.route', 'transport_info_id', string='Picking Route', copy=True)
    user_id = fields.Many2one('res.users', string='Responsable', default=lambda self: self.env.user.id)
    company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id, string='Compañía', readonly=True)
    note = fields.Text('Notas')

    @api.model
    def create(self, vals):
        name = self.env['ir.sequence'].next_by_code('picking.transport.seq')
        vals.update({
        'name': name
        })
        return super(PickingTransportInfo, self).create(vals)

    @api.multi
    def unlink(self):
        for rec in self:
            if rec.state != 'cancel':
                raise Warning("No se puede borrar a menos que esté cancelado")
        return super(PickingTransportInfo, self).unlink()

    @api.multi
    def cancelar(self):
        for rec in self:
            rec.write({'state':'cancel'})

    @api.multi
    def cotizar(self):
        sale_vals = {
            'partner_id': self.customer_id.id,
            'pricelist_id': self.customer_id.property_product_pricelist and self.customer_id.property_product_pricelist.id or False,
            'payment_term_id': self.customer_id.property_payment_term_id and self.customer_id.property_payment_term_id.id or False,
            'user_id': self.customer_id.user_id.id or self.customer_id.commercial_partner_id.user_id.id or self.env.uid,
            'company_id': self.company_id.id,
            'order_line': []
        }
        sale = self.env["sale.order"].create(sale_vals)
        for route in self.picking_route_ids:
            line_vals = {
                'order_id': sale.id,
                'product_id': route.product_id.id,
                'product_uom_qty': 1,

            }
            line = self.env["sale.order.line"].create(line_vals)
        self.write({'saleorder_id': sale.id, 'state':'cotizado'})
        return True


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
