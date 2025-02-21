from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    url_params = dict(request.args)
    headers = dict(request.headers)
    cookies = dict(request.cookies)
    form_data = dict(request.form)
    
    return render_template('index.html',
                         url_params=url_params,
                         headers=headers,
                         cookies=cookies,
                         form_data=form_data)

@app.route('/phone', methods=['GET', 'POST'])
def phone():
    message = ''
    if request.method == 'POST':
        phone_number = request.form.get('phone', '')
        message = ""
        # TODO: Add validation
    
    return render_template('phone.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
