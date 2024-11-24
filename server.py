from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the home page
@app.route("/")
def home():
    return render_template("index.html")  # Renders the index.html file
# Route for the resume page
@app.route('/resume')
def resume():
    return render_template('resume.html')

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
