from odoo import models, fields, api

class Schedule(models.Model):
    _name = 'hospital.schedule'
    _description = 'Doctor Schedule'

    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    date = fields.Date(string='Date', required=True)
    start_time = fields.Float(string='Start Time', required=True)
    end_time = fields.Float(string='End Time', required=True)
    patient_ids = fields.Many2many('hospital.patient', string='Patients')