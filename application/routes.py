import cv2
import os
import secrets
from PIL import Image
from flask import render_template,url_for,flash,redirect,request,Response
from wtforms import form
from application import app,db,bcrypt
from camera import VideoCamera
from application.models import User,List
from application.forms import RegistrationForm,LoginForm,UpdateAccountForm,ListForm
from flask_login import login_user,current_user,logout_user,login_required
import PoseModule as pm


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/list_of_exercise")
@login_required
def list_of_exercise():
    lists=List.query.all()
    return render_template("list_of_exercise.html", lists=lists)

@app.route("/about")
def about():
    return render_template("about.html",title='About')

@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('list_of_exercise'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('list_of_exercise'))
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page=request.args.get('next')
            return redirect(url_for(next_page.replace('/',''))) if next_page else redirect(url_for('list_of_exercise'))
        else:    
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex= secrets.token_hex(8)
    _,f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path,'static','profile_pics',picture_fn)
    
    output_size = (250,250)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route("/account",methods=['GET','POST'])
@login_required
def account():
    form=UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        prev_username=current_user.username
        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash(f"Account is updated",'success')
    elif request.method =='GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static',filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',image_file=image_file,form=form)


@app.route("/list/new",methods=['GET','POST'])
@login_required
def new_list():
    form=ListForm()
    if form.validate_on_submit():
        flash('New Exercise added to the list!','success')
        list=List(title=form.title.data , content=form.content.data , author=current_user)
        db.session.add(list)
        db.session.commit()
        return redirect(url_for('list_of_exercise'))
    return render_template('create_list.html', title='New Exercise',form=form,legend='Add New Exercise')


@app.route("/list/<int:list_id>")
def list(list_id):
    list=List.query.get_or_404(list_id)
    return render_template('list.html',title=list.title,list=list)


@app.route("/list/<int:list_id>/update",methods=['GET','POST'])
@login_required
def update_list(list_id):
    list=List.query.get_or_404(list_id)
    form=ListForm()
    if form.validate_on_submit():
        list.title=form.title.data
        list.content=form.content.data
        db.session.commit()
        flash('This Exercise has been updated!','success')
        return redirect(url_for('list',list_id=list.id))
    elif request.method =='GET':
        form.title.data=list.title
        form.content.data=list.content
    return render_template('create_list.html', title='Update Exercise',form=form,legend='Update Exercise')


@app.route("/list/<int:list_id>/delete",methods=['GET','DELETE'])
@login_required
def delete_list(list_id):
    list=List.query.get_or_404(list_id)
    db.session.delete(list)
    db.session.commit()
    flash('Exercise was deleted!','success')
    return redirect(url_for('list_of_exercise'))


def generate_frames(camera,list_id):
    list=List.query.get_or_404(list_id)
    pT=0
    lT=list.title
    detector  = pm.PoseDetector()
    amin = 180
    amax = 0
    count = 0
    dir = 0
    while True:
        ## read the camera frame
        data,pTime,l_title,ami,ama,cou,direc = camera.get_frame(pT,lT,amin,amax,count,dir)
        pT=pTime
        lT=l_title
        amin=ami
        amax=ama
        count=cou
        dir=direc
        frame = data[0]
        if not frame:
            break
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video/<int:list_id>')
@login_required
def video(list_id):
    list=List.query.get_or_404(list_id)
    return Response(generate_frames(VideoCamera(),list_id=list.id),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/vidtrain/<int:list_id>')
@login_required
def vidtrain(list_id):
    list=List.query.get_or_404(list_id)
    return render_template('vidtrain.html',title='Video Training',list=list)
