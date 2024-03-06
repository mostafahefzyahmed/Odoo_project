from odoo import fields, models


class Ticket(models.Model):
    _name = 'todo.ticket'  #: the model name (in dot-notation, module namespace)
    _description = 'Ticket'  #: the model's informal name

    name = fields.Char()
    number = fields.Integer()
    tag = fields.Char()
    state = fields.Selection([
        ('new', 'New'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    ])
    assigned_to = fields.Many2one('res.users')
    description = fields.Text()
    file = fields.Binary()



