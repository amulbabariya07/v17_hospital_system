from odoo import models, fields, api

class hospitalAppointment(models.Model):
    _name = 'patient.appointment'
    _description = 'Hospital Patient Appointment'

    patient_id = fields.Many2one('hospital.patient', string="Patient Name")
    gender = fields.Selection(selection=[('male', 'Male'),('female', 'Female'),('other', 'Other'),],string="Gender")

    @api.onchange('patient_id')
    def _onchange_patient(self):
        if self.patient_id:
            self.gender = self.patient_id.gender