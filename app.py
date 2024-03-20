from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired

# Flask application instance
app = Flask(__name__)

# secret key for the application
app.secret_key = 'secret_key'


# FlaskForm class for the feedback form using WTForms
class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    student_number = StringField('Student Number', validators=[DataRequired()])
    email = TextAreaField('Email', validators=[DataRequired()])
    grades = TextAreaField('Grades', validators=[DataRequired()])
    satisfaction = SelectField('Overall Satisfaction', choices=[('', 'Select Satisfaction Level'),
                                                                ('very-satisfied', 'Very Satisfied'),
                                                                ('satisfied', 'Satisfied'),
                                                                ('neutral', 'Neutral'),
                                                                ('unsatisfied', 'Unsatisfied'),
                                                                ('very-unsatisfied', 'Very Unsatisfied')],
                               validators=[DataRequired()])
    improvements = TextAreaField('Suggestions for Improvement')


# route for the root URL to handle GET and POST requests
@app.route('/submit', methods=['GET', 'POST'])
def feedback():
    # an instance of the FeedbackForm class
    form = FeedbackForm()

    print("test",request,form)
    # Checking if the form is submitted and valid
    if request.method == 'POST':
        # Get data from the form
        for i in form:
            print(i.data)
        name = form.name.data
        student_number = form.student_number.data
        email = form.email.data
        grades = form.grades.data
        satisfaction = form.satisfaction.data
        improvements = form.improvements.data

        # Storing data in a text file
        with open('feedback.txt', 'a') as file:
            file.write(f'Name: {name}\n')
            file.write(f'Students-Number: {student_number}\n')
            file.write(f'Email: {email}\n')
            file.write(f'Grades: {grades}\n')
            file.write(f'Overall Satisfaction: {satisfaction}\n')
            file.write(f'Suggestions for Improvement: {improvements}\n\n')

        # Returning a success message if the form is submitted successfully
        return 'Feedback submitted successfully!'

    # Render the forms.html template with the form instance
    return render_template('forms.html', form=form)


@app.route('/welcomepage.html')
def welcome():
    return render_template('welcomepage.html')


@app.route('/')
def redirect():
    return render_template('welcomepage.html')


@app.route('/informationpage.html')
def information():
    return render_template('informationpage.html')


@app.route('/tips.html')
def tips():
    return render_template('tips.html')


@app.route('/forms.html')
def forms():
    return render_template('forms.html')


# Running the Flask application
if __name__ == '__main__':
    app.run(debug=True)
