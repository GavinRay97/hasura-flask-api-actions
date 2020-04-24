# Insider Docker container, print does not function properly
# Use logging.warning()
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum_handler():
  req_data = request.get_json()
  numbers = req_data['input']['numbers']
  response = { 'total': sum(numbers) }
  logging.warn(req_data)
  return response

if __name__ == '__main__':
  app.run(debug = True, host = '0.0.0.0')