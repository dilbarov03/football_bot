from football import *
from news import *
from matchday import *
from standings import *
from bs4 import BeautifulSoup
import requests
import sqlite3

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State


bot = Bot(token="5379240859:AAF8_SxMBxC2DgQyV8ctjAcqj0RcrY3Hr_Y")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

logging.basicConfig(level=logging.INFO)


class Form(StatesGroup):
	#main = State()
	LaLiga = State()
	APL = State()
	France = State()
	Italy = State()
	Germany = State()


def main_menu():
	markup = types.ReplyKeyboardRemove()
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton('🔘Live matches')
	btn2 = types.KeyboardButton("⚽️All matches")
	btn3 = types.KeyboardButton("🇪🇸LaLiga")
	btn4 = types.KeyboardButton("🏴󠁧󠁢󠁥󠁮󠁧󠁿Premier League")
	btn5 = types.KeyboardButton("🇮🇹Seria A")
	btn6 = types.KeyboardButton("🇫🇷League 1")
	btn7 = types.KeyboardButton("🇩🇪Bundesliga")

	markup.add(btn1, btn2)
	markup.add(btn4, btn3)
	markup.add(btn5, btn6)
	markup.add(btn7)
	return markup

def back_menu():
	markup = types.ReplyKeyboardRemove()
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
	btn1 = types.KeyboardButton("🔙Main menu")
	markup.add(btn1)
	return markup

def add_db(m):
	conn = sqlite3.connect("mydata7.db") # или :memory: чтобы сохранить в RAM
	cursor = conn.cursor()
	#try:
	cursor.execute('CREATE TABLE IF NOT EXISTS user2 (id INTEGER UNIQUE)')
	#except:
	#	pass		

	try:
		cursor.execute("""INSERT INTO user2
                  VALUES (?)""", (m,)
               )
		conn.commit()
	except:
		pass

def spain_menu():
	markup = types.ReplyKeyboardRemove()
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton('📊Standings')
	btn2 = types.KeyboardButton("⚽️Matchday")
	btn3 = types.KeyboardButton("📰News")
	btn4 = types.KeyboardButton("🔙Main menu")

	markup.add(btn1, btn2)
	markup.add(btn3)
	markup.add(btn4)
	return markup

def apl_menu():
	markup = types.ReplyKeyboardRemove()
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton('📊Standings')
	btn2 = types.KeyboardButton("⚽️Matchday")
	btn3 = types.KeyboardButton("📰News")
	btn4 = types.KeyboardButton("🔙Main menu")

	markup.add(btn1, btn2)
	markup.add(btn3)
	markup.add(btn4)
	return markup

def italy_menu():
	markup = types.ReplyKeyboardRemove()
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton('📊Standings')
	btn2 = types.KeyboardButton("⚽️Matchday")
	btn3 = types.KeyboardButton("📰News")
	btn4 = types.KeyboardButton("🔙Main menu")

	markup.add(btn1, btn2)
	markup.add(btn3)
	markup.add(btn4)
	return markup

def france_menu():
	markup = types.ReplyKeyboardRemove()
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton('📊Standings')
	btn2 = types.KeyboardButton("⚽️Matchday")
	btn3 = types.KeyboardButton("📰News")
	btn4 = types.KeyboardButton("🔙Main menu")

	markup.add(btn1, btn2)
	markup.add(btn3)
	markup.add(btn4)
	return markup

def germany_menu():
	markup = types.ReplyKeyboardRemove()
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton('📊Standings')
	btn2 = types.KeyboardButton("⚽️Matchday")
	btn3 = types.KeyboardButton("📰News")
	btn4 = types.KeyboardButton("🔙Main menu")

	markup.add(btn1, btn2)
	markup.add(btn3)
	markup.add(btn4)
	return markup
'''
@bot.message_handler(commands=['stats'])
def statistika(message):
    try:
        conn = sqlite3.connect("mydata7.db") # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()
        try:
            cursor.execute('CREATE TABLE user2 (id INTEGER UNIQUE)')
        except:
            pass

        cursor.execute("SELECT id FROM user2")
        Lusers = cursor.fetchall()
        users=[]
        count=len(Lusers)

        bot.send_message(message.chat.id, f"👥Total number of users: {count}")
    except:
        pass

@bot.message_handler(commands=['rassilka'])
def before(message):
    try:
        if message.from_user.username=="Young_Proger" or message.from_user.username=="Oktamjon_03":
            f=bot.send_message(message.chat.id, "Jo'natmoqchi bo'lgan habaringizni yuboring(text, rasm, video...)")
            bot.register_next_step_handler(f, rassilka)
    except:
        print("Error")'''

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	add_db(message.chat.id)
	await bot.send_message(message.chat.id, "Hi, welcome to Football Daily.\n\n☑️I can show you live&line matches; TOP-5 league news, standings and matches.\n\nChoose the menu below👇", parse_mode='html', reply_markup=main_menu())
	try:
		await bot.send_message(-1001237603334, f"{message.from_user.first_name} - {message.chat.id} Futbol botdan foydalanishni boshladi")
	except:
		pass


@dp.message_handler(state=None)
async def echo_message(message: types.Message):
	if message.text == "🔙Main menu":
		await bot.send_message(message.chat.id, "Choose the menu below👇", reply_markup=main_menu())
	elif message.text == "🔘Live matches":
		output=live_scores()
		try:
			await bot.send_message(message.chat.id, output, reply_markup=main_menu())
		except:
			await bot.send_message(message.chat.id, "There is no live match at the moment", reply_markup=main_menu())
	elif message.text == "⚽️All matches":
		try:
			output=line_scores()
			firstpart, secondpart = output[:len(output)//2], output[len(output)//2:]
			p1, p2 = firstpart[:len(firstpart)//2], firstpart[len(firstpart)//2:]
			p3, p4 = secondpart[:len(secondpart)//2], secondpart[len(secondpart)//2:]
			await bot.send_message(message.chat.id, p1, reply_markup=main_menu())
			await bot.send_message(message.chat.id, p2, reply_markup=main_menu())
			await bot.send_message(message.chat.id, p3, reply_markup=main_menu())
			await bot.send_message(message.chat.id, p4, reply_markup=main_menu())

		except:
			await bot.send_message(message.chat.id, "Error. Try again", reply_markup=main_menu())
	
	elif message.text == "🇪🇸LaLiga":
		await bot.send_message(message.chat.id, "Choose the menu below👇", reply_markup=spain_menu())
		await Form.LaLiga.set()

	elif message.text == "🏴󠁧󠁢󠁥󠁮󠁧󠁿Premier League":
		await bot.send_message(message.chat.id, "Choose the menu below👇", reply_markup=apl_menu())
		await Form.APL.set()
	
	elif message.text == "🇮🇹Seria A":
		await bot.send_message(message.chat.id, "Choose the menu below👇", reply_markup=italy_menu())
		await Form.Italy.set()
	
	elif message.text == "🇫🇷League 1":
		await bot.send_message(message.chat.id, "Choose the menu below👇", reply_markup=france_menu())
		await Form.France.set()
	
	elif message.text == "🇩🇪Bundesliga":
		await bot.send_message(message.chat.id, "Choose the menu below👇", reply_markup=germany_menu())
		await Form.Germany.set()

	elif message.text == "📊Standings":
		await bot.send_message(message.chat.id, "You clicked to standings button")


@dp.message_handler(state=Form.LaLiga)
async def laliga(message: types.Message, state: FSMContext):
	if message.text == "🔙Main menu":
		await bot.send_message(message.chat.id, "Choose the menu below👇", reply_markup=main_menu())
		await state.finish()
	elif message.text == "📊Standings":
		try:
			output=laliga_ranking()
			await bot.send_message(message.chat.id, output, parse_mode='html')
		except:
			await bot.send_message(message.chat.id, "Error. Try again", reply_markup=main_menu(), parse_mode='html')
	elif message.text == "⚽️Matchday":
		try:
			output=matchday_laliga()
			await bot.send_message(message.chat.id, output, reply_markup=spain_menu(), parse_mode='html')
		except:
			await bot.send_message(message.chat.id, "Error. Try again", reply_markup=main_menu())
	elif message.text == "📰News":
		try:
			output=laliga_news()
			await bot.send_message(message.chat.id, output, reply_markup=spain_menu(), parse_mode='html')
		except:
			await bot.send_message(message.chat.id, "Error. Try again", reply_markup=main_menu())
	elif message.text!="🔙Main menu":
		await bot.send_message(message.chat.id, "Choose the menu below👇", reply_markup=spain_menu())
		await Form.LaLiga.set()


@dp.message_handler(state=Form.APL)
async def apl(message: types.Message, state: FSMContext):
	if message.text == "🔙Main menu":
		await bot.send_message(message.chat.id, "Choose the menu below👇", reply_markup=main_menu())
		await state.finish()
	elif message.text == "📊Standings":
		try:
			output=apl_ranking()
			await bot.send_message(message.chat.id, output, reply_markup=apl_menu(), parse_mode='html')
		except:
			await bot.send_message(message.chat.id, "Error. Try again", reply_markup=main_menu())
	elif message.text == "⚽️Matchday":
		try:
			output=matchday_apl()
			await bot.send_message(message.chat.id, output, reply_markup=apl_menu(), parse_mode='html')
		except:
			await bot.send_message(message.chat.id, "Error. Try again", reply_markup=main_menu())
	elif message.text == "📰News":
		try:
			output=apl_news()
			await bot.send_message(message.chat.id, output, reply_markup=apl_menu(), parse_mode='html')
		except:
			await bot.send_message(message.chat.id, "Error. Try again", reply_markup=main_menu())
	if message.text!="🔙Main menu":
		await bot.send_message(message.chat.id, "Choose the menu below👇", reply_markup=apl_menu())
		await Form.APL.set()

@dp.message_handler(state=Form.Italy)
async def italy(message: types.Message, state: FSMContext):
	if message.text == "🔙Main menu":
		await bot.send_message(message.chat.id, "Choose the menu below👇", reply_markup=main_menu())
		await state.finish()
	elif message.text == "📊Standings":
		try:
			output=italy_ranking()
			await bot.send_message(message.chat.id, output, reply_markup=italy_menu(), parse_mode='html')
		except:
			await bot.send_message(message.chat.id, "Error. Try again", reply_markup=main_menu())
	elif message.text == "⚽️Matchday":
		try:
			output=matchday_italy()
			await bot.send_message(message.chat.id, output, reply_markup=italy_menu(), parse_mode='html')
		except:
			await bot.send_message(message.chat.id, "Error. Try again", reply_markup=main_menu())
	elif message.text == "📰News":
		try:
			output=italy_news()
			await bot.send_message(message.chat.id, output, reply_markup=italy_menu(), parse_mode='html')
		except:
			await bot.send_message(message.chat.id, "Error. Try again", reply_markup=main_menu())
	if message.text!="🔙Main menu":
		await bot.send_message(message.chat.id, "Choose the menu below👇", reply_markup=italy_menu())
		await Form.Italy.set()

@dp.message_handler(state=Form.France)
async def france(message: types.Message, state: FSMContext):
	if message.text == "🔙Main menu":
		await bot.send_message(message.chat.id, "Choose the menu below👇", reply_markup=main_menu())
		await state.finish()
	elif message.text == "📊Standings":
		try:
			output=france_ranking()
			await bot.send_message(message.chat.id, output, reply_markup=france_menu(), parse_mode='html')
		except:
			await bot.send_message(message.chat.id, "Error. Try again", reply_markup=main_menu())
	elif message.text == "⚽️Matchday":
		try:
			output=matchday_france()
			await bot.send_message(message.chat.id, output, reply_markup=france_menu(), parse_mode='html')
		except:
			await bot.send_message(message.chat.id, "Error. Try again", reply_markup=main_menu())
	elif message.text == "📰News":
		try:
			output=france_news()
			await bot.send_message(message.chat.id, output, reply_markup=france_menu(), parse_mode='html')
		except:
			await bot.send_message(message.chat.id, "Error. Try again", reply_markup=main_menu())
	if message.text!="🔙Main menu":
		await bot.send_message(message.chat.id, "Choose the menu below👇", reply_markup=france_menu())
		await Form.France.set()

@dp.message_handler(state=Form.Germany)
async def germany(message: types.Message, state: FSMContext):
	if message.text == "🔙Main menu":
		await bot.send_message(message.chat.id, "Choose the menu below👇", reply_markup=main_menu())
		await state.finish()
	elif message.text == "📊Standings":
		try:
			output=bundesliga_ranking()
			await bot.send_message(message.chat.id, output, reply_markup=germany_menu(), parse_mode='html')
		except:
			await bot.send_message(message.chat.id, "Error. Try again", reply_markup=main_menu())
	elif message.text == "⚽️Matchday":
		try:
			output=matchday_bundesliga()
			await bot.send_message(message.chat.id, output, reply_markup=germany_menu(), parse_mode='html')
		except:
			await bot.send_message(message.chat.id, "Error. Try again", reply_markup=main_menu())
	elif message.text == "📰News":
		try:
			output=bundesliga_news()
			await bot.send_message(message.chat.id, output, reply_markup=germany_menu(), parse_mode='html')
		except:
			await bot.send_message(message.chat.id, "Error. Try again", reply_markup=main_menu())
	if message.text!="🔙Main menu":
		await bot.send_message(message.chat.id, "Choose the menu below👇", reply_markup=germany_menu())
		await Form.Germany.set()



if __name__ == '__main__':
    executor.start_polling(dp)