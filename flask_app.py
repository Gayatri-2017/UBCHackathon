
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from interests import search_interests
app = Flask(__name__)
app.config["DEBUG"] = True


# @app.route('/')
# def hello_world():
#     return 'Hello from Flask!'

@app.route("/", methods=["GET", "POST"])
def adder_page():
	errors = ""
	if request.method == "POST":
		interest = None
		try:
			interest = str(request.form["interest"])
		except:
			errors += "<p>{!r} is not valid.</p>\n".format(request.form["interest"])
		if interest is not None:
			result = search_interests(interest)
			return '''
				<html>
				<body>
				<p>The result is {result}</p>
				<p><a href="/">Click here to search again</a>
				</body>
				</html>
				'''.format(result=result)
	return '''
		<html>
		<body>
		<p>Choose your interest:</p>
		<form method="post" action=".">
			<p><input name="interest" /></p>
			<p><input type="submit" value="Search Interest" /></p>
		</form>
		</body>
		</html>
		'''.format(errors=errors)
if __name__ == "__main__":
    app.run(debug=True)