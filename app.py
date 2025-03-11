from flask import Flask, jsonify, request
import csv
from flask_cors import CORS
import random
app = Flask(__name__)
CORS(app)

movelist = ["R", "R'", "R2", "U", "U'", "U2", "D", "D'", "D2", "F", "F'", "F2", "L", "L'", "L2", "B", "B'", "B2"]
nanmoves = {
    "R": ["R'", "R2", "L", "L'", "L2"],
    "R'": ["R", "R2", "L", "L'", "L2"],
    "R2": ["R", "R'", "L", "L'", "L2"],
    "U": ["U'", "U2", "D", "D'", "D2"],
    "U'": ["U", "U2", "D", "D'", "D2"],
    "U2": ["U", "U'", "D", "D'", "D2"],
    "D": ["D'", "D2", "U", "U'", "U2"],
    "D'": ["D", "D2", "U", "U'", "U2"],
    "D2": ["D", "D'", "U", "U'", "U2"],
    "F": ["F'", "F2", "B", "B'", "B2"],
    "F'": ["F", "F2", "B", "B'", "B2"],
    "F2": ["F", "F'", "B", "B'", "B2"],
    "L": ["L'", "L2", "R", "R'", "R2"],
    "L'": ["L", "L2", "R", "R'", "R2"],
    "L2": ["L", "L'", "R", "R'", "R2"],
    "B": ["B'", "B2", "F", "F'", "F2"],
    "B'": ["B", "B2", "F", "F'", "F2"],
    "B2": ["B", "B'", "F", "F'", "F2"]
    #definitely not the best way to do this
}

def scramblemoves3():
    r1 = random.randint(22, 26)
    scramble = ""
    previous_move = ""

    for i in range(r1):
        moves = [move for move in movelist if move not in nanmoves.get(previous_move, []) and move != previous_move]
        g = random.choice(moves)
        scramble += g + " "
        previous_move = g
    return scramble.strip()

def read_csv(filepath):
    data = {}
    try:
        with open(filepath, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data[row['algname']] = row['algorithm']
    except FileNotFoundError:
        print(f"'{filepath}' not found.")
    return data

algorithms = read_csv('plls.csv')

alternate_algorithms = {}

@app.route('/scramble3', methods=['GET'])
def scramble3():
    return scramblemoves3()

@app.route('/compscrambles', methods=['GET'])
def compscrambles():
    scrambles = []
    for i in range(5):
        scrambles.append(f"{i+1}. {scramblemoves3()}")
    return "\n".join(scrambles)

@app.route('/compaveragecalc/<t1>/<t2>/<t3>/<t4>/<t5>', methods=['GET'])
def compaveragecalc(t1, t2, t3, t4, t5):
    times = [float(t1), float(t2), float(t3), float(t4), float(t5)]
    times.sort()
    times.pop(0)
    times.pop(-1)
    av=round(sum(times) / 3, 2)
    return f"Your WCA average is: {av}"
@app.route('/scramble2', methods=['GET'])
def scramblemoves2():
    r1 = random.randint(6, 8)
    scramble = ""
    previous_move = ""

    for i in range(r1):
        moves = [move for move in movelist if move not in nanmoves.get(previous_move, []) and move != previous_move]
        g = random.choice(moves)
        scramble += g + " "
        previous_move = g
    return scramble.strip()

@app.route('/<algname>', methods=['GET'])
def get_algorithm(algname):
    alg = algorithms.get(algname)
    if alg:
        return jsonify({
            "name": algname,
            "algorithm": alg
        })
    else:
        return jsonify({"error": "Algorithm not found"}), 404

@app.route('/alt/<algname>', methods=['POST'])
#trusting ppl post algorithms and not anything weird
def post_algorithm(algname):
    if algname not in algorithms:
        return jsonify({"error": "Algorithm name not found "}), 404
    if request.is_json:
        data = request.json
        alt_algorithm = data.get("alternate_algorithm")
    else:
        alt_algorithm = request.data.decode()

    if not alt_algorithm:
        return jsonify({"error": "Missing 'alternate_algorithm' "}), 400

    if algname not in alternate_algorithms:
        alternate_algorithms[algname] = []

    alternate_algorithms[algname].append(alt_algorithm)

    return jsonify({
        "message": f"Alternate algorithm for '{algname}' added successfully",
        "alternate_algorithms": alternate_algorithms[algname]
    })

@app.route('/alt/<algname>', methods=['GET'])
def get_algorithm_for_alt(algname):
    alt_algorithms_for_alg = alternate_algorithms.get(algname, [])
    if alt_algorithms_for_alg:
        return jsonify({
            "name": algname,
            "alternate_algorithms": alt_algorithms_for_alg
        })
    else:
        return jsonify({"error": "No alternate algorithms found for this algorithm"}), 404

@app.route('/allalgs', methods=['GET'])
def view_alternate_algorithms():
    return jsonify(alternate_algorithms)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Algorithm API",
        "endpoints (See docs for more info)": [
            f"/{name}" for name in algorithms.keys()
        ] + ["/scramble3" ,"/scramble2", "/allalgs", "/alt/<algname>, ","/compaveragecalc/<t1>/<t2>/<t3>/<t4>/<t5>","/compscrambles"]

    })

if __name__ == '__main__':
    app.run(debug=True)