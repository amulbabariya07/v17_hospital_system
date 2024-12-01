from odoo import models, fields, api

class hospitalPrescriptionLine(models.Model):
    _name = 'hospital.prescription.line'
    _description = 'Hospital Prescription Line'

    medicine_id = fields.Char(string="Medicine", required=True)
    dosage = fields.Char(string="Dosage", required=True)  
    frequency = fields.Selection(
        [('once', 'Once a Day'), ('twice', 'Twice a Day'), ('thrice', 'Three Times a Day'), ('custom', 'Custom')],
        string="Frequency",
        required=True
    )
    duration = fields.Integer(string="Duration (days)", required=True)
    notes = fields.Text(string="Notes")
    appointment_id = fields.Many2one('hospital.patient', string="Appointmnet", required=True)