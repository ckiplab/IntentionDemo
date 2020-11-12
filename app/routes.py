from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from app.control import control

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    pattern_string = ""

    if form.validate_on_submit():
        print('fff')
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        cmd_string, pattern_string = control(command)
        flash('Pattern: {}'.format(pattern_string))
        return redirect(url_for(cmd_string))
    return render_template('index.html', title='Intention Demo', form=form, pattern=pattern_string)


@app.route('/aboutYou', methods=['GET', 'POST'])
def aboutYou():
    form = LoginForm()
    pattern_string = ""
    if form.validate_on_submit():
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        cmd_string, pattern_string = control(command)
        flash('Pattern: {}'.format(pattern_string))
        return redirect(url_for(cmd_string))
    return render_template('aboutYou.html', title='Intention Demo', form=form, pattern=pattern_string)

@app.route('/request', methods=['GET', 'POST'])
def request():
    form = LoginForm()
    pattern_string = ""
    if form.validate_on_submit():
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        cmd_string, pattern_string = control(command)
        flash('Pattern: {}'.format(pattern_string))
        return redirect(url_for(cmd_string))
    return render_template('request.html', title='Intention Demo', form=form, pattern=pattern_string)

@app.route('/beauty_care', methods=['GET', 'POST'])
def beauty_care():
    form = LoginForm()
    pattern_string = ""
    if form.validate_on_submit():
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        cmd_string, pattern_string = control(command)
        flash('Pattern: {}'.format(pattern_string))
        return redirect(url_for(cmd_string))
    return render_template('beauty_care.html', title='Intention Demo', form=form, pattern=pattern_string)

@app.route('/choose', methods=['GET', 'POST'])
def choose():
    form = LoginForm()
    pattern_string = ""
    if form.validate_on_submit():
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        cmd_string, pattern_string = control(command)
        flash('Pattern: {}'.format(pattern_string))
        return redirect(url_for(cmd_string))
    return render_template('choose.html', title='Intention Demo', form=form, pattern=pattern_string)

@app.route('/else_recommend', methods=['GET', 'POST'])
def else_recommend():
    form = LoginForm()
    pattern_string = ""
    if form.validate_on_submit():
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        cmd_string, pattern_string = control(command)
        flash('Pattern: {}'.format(pattern_string))
        return redirect(url_for(cmd_string))
    return render_template('else_recommend.html', title='Intention Demo', form=form, pattern=pattern_string)

@app.route('/goodbye', methods=['GET', 'POST'])
def goodbye():
    form = LoginForm()
    pattern_string = ""
    if form.validate_on_submit():
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        cmd_string, pattern_string = control(command)
        flash('Pattern: {}'.format(pattern_string))
        return redirect(url_for(cmd_string))
    return render_template('goodbye.html', title='Intention Demo', form=form, pattern=pattern_string)

@app.route('/greeting', methods=['GET', 'POST'])
def greeting():
    form = LoginForm()
    pattern_string = ""
    if form.validate_on_submit():
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        cmd_string, pattern_string = control(command)
        flash('Pattern: {}'.format(pattern_string))
        return redirect(url_for(cmd_string))
    return render_template('greeting.html', title='Intention Demo', form=form, pattern=pattern_string)

@app.route('/help_decision', methods=['GET', 'POST'])
def help_decision():
    form = LoginForm()
    pattern_string = ""
    if form.validate_on_submit():
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        cmd_string, pattern_string = control(command)
        flash('Pattern: {}'.format(pattern_string))
        return redirect(url_for(cmd_string))
    return render_template('help_decision.html', title='Intention Demo', form=form, pattern=pattern_string)

@app.route('/inform', methods=['GET', 'POST'])
def inform():
    form = LoginForm()
    pattern_string = ""
    if form.validate_on_submit():
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        cmd_string, pattern_string = control(command)
        flash('Pattern: {}'.format(pattern_string))
        return redirect(url_for(cmd_string))
    return render_template('inform.html', title='Intention Demo', form=form, pattern=pattern_string)

@app.route('/noidea', methods=['GET', 'POST'])
def noidea():
    form = LoginForm()
    pattern_string = ""
    if form.validate_on_submit():
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        cmd_string, pattern_string = control(command)
        flash('Pattern: {}'.format(pattern_string))
        return redirect(url_for(cmd_string))
    return render_template('noidea.html', title='Intention Demo', form=form, pattern=pattern_string)

@app.route('/react', methods=['GET', 'POST'])
def react():
    form = LoginForm()
    pattern_string = ""
    if form.validate_on_submit():
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        cmd_string, pattern_string = control(command)
        flash('Pattern: {}'.format(pattern_string))
        return redirect(url_for(cmd_string))
    return render_template('react.html', title='Intention Demo', form=form, pattern=pattern_string)

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    form = LoginForm()
    pattern_string = ""
    if form.validate_on_submit():
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        cmd_string, pattern_string = control(command)
        flash('Pattern: {}'.format(pattern_string))
        return redirect(url_for(cmd_string))
    return render_template('reset.html', title='Intention Demo', form=form, pattern=pattern_string)

@app.route('/search_item', methods=['GET', 'POST'])
def search_item():
    form = LoginForm()
    pattern_string = ""
    if form.validate_on_submit():
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        cmd_string, pattern_string = control(command)
        flash('Pattern: {}'.format(pattern_string))
        return redirect(url_for(cmd_string))
    return render_template('search_item.html', title='Intention Demo', form=form, pattern=pattern_string)

@app.route('/search_makeup', methods=['GET', 'POST'])
def search_makeup():
    form = LoginForm()
    pattern_string = ""
    if form.validate_on_submit():
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        cmd_string, pattern_string = control(command)
        flash('Pattern: {}'.format(pattern_string))
        return redirect(url_for(cmd_string))
    return render_template('search_makeup.html', title='Intention Demo', form=form, pattern=pattern_string)

@app.route('/skinBad', methods=['GET', 'POST'])
def skinBad():
    form = LoginForm()
    pattern_string = ""
    if form.validate_on_submit():
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        cmd_string, pattern_string = control(command)
        flash('Pattern: {}'.format(pattern_string))
        return redirect(url_for(cmd_string))
    return render_template('skinBad.html', title='Intention Demo', form=form, pattern=pattern_string)

@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    form = LoginForm()
    pattern_string = ""
    if form.validate_on_submit():
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        cmd_string, pattern_string = control(command)
        flash('Pattern: {}'.format(pattern_string))
        return redirect(url_for(cmd_string))
    return render_template('thanks.html', title='Intention Demo', form=form, pattern=pattern_string)

@app.route('/nomatch', methods=['GET', 'POST'])
def nomatch():
    form = LoginForm()
    pattern_string = ""
    if form.validate_on_submit():
        print("nomatch")
        command = form.inputtext.data
        flash('Sentence inputted: {}'.format(command))
        cmd_string, pattern_string = control(command)
        flash('Pattern: {}'.format(pattern_string))
        return redirect(url_for(cmd_string))
    return render_template('nomatch.html', title='Intention Demo', form=form, pattern=pattern_string)
















