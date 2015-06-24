from openerp import models, fields, api

'''
This is a practice module and should be ignored
'''

class Course(models.Model):

    '''
    This class is  for me
    '''
    
    _name = 'openacademy.course'  # Model name
    name = fields.Char(string='Title', required=True)  # FIeld reserved to identify name rec
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.users', 
                                     ondelete = 'set null', 
                                     string = "Responsible",
                                     index = True)
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")
