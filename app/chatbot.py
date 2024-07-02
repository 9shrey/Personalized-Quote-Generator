from flask import Blueprint, render_template, request
from .model import generate_quote

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        problem = request.form['problem']
        quote = generate_quote(problem)
        return render_template('result.html', problem=problem, quote=quote)
    return render_template('index.html')
