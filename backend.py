from indictrans import Transliterator
from flask import Flask,request,jsonify
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
@app.route('/transliterate', methods=['POST'])
def transliterate():
        try:
            data=request.get_json()
            src=data['src']
            tar=data['tar']
            inp=data['inp']
            transliterate= Transliterator(source=src,target=tar,build_lookup=True)
            out= transliterate.transform(inp)
            """with open("input.txt", "a") as file:
                     file.write("Input:\n")
                     file.write(inp + "\n")
            with open("output.txt", "a") as file:
                    file.write("Output:\n")
                    file.write(out+"\n")"""
            return jsonify({'output':out},{'status':'SUCCESS'}),200
        except KeyError:
            return jsonify({'error': 'Invalid JSON format or missing "text" field'}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500
@app.route('/test')
def test():
    return "Backend running successfully."
if __name__ == '__main__':
    app.run(debug=True)
