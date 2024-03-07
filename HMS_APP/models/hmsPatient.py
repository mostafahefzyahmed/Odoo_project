from odoo import models, fields


class Patient(models.Model):
    _name = "hms_patient"
    _description = "Hospital Management System - Patient"
    _rec_name = "f_name"

    f_name = fields.Char("First name")
    l_name = fields.Char("Last name")
    birth_day = fields.Date("Birth date")
    history = fields.Html("History")
    cr_ratio = fields.Float("CR Ratio")
    blood = fields.Selection([
        ("type a", "Type A"),
        ("type b", "Type B"),
        ("type ab", "Type AB"),
        ("type o", "Type O"),
    ])
    pcr = fields.Boolean('PCR')
    image = fields.Binary("Image")
    address = fields.Text("Address")
    age = fields.Integer("Age")
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ])
    department_id = fields.Many2one("hms.department", string="Department")
    doctor_id = fields.Many2one("hms.doctor", string="Doctor")
