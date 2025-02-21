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
        phone_number = request.form.get('phone', None)
        if phone_number is None:
            message = "Номер телефона не указан"
        elif not phone_number:
            message = "Номер телефона не может быть пустым"
        else:
            cleaned = ''.join(c for c in phone_number if c.isdigit())
            if not cleaned.startswith('8'):
                cleaned = '8' + cleaned[1:] if cleaned.startswith('7') else '8' + cleaned
            
            if len(cleaned) == 11 and cleaned.startswith('8'):                    
                message = f"Номер телефона корректен: {cleaned[0]}-{cleaned[1:4]}-{cleaned[4:7]}-{cleaned[7:9]}-{cleaned[9:11]}"
            else:
                message = "Неверный формат номера телефона."
    
    return render_template('phone.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
