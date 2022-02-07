from email import message
from wtforms import Form, StringField
from wtforms.validators import Length, DataRequired


class SearchForm(Form):
    keyword = StringField(
        validators=[DataRequired(), Length(min=1, max=30)],
        description='keyword',
    )
