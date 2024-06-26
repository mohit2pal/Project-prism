from flask import Flask, request, render_template
import os 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_sqlmap', methods=['POST'])
def run_sqlmap():
    # Extract the URL, token, and level from the request data
    url = request.form.get('url')
    token = request.form.get('token')
    level = request.form.get('level')

    # Construct the sqlmap command
    command = f'sqlmap -u "{url}" --batch --headers="Authorization: Bearer {token}" --level={level} -v3 > temp_output.txt'

    # Run the command
    os.system(command)

    # Read the contents of the temporary file
    with open("temp_output.txt", "r") as file:
        output = file.read()
        
    # Remove the first 10 lines
    output_lines = output.split('\n')
    output = '\n'.join(output_lines[10:])

    # Remove the temporary file
    os.remove("temp_output.txt")

    # Return the output
    return output

if __name__ == '__main__':
    app.run(debug=True)