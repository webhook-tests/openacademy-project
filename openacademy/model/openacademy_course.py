from openerp import models, fields, api, _


class Course(models.Model):

    '''
    class for the openacademy course model
    '''

    _name = 'openacademy.course'  # Model name
    # Field reserved to identify name rec
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.users',
                                     ondelete='set null',
                                     string="Responsible",
                                     index=True)
    session_ids = fields.One2many('openacademy.session',
                                  'course_id',
                                  string="Sessions")

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]

    @api.one  # api.ode send default params: cr, uid, id context
    def copy(self, default=None):
        if default is None:
            default = {}
        default['name'] = self.name + ' (copy)'
        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            name = _(u"Copy of {}%").format(self.name)
        else:
            name = _(u"Copy of {}%").format(self.name, copied_count)
        return super(Course, self).copy(default)
