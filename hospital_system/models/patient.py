from odoo import models, fields, api


class hospital(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string="Patient's full name")
    age =  fields.Integer(string="Patient's age")
    gender = fields.Selection(selection=[('male', 'Male'),('female', 'Female'),('other', 'Other'),],string="Gender")
    blood_type = fields.Selection(selection=[('a+', 'A+'),('a-', 'A-'),('b+', 'B+'),('b-', 'B+'),('o+', 'O+'),('o-', 'O+'),('ab+', 'AB+'),('ab-', 'AB-'),])
    contact_number = fields.Char(string="Phone Numbers")
    email = fields.Char(string="Email")
    address = fields.Html(string="Address")
    emergency_contact = fields.Char("Emergency Contact")
    is_emergency_case = fields.Boolean(string="Is Emergency Case")