from indictrans import Transliterator
from flask import Flask,request,jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sincostan",
            database="transliteration_db"
        )
        print("Database connection successful")
    except Error as err:
        print(f"Error: {err}")
    return connection

app=Flask(__name__)
CORS(app)

@app.route('/api/transliterate', methods=['POST'])
def transliterate():
    connection = create_connection()
    cursor = connection.cursor()
    try:
        data = request.get_json()
        src = data['src']
        tar = data['tar']
        inp = data['inp']
        client_ip = request.remote_addr
        transliterate = Transliterator(source=src, target=tar, build_lookup=True)
        out = transliterate.transform(inp)
        sql_insert_query = """INSERT INTO transliteration (src, tar, inp, output,ipaddress) VALUES (%s, %s, %s, %s,%s)"""
        record_data = (src, tar, inp, out,client_ip)
        cursor.execute(sql_insert_query, record_data)
        connection.commit()
        print("Records inserted into transliteration table")
        return jsonify({'output':out},{'status':'SUCCESS'}),200
    

        
        
    except KeyError:
        return jsonify({'error': 'Invalid JSON format or missing "text" field'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

@app.route('/api/test')
def test():
    return "Backend running successfully."


if __name__ == '__main__':
    app.run(debug=True)
