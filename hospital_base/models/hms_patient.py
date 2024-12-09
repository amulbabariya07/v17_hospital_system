from odoo import api, fields, models
from datetime import date, datetime, timedelta

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Patient's full name", required=True, tracking=True)
    age = fields.Integer(string="Patient's age", compute="_compute_age", tracking=True)
    age_duration = fields.Char(string="Age Duration", compute="_compute_age_duration", tracking=True)
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender", tracking=True)
    date_of_birth = fields.Date("Date Of Birth")
    blood_type = fields.Selection(selection=[('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b-', 'B+'), ('o+', 'O+'), ('o-', 'O+'), ('ab+', 'AB+'), ('ab-', 'AB-')], tracking=True)
    contact_number = fields.Char(string="Phone Numbers", tracking=True)
    email = fields.Char(string="Email", tracking=True)
    address = fields.Html(string="Address", tracking=True)
    emergency_contact = fields.Char("Emergency Contact", tracking=True)
    is_emergency_case = fields.Boolean(string="Is Emergency Case", tracking=True)
    image = fields.Binary(attachment=True, tracking=True)  
    active = fields.Boolean(string="Active", default=True)
    hospital_prescription_line = fields.One2many(
        comodel_name='hospital.prescription.line', 
        inverse_name='appointment_id',
        string='Statement lines',
        required=True,
    )
    doctor_ids = fields.Many2many(
        comodel_name="hospital.doctor",  
        string="Doctor Assign"       
    )
    patient_code = fields.Char(string="Patient Code", readonly=True, copy=False)


    @api.depends("date_of_birth")
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.date_of_birth:
                age = today.year - record.date_of_birth.year - ((today.month, today.day) < (record.date_of_birth.month, record.date_of_birth.day))
                record.age = age
            else:
                record.age = 0 

    @api.depends("date_of_birth")
    def _compute_age_duration(self):
        for record in self:
            if record.date_of_birth:
                delta = datetime.now() - datetime.combine(record.date_of_birth, datetime.min.time())
                
                years = delta.days // 365
                months = (delta.days % 365) // 30
                days = (delta.days % 365) % 30
                hours = delta.seconds // 3600

                age_duration = f"{years} Years, {months} Months, {days} Days, {hours} Hours"
                record.age_duration = age_duration
            else:
                record.age_duration = "N/A"

    @api.model
    def create(self, vals):
        date_str = datetime.now().strftime('%Y%m%d')
        sequence = self.env['ir.sequence'].next_by_code('hospital.patient.sequence')
        if sequence:
            patient_code = f"PAT-{date_str}{sequence}"
        else:
            patient_code = f"PAT-{date_str}0001"
        
        vals['patient_code'] = patient_code
        return super(HospitalPatient, self).create(vals)    