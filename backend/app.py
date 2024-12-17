from flask import Flask, request, jsonify
import pandas as pd
from pattern_generator import generate_test_cases

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Parse input data
        input_data = request.json.get('data')
        df = pd.DataFrame(input_data)

        # Call the AI logic to generate new test cases
        generated_data = generate_test_cases(df)

        # Convert to list for output
        output = generated_data.to_dict(orient='records')
        return jsonify({"success": True, "data": output})
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
