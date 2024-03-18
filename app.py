from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired

# Create a Flask application instance
app = Flask(__name__)

# Set a secret key for the application (used for securely signing session cookies)
app.secret_key = 'secret_key'


# Define a FlaskForm class for the feedback form using WTForms
class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    course = StringField('Course', validators=[DataRequired()])
    short_answer = TextAreaField('Short-form Answer', validators=[DataRequired()])
    long_answer = TextAreaField('Long-form Answer', validators=[DataRequired()])
    satisfaction = SelectField('Overall Satisfaction', choices=[('', 'Select Satisfaction Level'),
                                                                ('very-satisfied', 'Very Satisfied'),
                                                                ('satisfied', 'Satisfied'),
                                                                ('neutral', 'Neutral'),
                                                                ('unsatisfied', 'Unsatisfied'),
                                                                ('very-unsatisfied', 'Very Unsatisfied')],
                               validators=[DataRequired()])
    recommend = RadioField('Would you recommend this course to others?', choices=[('yes', 'Yes'), ('no', 'No')],
                           validators=[DataRequired()])
    improvements = TextAreaField('Suggestions for Improvement')


# Define a route for the root URL ('/') to handle GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def feedback():
    # Create an instance of the FeedbackForm class
    form = FeedbackForm()

    # Check if the form is submitted and valid
    if form.validate_on_submit():
        # Get data from the form
        name = form.name.data
        course = form.course.data
        short_answer = form.short_answer.data
        long_answer = form.long_answer.data
        satisfaction = form.satisfaction.data
        recommend = form.recommend.data
        improvements = form.improvements.data

        # Store data in a text file
        with open('feedback.txt', 'a') as file:
            file.write(f'Name: {name}\n')
            file.write(f'Course: {course}\n')
            file.write(f'Short-form Answer: {short_answer}\n')
            file.write(f'Long-form Answer: {long_answer}\n')
            file.write(f'Overall Satisfaction: {satisfaction}\n')
            file.write(f'Recommend: {recommend}\n')
            file.write(f'Suggestions for Improvement: {improvements}\n\n')

        # Return a success message if the form is submitted successfully
        return 'Feedback submitted successfully!'

    # Render the feedback_form.html template with the form instance
    return render_template('feedback_form.html', form=form)


# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)



