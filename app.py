from flask import Flask, render_template, request
from form import WordSearchForm
from artist_used_most import artist_used_most, open_file
from make_pie_chart import make_pie_chart

app = Flask(__name__)

app.config['SECRET_KEY'] = 'kjhsdfkgjh345toisufg980sd7g2l34khasd987asdfk'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/", methods=["GET", "POST"])
def search():
    form = WordSearchForm()
    if form.validate_on_submit() and request.form['word_search'].strip():
        query = request.form['word_search']
        make_pie_chart(artist_used_most(query.lower(), open_file()))
        return render_template("base.html", data=query.lower(), form=form)
    return render_template("base.html", form=form)


@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response


if __name__ == '__main__':
    app.run()
