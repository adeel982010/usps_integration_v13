from odoo import models, api
#from custom.usps_integration_v13.usps_integration.models import endicia
import logging

_logger = logging.getLogger(__name__)


class refund_request(models.TransientModel):
    _name = "refund.request"

    def action_refund_request(self):
        """
        This function is used to Cancel shipping label based on the carrier type chosen in the delivery order
        parameters:
            No Parameters
        """
        picking_obj = self.env['stock.picking']
        if self._context.get('active_ids', False):
            active_ids = self._context.get('active_ids', False)
        for picking in picking_obj.browse(self._context['active_ids']):
            if picking.shipping_type.lower() == 'usps':
                result = self.with_context().action_refund_request_usps()
            if picking.shipping_type.lower() == 'ups':
                result = self.with_context().action_refund_request_ups()
        return {'type': 'ir.actions.act_window_close'}
