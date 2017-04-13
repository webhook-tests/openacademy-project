from openerp import models, fields, api


class Course(models.Model):

    '''
    class for the openacademy course model
    '''

    _name = 'openacademy.course'  # Model name
    # Field reserved to identify name rec
    course_name = fields.Char(string='Title', required=True)
    description = fields.Char(string='Description')
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

    @api.one  # api.one send default params: cr, uid, id context
    def copy(self, default=None):
        if default is None:
            default = {}
        copied_count = self.search_count(
            [('name', '=like', "{} (copy%)".format(self.name))])
        if not copied_count:
            new_name = ("{} (copy)").format(self.name)
        else:
            new_name = ("{} (copy {})").format(self.name, copied_count)
        default['name'] = new_name
        return super(Course, self).copy(default)
