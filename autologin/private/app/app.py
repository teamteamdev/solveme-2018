from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Regexp

app = Flask(__name__)
app.secret_key = 'Very Secret. Such Key.'


class LoginForm(FlaskForm):
    login = StringField('Username', validators=[DataRequired(),
                                                Regexp(r'^user$', message='Invalid username')])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Regexp(r'^so_insecure$',
                                                            message='Invalid password')])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        session['user'] = True
    return render_template('index.html', title='Dummy site', form=form)


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
