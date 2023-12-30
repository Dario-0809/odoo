from odoo import models, fields

class Contact(models.Model):
    _name = "contact.info"
    _description = "Contact Information"

    name = fields.Char(string='Name', required=True)
    birthdate = fields.Date(string='Birthdate')
    phone = fields.Char(string='Phone')
    
    
    def unlink(self):
        return super(Contact, self).unlink()
    
    def button_done(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Contacts',
            'res_model': 'contact.info',
            'view_mode': 'tree,form',
            'view_id': False,
            'target': 'main',
        }