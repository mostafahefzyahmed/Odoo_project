from odoo import models, fields


class Department(models.Model):
    _name = "hms.department"
    _description = "Hospital Management System - Department"

    name = fields.Char("Name")
    capacity = fields.Integer("Capacity")
    is_opened = fields.Boolean()
    patients_ids = fields.One2many("hms.patient", "department_id", string="Patients")
    doctors_ids = fields.One2many('hms.doctor', 'department_id', string='Doctors')

