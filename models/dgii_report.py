from odoo import models, fields, api

class DgiiReport(models.Model):
    _name = 'dgii.report'
    _description = 'DGII Report'

    name = fields.Char(
        string='Nombre del Reporte',
        required=True
    )
    report_type = fields.Selection(
        [
            ('606', '606 - Compras'),
            ('607', '607 - Ventas'),
            ('608', '608 - Notas de Crédito'),
        ],
        string='Tipo de Reporte',
        required=True
    )
    date_from = fields.Date(string='Fecha Desde')
    date_to = fields.Date(string='Fecha Hasta')
    state = fields.Selection(
        [
            ('draft', 'Borrador'),
            ('generated', 'Generado'),
        ],
        default='draft',
        string='Estado'
    )

    def action_generate_report(self):
        """Lógica para generar el reporte DGII"""
        self.state = 'generated'
