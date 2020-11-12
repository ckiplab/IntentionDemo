from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from app.control import control

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    print("form")
    if form.validate_on_submit():
        print('fff')
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        return redirect(url_for(control(command)))
    print('dddd')
    return render_template('index.html', title='Intention Demo', form=form, pattern='pattern')


@app.route('/lll', methods=['GET', 'POST'])
def lll():
    form = LoginForm()
    print("form")
    if form.validate_on_submit():
        print('fff')
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        return redirect(url_for(control(command)))
    print('dddd')
    return render_template('index1.html', title='Intention Demo', form=form, pattern='pattern')



