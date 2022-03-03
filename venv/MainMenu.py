#!/usr/bin/python
# -*- coding: utf-8 -*-
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
import config
from aiogram.utils.markdown import hlink
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = Bot(token='5068063653:AAEby3FBqFSZkvUysXrRi8f7w4RyNRXfiS0')
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
loginAccountPartnersKeyboard= InlineKeyboardMarkup (row_width=1)
frequentProblemButton= InlineKeyboardButton(text='Частые проблемы', callback_data='frequentProblem')
accountPartnersButton= InlineKeyboardButton(text='Кабинет пратнера', callback_data='accountPartners')
loginAccountPartnersKeyboard.add(frequentProblemButton, accountPartnersButton)


accountProblemKeyboard = InlineKeyboardMarkup(row_width=1)
accountPartnersProblemButton = InlineKeyboardButton(text='Чужие данные', callback_data='otherData')
otherDataButton = InlineKeyboardButton(text='Другой код', callback_data='otherCode')
lostAccessButton = InlineKeyboardButton(text='Пропал доступ', callback_data='lostAccess')
helpButton=InlineKeyboardButton(text='Помощь человека', callback_data='helpButton')
accountProblemKeyboard.add(accountPartnersProblemButton, otherDataButton, lostAccessButton, helpButton)

accountPartnersKeyboard=InlineKeyboardMarkup(row_width=1)
mainPageButton = InlineKeyboardButton(text='Главная страница', callback_data='mainPage')
linksAccountButton = InlineKeyboardButton(text='Ссылки', callback_data='linksAccount')
applicationAccountButton = InlineKeyboardButton(text='Заявки', callback_data='applicationAccount')
accountPartnersKeyboard.add(mainPageButton, linksAccountButton, applicationAccountButton)

linksAccountKeyboard=InlineKeyboardMarkup(row_width=1)
readyLinksButton=InlineKeyboardButton(text='Готовые ссылки', callback_data='readyLinks')
createLinksButton=InlineKeyboardButton(text='Создать ссылку', callback_data='createLinks')
statisticsButton=InlineKeyboardButton(text='Статистика', callback_data='statistics')
linksAccountKeyboard.add(readyLinksButton, createLinksButton, statisticsButton)

applicationAccountKeyboard=InlineKeyboardMarkup(row_width=1)
sandingApplicationButton= InlineKeyboardButton(text='Отправка заявки', callback_data='sandingApplication')
statusApplicationButton= InlineKeyboardButton(text='Статусы заявок', callback_data='statusApplication')
listApplicationExcelButton= InlineKeyboardButton(text='Выгрузка списка заявок в Excel', callback_data='listApplicationExcel')
applicationAccountKeyboard.add(sandingApplicationButton, statusApplicationButton, listApplicationExcelButton)

#Кнопки: "Отправить заявку"
submitApplicationKeyboard=InlineKeyboardMarkup(row_width=1)
applicationElbaButton=InlineKeyboardButton(text='Заявка на Эльбу', callback_data='applicationElba')
afterSubmitApplicationButton=InlineKeyboardButton(text='После отправки заявки', callback_data='afterSubmitApplication')
statusApplicationButton=InlineKeyboardButton(text='Статусы заявок', callback_data='statusApplication')
statusNotSubjectButton=InlineKeyboardButton(text='Статус: "Не подлежит вознаграждению"', callback_data='statusNotSubject')
submitApplicationKeyboard.add(applicationElbaButton, afterSubmitApplicationButton, statusApplicationButton, statusNotSubjectButton)
statusApplicationKeyboard=InlineKeyboardMarkup(row_width=1).add(statusApplicationButton, statusNotSubjectButton)
statusNotSubjectKyeboard=InlineKeyboardMarkup(row_width=1).add(statusNotSubjectButton)

#Кнопки: "Получение вознаграждения"
rewardKeyboard = InlineKeyboardMarkup(row_width=1)
termsAccrualButton=InlineKeyboardButton(text='Условия начисления', callback_data='termsAccrual')
freeKAPButton=InlineKeyboardButton(text='Бесплатная КЭП для физлиц', callback_data='freeKAP')
sendReportOnDiadokButton=InlineKeyboardButton(text='Отправить отчет в диадок', callback_data='sendReportOnDiadok')
whenComesButton=InlineKeyboardButton(text='Когда приходит', callback_data='whenComes')
notAcceptReportButton=InlineKeyboardButton(text='Не приняли отчет', callback_data='notAcceptReport')
moneyNotComeButton=InlineKeyboardButton(text='Не пришли деньги', callback_data='moneyNotCome')
getRewardedWODiadokButton=InlineKeyboardButton(text='Получить вознаграждения без Диадока', callback_data='getRewardedWODiadok')
partnersOSNOButton=InlineKeyboardButton(text='Партнерам на ОСНО', callback_data='partnersOSNO')
notTakeApplicatonButton=InlineKeyboardButton(text='Не учли заявку', callback_data='notTakeApplicaton')
rewardKeyboard.add(termsAccrualButton,freeKAPButton, whenComesButton, sendReportOnDiadokButton)
sendReportOnDiadokKeyboard=InlineKeyboardMarkup(row_width=1).add(partnersOSNOButton, freeKAPButton, notAcceptReportButton, moneyNotComeButton, getRewardedWODiadokButton )
whenComesKeyboard=InlineKeyboardMarkup(row_width=1).add(whenComesButton, notAcceptReportButton)

#Кнопки: "Какие продукты рекомендовать"
recommendationsKeyboard=InlineKeyboardMarkup(row_width=1)
chooseProductButton=InlineKeyboardButton(text='Выберите продукт', url='https://support.kontur.ru/pages/viewpage.action?pageId=18350835', parse_mode='Markdown', disable_web_page_preview=True)
chooseAudienceButton=InlineKeyboardButton(text='Выберите аудиторию', url='https://support.kontur.ru/pages/viewpage.action?pageId=83870810', parse_mode='Markdown', disable_web_page_preview=True)
recommendationsKeyboard.add(chooseProductButton, chooseAudienceButton)


@dp.message_handler(commands='start')
async def firstButton(message: types.Message):
    await message.answer('Какие у вас вопросы? \n'
                         'Выберите интересующий раздел нажав на кнопку, или выберите “Помощь человека” для связи с сотрудником реферальной программы.', reply_markup=firstMenuKeyboard)

#Блок проблем кабинета партнера--

@dp.callback_query_handler(text='accountProblemButton')
async def callAccountProblemKeyboard(callAcc: types.CallbackQuery):
    await callAcc.message.answer('Зайдите на сайт kontur.ru в раздел Реферальная программа - https://kontur.ru/partnership/online и нажмите «Войти в кабинет партнера».\n'
                              'Заходить в кабинет партнера необходимо по электронной почте, указанной при регистрации в реферальной программе.', reply_markup=loginAccountPartnersKeyboard)

@dp.callback_query_handler(text='frequentProblem')
async def frequentProblem(callfP: types.CallbackQuery):
    await callfP.message.answer(text='Список частых проблем со входом в кабинет партнёра и как их решить.',reply_markup = accountProblemKeyboard)

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

@dp.callback_query_handler(text='accountPartners')
async def lostAccess(callaP: types.CallbackQuery):
        await callaP.message.answer(text='Выберите раздел кабинет партнёра', reply_markup=accountPartnersKeyboard)

@dp.callback_query_handler(text='mainPage')
async def mainPage(callmP: types.CallbackQuery):
        await callmP.message.answer(text='Анкета\n'
                                         'На [главной странице](https://kontur.ru/account/partnership) кабинета партнера в блоке Анкета можно увидеть следующие данные: ФИО, электронная почта, телефон, код партнера. ФИО и почту при необходимости вы можете изменить самостоятельно в [личном кабинете](https://cabinet.kontur.ru/).\n'
                                         'Код партнера\n'
                                         'Уникальный партнерский код присваивается сразу после регистрации в программе. Он помогает фиксировать клиента за вами. Код вшит во все инструменты кабинета партнера.\n'
                                         'Новости\n'
                                         'С центрального баннера, расположенного на главной странице кабинета, можно перейти к новостям реферальной программы и Контура в целом.\n'
                                         'Инструменты продвижения продуктов\n'
                                         'Инструменты продвижения продуктов находятся на главной странице кабинета партнера. Ими можно пользоваться сразу после регистрации.\n', parse_mode='Markdown', disable_web_page_preview=True)

@dp.callback_query_handler(text='linksAccount')
async def linksAccount(calllAccou: types.CallbackQuery):
        await calllAccou.message.answer(text='Раздел ссылки в кабинете партнёра: https://kontur.ru/account/partnership\n'
                                         'Создать ссылку\n'
                                         'Вы можете сформировать свою ссылку на любую страницу сайта Контура с кодом партнера. Для этого выберите пункт «Создать свою ссылку», который находится после списка готовых ссылок или создайте ссылку вручную. Для этого в конце ссылки на нужную страницу добавьте параметр ?p=XXXX, где вместо XXXX вставьте ваш код партнера.\n'
                                         'Статистика\n'
                                         'В разделе доступна подробная статистика с фильтром по дате, продукту и метке. Здесь можно получить информацию о количестве переходов, заявках и конверсии.', parse_mode='Markdown', disable_web_page_preview=True, reply_markup=linksAccountKeyboard)


@dp.callback_query_handler(text='readyLinks')
async def readyLinks(callrL: types.CallbackQuery):
        await callrL.message.answer(text='В разделе «Ссылки» вы найдете готовые реферальные ссылки на более чем 40 продуктов, участвующих в программе. Во всех этих ссылках уже есть код партнера, что позволяет фиксировать переходы и покупки клиентов по ним. Нажмите на «Показать все ссылки», чтобы увидеть весь список.')


@dp.callback_query_handler(text='createLinks')
async def createLinks(callcL: types.CallbackQuery):
        await callcL.message.answer(text='Вы можете сформировать свою ссылку на любую страницу сайта Контура с кодом партнера. Для этого выберите пункт «Создать свою ссылку», который находится после списка готовых ссылок или создайте ссылку вручную. Для этого в конце ссылки на нужную страницу добавьте параметр ?p=XXXX, где вместо XXXX вставьте ваш код партнера.')

@dp.callback_query_handler(text='statistics')
async def statistics(callsts: types.CallbackQuery):
        await callsts.message.answer(text='В разделе доступна подробная статистика с фильтром по дате, продукту и метке. Здесь можно получить информацию о количестве переходов, заявках и конверсии.')

@dp.callback_query_handler(text='applicationAccount')
async def applicationAccount(callappAcc: types.CallbackQuery):
        await callappAcc.message.answer(text='В [разделе](https://kontur.ru/account/partnership/orders) можно увидеть список заявок ваших клиентов. Воспользуйтесь фильтром по дате, продукту в заявке, статусу. Нажмите на интересующую строку и посмотрите историю работы с каждой заявкой и строкам в счете.',parse_mode='Markdown', disable_web_page_preview=True,reply_markup =applicationAccountKeyboard)

@dp.callback_query_handler(text='sandingApplication')
async def sandingApplication(callsndApp: types.CallbackQuery):
        await callsndApp.message.answer(text='Чтобы отправить заявку за клиента:\n'
                                            '1. Зайдите в кабинет [партнера](https://kontur.ru/account/login?ReturnUrl=%2faccount%2fpartnership)\n'
                                            '2. В «Инструментах продвижения продуктов» выберите «Отправить заявку».\n'
                                            '3. Выберите продукт в списке.\n'
                                            '4. Внесите почту, телефон, название организации, ИНН и КПП клиента.\n'
                                            '5. В комментариях укажите пожелания клиента или необходимый тариф. Если открылся список дополнительных опций, то отметьте нужное.',parse_mode='Markdown', disable_web_page_preview=True,reply_markup=submitApplicationKeyboard)

@dp.callback_query_handler(text='statusApplication')
async def statusApplication(callstsApp: types.CallbackQuery):
        await callstsApp.message.answer(text='Каждой заявке присваивается статус, который означает ход ее обработки менеджером.\n'
                                             '🔸В работе — менеджер взял заявку в работу. Ожидайте смену статуса..\n'
                                             '🔸Отказ — на момент поступления заявки по клиенту уже велась работа, либо клиент не новый. Также отказ устанавливается, если по заявке нет выставленных счетов в течение 60 дней. Наведите курсор на статус и узнайте причину отказа.\n'
                                             '🔸Выставлен — менеджер выставил клиенту счет, ожидание оплаты.\n'
                                             '🔸Оплачен — клиент оплатил счет.\n'
                                             '🔸Нет оплаты — счет выставили, но клиент его еще не оплатил.\n'
                                             '🔸Подлежит вознаграждению — по счету будет начислено вознаграждение.\n'
                                             '🔸Вознагражден — вознаграждение уже начислено и находится в отчете, сумма указана рядом со статусом.\n')

@dp.callback_query_handler(text='listApplicationExcel')
async def listApplicationExcel(calllAppExc: types.CallbackQuery):
        await calllAppExc.message.answer(text='Есть возможность выгрузить заявки списком в Excel, чтобы детально проанализировать информацию об источниках. Воспользуйтесь кнопкой «Скачать» справа от фильтров.')


#Блок получения вознаграждения
@dp.callback_query_handler(text='rewardButton')
async def rewardButton(callRew: types.CallbackQuery):
        await callRew.message.answer(text='Как получить вознаграждение можно узнать по коротким, но подробным видеороликам.\n'
                                          '[Как получить вознаграждение физическим лицам](https://support.kontur.ru/pages/viewpage.action?pageId=83871245#id-%D0%9F%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%D0%B2%D0%BE%D0%B7%D0%BD%D0%B0%D0%B3%D1%80%D0%B0%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F-%D0%92%D0%B8%D0%B4%D0%B5%D0%BE%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D0%B8%D1%8F%C2%AB%D0%9A%D0%B0%D0%BA%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C%D0%B2%D0%BE%D0%B7%D0%BD%D0%B0%D0%B3%D1%80%D0%B0%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%D1%84%D0%B8%D0%B7%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%BC%D0%BB%D0%B8%D1%86%D0%B0%D0%BC%C2%BB)\n'
                                          '[Как получить вознаграждение юридическим лицам/ИП](https://support.kontur.ru/pages/viewpage.action?pageId=83871245#id-%D0%9F%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%D0%B2%D0%BE%D0%B7%D0%BD%D0%B0%D0%B3%D1%80%D0%B0%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F-%D0%92%D0%B8%D0%B4%D0%B5%D0%BE%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D0%B8%D1%8F%C2%AB%D0%9A%D0%B0%D0%BA%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C%D0%B2%D0%BE%D0%B7%D0%BD%D0%B0%D0%B3%D1%80%D0%B0%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%D1%8E%D1%80%D0%B8%D0%B4%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%BC%D0%BB%D0%B8%D1%86%D0%B0%D0%BC%C2%BB)\n'
                                          'Для получения вознаграждения понадобится КЭП.\n'
                                          '🔸КЭП для юрлиц или ИП\n'
                                          'Партнеры-юрлица или ИП, у которых нет электронной подписи, должны выпустить ее самостоятельно.\n'
                                          '🔸КЭП для физлиц\n'
                                          'Партнеры-физлица, у которых нет электронной подписи, могут получить ее бесплатно.',parse_mode='Markdown', disable_web_page_preview=True,reply_markup = rewardKeyboard)

@dp.callback_query_handler(text='termsAccrual')
async def termsAccrual(callAccural: types.CallbackQuery):
        await callAccural.message.answer(text='Вознаграждение начисляется только за новых клиентов по продукту. Продления не входят в реферальную программу.\n'
                                              'Вознаграждение начисляется за все новые сервисы, которые купит клиент по вашей заявке в течение 60 дней.\n'
                                              'Вознаграждение начисляется ежемесячно, в рублях, после достижения минимальной суммы реализации по всем продуктам.\n'
                                              'С размерами агентского вознаграждения по каждому продукту можно ознакомиться в [таблице](https://kontur.ru/partnership/online/rules#7).',parse_mode='Markdown', disable_web_page_preview=True,reply_markup=whenComesKeyboard)

@dp.callback_query_handler(text='whenComes')
async def whenComes(callwC: types.CallbackQuery):
        await callwC.message.answer(text='Вознаграждение поступает в виде отчета на вкладку [«Вознаграждение»](https://kontur.ru/account/partnership/prize) к 15 числу месяца за предыдущий период.\n'
                                         'Если оплата по заявке была в декабре, то вознаграждение придёт 15 января, если оплата была в январе, то 15 февраля.',parse_mode='Markdown', disable_web_page_preview=True)

@dp.callback_query_handler(text='notAcceptReport')
async def notTakeApplicaton(callnTA: types.CallbackQuery):
        await callnTA.message.answer(text='Если вы не нашли заявку в итоговом отчете, сначала необходимо проверить, что:\n'
                                          '🔸Счет был полностью оплачен.\n'
                                          '🔸Оплата счета прошла в прошлом отчетном месяце.\n'
                                          'Если все верно, напишите об ошибке на part@skbkontur.ru с указанием кода партнера и данными по заявке.',parse_mode='Markdown', disable_web_page_preview=True)

@dp.callback_query_handler(text='sendReportOnDiadok')
async def sendReportOnDiadok(callsRoD: types.CallbackQuery):
        await callsRoD.message.answer(text='Чтобы отправить отчет о вознаграждении в СКБ Контур и получить вознаграждение, необходимо отправить отчёт в Диадок.\n'
                                           '[Как отправить отчёт](https://support.kontur.ru/pages/viewpage.action?pageId=83871219)\n'
                                           'Если у вас несколько отчетов, то отправьте их каждый по отдельности.\n'
                                           'После проверки отчета вознаграждение будет перечислено в течение 5 рабочих дней.\n'
                                           'У физлиц из итоговой суммы вознаграждения удерживается 13% НДФЛ.', parse_mode='Markdown', disable_web_page_preview=True,reply_markup=sendReportOnDiadokKeyboard)

@dp.callback_query_handler(text='freeKAP')
async def freeKAP(callfKAP: types.CallbackQuery):
        await callfKAP.message.answer(text='Чтобы выпустить электронную подпись для получения вознаграждения для физлица, отправьте, пожалуйста, на почту part@skbkontur.ru актуальную информацию: \n'
                                           '🔸ФИО\n'
                                           '🔸Регион, город/населенный пункт по месту где можете удостоверить личность\n'
                                           '🔸Телефон\n'
                                           '🔸Адрес электронной почты\n'
                                           '🔸ИНН\n'
                                           '🔸Код партнёра.\n'
                                           'После получения подписи вы сможете отправить отчёт в Диадок для получения вознаграждения.',reply_markup=sendReportOnDiadokKeyboard)

@dp.callback_query_handler(text='notAcceptReport')
async def notAcceptReport(callnAR: types.CallbackQuery):
        await callnAR.message.answer(text='Если отчет по вознаграждению был отклонен с комментарием: «Вы выслали документы в «Головное подразделение» СКБ Контур — это значит, что вы отправили отчет на неверное подразделение. Документы на получение агентского вознаграждения необходимо отправлять в подразделение «Отчетность партнеров все регионы». Отправьте отчет заново, выбрав верное подразделение.')

@dp.callback_query_handler(text='moneyNotCome')
async def moneyNotCome(callmNC: types.CallbackQuery):
        await callmNC.message.answer(text='Если прошло больше 8 дней после отправки отчета о вознаграждении в Диадок, а деньги не поступили на ваш расчетный счет, проверьте:\n'
                                          '🔸Отчет должен быть отправлен на подразделение ЗАО «ПФ «СКБ Контур», ИНН: 6663003127, подразделение «Отчетность партнеров, все регионы».\n'
                                          '🔸Отчет должен быть подписан сертификатом физлица, если вы участвуете в программе как физическое лицо или сертификатом юрлица, если вы участвуете в программе как юридическое лицо.\n'
                                          'Если все верно, напишите о проблеме на part@skbkontur.ru с указанием кода партнера.')

@dp.callback_query_handler(text='getRewardedWODiadok')
async def getRewardedWODiadok(callgRWOD: types.CallbackQuery):
        await callgRWOD.message.answer(text='Получить вознаграждение без электронной подписи могут только физические лица. При этом ставка вознаграждения будет снижена на 40% из-за того, что мы не получаем от партнера подписанных отчетных документов.\n'
                                            'Чтобы вывести вознаграждение по ускоренному способу, при формировании отчета на последнем этапе выберите «Ускоренный способ». Ожидайте денежный перевод в течение 5-ти рабочих дней.')

@dp.callback_query_handler(text='partnersOSNO')
async def partnersOSNO(callpOSNO: types.CallbackQuery):
        await callpOSNO.message.answer(text='Юрлица или ИП, имеющие режим налогообложения ОСНО, обязаны отчитываться по НДС, поэтому при выставлении счета и акта Контуру за оказанные услуги, им также необходимо предоставить счет-фактуру (далее — с/ф). Счет, акт и отчет формируются автоматически в кабинете партнера при начислении вознаграждения, а с/ф необходимо подготовить самостоятельно.\n'
                                            'Какие требования к счету-фактуре:\n'
                                            '🔸С/ф должна быть сформирована в xml формате в соответствии с приказом 820.\n'
                                            '🔸С/ф формируется в своей бухгалтерской программе или, если программа не позволяет сформировать с/ф в xml формате, можно создать ее вручную в Диадоке: в меню Документы в списке «Создать в редакторе» выберите «Счет-фактура». Откроется страница создания счета-фактуры. Заполните поля. Подробнее в статье Создание счета-фактуры.\n'
                                            '🔸В с/ф «Наименование товара» в колонке (1а) укажите в соответствии с наименованием в акте в сформированном в кабинете партнера отчете по вознаграждению.\n'
                                            '🔸Дата с/ф должна совпадать с датой акта в сформированном в кабинете партнера отчете по вознаграждению.\n'
                                            '🔸С/ф необходимо отправлять в Диадок в одном пакете с отчетом по вознаграждению (счет, акт и таблица отчета), сформированном в кабинете партнера.\n')

#Блок отправки заявки
@dp.callback_query_handler(text='submitApplication')
async def submitApplication(callsApplic: types.CallbackQuery):
        await callsApplic.message.answer(text='Чтобы отправить заявку за клиента:\n'
                                            '1. Зайдите в кабинет [партнера](https://kontur.ru/account/login?ReturnUrl=%2faccount%2fpartnership)\n'
                                            '2. В «Инструментах продвижения продуктов» выберите «Отправить заявку».\n'
                                            '3. Выберите продукт в списке.\n'
                                            '4. Внесите почту, телефон, название организации, ИНН и КПП клиента.\n'
                                            '5. В комментариях укажите пожелания клиента или необходимый тариф. Если открылся список дополнительных опций, то отметьте нужное.',parse_mode='Markdown', disable_web_page_preview=True,reply_markup=submitApplicationKeyboard)

@dp.callback_query_handler(text='afterSubmitApplication')
async def afterSubmitApplication(callaSApp: types.CallbackQuery):
        await callaSApp.message.answer(text='В течение 15 минут отправленная заявка появится в кабинете партнера на вкладке [Заявки.](https://kontur.ru/account/partnership/orders) Если этого не произошло, напишите на part@skbkontur.ru\n'
                                            'В течение 2-3 часов по контактам из заявки связывается менеджер продаж Контура, консультирует и выставляет счет. Если по заявке не связались, напишите об этом нам на эл. почту part@skbkontur.ru\n'
                                            'После того, как клиент оплатит счет, вам будет начислено вознаграждение. Оно поступит в виде отчета на вкладку [Вознаграждение](https://kontur.ru/account/partnership/prize) к 15 числу месяца, следующего за месяцем, в котором прошла оплата.\n',parse_mode='Markdown', disable_web_page_preview=True, reply_markup=statusApplicationKeyboard)

@dp.callback_query_handler(text='statusApplication')
async def statusApplication(callsAppli: types.CallbackQuery):
        await callsAppli.message.answer(text='Статусы заявок на вкладке [Заявки](https://kontur.ru/account/partnership/orders) информируют о том, на каком этапе находится заявка. Можно воспользоваться фильтром по дате, продукту, статусу. Кликните на нужную строку и посмотрите историю работы с каждой заявкой и строкам в счете.\n'
                                             '🔸В работе — менеджер взял заявку в работу. Ожидайте смену статуса.\n'
                                             '🔸Отказ — на момент поступления заявки по клиенту уже велась работа, либо клиент не новый. Также отказ устанавливается, если по заявке нет выставленных счетов в течение 60 дней. Наведите курсор на статус и узнайте причину отказа.\n'
                                             '🔸Счет выставлен — кликните на статус, чтобы посмотреть детальную информацию о счете.\n'
                                             '🔸Выставлен — менеджер выставил клиенту счет, ожидание оплаты.\n'
                                             '🔸Оплачен — клиент оплатил счет, ожидайте расчета вознаграждения.\n'
                                             '🔸Нет оплаты — клиент еще не оплатил счет.\n'
                                             '🔸Подлежит вознаграждению — по счету будет начислено вознаграждение.\n'
                                             '🔸Вознагражден — вознаграждение уже начислено.\n',parse_mode='Markdown', disable_web_page_preview=True, reply_markup=statusNotSubjectKyeboard)

@dp.callback_query_handler(text='statusNotSubject')
async def statusNotSubjectButton(callsNSB: types.CallbackQuery):
        await callsNSB.message.answer(text='У выставления данного статуса может быть несколько причин:\n'
                                           '🔸Клиент не новый, счет на продление. В реферальной программе вознаграждение начисляется только за подключение новых клиентов по продукту.\n'
                                           '🔸Продукт не участвует в реферальной программе. Например, Контур EDI. Проверить, участвует ли продукт и какой по нему % вознаграждения, можно в п.5.2 [договора-оферты.](https://kontur.ru/partnership/online/oferta)\n'
                                           '🔸Счет выставлен на дополнительную услугу, например за организацию рабочего места или дополнительный сертификат в рамках какого-либо продукта. Доп.услуги в рамках реферальной программы не вознаграждаются.\n'
                                           '🔸Счет еще не оплачен. Смена статуса произойдет после поступления оплаты на расчетный счет Контура.',parse_mode='Markdown', disable_web_page_preview=True)

#Блок рекомендаций продукта
@dp.callback_query_handler(text='recommendations')
async def recommendations(callRec: types.CallbackQuery):
        await callRec.message.answer(text='Выберите продукт, который хотите рекомендовать или аудиторию, которой хотите рекомендовать.',reply_markup = recommendationsKeyboard)





@dp.callback_query_handler(text='helpButton')
async def helpMessage(helpMessage : types.Message):
    await helpMessage.answer('Оператор скоро вам ответит')


executor.start_polling(dp,skip_updates=True)




