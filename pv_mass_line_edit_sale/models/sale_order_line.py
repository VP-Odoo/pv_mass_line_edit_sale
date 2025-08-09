# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    select_all_lines = fields.Boolean(
        string='Select All Lines',
        default=False,
        help='Master toggle: when checked, all lines get “Apply to All”'
    )

    @api.onchange('select_all_lines')
    def _onchange_select_all_lines(self):
        for order in self:
            # write to all lines at once
            order.order_line.write({'apply_all': order.select_all_lines})


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    apply_all = fields.Boolean(
        string='Apply to All',
        default=False,
        help='When checked, changes you make on any “applied” line propagate to all'
    )

    @api.onchange('apply_all')
    def _onchange_apply_all(self):
        # auto-check all lines if user checks one
        if self.apply_all and self.order_id:
            self.order_id.order_line.write({'apply_all': True})

    def write(self, vals):
        # avoid recursive propagation
        if not self.env.context.get('mass_edit_propagation'):
            # isolate the fields to propagate (everything except the checkbox)
            to_propagate = {k: v for k, v in vals.items() if k != 'apply_all'}
            if to_propagate and any(line.apply_all for line in self):
                # collect all lines on each order that are “applied”
                lines = self.env['sale.order.line']
                for line in self.filtered('apply_all'):
                    siblings = line.order_id.order_line.filtered(
                        lambda l: l.apply_all and l.id != line.id
                    )
                    lines |= siblings
                # do one bulk write under a flag to skip recursion
                if lines:
                    lines.with_context(mass_edit_propagation=True).write(to_propagate)
        # finally write normally on the current record(s)
        return super(SaleOrderLine, self).write(vals)
