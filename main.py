#from turtle import title
import requests 
from re import purge
from cgitb import text
import disnake
from disnake.ext import commands
import asyncio

import json
import random
import os
# кукарику всм пунктами, списками? +а ок

intents = disnake.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix=('lq!'),intents=intents,)

bot.remove_command('help')
class HelpTest(disnake.ui.Select):
    def __init__(self):
        options = [
            disnake.SelectOption(
                label='🗂Модерация',
            )


        ]
        super().__init__(
            placeholder='test',
            min_values=1,
            max_values=1,
            options=options 

        )
    async def callback(self, interaction: disnake.MessageInteraction):
        await interaction.response.send_message(embed=disnake.Embed(title='Модерация', description='lq!ban \n lq!kick', color=disnake.Colour.red()))
class HelpTestV(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(HelpTest())
@bot.slash_command(description='Помощь')
async def help(inter:disnake.AppCmdInter):
    await inter.response.send_message(view=HelpTestV())
async def test(ctx):
    await ctx.send(f'test')
class Help(disnake.ui.View):
    def __init__(self):
        super().__init__()
@bot.command()
async def popit(ctx):
    v1 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v2 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v3 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v4 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v5 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v6 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v7 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v8 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v9 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v10 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v11 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v12 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v13 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v14 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v15 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v16 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v17 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v18 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v19 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v20 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v21 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v22 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v23 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v24 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow']
    v25 = ['white_large','orange', 'blue', 'red', 'purple', 'green', 'yellow'] 

    embed = disnake.Embed(
        title = 'Поп-ит',
        description = f'||:{str(random.choice(v1))}_square:|| ||:{str(random.choice(v2))}_square:|| ||:{str(random.choice(v3))}_square:|| ||:{str(random.choice(v4))}_square:|| ||:{str(random.choice(v5))}_square:||\n||:{str(random.choice(v6))}_square:|| ||:{str(random.choice(v7))}_square:|| ||:{str(random.choice(v8))}_square:|| ||:{str(random.choice(v9))}_square:|| ||:{str(random.choice(v10))}_square:||\n||:{str(random.choice(v11))}_square:|| ||:{str(random.choice(v12))}_square:|| ||:{str(random.choice(v13))}_square:|| ||:{str(random.choice(v14))}_square:|| ||:{str(random.choice(v15))}_square:||\n||:{str(random.choice(v16))}_square:|| ||:{str(random.choice(v17))}_square:|| ||:{str(random.choice(v18))}_square:|| ||:{str(random.choice(v19))}_square:|| ||:{str(random.choice(v20))}_square:||\n||:{str(random.choice(v21))}_square:|| ||:{str(random.choice(v22))}_square:|| ||:{str(random.choice(v23))}_square:|| ||:{str(random.choice(v24))}_square:|| ||:{str(random.choice(v25))}_square:||',
        colour = disnake.Colour.from_rgb(228,100,16)
    )
    embed.set_footer(text=f'Powered by IndigoBot! \nПо запросу **{ctx.author}**')
    msgg = await ctx.send(embed=embed)
@bot.command()
async def ball(ctx,*, text):
    v1 = ['Да','Нет', 'Хз', 'Возможно', 'Конечно', '...', 'ERROR 1000-7']
    embed = disnake.Embed(
        title = f'{text}',
        description = f'{str(random.choice(v1))}',
        colour = disnake.Colour.random()
    )
    embed.set_footer(text=f'Powered by IndigoBot! \nПо запросу {ctx.author}')
    msgg = await ctx.send(embed=embed)
@bot.command()
async def hack(ctx,*, text):

    if text == "<@921837838872485898>":
        return await ctx.send(embed=disnake.Embed(title='Error', description='ПОШЕЛ НАХУЙ ЭТО МОЙ СОЗДАТЕЛЬ', color=disnake.Colour.dark_green()))
    else:
        d =await ctx.send(embed=disnake.Embed(title='Hacking', description=f'Hacking {text}', color=disnake.Colour.dark_green()))
        await asyncio.sleep(10.1)
        await d.edit(embed=disnake.Embed(title='Hacked!', description=f'User {text} hacked!  ', color=disnake.Colour.dark_green()))


@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, user:disnake.Member=None, time=None, reason='Отсутвует'):
    mute_role = disnake.utils.get(ctx.guild.roles, name='LQMUTED')
    if not mute_role:
        mute_role = await ctx.guild.create_role(name='LQMUTED', permissions=disnake.Permissions(send_messages=False, read_messages=False))
    else:
        if user == ctx.author:
            await ctx.send(embed=disnake.Embed(title='Есть ли смысл самого себя мьютить?'))
            return
        else:
            await user.add_roles(mute_role, reason=reason)
            if time:
                time = float(convert_time(time))
                print(time)
                await asyncio.sleep(time)
                
                await user.remove_roles(mute_role, reason='UNMUTE '+reason)
            else:
                pass
@bot.slash_command(description='Мьют а что такого?')
@commands.has_permissions(manage_messages=True)
async def mute(inter, user:disnake.Member=None, time=None, reason='Отсутвует'):
    mute_role = disnake.utils.get(inter.guild.roles, name='LQMUTED')
    if not user:
        await inter.response.send_message(embed=disnake.Embed(title='вы не указали юзера!'))
        return
    if not mute_role:
        mute_role = await inter.guild.create_role(name='LQMUTED', permissions=disnake.Permissions(send_messages=False, read_messages=False))
    else:
        if user == inter.author:
            await inter.response.send_message(embed=disnake.Embed(title='Есть ли смысл самого себя мьютить?'))
            return
        else:
            await user.add_roles(mute_role, reason=reason)
            if time:
                time = float(convert_time(time))
                print(time)
                await asyncio.sleep(time)
                
                await user.remove_roles(mute_role, reason='UNMUTE '+reason)
            else:
                pass
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed=disnake.Embed(title='Команда не была найдена', description='Введите `lq!help` или `/help` для помощи', color=disnake.Colour.red()))
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('**Пожалуйста, введите текст.**')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=disnake.Embed(title='Вы не модератор! <:nolol:958447133294473296> ', color=disnake.Colour.red()))
    else:
        print(error)
@bot.event
async def on_slash_command_error(inter, error):
    if isinstance(error, commands.MissingPermissions):
        await inter.response.send_message(embed=disnake.Embed(title='Вы не модератор! <:nolol:958447133294473296> ', color=disnake.Colour.red()))
    else:
        await inter.response.send_message(embed=disnake.Embed(title='Тут это ошибочка', description=error))
def convert_time(time:str):
    if time.endswith('w'):
        time -= 'w'
        return float(int(time) * 604800)
    elif time.endswith('s'):
        time -= 's'
        return float(int(time) * 1)
    elif time.endswith('mon'):
        time -= 'mon'
        return float(int(time) * 2629744)
    elif time.endswith('d'):
        time -= 'd'
        return float(int(time) * 86400)
    elif time.endswith('h'):
        time -= 'h'
        return float(int(time) * 3600)
    elif time.endswith('m'):
        time -= 'm'
        return float(int(time) * 60)
    else:
        return 0
@commands.has_permissions(ban_members=True)
@bot.command(description='Банит чела')
async def ban(ctx, user:disnake.Member=None, time:str=None, * ,reason='Отсуствует'):
    if not user:
        await ctx.send(embed=disnake.Embed(title='Вы не указали пользователя! <:nolol:958447133294473296> ', color=disnake.Colour.red()))
        return
    if user == ctx.author:
        await ctx.send(embed=disnake.Embed(title='Вы не можете забанить самого себя! <:nolol:958447133294473296> ', color=disnake.Colour.red()))
        return
    await user.send(embed=disnake.Embed (title='Вас забанили :no_entry: ', description=f'вас забанили на сервере: {ctx.guild.name}\nПричина: {reason}'))
    await user.ban(reason=reason)
    await ctx.send(embed=disnake.Embed(title='Пользователь был успешно забанен! :white_check_mark: ', description=f'**Подробности:**\nМодератор: {ctx.author}\nЧеловек: {user}\nПричина: {reason}', color=disnake.Colour.brand_green()))
    if time:
        time = float(convert_time(time))
        print(time)
        await asyncio.sleep(time)
        
        await user.unban()
    else:
        pass
@commands.has_permissions(ban_members=True)
@bot.slash_command(description='Банит чела', name='бан')
async def ban_member(inter, user:disnake.Member=None, * ,reason='Отсуствует'):
    if not user:
        await inter.response.send_message(embed=disnake.Embed(title='Вы не указали пользователя! <:nolol:958447133294473296> ', color=disnake.Colour.red()))
        return
    if user == inter.author:
        await inter.response.send_message(embed=disnake.Embed(title='Вы не можете забанить самого себя! <:nolol:958447133294473296> ', color=disnake.Colour.red()))
        return
    await user.ban(reason=reason)
    await inter.response.send_message(embed=disnake.Embed(title=f'Пользователь был успешно забанен! :white_check_mark: ', description=f'подробности:\nМодератор: {inter.author} \nЧеловек:{user}\nПричина:{reason}', color=disnake.Colour.brand_green()))
    await user.send(embed=disnake.Embed(title='Вас забанили :no_entry: ', description=f'вас забанили на сервере {inter.guild.name}\nза {reason}'))
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user:disnake.Member=None, * ,reason='Отсуствует'):
    if not user:
        await ctx.send(embed=disnake.Embed(title='Вы не указали пользователя! <:nolol:958447133294473296>', color=disnake.Colour.red()))
        return
    await user.kick(reason=reason)
    await ctx.send(embed=disnake.Embed(title=f'Пользователь был успешно кикнут! :white_check_mark: ', description=f'Подробности:\nМодератор: {ctx.author} \nЧеловек:{user}\nПричина:{reason}', color=disnake.Colour.brand_green()))

@bot.command()
async def help(ctx):
    await ctx.send(embed=disnake.Embed(title='Мои команды!', description=' \n`lq!test` **Просто тест** \n`lq!ban` **Блокировка человека на сервере** \n`lq!kick` **Выгоняет человека с сервера** \n`lq!adb` **Инструкция как поставить рекавери** \n`lq!say` **Писать от имени бота** \n`lq!search` **Поиск в гугл** \n`lq!popit` **Простой поп ит** \n`lq!ball` **Да или нет** ', color=disnake.Colour.random()))
@bot.command()
async def invite(ctx):
    await ctx.send(embed=disnake.Embed(title='Мой инвайт!', description='https://discord.thorize?client_id=948178804256432159&permissions=277025401856&scope=bot+applications.commands', color=disnake.Colour.random()))
@bot.command()
async def adb(ctx):
    await ctx.send(embed=disnake.Embed(title='Как поставить кастомное рекавери :calling: **(Гайд)** ', description=' \n> ```1. Заходим в cmd, выключаем телефон или планшет \n> 2. потом грузимся в fastboot, и нам надо драйвера fastboot и adb (platform-tools) \n> 3. потом вводим команду fastboot, а далее fastboot devices, \n> 4. потом вводим команду fastboot flash recovery {ваш рекавери} ``` ', color=disnake.Colour.random()))
@bot.event
async def on_message(message):
    if message.content == "<@948178804256432159>":
        await message.channel.send(embed=disnake.Embed(title='Привет! Я IndigoBOT!', description='Мой префикс `lq!`, чтоб узнать мои команды, \nвведите команду `lq!help`', color=disnake.Colour.random()))
    if message.guild:
     await bot.process_commands(message)
@bot.event
async def on_ready():
    print('Бот запущен!')
    while True: 
        await bot.change_presence(status=disnake.Status.online, activity=disnake.Game("IndigoBOT!(BETA)"))
        await asyncio.sleep(5)
        
        await bot.change_presence(status=disnake.Status.online,activity=disnake.Game("Надо помощь? Введите команду lq!help"))
@bot.command()
async def say(ctx, *, text:str=None, amount = 1):
    if text == None:
        Embed = disnake.Embed(title='<:nolol:958447133294473296>|Ошибка', description = 'Вы не указали текст', color=disnake.Color.red())
        Embed.set_footer(text=f'{ctx.author}')
        await ctx.send(embed=Embed)
    else:
        await ctx.channel.purge(limit = amount)
        Embed = disnake.Embed(description = text, color=0x4b0082)
        Embed.set_footer(text=f'{ctx.author}')
        await ctx.send(embed=Embed)
@bot.command()
async def search(ctx, *,text):
    embed=disnake.Embed(title=text, url=f'https://google.gik-team.com/?q={text}', color=0x30d5c8)
    embed.set_footer(text=f'Искал: {ctx.author} • Поиск в Google')
    await ctx.send(embed=embed)
@bot.command()
async def version(ctx):
    await ctx.send(embed=disnake.Embed(title='Version', description='██╗███╗░░██╗██████╗░██╗░██████╗░░█████╗░ IndigoBOT!\n██║████╗░██║██╔══██╗██║██╔════╝░██╔══██╗ Python \n██║██╔██╗██║██║░░██║██║██║░░██╗░██║░░██║Disnake \n██║██║╚████║██║░░██║██║██║░░╚██╗██║░░██║BOT \n ██║██║░╚███║██████╔╝██║╚██████╔╝╚█████╔╝\n╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░╚═════╝░░╚════╝░', color=disnake.Colour.dark_green()))
@bot.command()
async def update(ctx):
    m =await ctx.send(embed=disnake.Embed(title='Поиск обновлений', description='Подождите', color=disnake.Colour.dark_green()))
    await asyncio.sleep(4.3)
    await m.edit(embed=disnake.Embed(title='Обновление найдено!', description='Загрузка обновления ', color=disnake.Colour.dark_green()))
    await asyncio.sleep(4.9)
    await m.edit(embed=disnake.Embed(title='Обновление загружено!', description='🟩', color=disnake.Colour.dark_green()))
    await asyncio.sleep(0.3)
    await m.edit(embed=disnake.Embed(title='Обновление загружено!', description='🟩🟩', color=disnake.Colour.dark_green()))
    await asyncio.sleep(0.2) 
    await m.edit(embed=disnake.Embed(title='Обновление загружено!', description='🟩🟩🟩', color=disnake.Colour.dark_green()))
    await asyncio.sleep(0.7) 
    await m.edit(embed=disnake.Embed(title='Обновление загружено!', description='🟩🟩🟩🟩', color=disnake.Colour.dark_green()))
    await asyncio.sleep(0.5)
    await m.edit(embed=disnake.Embed(title='Обновление загружено!', description='🟩🟩🟩🟩🟩', color=disnake.Colour.dark_green()))
    await asyncio.sleep(0.3)
    await m.edit(embed=disnake.Embed(title='Обновление загружено!', description='🟩🟩🟩🟩🟩🟩', color=disnake.Colour.dark_green()))
    await asyncio.sleep(0.3)
    await m.edit(embed=disnake.Embed(title='Обновление загружено!', description='🟩🟩🟩🟩🟩🟩🟩', color=disnake.Colour.dark_green()))
    await asyncio.sleep(0.9)
    await m.edit(embed=disnake.Embed(title='Обновление загружено!', description='🟩🟩🟩🟩🟩🟩🟩🟩', color=disnake.Colour.dark_green()))
    await asyncio.sleep(0.3)
    await m.edit(embed=disnake.Embed(title='Обновление загружено!', description='🟩🟩🟩🟩🟩🟩🟩🟩🟩', color=disnake.Colour.dark_green()))
    await asyncio.sleep(0.6)
    await m.edit(embed=disnake.Embed(title='Обновление загружено!', description='🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩', color=disnake.Colour.dark_green()))
    await asyncio.sleep(0.3)
    await m.edit(embed=disnake.Embed(title='Обновление загружено!', description='🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩', color=disnake.Colour.dark_green()))
    await asyncio.sleep(0.4)
    await m.edit(embed=disnake.Embed(title='Обновление завершено!', description='Через 5 Секунд будет рестарт бота!', color=disnake.Colour.dark_green()))
    await asyncio.sleep(5.0)
    await bot.change_presence(status=disnake.Status.offline, activity=None)
    await asyncio.sleep(0.1)
    await m.edit(embed=disnake.Embed(title='Загрузка', description='Подождите.', color=disnake.Colour.dark_green()))
    await asyncio.sleep(0.1)
    await m.edit(embed=disnake.Embed(title='Загрузка', description='Подождите..', color=disnake.Colour.dark_green()))
    await asyncio.sleep(0.1)
    await m.edit(embed=disnake.Embed(title='Загрузка', description='Подождите...', color=disnake.Colour.dark_green()))
    await asyncio.sleep(1.9)
    await m.edit(embed=disnake.Embed(title='Бот загружен!', description='Можете использовать бота!', color=disnake.Colour.dark_green()))
bot.run(os.environ['TOKEN'])
