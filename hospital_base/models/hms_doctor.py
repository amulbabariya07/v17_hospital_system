from odoo import models, fields, api

class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor'

    name = fields.Char(string='Name', required=True)
    specialization = fields.Selection([
        ('general', 'General Physician'),
        ('cardio', 'Cardiologist'),
        ('ortho', 'Orthopedic'),
        ('neuro', 'Neurologist'),
        ('derma', 'Dermatologist'),
    ], string='Specialization', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    schedule_ids = fields.One2many('hospital.schedule', 'doctor_id', string='Schedules')
    active = fields.Boolean(string='Active', default=True)

