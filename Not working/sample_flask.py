
@app.route('/analysis/<filename>')
def analysis(filename):
    x = pd.DataFrame(np.random.randn(20, 5))
    return render_template("analysis.html", name=filename, data=x.to_html())

