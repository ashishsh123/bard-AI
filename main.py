from flask import Flask, request, jsonify
from bardapi import Bard
app = Flask(__name__)
# Replace 'YOUR_API_KEY' with your actual API key
token = 'bwisMLiDYpgCsxdCrpiQY4Gbo3gg3RkDkbUkssmi49GKiomc6b_pPW9re4zYrUfKiLveYA.'
bard = Bard(token=token)
@app.route('/get_answer', methods=['POST'])
def get_answer():
    data = request.get_json()
    query = data.get('query', '')
    if query:
        result = bard.get_answer(query)['content']
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Missing query parameter'})

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=5000)