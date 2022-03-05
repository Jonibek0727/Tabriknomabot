import asyncio
from aiogram.types import Message, CallbackQuery, InputMedia

from aiogram import types

from data.config import ADMINS, GROUP_CHAT_ID
from loader import dp, db, bot

from keyboards.default.def_btn import bayramlar, create_btn
from keyboards.inline.inline_btn import rasmni_korish, change_photo

from telegram import InputMediaPhoto
from aiogram.dispatcher import FSMContext


from PIL import Image, ImageFont, ImageDraw
import os
from data.sher import sherlar
from random import randint








@dp.message_handler(text="🔙 Ortga")
async def get_all_users(message: types.Message):
	await message.answer("Bayramlardan birini tanlang", reply_markup=bayramlar)









################### user_id=ADMINS ni ochirish kerek ################3333
@dp.message_handler(text="👩🏼 8-Mart 🌹")
async def get_all_users(message: types.Message):


    await message.answer(f"Qanday usulda 8- mart uchun tabriknoma yasamoqchisiz? ", reply_markup=create_btn("👩 Ism yoziladigan", "👤 Ism yozilmaydigan"))



##### barcha nomsiz rasmlar
jami_nomsiz = 20

##### barcha nomli rasmlar
jami_nomli = 13

tr_1 = 1
ism = ""


@dp.message_handler(text="👤 Ism yozilmaydigan")
async def get_all_users(message: types.Message):
	global call_1
	call_1 = "ortga_8-mart_2"
	global call_2
	call_2 = "oldinga_8-mart_2"
	global check
	check = "8-mart-ismsiz"
	global tr_1
	tr_1 = 1
	# print("1")

	global caption
	caption = sherlar[f"{randint(1, 10)}"]
		
	await message.answer_photo(photo=open("media/photo/8-mart/nomsiz_1.jpg","rb"),caption=caption, reply_markup=rasmni_korish(jami_nomsiz, call_1, call_2, check))




@dp.callback_query_handler(text="oldinga_8-mart_2")
async def change_(call: CallbackQuery):
	# await call.message.delete()
	# print("2")

	global tr_1
	tr_1 += 1

	if tr_1>jami_nomsiz:
		tr_1 -= 1
		await call.answer("Bu oxirgi rasm")
	else:
		# await call.message.answer_photo(photo=open(f"media/photo/8-mart{tr_1}.jpg","rb"), caption=f"O'zingizga yoqqan rasmni tanlang", reply_markup=change_photo(tr_1))


		global caption
		caption = sherlar[f"{randint(1, 10)}"]
		
		new_photo = open(f'media/photo/8-mart/nomsiz_{tr_1}.jpg', 'rb')
		await bot.edit_message_media(media=InputMedia(type='photo', media=new_photo, caption = caption), chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=change_photo(tr_1, jami_nomsiz, call_1, call_2, check))	

		# await call.message.edit_media(media=open('media/photo/8-mart3.jpg', 'rb') )




@dp.callback_query_handler(text="ortga_8-mart_2")
async def change_(call: CallbackQuery):
	# await call.message.delete()
	global tr_1
	tr_1 -= 1

	if tr_1==0:
		tr_1 += 1
		await call.answer("Bu birinchi rasm")
	else:
		# await call.message.answer_photo(photo=open(f"media/photo/8-mart{tr_1}.jpg","rb"), caption=f"O'zingizga yoqqan rasmni tanlang", reply_markup=change_photo(tr_1))

		global caption
		caption = sherlar[f"{randint(1, 10)}"]
		

		new_photo = open(f'media/photo/8-mart/nomsiz_{tr_1}.jpg', 'rb')
		await bot.edit_message_media(media=InputMedia(type='photo', media=new_photo, caption = caption), chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=change_photo(tr_1, jami_nomsiz, call_1, call_2, check))	

		# await call.message.edit_media(media=open('media/photo/8-mart3.jpg', 'rb') )





###################   8- mart uchun ism yoziladigan  bolim ###############333
###################   8- mart uchun ism yoziladigan  bolim ###############333


def rasm_qayta_ishla(tr, user_id):
	img = Image.open(f"media/photo/8-mart/nomli_{tr}.jpg")

	if tr == 1:


		font = ImageFont.truetype("media/fonts/ANTQUABI.ttf", 92)  ## impact, arial
# font = ImageFont.truetype("resources/HelveticaNeueLight.ttf", fontsize)
		draw = ImageDraw.Draw(img)

		draw.text((500,310), ism, (255,40,0), font=font)
		# draw.text((640,475), iftor, (0,190,120), font=font2)

		img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

		# img.show()

	elif tr == 2:


		font = ImageFont.truetype("media/fonts/ANTQUABI.ttf", 142)  ## impact, arial
# font = ImageFont.truetype("resources/HelveticaNeueLight.ttf", fontsize)
		draw = ImageDraw.Draw(img)

		draw.text((1510,300), ism, (25,0,30), font=font)
		# draw.text((640,475), iftor, (0,190,120), font=font2)

		img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

		# img.show()

	elif tr == 3:


		font = ImageFont.truetype("media/fonts/Gstswzrm.ttf", 190)  ## impact, arial
# font = ImageFont.truetype("resources/HelveticaNeueLight.ttf", fontsize)
		draw = ImageDraw.Draw(img)

		draw.text((1200,1900), "Bayramingiz bilan "+ism, (55,190,30), font=font)
		# draw.text((640,475), iftor, (0,190,120), font=font2)

		img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

		# img.show()

	elif tr == 4:
		
		font = ImageFont.truetype("media/fonts/BRITANIC.ttf", 105)  ## impact, arial

		draw = ImageDraw.Draw(img)

		draw.text((700,80), ism, (55,190,30), font=font)
		

		img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

		# img.show()

	elif tr == 5:
			
		font = ImageFont.truetype("media/fonts/Gstswzrm.ttf", 80)  ## impact, arial

		draw = ImageDraw.Draw(img)

		draw.text((380,110), ism, (55,190,30), font=font)
		

		img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

		# img.show()


	elif tr == 6:
			
		font = ImageFont.truetype("media/fonts/Gstswzrm.ttf", 40)  ## impact, arial

		draw = ImageDraw.Draw(img)

		draw.text((230,55), ism, (25,220,150), font=font)
		

		img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

		# img.show()

	elif tr == 7:
		
		font = ImageFont.truetype("media/fonts/BRITANIC.ttf", 95)  ## impact, arial

		draw = ImageDraw.Draw(img)

		draw.text((70,75), ism, (255,10,10), font=font)
		

		img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

		# img.show()

	elif tr == 8:
		
		font = ImageFont.truetype("media/fonts/Gstswzrm.ttf", 50)  ## impact, arial

		draw = ImageDraw.Draw(img)

		draw.text((180,185), ism, (155,0,0), font=font)
		

		img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

		# img.show()

	elif tr == 9:
		
		font = ImageFont.truetype("media/fonts/TR Kastler Bold Italik.ttf", 100)  ## impact, arial

		draw = ImageDraw.Draw(img)

		draw.text((175,145), ism, (255,20,150), font=font)
		

		img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

	elif tr == 10:
		
		font = ImageFont.truetype("media/fonts/TR Renfrew.ttf", 40)  ## impact, arial

		draw = ImageDraw.Draw(img)

		draw.text((55,65), ism, (255,100,0), font=font)
		

		img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

	elif tr == 11:
		
		font = ImageFont.truetype("media/fonts/HARLOWSI.ttf", 45)  ## impact, arial

		draw = ImageDraw.Draw(img)

		draw.text((40,45), ism, (0,255,0), font=font)
		

		img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

	elif tr == 12:
		
		font = ImageFont.truetype("media/fonts/HARLOWSI.ttf", 105)  ## impact, arial

		draw = ImageDraw.Draw(img)

		draw.text((120,75), ism, (0,255,0), font=font)
		

		img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

	elif tr == 13:
		
		font = ImageFont.truetype("media/fonts/HARLOWSI.ttf", 105)  ## impact, arial

		draw = ImageDraw.Draw(img)

		draw.text((230,345), ism, (90,50,0), font=font)
		

		img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")












###################   8- mart uchun ism yoziladigan  bolim ###############333

@dp.message_handler(text="👩 Ism yoziladigan", state=None)
async def get_all_users(message: types.Message, state=FSMContext):



	global tr_1
	tr_1 = 1
	await message.answer("Kim uchun tabriknoma yasatmoqchisiz? \n\nIsmini kiriting:") 
	await state.set_state("8-mart-ism")


@dp.message_handler(state="8-mart-ism")
async def get_all_users(message: types.Message, state=FSMContext):
	await state.finish()

	global call_1
	call_1 = "ortga_8-mart_1"
	global call_2
	call_2 = "oldinga_8-mart_1"
	global check
	check = "8-mart-ismli"
	global ism
	ism = message.text
	# await message.answer("Kim uchun tabriknoma yasatmoqchisiz? \nIsmini kiriitng:") 
	# print(ism)
	rasm_qayta_ishla(tr_1, message.from_user.id)

	global caption
	caption = sherlar[f"{randint(1, 10)}"]
		
	new_photo = open(f'media/photo/8-mart/{message.from_user.id}_{tr_1}.jpg', 'rb')
	await message.answer_photo(photo=new_photo,caption=caption, reply_markup=rasmni_korish(jami_nomli, call_1, call_2, check))

	os.remove(f'media/photo/8-mart/{message.from_user.id}_{tr_1}.jpg')
    # await state.set_state("send_users")





@dp.callback_query_handler(text="oldinga_8-mart_1")
async def change_(call: CallbackQuery):
	# await call.message.delete()
	# print("2")

	global tr_1
	tr_1 += 1

	if tr_1>jami_nomli:
		tr_1 -= 1
		await call.answer("Bu oxirgi rasm")
	else:
		# await call.message.answer_photo(photo=open(f"media/photo/8-mart{tr_1}.jpg","rb"), caption=f"O'zingizga yoqqan rasmni tanlang", reply_markup=change_photo(tr_1))

		global caption
		caption = sherlar[f"{randint(1, 10)}"]
		
		rasm_qayta_ishla(tr_1, call.from_user.id)
		new_photo = open(f'media/photo/8-mart/{call.from_user.id}_{tr_1}.jpg', 'rb')
		await bot.edit_message_media(media=InputMedia(type='photo', media=new_photo, caption = caption), chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=change_photo(tr_1, jami_nomli, call_1, call_2, check))	
		try:
			
			os.remove(f'media/photo/8-mart/{call.from_user.id}_{tr_1}.jpg')
		except Exception as e:
			pass

		# await call.message.edit_media(media=open('media/photo/8-mart3.jpg', 'rb') )




@dp.callback_query_handler(text="ortga_8-mart_1")
async def change_(call: CallbackQuery):
	# await call.message.delete()
	global tr_1
	tr_1 -= 1
	# print("ortga ism yozilgan")

	if tr_1 == 0:
		tr_1 += 1
		await call.answer("Bu birinchi rasm")
	else:
		# await call.message.answer_photo(photo=open(f"media/photo/8-mart{tr_1}.jpg","rb"), caption=f"O'zingizga yoqqan rasmni tanlang", reply_markup=change_photo(tr_1))

		
		global caption
		caption = sherlar[f"{randint(1, 10)}"]
		
		rasm_qayta_ishla(tr_1, call.from_user.id)
		new_photo = open(f'media/photo/8-mart/{call.from_user.id}_{tr_1}.jpg', 'rb')
		await bot.edit_message_media(media=InputMedia(type='photo', media=new_photo, caption = caption), chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=change_photo(tr_1, jami_nomli, call_1, call_2, check))	

		os.remove(f'media/photo/8-mart/{call.from_user.id}_{tr_1}.jpg')


@dp.callback_query_handler(text="place")
async def change_(call: CallbackQuery):
	# await call.message.delete()
	
	await call.answer(f"Bu {tr_1} - rasm")
	




@dp.callback_query_handler(text="8-mart-ismli")
async def change_(call: CallbackQuery):
	# await call.message.delete()
	
	# await call.answer(f"{tr_1} - rasm")
	rek = f"\n🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n🌺 8- mart 'Xalqaro xotin-qizlar kuni' bayrmi bilan tabriklayman! 🌷 {ism} doimo yuzingizdan kulgu, labingizdan tabassum, ko'zlaringizdan esa baxt uchqunlari arimasin. 💐"
	rek += "🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n\n@tabriknoma_yasovchi_bot"
	caption_ = caption + rek

	rasm_qayta_ishla(tr_1, call.from_user.id)
	new_photo = open(f'media/photo/8-mart/{call.from_user.id}_{tr_1}.jpg', 'rb')

	await bot.edit_message_media(media=InputMedia(type='photo', media=new_photo, caption = caption_), chat_id=call.message.chat.id, message_id=call.message.message_id)	

	os.remove(f'media/photo/8-mart/{call.from_user.id}_{tr_1}.jpg')
	


@dp.callback_query_handler(text="8-mart-ismsiz")
async def change_(call: CallbackQuery):
	# await call.message.delete()
	
	# await call.answer(f"{tr_1} - rasm")
	rek = "\n🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n🌺 8- mart 'Xalqaro xotin-qizlar kuni' bayrmi bilan tabriklayman! 🌷 Doimo yuzingizdan kulgu arimasin. 💐"
	rek += "🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n\n@tabriknoma_yasovchi_bot"
	caption_ = caption + rek

	# rasm_qayta_ishla(tr_1, call.from_user.id)
	# new_photo = open(f'media/photo/8-mart/{call.from_user.id}_{tr_1}.jpg', 'rb')

	# await bot.edit_message_media(media=InputMedia(type='photo', media=new_photo, caption = caption_), chat_id=call.message.chat.id, message_id=call.message.message_id)	

	# os.remove(f'media/photo/8-mart/{call.from_user.id}_{tr_1}.jpg')
	# 

	new_photo = open(f'media/photo/8-mart/nomsiz_{tr_1}.jpg', 'rb')
	await bot.edit_message_media(media=InputMedia(type='photo', media=new_photo, caption = caption_), chat_id=call.message.chat.id, message_id=call.message.message_id)	
