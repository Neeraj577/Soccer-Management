from application import app, db
from flask import render_template, request, url_for, redirect, flash
from application.models import SoccerMgmt 


@app.route('/', methods=['GET'] )
def home():
    total = SoccerMgmt.query.all()
    # print(total)
    return render_template('index.html', players=total)



@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/about', methods=['GET','POST'])
def about():
    #query all the players info
    players_db = SoccerMgmt.query.all()

    return render_template('players.html', players = players_db)

@app.route('/add', methods=['POST','GET'])
def add():
    if request.method == 'POST':
        name = request.form.get('name')
        position = request.form.get('position')
        age_group = request.form.get('age_group')
        day = request.form.get('day')
        fav_club = request.form.get('fav_club')

        entry = SoccerMgmt(name=name, position=position, age_group=age_group, day=day, fav_club=fav_club)
        db.session.add(entry)
        db.session.commit()
        flash('Player Added successfully!', 'success')
        return redirect(url_for('home'))

    else:
        return render_template('Add_contact.html')

@app.route('/player/<int:id>', methods=['GET'])
def profile(id):
    player = SoccerMgmt.query.get_or_404(id)

    
    return render_template('profile.html', player=player)

# Add route for deleting a player
@app.route("/delete/<int:id>", methods=['POST'])
def delete(id):
    player = SoccerMgmt.query.get_or_404(id)
    db.session.delete(player)
    db.session.commit()
    flash('Player deleted successfully!', 'success')
    return redirect(url_for('about'))

@app.route('/login')
def login():
    return render_template('base.html')

@app.route('/register')
def register():
    return render_template('base.html')