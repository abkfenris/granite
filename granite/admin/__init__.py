from flask_admin import Admin
from flask_admin.contrib.geoa import ModelView as _ModelView
from flask_admin.model import InlineFormAdmin

from granite.models import db, Project, Path, Slope, Parking


MAP_HEIGHT_WIDTH = {'data-height': 400, 'data-width': 600}


class ModelView(_ModelView):
    pass


class InlineForm(InlineFormAdmin):
    form_widget_args = {'geom': MAP_HEIGHT_WIDTH}


class ProjectView(ModelView):
    inline_models = (InlineForm(Slope), InlineForm(Path), InlineForm(Parking))
    form_widget_args = {'geom': MAP_HEIGHT_WIDTH}


admin = Admin(name='Granite BC Mapping', template_mode='bootstrap3')
admin.add_view(ProjectView(Project, db.session))
admin.add_view(ModelView(Slope, db.session))
admin.add_view(ModelView(Path, db.session))
admin.add_view(ModelView(Parking, db.session))
