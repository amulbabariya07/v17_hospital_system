from odoo import models, fields, api


class hospitalAppointment(models.Model):
    _name = 'patient.appointment'
    _description = 'Hospital Patient Appointment.'

    patient_id = fields.Many2one('hospital.patient', string="Patient Name")