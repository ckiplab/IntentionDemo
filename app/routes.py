from app import app
from flask import render_template, flash, request, redirect, url_for
from app.forms import LoginForm
from app.control import ctrl

CMD_LIST = [
    ('aboutYou', '關於你',),
    ('request', '要求',),
    ('beauty_care', '美容',),
    ('choose', '選擇',),
    ('else_recommend', '推薦其他',),
    ('goodbye', '道別',),
    ('greeting', '打招呼',),
    ('help_decision', '幫助選擇',),
    ('inform', '告知',),
    ('noidea', '不知道',),
    ('react', '使用者回饋',),
    ('reset', '清除',),
    ('search_item', '尋找物件',),
    ('search_makeup', '尋找妝容',),
    ('skinBad', '皮膚不好',),
    ('thanks', '感謝',),
]

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    pattern_string = ""

    pattern = request.args.get('pattern')
    suggestions = []
    if pattern:
        sug = ctrl.intent_pattern[pattern]
        for s in sug:
            if s.find('name') == -1:
                suggestions.append(s)

    if form.validate_on_submit():
        print('fff')
        command = form.inputtext.data
        flash('已輸入指令: {}'.format(command))
        cmd_string, pattern_string = ctrl.control(command)
        zh_string = ""
        for k in CMD_LIST:
            if k[0] == cmd_string:
                zh_string = k[1]
        flash('Pattern: [{} {}] {}'.format(cmd_string, zh_string, pattern_string))
        # return redirect(url_for(cmd_string))
        print(cmd_string)
        return render_template('index.html', title='Intention Demo', form=form, cmd=cmd_string, cmd_list=CMD_LIST, suggestions=suggestions)
    return render_template('index.html', title='Intention Demo', form=form, cmd="", cmd_list=CMD_LIST, suggestions=suggestions)


# @app.route('/aboutYou', methods=['GET', 'POST'])
# def aboutYou():
#     form = LoginForm()
#     pattern_string = ""
#     if form.validate_on_submit():
#         command = form.inputtext.data
#         flash('已輸入指令: {}'.format(command))
#         cmd_string, pattern_string = control(command)
#         flash('Pattern: {}'.format(pattern_string))
#         return redirect(url_for(cmd_string))
#     return render_template('aboutYou.html', title='Intention Demo', form=form, pattern=pattern_string)

# @app.route('/request', methods=['GET', 'POST'])
# def request():
#     form = LoginForm()
#     pattern_string = ""
#     if form.validate_on_submit():
#         command = form.inputtext.data
#         flash('已輸入指令: {}'.format(command))
#         cmd_string, pattern_string = control(command)
#         flash('Pattern: {}'.format(pattern_string))
#         return redirect(url_for(cmd_string))
#     return render_template('request.html', title='Intention Demo', form=form, pattern=pattern_string)

# @app.route('/beauty_care', methods=['GET', 'POST'])
# def beauty_care():
#     form = LoginForm()
#     pattern_string = ""
#     if form.validate_on_submit():
#         command = form.inputtext.data
#         flash('已輸入指令: {}'.format(command))
#         cmd_string, pattern_string = control(command)
#         flash('Pattern: {}'.format(pattern_string))
#         return redirect(url_for(cmd_string))
#     return render_template('beauty_care.html', title='Intention Demo', form=form, pattern=pattern_string)

# @app.route('/choose', methods=['GET', 'POST'])
# def choose():
#     form = LoginForm()
#     pattern_string = ""
#     if form.validate_on_submit():
#         command = form.inputtext.data
#         flash('已輸入指令: {}'.format(command))
#         cmd_string, pattern_string = control(command)
#         flash('Pattern: {}'.format(pattern_string))
#         return redirect(url_for(cmd_string))
#     return render_template('choose.html', title='Intention Demo', form=form, pattern=pattern_string)

# @app.route('/else_recommend', methods=['GET', 'POST'])
# def else_recommend():
#     form = LoginForm()
#     pattern_string = ""
#     if form.validate_on_submit():
#         command = form.inputtext.data
#         flash('已輸入指令: {}'.format(command))
#         cmd_string, pattern_string = control(command)
#         flash('Pattern: {}'.format(pattern_string))
#         return redirect(url_for(cmd_string))
#     return render_template('else_recommend.html', title='Intention Demo', form=form, pattern=pattern_string)

# @app.route('/goodbye', methods=['GET', 'POST'])
# def goodbye():
#     form = LoginForm()
#     pattern_string = ""
#     if form.validate_on_submit():
#         command = form.inputtext.data
#         flash('已輸入指令: {}'.format(command))
#         cmd_string, pattern_string = control(command)
#         flash('Pattern: {}'.format(pattern_string))
#         return redirect(url_for(cmd_string))
#     return render_template('goodbye.html', title='Intention Demo', form=form, pattern=pattern_string)

# @app.route('/greeting', methods=['GET', 'POST'])
# def greeting():
#     form = LoginForm()
#     pattern_string = ""
#     if form.validate_on_submit():
#         command = form.inputtext.data
#         flash('已輸入指令: {}'.format(command))
#         cmd_string, pattern_string = control(command)
#         flash('Pattern: {}'.format(pattern_string))
#         return redirect(url_for(cmd_string))
#     return render_template('greeting.html', title='Intention Demo', form=form, pattern=pattern_string)

# @app.route('/help_decision', methods=['GET', 'POST'])
# def help_decision():
#     form = LoginForm()
#     pattern_string = ""
#     if form.validate_on_submit():
#         command = form.inputtext.data
#         flash('已輸入指令: {}'.format(command))
#         cmd_string, pattern_string = control(command)
#         flash('Pattern: {}'.format(pattern_string))
#         return redirect(url_for(cmd_string))
#     return render_template('help_decision.html', title='Intention Demo', form=form, pattern=pattern_string)

# @app.route('/inform', methods=['GET', 'POST'])
# def inform():
#     form = LoginForm()
#     pattern_string = ""
#     if form.validate_on_submit():
#         command = form.inputtext.data
#         flash('已輸入指令: {}'.format(command))
#         cmd_string, pattern_string = control(command)
#         flash('Pattern: {}'.format(pattern_string))
#         return redirect(url_for(cmd_string))
#     return render_template('inform.html', title='Intention Demo', form=form, pattern=pattern_string)

# @app.route('/noidea', methods=['GET', 'POST'])
# def noidea():
#     form = LoginForm()
#     pattern_string = ""
#     if form.validate_on_submit():
#         command = form.inputtext.data
#         flash('已輸入指令: {}'.format(command))
#         cmd_string, pattern_string = control(command)
#         flash('Pattern: {}'.format(pattern_string))
#         return redirect(url_for(cmd_string))
#     return render_template('noidea.html', title='Intention Demo', form=form, pattern=pattern_string)

# @app.route('/react', methods=['GET', 'POST'])
# def react():
#     form = LoginForm()
#     pattern_string = ""
#     if form.validate_on_submit():
#         command = form.inputtext.data
#         flash('已輸入指令: {}'.format(command))
#         cmd_string, pattern_string = control(command)
#         flash('Pattern: {}'.format(pattern_string))
#         return redirect(url_for(cmd_string))
#     return render_template('react.html', title='Intention Demo', form=form, pattern=pattern_string)

# @app.route('/reset', methods=['GET', 'POST'])
# def reset():
#     form = LoginForm()
#     pattern_string = ""
#     if form.validate_on_submit():
#         command = form.inputtext.data
#         flash('已輸入指令: {}'.format(command))
#         cmd_string, pattern_string = control(command)
#         flash('Pattern: {}'.format(pattern_string))
#         return redirect(url_for(cmd_string))
#     return render_template('reset.html', title='Intention Demo', form=form, pattern=pattern_string)

# @app.route('/search_item', methods=['GET', 'POST'])
# def search_item():
#     form = LoginForm()
#     pattern_string = ""
#     if form.validate_on_submit():
#         command = form.inputtext.data
#         flash('已輸入指令: {}'.format(command))
#         cmd_string, pattern_string = control(command)
#         flash('Pattern: {}'.format(pattern_string))
#         return redirect(url_for(cmd_string))
#     return render_template('search_item.html', title='Intention Demo', form=form, pattern=pattern_string)

# @app.route('/search_makeup', methods=['GET', 'POST'])
# def search_makeup():
#     form = LoginForm()
#     pattern_string = ""
#     if form.validate_on_submit():
#         command = form.inputtext.data
#         flash('已輸入指令: {}'.format(command))
#         cmd_string, pattern_string = control(command)
#         flash('Pattern: {}'.format(pattern_string))
#         return redirect(url_for(cmd_string))
#     return render_template('search_makeup.html', title='Intention Demo', form=form, pattern=pattern_string)

# @app.route('/skinBad', methods=['GET', 'POST'])
# def skinBad():
#     form = LoginForm()
#     pattern_string = ""
#     if form.validate_on_submit():
#         command = form.inputtext.data
#         flash('已輸入指令: {}'.format(command))
#         cmd_string, pattern_string = control(command)
#         flash('Pattern: {}'.format(pattern_string))
#         return redirect(url_for(cmd_string))
#     return render_template('skinBad.html', title='Intention Demo', form=form, pattern=pattern_string)

# @app.route('/thanks', methods=['GET', 'POST'])
# def thanks():
#     form = LoginForm()
#     pattern_string = ""
#     if form.validate_on_submit():
#         command = form.inputtext.data
#         flash('已輸入指令: {}'.format(command))
#         cmd_string, pattern_string = control(command)
#         flash('Pattern: {}'.format(pattern_string))
#         return redirect(url_for(cmd_string))
#     return render_template('thanks.html', title='Intention Demo', form=form, pattern=pattern_string)

# @app.route('/nomatch', methods=['GET', 'POST'])
# def nomatch():
#     form = LoginForm()
#     pattern_string = ""
#     if form.validate_on_submit():
#         print("nomatch")
#         command = form.inputtext.data
#         flash('已輸入指令: {}'.format(command))
#         cmd_string, pattern_string = control(command)
#         flash('Pattern: {}'.format(pattern_string))
#         return redirect(url_for(cmd_string))
#     return render_template('nomatch.html', title='Intention Demo', form=form, pattern=pattern_string)
















