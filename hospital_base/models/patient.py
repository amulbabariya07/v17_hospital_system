from odoo import models, fields, api


class hospital(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Patient's full name", required=True, tracking=True)
    age =  fields.Integer(string="Patient's age", tracking=True)
    gender = fields.Selection(selection=[('male', 'Male'),('female', 'Female'),('other', 'Other'),],string="Gender", tracking=True)
    blood_type = fields.Selection(selection=[('a+', 'A+'),('a-', 'A-'),('b+', 'B+'),('b-', 'B+'),('o+', 'O+'),('o-', 'O+'),('ab+', 'AB+'),('ab-', 'AB-'),], tracking=True)
    contact_number = fields.Char(string="Phone Numbers", tracking=True)
    email = fields.Char(string="Email", tracking=True)
    address = fields.Html(string="Address", tracking=True)
    emergency_contact = fields.Char("Emergency Contact", tracking=True)
    is_emergency_case = fields.Boolean(string="Is Emergency Case", tracking=True)

