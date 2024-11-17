import os
#e
import aiohttp
import disnake as discord
import time
import asyncio
from disnake.ext import commands
import random
import sqlite3
# -----------------------
intents = discord.Intents.all()
intents.members = True
# хуйня ебаная

# переменные
rolemute = 'Mute'
text = '͜•人 ͜•@everyone```diff\nMZUT TEAM```\nhttps://discord.gg/44UZQVsNcV'
prefix = '/'
wl = [1262346557315878913]


#status
st1 = "As"
st2 = "Asko"
st3 = "Askori"
st4 = "Askoria"
#status cooldown 
# желательно 3 и больше секунды (в другом случае бот замедляется)
st1cd =  3
st2cd = 3
st3cd = 3
st4cd = 3
#1001010100110




bot = commands.Bot(command_prefix = prefix, intents = intents)

bot.remove_command('help')
#СТАТУС НАЧАЛО

@bot.event
async def on_ready():
  print('Loading...')
  await asyncio.sleep(0.5)
  os.system('clear')
  print('Loading..')
  await asyncio.sleep(0.5)
  os.system('clear')
  print('Loading.')
  await asyncio.sleep(0.5)
  os.system('clear')
  print('Loading...')
  await asyncio.sleep(0.5)
  os.system('clear')
  print('Loading..')
  await asyncio.sleep(0.5)
  os.system('clear')
  print('▄▀█ █▀ █▄▀ █▀█ █▀█ █ ▄▀█')
  print('█▀█ ▄█ █░█ █▄█ █▀▄ █ █▀█')
  print('') 
  print('█▄▄ █▄█   █▄░█ █▀█ ▀█▀ █▀▀ █░░ ▄▀█ █▀▀ █▄▀')
  print('█▄█ ░█░   █░▀█ █▄█ ░█░ █▀░ █▄▄ █▀█ █▄▄ █░█ ')

  print('Логи будут высвечиватся ниже-----')



  while True:
    await bot.change_presence(status = discord.Status.online, activity = discord.Game(name = st1))
    await asyncio.sleep(st1cd)
    await bot.change_presence(status = discord.Status.online, activity = discord.Game(name = st2))
    await asyncio.sleep(st2cd)
    await bot.change_presence(status = discord.Status.online, activity = discord.Game(name = st3))
    await asyncio.sleep(st3cd)
    await bot.change_presence(status = discord.Status.online, activity = discord.Game(name = st4))
    await asyncio.sleep(st4cd)

# СТАТУС КОНЕЦ

#асинки
async def checker(ctx):
  member = ctx.author
  tag = member.name + "#" + member.discriminator
  display_name = member.display_name  
  user_id = member.id  
  guild = ctx.guild
  guild_name = guild.name  
  guild_id = guild.id  
  member_count = guild.member_count 
  print(f"Пользователь: {tag} ({display_name}, ID: {user_id})")
  print(f"Сервер: {guild_name} (ID: {guild_id}, Участников: {member_count})")


# КОМАНДЫ НАЧАЛО

@bot.slash_command(name='ban')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    """Бро, это очевидно."""
    try:
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} был забанен.")
    except discord.Forbidden:
        await ctx.send("У меня нет прав на бан этого пользователя.")
        
       

@bot.slash_command(name='hug')
async def hug(ctx, member: discord.Member = None):
    """Обнять упомянутого пользователя"""
    if member is None:
        await ctx.send('Упомяни кого хочешь обнять!')
    else:
        await ctx.send(f'{ctx.author.name} обнимает {member.name}!')
        print("------\n.hug")
        await asyncio.create_task(checker(ctx))


@bot.slash_command(name='roll')
async def roll(ctx):
    """Бросить кубик"""
    number = random.randint(1, 6)
    await ctx.send(f'🎲 Вы бросили кубик и получили: {number}')
    print("------\n.roll")
    await asyncio.create_task(checker(ctx))

@bot.slash_command(name='userinfo')
async def userinfo(ctx, member: discord.Member = None):
    """Отображает информацию о упомянутом пользователе"""
    member = member or ctx.author
    embed = discord.Embed(title=f'Информация о {member.name}', color=discord.Color.blue())
    embed.add_field(name='ID', value=member.id)
    embed.add_field(name='Создан', value=member.created_at.strftime('%Y-%m-%d %H:%M:%S'))
    embed.add_field(name='Вступил в сервер', value=member.joined_at.strftime('%Y-%m-%d %H:%M:%S'))
    await ctx.send(embed=embed)
    print("------\n.usinfo")
    await asyncio.create_task(checker(ctx))

@bot.slash_command(name="guess", description="Попробуй угадать число от 1 до 100!")
async def guess(interaction: discord.ApplicationCommandInteraction):
    """Игра на угадывание числа."""
    number = random.randint(1, 100)  # Загаданное число
    
    embed = discord.Embed(
        title="Игра: Угадай число!",
        description="Я загадал число от 1 до 100. Введите ваше предположение в чат.",
        color=discord.Color.blue()
    )
    await interaction.response.send_message(embed=embed)

    def check(message: discord.Message):
        return (
            message.author == interaction.author
            and message.channel == interaction.channel
            and message.content.isdigit()
        )

    while True:
        try:
            # Ожидание ответа от пользователя
            guess_message = await bot.wait_for("message", check=check, timeout=30.0)
            guess_number = int(guess_message.content)

            if guess_number < number:
                embed.description = "Слишком маленькое число. Попробуй ещё раз!"
                await interaction.channel.send(embed=embed)
            elif guess_number > number:
                embed.description = "Слишком большое число. Попробуй ещё раз!"
                await interaction.channel.send(embed=embed)
            else:
                embed.description = f"Поздравляю! Ты угадал число {number}. 🎉"
                embed.color = discord.Color.green()
                await interaction.channel.send(embed=embed)
                break
        except asyncio.TimeoutError:
            embed.description = f"Время вышло! Загаданное число было {number}."
            embed.color = discord.Color.red()
            await interaction.channel.send(embed=embed)
            break


@bot.slash_command(name='factorial')
async def factorial(ctx, number: int):
    """Вычисляет факториал числа."""
    if number < 0:
        await ctx.send("Факториал не существует для отрицательных чисел.")
        return
    result = 1
    for i in range(1, number + 1):
        result *= i
    await ctx.send(f"Факториал числа {number} равен {result}.")

@bot.slash_command(name='pi')
async def pi(ctx, precision: int = 100):
    """Выводит число Пи с заданной точностью."""
    from math import pi
    pi_value = round(pi, precision)
    await ctx.send(f"Число Пи с точностью до {precision} знаков: {pi_value}")

@bot.slash_command(name="lovecalc", description="Посчитать совместимость с другим пользователем")
async def lovecalc(interaction: discord.CommandInteraction, user: discord.User):
    compatibility = random.randint(0, 100)
    embed = discord.Embed(
        title="Тест на совместимость",
        description=f"💖 Совместимость между вами и {user.mention} составляет **{compatibility}%**!",
        color=discord.Color.purple()
    )
    await interaction.send(embed=embed)

@bot.slash_command(name="catfact", description="Получить случайный факт о кошках")
async def catfact(interaction: discord.CommandInteraction):
    facts = [
        "Кошки могут поворачиваться на 180 градусов, чтобы следить за объектами.",
        "Кошки способны прыгать на 5 раз больше длины своего тела.",
        "Некоторые кошки могут бегать со скоростью до 48 км/ч.",
        "Кошки могут производить более 100 различных звуков.",
        "У кошек уникальные отпечатки носа, как у людей — их невозможно перепутать.",
        "Кошки могут спать от 12 до 16 часов в день, это примерно 2/3 жизни.",
        "Кошки могут мявкать по-разному в зависимости от породы, а также в зависимости от настроения.",
        "У кошек есть третье веко, которое они используют для защиты глаз.",
        "Кошки обладают хорошим слухом и могут слышать частоты, которые недоступны для человеческого уха.",
        "Кошки могут прыгать на высоту, в 6 раз превышающую их длину тела.",
        "Кошки могут следить за объектами в темноте благодаря большому количеству палочек в их глазах.",
        "Когда кошка поднимает хвост, это часто означает, что она счастлива и дружелюбна.",
        "У кошек есть способность «засыпать» с открытыми глазами, что помогает им оставаться настороже.",
        "Кошки могут отдыхать с поднятыми лапами, сохраняя при этом их в тепле, что помогает поддерживать тело в форме.",
        "Около 30% кошек любят воду и могут спокойно играть в ванной или запрыгивать в раковину.",
        "Исследования показывают, что кошки могут выстраивать более крепкие связи с людьми, чем с другими кошками.",
        "У кошек есть способность использовать свои усы для оценки ширины пространства перед ними.",
        "Когда кошка мурчит, это может означать как удовольствие, так и стресс — важно учитывать контекст.",
        "Кошки — отличные охотники, их точность и скорость делают их невероятно эффективными в ловле добычи.",
        "Известно, что кошки могут воспринимать иерархию в стае людей и соответственно менять свое поведение.",
        "Каждая кошка может быть любима и уважена за свою индивидуальность — они умеют быть и независимыми, и привязанными.",
        "Кошки могут общаться не только с людьми, но и с другими кошками, используя специальные звуки и жесты.",
        "Некоторые кошки любят лазить по деревьям, и даже могут спать на их ветках.",
        "У кошек есть уникальная способность к засыпанию, которая позволяет им быстро восстанавливать энергию.",
        "Кошки известны своим вниманием к гигиене — они часто тщательно вылизывают свои лапки и шерсть.",
        "Кошки могут ловить мышей на расстоянии до 10 метров благодаря своему острию зрения.",
        "При движении кошки ее хвост сохраняет баланс, это помогает ей быть такой гибкой и ловкой.",
        "Маленькие кошки могут родить потомство в возрасте всего 5-6 месяцев.",
        "С древнейших времен кошки были символом тайны и магии, а также олицетворением независимости.",
        "Глаза кошек могут расширяться или сужаться в зависимости от света или их настроения.",
        "Кошки не только мурлыкают, но также могут издавать разные звуки, чтобы выразить свои чувства, например, хрюкать или рычать.",
        "Когда кошка хочет привлечь внимание хозяев, она может тереться головой о их ноги — это проявление привязанности.",
        "У кошек очень чувствительная кожа, поэтому они могут ощущать малейшие изменения в температуре и влажности."
    ]
    
    selected_fact = random.choice(facts)
    embed = discord.Embed(title="Факт о кошках", description=selected_fact, color=discord.Color.purple())
    await interaction.send(embed=embed)

@bot.event
async def on_member_join(member: discord.Member):
    # Канал приветствий (если он существует)
    channel = discord.utils.get(member.guild.text_channels, name="приветствия")
    
    # Картинка для приветствия
    welcome_image = "https://cdn.discordapp.com/attachments/1306168235414130808/1307715252082839582/standard.gif?ex=673b503c&is=6739febc&hm=7013c19a7b3c40dec7e8b4ea06ed70a770119a3bfd958d445cf5e6aa38fc4610& "  # Укажите ссылку на вашу картинку

    # Приветственное сообщение
    embed = discord.Embed(
        title=f"Добро пожаловать, {member.name}!",
        description=f"Приветствуем тебя на нашем сервере, {member.mention}! Мы рады, что ты присоединился!",
        color=discord.Color.blue()
    )
    embed.set_image(url=welcome_image)

    # Если канал найден, отправляем сообщение с картинкой
    if channel:
        await channel.send(embed=embed)
    else:
        # Если канал не найден, отправляем в общий чат
        await member.guild.system_channel.send(embed=embed)





@bot.slash_command(name='calc')
async def calc(ctx, num1: float, operator: str, num2: float):
    """Выполняет простые арифметические операции."""
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            await ctx.send("На ноль делить нельзя!")
            return
        result = num1 / num2
    else:
        await ctx.send("Неверный оператор. Используйте: +, -, *, /.")
        return
    await ctx.send(f"Результат: {result}")

@bot.slash_command(name='number')
async def random_number(ctx, start: int, end: int):
    """Генерирует случайное число в заданном диапазоне."""
    if start > end:
        await ctx.send("Начало диапазона не может быть больше конца.")
        return
    random_num = random.randint(start, end)
    await ctx.send(f"Случайное число от {start} до {end}: {random_num}")

@bot.slash_command(name="pet_cat", description="Погладь котика для хорошего настроения!")
async def pet_cat(ctx):
    await ctx.send("🐱 Вы погладили котика! Котик мурчит и становится счастливым!")

@bot.slash_command(name='character')
async def character(ctx):
    """Более тысячи параметров для генерации персонажа"""
    names = [
        "Алексей", "Екатерина", "Иван", "Мария", "Сергей", "Анастасия", "Дмитрий", 
        "Ольга", "Андрей", "Сосал", "Александр", "Виктор", "Михаил", "Наталья", 
        "Елизавета", "Георгий", "Тимофей", "Дарина", "Вера", "София", "Кирилл"
    ]

    weapons = [
        "меч", "щит", "лук", "арбалет", "копье", "палица", "топор", "сабля", 
        "боевой молот", "алебарда", "кикери", "катана", "дага", "крюк", "ястребинный меч",
        "двойные кинжалы", "боевой топор", "секира", "рапира", "меч с проклятой рукояткой",
        "меч дракона", "цепи", "глефа", "древний посох", "меч с рунами", "алебарда с лезвием черного металла",
        "стрелы с магическим наконечником", "теневая сабля", "гарпун", "метательные звезды", "джаггернаут",
        "громовой топор", "рукоятка змеи", "небесный меч", "шипы из адского железа"
    ]
    
    magical_items = [
        "чаша судьбы", "плащ невидимости", "посох древнего магистра", 
        "камень всеведущего", "книга заклинаний", "кристалл мудрости", 
        "сфера времени", "заклинательный амулет", "волшебный жезл",
        "кристалл вечности", "амулет душ", "перо феникса", "зеркало истины",
        "зачарованный мантия", "талисман удачи", "чашка бесконечности", "куб бесконечного знания",
        "саркофаг времени", "перстень крови", "медальон врат", "свиток древних знаний", 
        "шар ясновидения", "печать демона", "кубок маны", "тотем духа", "лунный амулет",
        "ожерелье стихий", "книга пророчеств", "шлем Тёмного мага"
    ]
    
    titles = [
        "рыцарь", "маг", "воин", "шаман", "лучник", "колдун", "разведчик", "воевода", "принц", 
        "король", "палач", "странник", "владыка", "разрушитель", "целитель", "тиран", "победитель", 
        "покоритель", "паломник", "священник", "капитан", "предатель", "тень", "старейшина", "чародей", 
        "легенда", "провидец", "сказочник", "ветеран", "древний", "воин-странник", "магистр", "чародей-эксперт", 
        "повелитель", "темный маг", "мастер меча", "повелитель стихий", "потомок богов", "железный рыцарь", 
        "покровитель", "посланник", "парашютист", "мститель", "следопыт", "король магии", "кровавый маг", 
        "покоритель миров", "охотник на демонов", "демоноборец", "архимаг", "повелитель темных сил", "мудрец", 
        "психолог", "механик", "генерал", "эксперт по алхимии", "прикрытие", "авантюрист", "повелитель природы", 
        "страж", "странствующий маг", "воин света", "предвестник", "древний страж", "царь зверей", "повелитель времени"
    ]

    # Генерация случайных элементов для персонажа
    name = random.choice(names)
    weapon = random.choice(weapons)
    magical_item = random.choice(magical_items)
    title = random.choice(titles)
# Создание Embed с украшенным текстом
    embed = discord.Embed(
        title="Ваш Новый Персонаж",
        description="Вот персонаж, который вы только что создали! Удачи в путешествиях по этому волшебному миру!",
        color=discord.Color.from_rgb(75, 0, 130)  # Темно-синий цвет
    )
    embed.add_field(name="Имя", value=f" 🧐 {name}", inline=False)
    embed.add_field(name="Оружие", value=f"🏹 {weapon}", inline=False)
    embed.add_field(name="Магический Предмет", value=f"🔮 {magical_item}", inline=False)
    embed.add_field(name="Звание", value=f"🏅 {title}", inline=False)

    await ctx.send(embed=embed)








@bot.slash_command(name="feedback", description="Оставьте отзыв")
async def feedback(interaction: discord.AppCmdInter, message: str):
    
    # Здесь message — обязательное поле для ввода
    await interaction.response.send_message(f"Ваш отзыв: {message}")



@bot.slash_command(name='8ball', aliases=['8b'])
async def eight_ball(*, interaction: discord.AppCmdInter,  question):
  """Задает вопрос волшебному шару."""
  responses = [
    "Да, конечно.",
    "Безусловно.",
    "Без сомнения.",
    "Скорее всего.",
    "Хорошие шансы.",
    "Подожди и посмотри.",
    "Спроси снова позже.",
    "Лучше не говорить сейчас.",
    "Моя ответ - нет.",
    "Очень сомнительно."
  ]
  await interaction.response.send_message(f"Вопрос: {question}\nОтвет: {random.choice(responses)}")
  print("------\n.8b")
  await asyncio.create_task(checker(ctx))

@bot.slash_command(name='mute')
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member):
    """Мутит пользователя"""
    #Запрещает пользователю отправлять
    print("------\n.mute")
    await asyncio.create_task(checker(ctx))
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not role:
        # Если роли "Muted" нет, создаем ее
        
        role = await ctx.guild.create_role(name=rolemute, permissions=discord.Permissions(send_messages=False))
        # Назначаем роль "Muted" всем каналам
        for channel in ctx.guild.channels:
          await channel.set_permissions(role, send_messages=False)
    
    await member.add_roles(role)
    await ctx.send(f"{member.mention} был отключен от чата.")

 

@bot.slash_command(name='help')
async def help(ctx):
    """Справочник📖"""
    print("------\n.help")
    await asyncio.create_task(checker(ctx))
    embed = discord.Embed(
        title="📖 Справочник команд",
        description="Используй команды с указанным префиксом: .\nВот список доступных команд:",
        color=discord.Color.purple()
    )
    
    # Категория: Управление
    embed.add_field(
        name="⚙️ Управление сервером",
        value=(
            f"{prefix}**ban [пользователь]** - Банит пользователя\n\n"
            f"{prefix}**hug [пользователь]** - Обнять упомянутого пользователя\n\n"
            f"{prefix}**roll** - Бросить кубик\n\n"
            f"{prefix}**userinfo [пользователь]** - Информация о пользователе\n\n"
            f"{prefix}**factorial [число]** - Вычисляет факториал числа\n\n"
            f"{prefix}**pi [точность]** - Выводит число Пи с заданной точностью\n\n"
            f"{prefix}**calc [число1] [оператор] [число2]** - Выполняет арифметические операции\n\n"
            f"{prefix}**number [начало] [конец]** - Генерирует случайное число в диапазоне\n\n"
            f"{prefix}**mute [пользователь]** - Мутит пользователя\n\n"
            f"{prefix}**unmute [пользователь]** - Размут пользователя\n\n"
            f"{prefix}**shutdown** - Выключает бота (только владелец)"
        ),
        inline=False
    )

    # Категория: Развлечения
    embed.add_field(
        name="🎮 Развлечения",
        value=(
            f"{prefix}**guess** - Игра: Угадай число от 1 до 100\n\n"
            f"{prefix}**lovecalc [пользователь]** - Проверка совместимости с другим пользователем\n\n"
            f"{prefix}**catfact** - Случайный факт о кошках\n\n"
            f"{prefix}**pet_cat** - Погладь котика для хорошего настроения\n\n"
            f"{prefix}**8ball [вопрос]** - Вопрос волшебному шару"
        ),
        inline=False
    )

    # Категория: Генерация персонажей
    embed.add_field(
        name="⚔️ Генерация персонажей",
        value=(
            f"{prefix}**character** - Генерация персонажа с оружием, магическим предметом и титулом"
        ),
        inline=False
    )

    
#
    embed.set_footer(text="NotFlack | Сделано с ❤️", icon_url="https://cdn.discordapp.com/attachments/1306168235414130808/1307066703078752429/32_8EE3FB2.png?ex=6738f43a&is=6737a2ba&hm=610304b72ebb49c5dd054844756e77e7ecb87a499517b686d7be20d03b61ed5c&")
    
    await ctx.send(embed=embed)

@bot.slash_command(name='clear')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    """Быстрое удаление сообщений"""
    await ctx.channel.purge(limit=amount + 1)  # +1 для удаления команды
    await ctx.send(f'Удалено {amount} сообщений.', delete_after=5)
    print("------\n.clerg")
    await asyncio.create_task(checker(ctx))

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("У вас недостаточно прав для выполнения этой команды.")

@bot.slash_command(name='cat')
async def cat(ctx):
    """Выводит фотку котика ^-^"""
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.thecatapi.com/v1/images/search') as response:
            cat_data = await response.json()
            await ctx.send(cat_data[0]['url'])
            print("------\n.cat")
            await asyncio.create_task(checker(ctx))
@bot.slash_command(name='dog')
async def dog(ctx):
    """Рандомное фото собаки"""
    async with aiohttp.ClientSession() as session:
        async with session.get('https://dog.ceo/api/breeds/image/random') as response:
            dog_data = await response.json()
            await ctx.send(dog_data['message'])
@bot.slash_command(name='randcolor')
async def color(ctx):
    """Выводит рандомный HEX код"""
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    await ctx.send(f'Ваш случайный цвет: {color}')







import datetime
@bot.slash_command(name='time')
async def время(ctx):
  """Показывает текущее время."""
  current_time = datetime.datetime.now().strftime("%H:%M:%S")
  await ctx.send(f"Текущее время (не точно): {current_time}")
  await asyncio.create_task(checker(ctx))


@bot.slash_command(name='idea')
@commands.cooldown(1, 180, commands.BucketType.user)
async def idea(ctx, *, message):
  """оповещает создателя."""
  author_id = ctx.author.id
  await asyncio.create_task(checker(ctx))
  sent_message = await ctx.send(f"Идея от: <@!{author_id}>\n```{message}```\n *Отправлено!*")
  await sent_message.add_reaction("✅")
  # Отправляем сообщение в личку создателя
  dm_channel = await bot.fetch_user(1262346557315878913)
  await client.fetch_user(847491579106820167)
  await dm_channel.send(f"Идея от: <@!{author_id}> \n```{message}```")
  print("------\n.ideag")
  await asyncio.create_task(checker(ctx))

@bot.slash_command(name='meme')
async def meme(ctx):
    """Рандомный мем(на англ)"""
    async with aiohttp.ClientSession() as session:
        async with session.get('https://meme-api.com/gimme') as response:
            meme_data = await response.json()
            await ctx.send(meme_data['url'])
            print("------\n.meme")
            await asyncio.create_task(checker(ctx))






@idea.error
async def idea_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.send(f"Подожди ещё {error.retry_after:.2f} секунд, не нужно забивать личку создателя!")
    await asyncio.create_task(checker(ctx))



@bot.slash_command(name='ping')
async def ping(ctx):
    """Задержка между ботом и Discord api"""
    start_time = time.monotonic()
    end_time = time.monotonic()
    latency = (end_time - start_time) * 1000
    await ctx.send(f'Pong! Задержка: {latency:.2f} мс')
    print("------\n.ping")
    await asyncio.create_task(checker(ctx))



bot.run('MTMwNTU4MDQ5Mjc0NTA4MDg2Mg.GwqfIE.sY_ct4a7vHqxknsZCAe4tZExMjIyO2b0UjwnNk')
