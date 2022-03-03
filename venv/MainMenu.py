#!/usr/bin/python
# -*- coding: utf-8 -*-
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
import config
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = Bot(token='5068063653:AAGNUJg75XuCcQwMm7Tl-7LFBCEOa2WOw58')
dp = Dispatcher(bot)

#Главное меню
firstMenuKeyboard=InlineKeyboardMarkup(row_width=1)
accountProblemButton=InlineKeyboardButton(text='Вход в кабинет партнера', callback_data='accountProblemButton')
rewardButton=InlineKeyboardButton(text='Получение вознаграждения', callback_data='rewardButton')
submitApplication=InlineKeyboardButton(text='Отправить заявку', callback_data='submitApplication')
recommendations=InlineKeyboardButton(text='Какие продукты рекомендовать', callback_data='recommendations')
more=InlineKeyboardButton(text='Еще...', callback_data='more')
helpButton=InlineKeyboardButton(text='Помощь человека', callback_data='helpButton')
firstMenuKeyboard.add(accountProblemButton, rewardButton, submitApplication, recommendations, more, helpButton)

#Кнопки: "Вход в кабинет партнера"
accountProblemKeyboard = InlineKeyboardMarkup(row_width=1)
accountPartnersProblemButton = InlineKeyboardButton(text='Чужие данные', callback_data='otherData')
otherDataButton = InlineKeyboardButton(text='Другой код', callback_data='otherCode')
lostAccessButton = InlineKeyboardButton(text='Пропал доступ', callback_data='lostAccess')
helpButton=InlineKeyboardButton(text='Помощь человека', callback_data='helpButton')
accountProblemKeyboard.add(accountPartnersProblemButton, otherDataButton, lostAccessButton, helpButton)


@dp.message_handler(commands='start')
async def firstButton(message: types.Message):
    await message.answer('Какие у вас вопросы? \n'
                         'Выберите интересующий раздел нажав на кнопку, или выберите “Помощь человека” для связи с сотрудником реферальной программы.', reply_markup=firstMenuKeyboard)

@dp.callback_query_handler(text='accountProblemButton')
async def callAccountProblemKeyboard(callAcc: types.CallbackQuery):
    await callAcc.message.answer('Зайдите на сайт kontur.ru в раздел Реферальная программа - https://kontur.ru/partnership/online и нажмите «Войти в кабинет партнера».\n'
                              'Заходить в кабинет партнера необходимо по электронной почте, указанной при регистрации в реферальной программе.')
    await callAcc.message.answer(text='Список частых проблем со входом в кабинет партнёра и как их решить.',reply_markup = accountProblemKeyboard)

@dp.callback_query_handler(text='otherData')
async def callOtherData(callOD: types.CallbackQuery):
    await callOD.message.answer('Если при входе в кабинет партнёра или при регистрации в реферальной программе вы видите чужое ФИО, то значит к аккаунту по вашей почте установилось имя из ЭЦП, которая привязана к аккаунту.\n'
                                      'Решение:\n'
                                      '1 Вы можете зайти в личный кабинет и поменять ФИО - https://cabinet.kontur.ru/\n'
                                      '2 Если вы участвуете в реферальной программе как физлицо и ФИО из аккаунта должны быть на этой почте, например, по ней вы работаете в Экстерне, то вам нужно зарегистрировать новую почту на ваши ФИО. После регистрации напишите на почту part@skbkontur.ru и мы подключим дополнительный аккаунт к реферальному коду.')

@dp.callback_query_handler(text='otherCode')
async def otherCode(callOC: types.CallbackQuery):
        await callOC.message.answer(text='Если вы авторизовались по вашей почте и в кабинете партнёра теперь отображается новый код, то значит произошло объединение аккаунтов и вы создали новый кабинет партнёра.\n'
                                       'Напишите на почту part@skbkontur.ru и мы поможем восстановить доступ к старому аккаунту.')

@dp.callback_query_handler(text='lostAccess')
async def lostAccess(callLA: types.CallbackQuery):
        await callLA.message.answer(text='Возможно 2 сценария, почему так произошло:\n'
                                       '1) Вы авторизованы по ЭЦП, а аккаунт привязан к почте. Вам нужно выйти из аккаунта и войти по почте.\n'
                                       '2) Если вы точно знаете, что заходите по нужной почте и пропал доступ в кабинет партнёра, то значит произошло объединение аккаунтов.\n'
                                       'Напишите на почту part@skbkontur.ru с вашей почты, которая была подключена к реферальному коду и мы поможем восстановить доступ.\n')

@dp.callback_query_handler(text='helpButton')
async def helpMessage(helpMessage : types.Message):
    await helpMessage.answer('Оператор скоро вам ответит')


executor.start_polling(dp,skip_updates=True)




