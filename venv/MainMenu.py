#!/usr/bin/python
# -*- coding: utf-8 -*-
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
#import config
import logging



from aiogram.utils.markdown import hlink
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = Bot(token='5151766578:AAGo3PINTeoi5Awu32XjzEW4tgbHSVy5kHc')
dp = Dispatcher(bot)
log_format='%(asctime)s - %(filename)s: - %(message)s - %(name)s'
logging.basicConfig(level='DEBUG', filename='metrics.log',format=log_format, datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger()

#Главное меню
firstMenuKeyboard = types.ReplyKeyboardMarkup(row_width=1)
accountProblemButton = types.KeyboardButton(text='Вход в кабинет партнера', callback_data='accountProblemButton')
rewardButton = types.KeyboardButton(text='Получение вознаграждения', callback_data='rewardButton')
submitApplication = types.KeyboardButton(text='Отправить заявку', callback_data='submitApplication')
recommendations = types.KeyboardButton(text='Какие продукты рекомендовать', callback_data='recommendations')
more = types.KeyboardButton(text='Еще...', callback_data='more')
helpButton = types.KeyboardButton(text='Помощь человека', callback_data='helpButton')
firstMenuKeyboard.add(accountProblemButton, rewardButton, submitApplication, recommendations, more)#, helpButton)

#Кнопки: "Вход в кабинет партнера"

loginAccountPartnersKeyboard = types.ReplyKeyboardMarkup (row_width=1)
frequentProblemButton = types.KeyboardButton(text='Частые проблемы', callback_data='frequentProblem')
accountPartnersButton = types.KeyboardButton(text='Кабинет партнера', callback_data='accountPartners')
loginAccountPartnersKeyboard.add(frequentProblemButton, accountPartnersButton)


accountProblemKeyboard = types.ReplyKeyboardMarkup(row_width=1)
accountPartnersProblemButton = types.KeyboardButton(text='Чужие данные', callback_data='otherData')
otherDataButton = types.KeyboardButton(text='Другой код', callback_data='otherCode')
lostAccessButton = types.KeyboardButton(text='Пропал доступ', callback_data='lostAccess')
helpButton = types.KeyboardButton(text='Помощь человека', callback_data='helpButton')
accountProblemKeyboard.add(accountPartnersProblemButton, otherDataButton, lostAccessButton)#, helpButton)


accountPartnersKeyboard = types.ReplyKeyboardMarkup(row_width=1)
mainPageButton = types.KeyboardButton(text='Главная страница', callback_data='mainPage')
linksAccountButton = types.KeyboardButton(text='Ссылки', callback_data='linksAccount')
applicationAccountButton = types.KeyboardButton(text='Заявки', callback_data='applicationAccount')
accountPartnersKeyboard.add(mainPageButton, linksAccountButton, applicationAccountButton)

linksAccountKeyboard = types.ReplyKeyboardMarkup(row_width=1)
readyLinksButton = types.KeyboardButton(text='Готовые ссылки', callback_data='readyLinks')
createLinksButton = types.KeyboardButton(text='Создать ссылку', callback_data='createLinks')
statisticsButton = types.KeyboardButton(text='Статистика', callback_data='statistics')
linksAccountKeyboard.add(readyLinksButton, createLinksButton, statisticsButton)

applicationAccountKeyboard = types.ReplyKeyboardMarkup(row_width=1)
sandingApplicationButton = types.KeyboardButton(text='Отправка заявки', callback_data='sandingApplication')
statusApplicationButton = types.KeyboardButton(text='Статусы заявок', callback_data='statusApplication')
listApplicationExcelButton = types.KeyboardButton(text='Выгрузка списка заявок в Excel', callback_data='listApplicationExcel')
applicationAccountKeyboard.add(sandingApplicationButton, statusApplicationButton, listApplicationExcelButton)

#Кнопки: "Отправить заявку"
submitApplicationKeyboard = types.ReplyKeyboardMarkup(row_width=1)
applicationElbaButton = types.KeyboardButton(text='Заявка на Эльбу', callback_data='applicationElba')
afterSubmitApplicationButton = types.KeyboardButton(text='После отправки заявки', callback_data='afterSubmitApplication')
statusApplicationButton = types.KeyboardButton(text='Статусы заявок', callback_data='statusApplication')
statusNotSubjectButton = types.KeyboardButton(text='Статус: "Не подлежит вознаграждению"', callback_data='statusNotSubject')
submitApplicationKeyboard.add(applicationElbaButton, afterSubmitApplicationButton, statusApplicationButton, statusNotSubjectButton)
statusApplicationKeyboard = types.ReplyKeyboardMarkup(row_width=1).add(statusApplicationButton, statusNotSubjectButton)
statusNotSubjectKyeboard = types.ReplyKeyboardMarkup(row_width=1).add(statusNotSubjectButton)

#Кнопки: "Получение вознаграждения"
rewardKeyboard = types.ReplyKeyboardMarkup(row_width=1)
termsAccrualButton=types.KeyboardButton(text='Условия начисления', callback_data='termsAccrual')
freeKAPButton=types.KeyboardButton(text='Бесплатная КЭП для физлиц', callback_data='freeKAP')
sendReportOnDiadokButton=types.KeyboardButton(text='Отправить отчет в диадок', callback_data='sendReportOnDiadok')
whenComesButton=types.KeyboardButton(text='Когда приходит', callback_data='whenComes')
notAcceptReportButton=types.KeyboardButton(text='Не приняли отчет', callback_data='notAcceptReport')
moneyNotComeButton=types.KeyboardButton(text='Не пришли деньги', callback_data='moneyNotCome')
getRewardedWODiadokButton=types.KeyboardButton(text='Получить вознаграждения без Диадока', callback_data='getRewardedWODiadok')
partnersOSNOButton=types.KeyboardButton(text='Партнерам на ОСНО', callback_data='partnersOSNO')
notTakeApplicatonButton=types.KeyboardButton(text='Не учли заявку', callback_data='notTakeApplicaton')
rewardKeyboard.add(termsAccrualButton,freeKAPButton, whenComesButton, sendReportOnDiadokButton)
sendReportOnDiadokKeyboard=types.ReplyKeyboardMarkup(row_width=1).add(partnersOSNOButton, freeKAPButton, notAcceptReportButton, moneyNotComeButton, getRewardedWODiadokButton )
whenComesKeyboard=types.ReplyKeyboardMarkup(row_width=1).add(whenComesButton, notAcceptReportButton)

#Кнопки: "Какие продукты рекомендовать"
recommendationsKeyboard=types.ReplyKeyboardMarkup(row_width=1)
chooseProductButton=types.KeyboardButton(text='Выберите продукт', url='https://support.kontur.ru/pages/viewpage.action?pageId=18350835', parse_mode='Markdown', disable_web_page_preview=True)
chooseAudienceButton=types.KeyboardButton(text='Выберите аудиторию', url='https://support.kontur.ru/pages/viewpage.action?pageId=83870810', parse_mode='Markdown', disable_web_page_preview=True)
recommendationsKeyboard.add(chooseProductButton, chooseAudienceButton)

#Кнопки: "Еще"
moreKeyboard=types.ReplyKeyboardMarkup(row_width=1)
officialRepresentativesButton=types.KeyboardButton(text='Официальным представителям', callback_data='officialRepresentatives')
termsRefPathershipsButton=types.KeyboardButton(text='Условия реферального партнерства', callback_data='termsRefPatherships')
toolsAndPromotionButton=types.KeyboardButton(text='Инструменты и продвижение', callback_data='toolsAndPromotion')
moreKeyboard.add(officialRepresentativesButton, notTakeApplicatonButton, accountPartnersButton, termsRefPathershipsButton, toolsAndPromotionButton )

termsRefPathershipsKeyboard=types.ReplyKeyboardMarkup(row_width=1)
whoCanParticipateButton=types.KeyboardButton(text='Кто может участвовать', callback_data='whoCanParticipate')
formsOfParthershipButton=types.KeyboardButton(text='Формы партнерства', callback_data='formsOfParthership')
howMuchCanEarnButton=types.KeyboardButton(text='Сколько можно заработать', callback_data='howMuchCanEarn')
termsRefPathershipsKeyboard.add(whoCanParticipateButton, formsOfParthershipButton, howMuchCanEarnButton)

howMuchCanEarnKeyboard=types.ReplyKeyboardMarkup(row_width=1)
additionalRemunerationButton=types.KeyboardButton(text='Дополнительное вознаграждение', callback_data='additionalRemuneration')
howMuchCanEarnKeyboard.add(additionalRemunerationButton)

formsOfParthershipKeyboard=types.ReplyKeyboardMarkup(row_width=1)
otherPatnershipOptionButton=types.KeyboardButton(text='Другие варианты партнерства', callback_data='otherPatnershipOption')
naturalPersonButton=types.KeyboardButton(text='Физлицо', callback_data='naturalPerson')
selfEmployedButton=types.KeyboardButton(text='Самозанятый', callback_data='selfEmployed')
urFaceButton=types.KeyboardButton(text='Юрлицо/ИП', callback_data='urFace')
retireeButton=types.KeyboardButton(text='Пенсионеры', callback_data='retiree')
formsOfParthershipKeyboard.add(naturalPersonButton, selfEmployedButton, urFaceButton, otherPatnershipOptionButton)
naturalPersonKeyboard=types.ReplyKeyboardMarkup(row_width=1).add(retireeButton)

toolsAndPromotionKeyboard=types.ReplyKeyboardMarkup(row_width=1)
websiteBannersButton=types.KeyboardButton(text='Баннеры для сайта', callback_data='websiteBanners')
socialMediaBannersButton=types.KeyboardButton(text='Баннеры для соцсетей', callback_data='socialMediaBanners')
widgetsButton=types.KeyboardButton(text='Виджеты', callback_data='widgets')
QRCodeButton=types.KeyboardButton(text='QR-код', callback_data='QRCode')
toolsAndPromotionKeyboard.add(websiteBannersButton, socialMediaBannersButton, widgetsButton, QRCodeButton)

officialRepresentativesKeyboard=types.ReplyKeyboardMarkup(row_width=1).add(toolsAndPromotionButton, applicationElbaButton, afterSubmitApplicationButton, statusApplicationButton)

backToMainMenuKeyboard=types.ReplyKeyboardMarkup(row_width=1)
backToMainMenuButton=types.KeyboardButton(text="Вернуться в главное меню", callback_data='backToMainMenu')
backToMainMenuKeyboard.add(backToMainMenuButton)#, helpButton)

@dp.message_handler(commands='start')
async def firstButton(message: types.Message):
    await message.answer('Здравствуйте!\n'
                         'Какие у вас появились вопросы?\n'
                         'Выберите интересующий раздел нажав на кнопку, или выберите “Помощь человека” для связи с сотрудником реферальной программы.', reply_markup=firstMenuKeyboard)

#Блок проблем кабинета партнера--

@dp.message_handler(content_types=['text'])
async def messageKeyboard(message):
    if message.text == "Вход в кабинет партнера":
        await bot.send_message(message.from_user.id,'Зайдите на сайт kontur.ru в раздел Реферальная программа - https://kontur.ru/partnership/online и нажмите «Войти в кабинет партнера».\n'
                              'Заходить в кабинет партнера необходимо по электронной почте, указанной при регистрации в реферальной программе.', reply_markup=loginAccountPartnersKeyboard)
        logger.debug('Пользователь нажал кнопку "Вход в кабинет партнера"')



    if message.text == "Частые проблемы":
        await bot.send_message(message.from_user.id,'Список частых проблем со входом в кабинет партнёра и как их решить.', reply_markup=accountProblemKeyboard)
        logger.debug('Пользователь нажал кнопку "Частые проблемы"')

    if message.text == "Чужие данные":
        await bot.send_message(message.from_user.id,'Если при входе в кабинет партнёра или при регистрации в реферальной программе вы видите чужое ФИО, то значит к аккаунту по вашей почте установилось имя из ЭЦП, которая привязана к аккаунту.\n'
                                      'Решение:\n'
                                      '1 Вы можете зайти в личный кабинет и поменять ФИО - https://cabinet.kontur.ru/\n'
                                      '2 Если вы участвуете в реферальной программе как физлицо и ФИО из аккаунта должны быть на этой почте, например, по ней вы работаете в Экстерне, то вам нужно зарегистрировать новую почту на ваши ФИО. После регистрации напишите на почту part@skbkontur.ru и мы подключим дополнительный аккаунт к реферальному коду.', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Чужие данные"')


    if message.text == "Другой код":
        await bot.send_message(message.from_user.id,'Если вы авторизовались по вашей почте и в кабинете партнёра теперь отображается новый код, то значит произошло объединение аккаунтов и вы создали новый кабинет партнёра.\n'
                                       'Напишите на почту part@skbkontur.ru и мы поможем восстановить доступ к старому аккаунту.', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Другой код"')


    if message.text == "Пропал доступ":
        await bot.send_message(message.from_user.id,'Возможно 2 сценария, почему так произошло:\n'
                                       '1) Вы авторизованы по ЭЦП, а аккаунт привязан к почте. Вам нужно выйти из аккаунта и войти по почте.\n'
                                       '2) Если вы точно знаете, что заходите по нужной почте и пропал доступ в кабинет партнёра, то значит произошло объединение аккаунтов.\n'
                                       'Напишите на почту part@skbkontur.ru с вашей почты, которая была подключена к реферальному коду и мы поможем восстановить доступ.\n', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Пропал доступ"')


    if message.text == "Кабинет партнера":
        await bot.send_message(message.from_user.id,'Выберите раздел кабинет партнёра', reply_markup=accountPartnersKeyboard)
        logger.debug('Пользователь нажал кнопку "Аккаунт партнера"')


    if message.text == "Главная страница":
        await bot.send_message(message.from_user.id,'*Анкета*\n'
                                         'На [главной странице](https://kontur.ru/account/partnership) кабинета партнера в блоке Анкета можно увидеть следующие данные: ФИО, электронная почта, телефон, код партнера. ФИО и почту при необходимости вы можете изменить самостоятельно в [личном кабинете](https://cabinet.kontur.ru/).\n'
                                         '\n'
                                         '*Код партнера*\n'
                                         'Уникальный партнерский код присваивается сразу после регистрации в программе. Он помогает фиксировать клиента за вами. Код вшит во все инструменты кабинета партнера.\n'
                                         '\n'
                                         '*Новости*\n'
                                         'С центрального баннера, расположенного на главной странице кабинета, можно перейти к новостям реферальной программы и Контура в целом.\n'
                                         '\n'
                                         '*Инструменты продвижения продуктов*\n'
                                         'Инструменты продвижения продуктов находятся на главной странице кабинета партнера. Ими можно пользоваться сразу после регистрации.\n', parse_mode='Markdown', disable_web_page_preview=True, reply_markup=toolsAndPromotionKeyboard)
        logger.debug('Пользователь нажал кнопку "Главная страница"')


    if message.text == "Ссылки":
        await bot.send_message(message.from_user.id,'Раздел ссылки в кабинете партнёра: https://kontur.ru/account/partnership\n'
                                         'Создать ссылку\n'
                                         'Вы можете сформировать свою ссылку на любую страницу сайта Контура с кодом партнера. Для этого выберите пункт «Создать свою ссылку», который находится после списка готовых ссылок или создайте ссылку вручную. Для этого в конце ссылки на нужную страницу добавьте параметр ?p=XXXX, где вместо XXXX вставьте ваш код партнера.\n'
                                         'Статистика\n'
                                         'В разделе доступна подробная статистика с фильтром по дате, продукту и метке. Здесь можно получить информацию о количестве переходов, заявках и конверсии.', parse_mode='Markdown', disable_web_page_preview=True, reply_markup=linksAccountKeyboard)
        logger.debug('Пользователь нажал кнопку "Ссылки"')


    if message.text == "Готовые ссылки":
        await bot.send_message(message.from_user.id,'В разделе «Ссылки» вы найдете готовые реферальные ссылки на более чем 40 продуктов, участвующих в программе. Во всех этих ссылках уже есть код партнера, что позволяет фиксировать переходы и покупки клиентов по ним. Нажмите на «Показать все ссылки», чтобы увидеть весь список.', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Готовые ссылки"')


    if message.text == "Создать ссылку":
        await bot.send_message(message.from_user.id,'Вы можете сформировать свою ссылку на любую страницу сайта Контура с кодом партнера. Для этого выберите пункт «Создать свою ссылку», который находится после списка готовых ссылок или создайте ссылку вручную. Для этого в конце ссылки на нужную страницу добавьте параметр ?p=XXXX, где вместо XXXX вставьте ваш код партнера.', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Создать ссылки"')


    if message.text == "Статистика":
        await bot.send_message(message.from_user.id,'В разделе доступна подробная статистика с фильтром по дате, продукту и метке. Здесь можно получить информацию о количестве переходов, заявках и конверсии.', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Статистика"')


    if message.text == "Заявки":
        await bot.send_message(message.from_user.id,'В [разделе](https://kontur.ru/account/partnership/orders) можно увидеть список заявок ваших клиентов. Воспользуйтесь фильтром по дате, продукту в заявке, статусу. Нажмите на интересующую строку и посмотрите историю работы с каждой заявкой и строкам в счете.',parse_mode='Markdown', disable_web_page_preview=True,reply_markup =applicationAccountKeyboard)
        logger.debug('Пользователь нажал кнопку "Заявки"')


    if message.text == "Отправка заявки":
        await bot.send_message(message.from_user.id,'Чтобы отправить заявку за клиента:\n'
                                            '1. Зайдите в кабинет [партнера](https://kontur.ru/account/login?ReturnUrl=%2faccount%2fpartnership)\n'
                                            '2. В «Инструментах продвижения продуктов» выберите «Отправить заявку».\n'
                                            '3. Выберите продукт в списке.\n'
                                            '4. Внесите почту, телефон, название организации, ИНН и КПП клиента.\n'
                                            '5. В комментариях укажите пожелания клиента или необходимый тариф. Если открылся список дополнительных опций, то отметьте нужное.',parse_mode='Markdown', disable_web_page_preview=True,reply_markup=submitApplicationKeyboard)
        logger.debug('Пользователь нажал кнопку "Отправка заявки"')


    if message.text == "Статусы заявок":
        await bot.send_message(message.from_user.id,'Каждой заявке присваивается статус, который означает ход ее обработки менеджером.\n'
                                             '🔸В работе — менеджер взял заявку в работу. Ожидайте смену статуса..\n'
                                             '🔸Отказ — на момент поступления заявки по клиенту уже велась работа, либо клиент не новый. Также отказ устанавливается, если по заявке нет выставленных счетов в течение 60 дней. Наведите курсор на статус и узнайте причину отказа.\n'
                                             '🔸Выставлен — менеджер выставил клиенту счет, ожидание оплаты.\n'
                                             '🔸Оплачен — клиент оплатил счет.\n'
                                             '🔸Нет оплаты — счет выставили, но клиент его еще не оплатил.\n'
                                             '🔸Подлежит вознаграждению — по счету будет начислено вознаграждение.\n'
                                             '🔸Вознагражден — вознаграждение уже начислено и находится в отчете, сумма указана рядом со статусом.\n', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Статусы заявки"')


    if message.text == "Выгрузка списка заявок в Excel":
        await bot.send_message(message.from_user.id,'Есть возможность выгрузить заявки списком в Excel, чтобы детально проанализировать информацию об источниках. Воспользуйтесь кнопкой «Скачать» справа от фильтров.', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Выгрузка списка заявок в Excel"')


    if message.text == "Получение вознаграждения":
        await bot.send_message(message.from_user.id,'Как получить вознаграждение можно узнать по коротким, но подробным видеороликам.\n'
                                          '[Как получить вознаграждение физическим лицам](https://support.kontur.ru/pages/viewpage.action?pageId=83871245#id-%D0%9F%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%D0%B2%D0%BE%D0%B7%D0%BD%D0%B0%D0%B3%D1%80%D0%B0%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F-%D0%92%D0%B8%D0%B4%D0%B5%D0%BE%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D0%B8%D1%8F%C2%AB%D0%9A%D0%B0%D0%BA%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C%D0%B2%D0%BE%D0%B7%D0%BD%D0%B0%D0%B3%D1%80%D0%B0%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%D1%84%D0%B8%D0%B7%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%BC%D0%BB%D0%B8%D1%86%D0%B0%D0%BC%C2%BB)\n'
                                          '[Как получить вознаграждение юридическим лицам/ИП](https://support.kontur.ru/pages/viewpage.action?pageId=83871245#id-%D0%9F%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%D0%B2%D0%BE%D0%B7%D0%BD%D0%B0%D0%B3%D1%80%D0%B0%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F-%D0%92%D0%B8%D0%B4%D0%B5%D0%BE%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D0%B8%D1%8F%C2%AB%D0%9A%D0%B0%D0%BA%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C%D0%B2%D0%BE%D0%B7%D0%BD%D0%B0%D0%B3%D1%80%D0%B0%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%D1%8E%D1%80%D0%B8%D0%B4%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%BC%D0%BB%D0%B8%D1%86%D0%B0%D0%BC%C2%BB)\n'
                                          'Для получения вознаграждения понадобится КЭП.\n'
                                          '🔸КЭП для юрлиц или ИП\n'
                                          'Партнеры-юрлица или ИП, у которых нет электронной подписи, должны выпустить ее самостоятельно.\n'
                                          '🔸КЭП для физлиц\n'
                                          'Партнеры-физлица, у которых нет электронной подписи, могут получить ее бесплатно.',parse_mode='Markdown', disable_web_page_preview=True, reply_markup = rewardKeyboard)
        logger.debug('Пользователь нажал кнопку "Получаение вознаграждения"')


    if message.text == "Условия начисления":
        await bot.send_message(message.from_user.id,'Вознаграждение начисляется только за новых клиентов по продукту. Продления не входят в реферальную программу.\n'
                                              'Вознаграждение начисляется за все новые сервисы, которые купит клиент по вашей заявке в течение 60 дней.\n'
                                              'Вознаграждение начисляется ежемесячно, в рублях, после достижения минимальной суммы реализации по всем продуктам.\n'
                                              'С размерами агентского вознаграждения по каждому продукту можно ознакомиться в [таблице](https://kontur.ru/partnership/online/rules#7).',parse_mode='Markdown', disable_web_page_preview=True,reply_markup=whenComesKeyboard)
        logger.debug('Пользователь нажал кнопку "Условия начисления"')


    if message.text == "Когда приходит":
        await bot.send_message(message.from_user.id,'Вознаграждение поступает в виде отчета на вкладку [«Вознаграждение»](https://kontur.ru/account/partnership/prize) к 15 числу месяца за предыдущий период.\n'
                                         'Если оплата по заявке была в декабре, то вознаграждение придёт 15 января, если оплата была в январе, то 15 февраля.',parse_mode='Markdown', disable_web_page_preview=True, reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Когда приходит"')


    if message.text == "Не учли заявку":
        await bot.send_message(message.from_user.id,'Если вы не нашли заявку в итоговом отчете, сначала необходимо проверить, что:\n'
                                          '🔸Счет был полностью оплачен.\n'
                                          '🔸Оплата счета прошла в прошлом отчетном месяце.\n'
                                          'Если все верно, напишите об ошибке на part@skbkontur.ru с указанием кода партнера и данными по заявке.',parse_mode='Markdown', disable_web_page_preview=True, reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Не учли заявку"')


    if message.text == "Отправить отчет в диадок":
        await bot.send_message(message.from_user.id,'Чтобы отправить отчет о вознаграждении в СКБ Контур и получить вознаграждение, необходимо отправить отчёт в Диадок.\n'
                                           '[Как отправить отчёт](https://support.kontur.ru/pages/viewpage.action?pageId=83871219)\n'
                                           'Если у вас несколько отчетов, то отправьте их каждый по отдельности.\n'
                                           'После проверки отчета вознаграждение будет перечислено в течение 5 рабочих дней.\n'
                                           'У физлиц из итоговой суммы вознаграждения удерживается 13% НДФЛ.', parse_mode='Markdown', disable_web_page_preview=True,reply_markup=sendReportOnDiadokKeyboard)
        logger.debug('Пользователь нажал кнопку "Отправить отчет в диадок"')


    if message.text == "Бесплатная КЭП для физлиц":
        await bot.send_message(message.from_user.id,'Чтобы выпустить электронную подпись для получения вознаграждения для физлица, отправьте, пожалуйста, на почту part@skbkontur.ru актуальную информацию: \n'
                                           '🔸ФИО\n'
                                           '🔸Регион, город/населенный пункт по месту где можете удостоверить личность\n'
                                           '🔸Телефон\n'
                                           '🔸Адрес электронной почты\n'
                                           '🔸ИНН\n'
                                           '🔸Код партнёра.\n'
                                           'После получения подписи вы сможете отправить отчёт в Диадок для получения вознаграждения.',reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Бесплатная КЭП для физлиц"')


    if message.text == "Не приняли отчет":
        await bot.send_message(message.from_user.id,'Если отчет по вознаграждению был отклонен с комментарием: «Вы выслали документы в «Головное подразделение» СКБ Контур — это значит, что вы отправили отчет на неверное подразделение. Документы на получение агентского вознаграждения необходимо отправлять в подразделение «Отчетность партнеров все регионы». Отправьте отчет заново, выбрав верное подразделение.', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Не приняли отчет"')


    if message.text == "Не пришли деньги":
        await bot.send_message(message.from_user.id,'Если прошло больше 8 дней после отправки отчета о вознаграждении в Диадок, а деньги не поступили на ваш расчетный счет, проверьте:\n'
                                          '🔸Отчет должен быть отправлен на подразделение ЗАО «ПФ «СКБ Контур», ИНН: 6663003127, подразделение «Отчетность партнеров, все регионы».\n'
                                          '🔸Отчет должен быть подписан сертификатом физлица, если вы участвуете в программе как физическое лицо или сертификатом юрлица, если вы участвуете в программе как юридическое лицо.\n'
                                          'Если все верно, напишите о проблеме на part@skbkontur.ru с указанием кода партнера.', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Не пришли деньги"')


    if message.text == "Получить вознаграждения без Диадок":
        await bot.send_message(message.from_user.id,'Получить вознаграждение без электронной подписи могут только физические лица. При этом ставка вознаграждения будет снижена на 40% из-за того, что мы не получаем от партнера подписанных отчетных документов.\n'
                                            'Чтобы вывести вознаграждение по ускоренному способу, при формировании отчета на последнем этапе выберите «Ускоренный способ». Ожидайте денежный перевод в течение 5-ти рабочих дней.', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Получить вознаграждения без Диадок"')


    if message.text == "Партнерам на ОСНО":
        await bot.send_message(message.from_user.id,'Юрлица или ИП, имеющие режим налогообложения ОСНО, обязаны отчитываться по НДС, поэтому при выставлении счета и акта Контуру за оказанные услуги, им также необходимо предоставить счет-фактуру (далее — с/ф). Счет, акт и отчет формируются автоматически в кабинете партнера при начислении вознаграждения, а с/ф необходимо подготовить самостоятельно.\n'
                                            'Какие требования к счету-фактуре:\n'
                                            '🔸С/ф должна быть сформирована в xml формате в соответствии с приказом 820.\n'
                                            '🔸С/ф формируется в своей бухгалтерской программе или, если программа не позволяет сформировать с/ф в xml формате, можно создать ее вручную в Диадоке: в меню Документы в списке «Создать в редакторе» выберите «Счет-фактура». Откроется страница создания счета-фактуры. Заполните поля. Подробнее в статье Создание счета-фактуры.\n'
                                            '🔸В с/ф «Наименование товара» в колонке (1а) укажите в соответствии с наименованием в акте в сформированном в кабинете партнера отчете по вознаграждению.\n'
                                            '🔸Дата с/ф должна совпадать с датой акта в сформированном в кабинете партнера отчете по вознаграждению.\n'
                                            '🔸С/ф необходимо отправлять в Диадок в одном пакете с отчетом по вознаграждению (счет, акт и таблица отчета), сформированном в кабинете партнера.\n', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Партнерам на ОСНО"')

#Блок отправки заявки
    if message.text == "Отправить заявку":
        await bot.send_message(message.from_user.id,'Чтобы отправить заявку за клиента:\n'
                                            '1. Зайдите в кабинет [партнера](https://kontur.ru/account/login?ReturnUrl=%2faccount%2fpartnership)\n'
                                            '2. В «Инструментах продвижения продуктов» выберите «Отправить заявку».\n'
                                            '3. Выберите продукт в списке.\n'
                                            '4. Внесите почту, телефон, название организации, ИНН и КПП клиента.\n'
                                            '5. В комментариях укажите пожелания клиента или необходимый тариф. Если открылся список дополнительных опций, то отметьте нужное.',parse_mode='Markdown', disable_web_page_preview=True,reply_markup=submitApplicationKeyboard)
        logger.debug('Пользователь нажал кнопку "Отправить заявку"')


    if message.text == "После отправки заявки":
        await bot.send_message(message.from_user.id,'В течение 15 минут отправленная заявка появится в кабинете партнера на вкладке [Заявки.](https://kontur.ru/account/partnership/orders) Если этого не произошло, напишите на part@skbkontur.ru\n'
                                            'В течение 2-3 часов по контактам из заявки связывается менеджер продаж Контура, консультирует и выставляет счет. Если по заявке не связались, напишите об этом нам на эл. почту part@skbkontur.ru\n'
                                            'После того, как клиент оплатит счет, вам будет начислено вознаграждение. Оно поступит в виде отчета на вкладку [Вознаграждение](https://kontur.ru/account/partnership/prize) к 15 числу месяца, следующего за месяцем, в котором прошла оплата.\n',parse_mode='Markdown', disable_web_page_preview=True, reply_markup=statusApplicationKeyboard)
        logger.debug('Пользователь нажал кнопку "После отправки заявки"')


    if message.text == "После отправки заявки":
        await bot.send_message(message.from_user.id,'Статусы заявок на вкладке [Заявки](https://kontur.ru/account/partnership/orders) информируют о том, на каком этапе находится заявка. Можно воспользоваться фильтром по дате, продукту, статусу. Кликните на нужную строку и посмотрите историю работы с каждой заявкой и строкам в счете.\n'
                                             '🔸В работе — менеджер взял заявку в работу. Ожидайте смену статуса.\n'
                                             '🔸Отказ — на момент поступления заявки по клиенту уже велась работа, либо клиент не новый. Также отказ устанавливается, если по заявке нет выставленных счетов в течение 60 дней. Наведите курсор на статус и узнайте причину отказа.\n'
                                             '🔸Счет выставлен — кликните на статус, чтобы посмотреть детальную информацию о счете.\n'
                                             '🔸Выставлен — менеджер выставил клиенту счет, ожидание оплаты.\n'
                                             '🔸Оплачен — клиент оплатил счет, ожидайте расчета вознаграждения.\n'
                                             '🔸Нет оплаты — клиент еще не оплатил счет.\n'
                                             '🔸Подлежит вознаграждению — по счету будет начислено вознаграждение.\n'
                                             '🔸Вознагражден — вознаграждение уже начислено.\n',parse_mode='Markdown', disable_web_page_preview=True, reply_markup=statusNotSubjectKyeboard)
        logger.debug('Пользователь нажал кнопку "Статусы заявок"')


    if message.text == 'Статус: "Не подлежит вознаграждению"':
        await bot.send_message(message.from_user.id,'У выставления данного статуса может быть несколько причин:\n'
                                           '🔸Клиент не новый, счет на продление. В реферальной программе вознаграждение начисляется только за подключение новых клиентов по продукту.\n'
                                           '🔸Продукт не участвует в реферальной программе. Например, Контур EDI. Проверить, участвует ли продукт и какой по нему % вознаграждения, можно в п.5.2 [договора-оферты.](https://kontur.ru/partnership/online/oferta)\n'
                                           '🔸Счет выставлен на дополнительную услугу, например за организацию рабочего места или дополнительный сертификат в рамках какого-либо продукта. Доп.услуги в рамках реферальной программы не вознаграждаются.\n'
                                           '🔸Счет еще не оплачен. Смена статуса произойдет после поступления оплаты на расчетный счет Контура.',parse_mode='Markdown', disable_web_page_preview=True, reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Статус: "Не подлежит вознаграждению"')


    if message.text == 'Заявка на Эльбу':
        await bot.send_message(message.from_user.id,'По продукту Эльба нельзя отправить заявку, потому что у Эльбы регистрация и нет формы заявки. Зарегистрироваться можно только на сайте Эльбы.\n'
                                         '\n'
                                         'Чтобы порекомендовать клиентам Эльбу, отправьте клиенту реферальную ссылку из кабинета партнёра: https://kontur.ru/account/partnership/links', reply_markup=backToMainMenuKeyboard)
        logger.debug('Заявка на Эльбу')



#Блок еще
    if message.text == 'Еще...':
        await bot.send_message(message.from_user.id,'Другие вопросы', reply_markup=moreKeyboard)
        logger.debug('Пользователь нажал кнопку "Еще"')


    if message.text == 'Официальным представителям':
        await bot.send_message(message.from_user.id,'Если вы уже сотрудничаете с Контуром как официальный представитель, то вы тоже можете использовать кабинет партнёра для отправки заявок за клиента.\n'
                                         '🔸Если у вас открыт прайс на продукт и у клиента нет брони, то он попадёт к вам на обслуживание, и вы выступите как L-агент и S-агент. \n'
                                         '🔸Если у вас не открыт прайс на продукт или клиент уже забронирован, то он уйдёт по распределению в другой отдел продаж, а вы получите вознаграждение как L-агент.', reply_markup=officialRepresentativesKeyboard)
        logger.debug('Пользователь нажал кнопку "Официальным представителям"')


    if message.text == 'Условия реферального партнерства':
        await bot.send_message(message.from_user.id,'Реферальная программа — это упрощенная форма сотрудничества по [договору-оферте](https://kontur.ru/partnership/online/oferta). При регистрации каждому партнеру присваивается уникальный партнерский код. Его можно увидеть в [кабинете партнера](https://kontur.ru/account/partnership) в блоке «Анкета». Все инструменты кабинета содержат такой код. Он позволяет системе фиксировать клиента за вами.\n'
                                          'Партнеры рекомендуют сервисы Контура с помощью реферальных ссылок и других инструментов кабинета партнера. Продажу сервисов осуществляет Контур, а партнеру начисляется вознаграждение за привлеченных новых клиентов. Вознаграждение приходит в виде отчета в кабинет партнера на следующий месяц после оплаты клиентом сервиса.',parse_mode='Markdown', disable_web_page_preview=True, reply_markup=termsRefPathershipsKeyboard)
        logger.debug('Пользователь нажал кнопку "Условия реферального партнерства"')


    if message.text == 'Кто может участвовать':
        await bot.send_message(message.from_user.id,'Кто может участвовать\n'
                                          '🔸Бухгалтеры, вебмастера, физические и юридические лица, которым интересно данное предложение.\n'
                                          '🔸SMM-специалисты, занимающиеся продвижением услуг в социальных сетях.\n'
                                          '🔸Владельцы специализированных порталов и блогов (бухгалтерия, бизнес).\n'
                                          '🔸Любые лояльные пользователи, которые готовы рекомендовать продукты СКБ Контур для решения бизнес-задач своим коллегам, друзьям и знакомым.\n'
                                          'Кто не может участвовать\n'
                                          '🔸Физические лица, состоящие с СКБ Контур в трудовых отношениях.\n'
                                          '🔸Юридические лица, оказывающие СКБ Контур услуги по аналогичным договорам.\n'
                                          '🔸Иные аффилированные с СКБ Контур физические и юридические лица.', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Кто может учавствовать"')


    if message.text == 'Сколько можно заработать':
        await bot.send_message(message.from_user.id,'Вознаграждение — фиксированный процент от оплаты новых пользователей, которые отправили заявку/зарегистрировались в сервисе СКБ Контур с партнерским кодом или перешли по реферальной ссылке партнера. Размер вознаграждения зависит от выбранного сервиса — от 5 до 50%. В среднем наши партнеры зарабатывают 20 000 рублей в месяц. Посмотрите [таблицу](https://kontur.ru/partnership/online/rules#7) вознаграждения по продуктам.', parse_mode='Markdown', disable_web_page_preview=True, reply_markup=howMuchCanEarnKeyboard)
        logger.debug('Пользователь нажал кнопку "Сколько можно заработать"')


    if message.text == 'Дополнительное вознаграждение':
        await bot.send_message(message.from_user.id,'Если вы приведете в программу другого реферального партнера, то мы будем начислять вам дополнительные 2% от оплаченных счетов его клиентов. Для этого воспользуйтесь инструментом «Приводите новых партнеров» на главной странице кабинета.', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Дополнительные вознаграждения"')


    if message.text == 'Формы партнерства':
        await bot.send_message(message.from_user.id,'Формы партнерства:', reply_markup=formsOfParthershipKeyboard)
        logger.debug('Пользователь нажал кнопку "Формы партнерства"')


    if message.text == 'Другие варианты партнерства':
        await bot.send_message(message.from_user.id,'Официальный представитель\n'
                                          'Форма сотрудничества для юридических лиц и ИП, по которой после прохождения обучения и заключения договора партнер становится официальным представителем – Сервисным центром. Это подразумевает полное взаимодействие с клиентом на всех этапах: консультирование, работа с продажами и продлениями.\n'
                                          'Если вас интересует данный тип сотрудничества, то оставьте заявку на странице и обсудите варианты сотрудничества.\n'
                                          'Международное партнерство\n'
                                          'Почта для зарубежных партнеров world@skbkontur.ru.', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Другие варианты партнерства"')


    if message.text == 'Физлицо':
        await bot.send_message(message.from_user.id,'Из вознаграждения удерживается НДФЛ — 13 %. \n'
                                         'Бесплатная КЭП для получения вознаграждения.', reply_markup=naturalPersonKeyboard)
        logger.debug('Пользователь нажал кнопку "Физлицо"')


    if message.text == 'Самозанятый':
        await bot.send_message(message.from_user.id,'Юридически самозанятое население из-за спецрежима не имеет права работать по агентской схеме и по агентскому договору, который является основным в реферальной программе. Самозанятый может работать в программе как физлицо, но из суммы вознаграждения будет вычитываться и уплачиваться в ФНС 13% НДФЛ.', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Самозанятый"')


    if message.text == 'Юрлицо/ИП':
        await bot.send_message(message.from_user.id,'Нет вычета НДФЛ 13 %.\n'
                                         'Необходимо приобрести электронную подпись на юрлицо, если ее нет.\n'
                                         'Для перечисления вознаграждения у партнера должен быть открыт счет в банке.', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Юрлицо\ИП"')


    if message.text == 'Пенсионеры':
        await bot.send_message(message.from_user.id,'Пенсионерам не запрещено участвовать в программе, но есть свои нюансы. В момент вывода вознаграждения на счет мы подаем данные в ПФР о полученном вами доходе.\n'
                                              'Потенциальному партнеру, который является пенсионером, необходимо уточнить в своем отделении ПФР, повлияет ли доход по агентскому договору на пенсионные отчисления. При необходимости можно зарегистрировать кабинет на другого человека.', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Пенсионеры"')


    if message.text == 'Инструменты и продвижение':
        await bot.send_message(message.from_user.id,'Чтобы рекомендовать сервисы Контура, используйте [инструменты продвижения](https://kontur.ru/partnership/tools) из кабинета партнера. Инструменты бесплатны, пользоваться ими можно сразу после регистрации в реферальной программе.', parse_mode='Markdown', disable_web_page_preview=True, reply_markup=toolsAndPromotionKeyboard)
        logger.debug('Пользователь нажал кнопку "Инструменты и продвежение"')


    if message.text == 'Баннеры для сайта':
        await bot.send_message(message.from_user.id,'Если у вас есть свой интернет-ресурс — сайт или блог, то разместите на нем рекламные баннеры продуктов Контура. Все баннеры разработаны нашими дизайнерами и отлично смотрятся на любых сайтах. Это удобный инструмент онлайн-продвижения.\n'
                                         'Как разместить баннер:\n'
                                         '1. Нажмите «Подготовить баннер».\n'
                                         '2. Выберите продукт в списке, нажав на его название.\n'
                                         '3. Выберите нужный размер. Выберите страницу для ссылки и проставьте метку SUBID, если нужно.\n'
                                         '4. Нажмите «Скопировать код». Полученный код теперь можно вставить на сайт[.](https://support.kontur.ru/download/attachments/16221763/014.png)',parse_mode='Markdown', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Банеры для сайта"')


    if message.text == 'Баннеры для соцсетей':
        await bot.send_message(message.from_user.id,'У нас есть готовые баннеры для соцсетей, с помощью которых партнеры могут продвигаться и в этом онлайн-канале. Чтобы разместить баннер в социальной сети:\n'
                                              '1. Нажмите «Разместить пост» в блоке «Публикация баннера в социальных сетях».\n'
                                              '2. Выберите продукт в списке, баннер и нажмите «Публиковать».\n'
                                              '3. В открывшемся окне выберите, куда будет вести ссылка и установите метку SUBID, если нужно.\n'
                                              '4. Нажмите на значок той социальной сети, где хотите разместить ссылку: Вконтакте, Facebook, Одноклассники, Instagram.\n'
                                              '5. Выберите, куда опубликовать подготовленный баннер: на свою страницу, в сообщество или поделиться им в личных сообщениях.', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Банеры для соцсетей "')


    if message.text == 'Виджеты':
        await bot.send_message(message.from_user.id,'С помощью виджетов клиенты смогут оставлять заявки на продукты Контура, не уходя с вашего сайта. При этом заявки будут уходить с вашим кодом партнера.\n'
                                              'Все виджеты можно найти в разделе [Инструменты](https://kontur.ru/partnership/tools) и на главной странице кабинета партнера.\n'
                                              'Доступны несколько типов виджетов:\n'
                                              '🔸Виджет формы заявки. Чтобы получить виджет — заполните форму: укажите ваш код партнера, продукт. Получите HTML-код, скопируйте его и интегрируйте на свой сайт сами или с помощью разработчика вашего сайта.\n'
                                              '🔸Виджет продуктовой строки поиска. Данный тип виджета демонстрирует возможность поиска в сервисе. Доступны виджеты по продуктам: Диадок, Фокус, Светофор, Норматив, Закупки.\n'
                                              '🔸Виджет подбора сертификата подписи.\n'
                                              '🔸Виджет калькулятора и виджет цен. Встройте на сайт калькулятор отпускных, больничных, декретных от Контур.Бухгалтерии, чтобы продемонстрировать возможности сервиса и заинтересовать им[.](https://www.mindomo.com/ru/mindmap/mind-map-4f85d62500074a8bb7c2baabfddc6cb9#:~:text=https%3A//support.kontur.ru/download/attachments/16221763/019.png)', parse_mode='Markdown', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Виджеты"')


    if message.text == 'QR-код':
        await bot.send_message(message.from_user.id,    'QR-код — это двухмерный штрихкод, который содержит зашифрованную информацию: ссылку на сайт или соцсеть, текст или статью. Ваши офлайн-клиенты, наведя камеру мобильного на QR-код, размещенный на визитке или листовке, смогут перейти на сайт или другой онлайн-ресурс\n'
                                             'Чтобы сгенерировать QR-код со своей реферальной ссылкой:\n'
                                             '1. Нажмите «Получить QR-код» в инструментах продвижения кабинета партнера.\n'
                                             '2. Откроется генератор QR-кодов. В поле «URL-адрес» введите реферальную ссылку со своим партнерским кодом. Как создать такую ссылку, читайте выше в разделе «Реферальные ссылки».\n'
                                             '3. Произведите настройки внешнего вида и нажмите «Создать QR-код». В правой части страницы сгенерируется QR-код.\n'
                                             '4. Выберите формат, в котором будете его сохранять: PNG или SVG. Нажмите «Скачать».\n'
                                             '5. Дождитесь, пока картинка скачается на ваше устройство.\n', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "QR-код"')

#Кнопка возврата
    if message.text == 'Вернуться в главное меню':
        await bot.send_message(message.from_user.id, 'Выберите интересующий раздел', reply_markup=firstMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Вернуться в главное меню"')

#Блок рекомендаций продукта
    if message.text == 'Какие продукты рекомендовать':
        await bot.send_message(message.from_user.id,'Выберите продукт, который хотите рекомендовать или аудиторию, которой хотите рекомендовать.',reply_markup = recommendationsKeyboard)
        logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

    if message.text == 'Выберите продукт':
        await bot.send_message(message.from_user.id,'[Выберите продукт](https://support.kontur.ru/pages/viewpage.action?pageId=18350835)',parse_mode='Markdown', reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Выберите продукт"')

    if message.text == 'Выберите аудиторию':
        await bot.send_message(message.from_user.id,
                               '[Выберите аудиторию](https://support.kontur.ru/pages/viewpage.action?pageId=83870810)',parse_mode='Markdown',reply_markup=backToMainMenuKeyboard)
        logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='helpButton')
async def helpMessage(helpMessage : types.Message):
    await helpMessage.answer('Оператор скоро вам ответит')


executor.start_polling(dp,skip_updates=True)




