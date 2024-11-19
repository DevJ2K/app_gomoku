from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter, status, HTTPException
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask, request, make_response
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, HTMLResponse
from flask import Flask, redirect, url_for, request, session, render_template
import logging
from flask_session import Session
from gomoku.srcs.Gomoku import Gomoku
from gomoku.srcs.algorithms.gomoku_state import terminate_state
from gomoku.srcs.rules.GomokuSettings import GomokuSettings
import requests
import sys
import os
import time
import random

load_dotenv()

flask_app = Flask(__name__)

logging.basicConfig(filename='flask.log', level=logging.DEBUG)

flask_app.config['SESSION_TYPE'] = 'filesystem'
flask_app.config['TEMPLATES_AUTO_RELOAD'] = True

flask_app.config['SESSION_COOKIE_SECURE'] = True
flask_app.config['SESSION_COOKIE_SAMESITE'] = 'None'

Session(flask_app)

CLIENT_ID = os.getenv('UID')
CLIENT_SECRET = os.getenv('SECRET_TOKEN')
REDIRECT_URI = 'http://127.0.0.1:8000/auth/callback'

@flask_app.route('/')
def index():
	flask_app.logger.info('This is info output')
	if 'token' in session and session['token'] is not None:
		url = 'https://api.intra.42.fr/v2/me'
		headers = {
			'Authorization': f'Bearer {session["token"]}'
		}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			resultat = response.json()
			data = {
				'login': resultat['login']
			}
			flask_app.logger.info('before redirect')
			return redirect("http://localhost:5173/#/")
			# else:
			#     return render_template('whitelist.html')
		else:
			return render_template('login.html', error="Unable to fetch data from API")
	# else:
	#     return render_template('login.html')

@flask_app.route('/login')
def login():
	auth_url = f'https://api.intra.42.fr/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code'
	return redirect(auth_url)

@flask_app.route('/callback')
def auth_callback():
	flask_app.logger.info('This is info output')
	code = request.args.get('code')
	if not code:
		return 'No code provided', 400

	token_url = 'https://api.intra.42.fr/oauth/token'
	token_data = {
		'grant_type': 'authorization_code',
		'client_id': CLIENT_ID,
		'client_secret': CLIENT_SECRET,
		'code': code,
		'redirect_uri': REDIRECT_URI
	}

	token_response = requests.post(token_url, data=token_data)
	if token_response.status_code != 200:
		return f"Error fetching token: {token_response.text}", token_response.status_code
	token_json = token_response.json()

	try:
		flask_app.logger.info('Add session cookie')
		session['token'] = token_json['access_token']
	except KeyError:
		return 'Access token not found in the response', 500
	return redirect(url_for('index'))

@flask_app.route('/logout')
def logout():
	session.pop('token', None)
	return redirect(url_for('ranking'))

load_dotenv()

flask_app = Flask(__name__)

logging.basicConfig(filename='flask.log', level=logging.DEBUG)

flask_app.config['SESSION_TYPE'] = 'filesystem'

flask_app.config['TEMPLATES_AUTO_RELOAD'] = True
# flask_app.config['SESSION_COOKIE_SECURE'] = True
# flask_app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

Session(flask_app)

CLIENT_ID = os.getenv('UID')
CLIENT_SECRET = os.getenv('SECRET_TOKEN')
REDIRECT_URI = 'http://127.0.0.1:8000/auth/callback'

@flask_app.route('/')
def index():
    flask_app.logger.info('This is info output')
    if 'token' in session and session['token'] is not None:
        url = 'https://api.intra.42.fr/v2/me'
        headers = {
            'Authorization': f'Bearer {session["token"]}'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            resultat = response.json()
            data = {
                'login': resultat['login']
            }
            flask_app.logger.info('before redirect')
            resp = make_response(redirect('http://localhost:5173/#/'))
            resp.set_cookie('token', session['token'], secure=False)
            return resp
            # return redirect('http://localhost:5173/#/')
            # else:
            #     return render_template('whitelist.html')
        # else:
        #     return render_template('login.html', error="Unable to fetch data from API")
    # else:
    #     return render_template('login.html')

@flask_app.route('/login')
def login():
    auth_url = f'https://api.intra.42.fr/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code'
    return redirect(auth_url)

@flask_app.route('/callback')
def auth_callback():
    flask_app.logger.info('This is info output')
    code = request.args.get('code')
    if not code:
        return 'No code provided', 400

    token_url = 'https://api.intra.42.fr/oauth/token'
    token_data = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'redirect_uri': REDIRECT_URI
    }

    token_response = requests.post(token_url, data=token_data)
    if token_response.status_code != 200:
        return f"Error fetching token: {token_response.text}", token_response.status_code
    token_json = token_response.json()

    try:
        flask_app.logger.info('Add session cookie')
        session['token'] = token_json['access_token']
    except KeyError:
        return 'Access token not found in the response', 500
    return redirect(url_for('index'))

@flask_app.route('/logout')
def logout():
    session.pop('token', None)
    return redirect(url_for('ranking'))

@flask_app.route('/get-cookie/')
def get_cookie():
    if 'token' in session:
        return 'token'
    else:
        return 'notfound'

# Import my package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'gomoku')))

class Item(BaseModel):
	name: str
	description: str | None = None
	price: float
	tax: float | None = None

class NewGameModel(BaseModel):
	mode: str
	main_player: str
	IA_suggestion: bool
	options: dict[str, bool]
	opening: str

class MoveModel(BaseModel):
	player_move: dict[str, int]

class TimeoutModel(BaseModel):
	who_timeout: str


app = FastAPI()
router = APIRouter()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=['GET', 'POST'],
	allow_headers=["*"],
)

# @app.get("/")
# async def root():
# 	return {
# 		"response": 200,
# 		"message": "API is working !"
# 	}


all_games: dict[str, Gomoku] = {}

@app.post("/game/new")
async def new_game(body: NewGameModel):
	game_id = str(int(time.time()))
	while all_games.get(game_id) != None:
		game_id += str(random.randint(0, 9))
	print(game_id)
	IA = True if body.mode == "ia" else False
	opts = body.options

	allowed_capture = opts.get("allowed_capture")
	allowed_win_by_capture = opts.get("allowed_win_by_capture")
	allowed_double_three = opts.get("allowed_double_three")

	if allowed_capture is None or allowed_win_by_capture is None or allowed_double_three is None:
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The provided options are invalid. Please check the format and try again.")


	main_player = body.main_player

	all_games[game_id] = Gomoku(
		IA=IA,
		IA_suggestion=body.IA_suggestion,
		settings=GomokuSettings(
			allowed_capture=allowed_capture,
			allowed_win_by_capture=allowed_win_by_capture,
			allowed_double_three=allowed_double_three
		),
		main_player=main_player
	)

	board = all_games[game_id].run()
	if board == None:
		raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Sorry, the IA cannot continue the game, you win by forfeit...")

	return {
		"game_id": game_id,
		"player_turn": all_games[game_id].player_turn,
		"IA_suggestion": body.IA_suggestion,
		"board": board,
		"message": "..."
	}

@app.post("/game/{game_id}/move", status_code=status.HTTP_200_OK)
async def play_move(game_id: str, body: MoveModel):
	gomoku = all_games[game_id]
	if gomoku is None:
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The provided game id is invalid. Please check the game_id and try again.")


	x = body.player_move.get("x")
	y = body.player_move.get("y")

	if x is None or y is None:
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The provided coordinates are invalid. Please check the coordinates and try again.")

	try:
		after_move_dict = gomoku.apply_move(x, y)
	except Exception as e:
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
	return {
		"player_turn": gomoku.player_turn,
		"IA_suggestion": after_move_dict['IA_suggestion'],
		"IA_duration": after_move_dict['IA_duration'],
		"board": gomoku.board,
		"black_capture": gomoku.black_capture,
		"white_capture": gomoku.white_capture,
		"message": after_move_dict['message'],
		"status": after_move_dict['status']
	}

@app.post("/game/{game_id}/timeout")
async def timeout(game_id: str, body: TimeoutModel):
	pass

app.mount("/auth", WSGIMiddleware(flask_app))

if __name__ == "__main__":
	from gomoku.main import basic_function
	# import time
	basic_function();
	# for i in range(1200):
	#     print(f"Time : {i}")
	#     time.sleep(1);

