import discord
from discord.ext import commands,tasks
import random
import json
import os
from itertools import cycle
from asyncio import sleep as s
import datetime
import time
import requests
import random
from replit import db
from keep_alive import keep_alive
import nest_asyncio
import asyncio
nest_asyncio.apply()

client = commands.Bot(command_prefix = '!')



name_id = {'AGELaVolpe': '720352409817186345', 'AGE_Atomsk': '433367046248595466', 'AGE_Bruno': '245258944212238341',\
           'AGE_Cats': '359361962414440449', 'Cats On Mars': '359361962414440449', 'AGE_Leofar': '328108124953247746',\
              'Leofarr': '328108124953247746', 'AGE_LoRD': '346869109339717633', 'LoRDKYRaN': '346869109339717633',\
            'AGE_Lux': '400768894521966604', 'luxury777': '400768894521966604', 'AGE_Solid': '222808023255613440',\
            'SolidD': '222808023255613440', 'AGE_Vent': '207924668844212225', 'Vent': '207924668844212225',\
            'Ainthe': '234077877958606849', 'Angel': '563787164987686925', 'Apeks': '139662285089013760',\
            'Ben': '281087273418752001', 'traffyboi': '120428736637173760',\
                'CloudExt': '362102976581599241', 'Collin': '884080970666504202',\
            'Collin still PURE F2P': '884080970666504202', 'Consutron': '153660394349658112', 'Dan': '274133775917645824',\
            'Dante': '270699806949638144', 'Evian': '591897303573331978', 'Glass': '244998176275300352', \
            'Gunther': '315112026093649920', 'G̷̉̕u̷͑̚ǹ̴̕ẗ̴̕ḧ̵̏e̴͆́ṙ̵͝': '315112026093649920', 'Idk': '168124858113196032',\
            'Ioni': '202635850599759873', 'JAV_Dostic': '312642855330119681', 'JAV_Eolf ': '162171044566794240',\
            'JAV_Moss': '207111511410212865', 'JAV_booyah': '211679799867998218', 'eph || booyah': '211679799867998218',\
            'KENSHIN': '509805857425588224', 'Levi': '223398953549299712', 'Link2D3atH': '139262103214227456',\
            'Mixer': '201177323293114368', 'MoonMan': '250779681257684992', '#Yui': '314404530936610827',\
            'Odyn': '553055447469522944', 'ReddlsRow': '274682038970482688', 'SenorTonto': '130852537199886337',\
            'Spikeman': '134863783444086784', 'Spike/Chitoge': '134863783444086784', 'Tachii': '176147192719998977',\
             'Tedo': '826618819191242792', 'Tydio': '339045828276781056',\
            'ULTRA_Foxs': '396398521462554624', 'Foxcolt': '396398521462554624', 'UltraChuck': '199916175776284674',\
            'Chuckno14': '199916175776284674', 'Ultra_Asa': '189088073689071617', 'AsaTyre': '189088073689071617',\
            'Ultra_Moon': '497120107819040768', 'Moon': '497120107819040768', 'virant (Variant-1)': '579199616143327258',\
            'WindaRB': '673517909125103619', 'Daedalus': '106850505631772672', 'latvice': '281088989610377216',\
            'mUmU': '500124144755671040', 'zero00': '563082215198556211', 'maple': '253994447782543361',\
            'GonBu': '465942228791984149', 'aile': '123456789', 'zeta': '333666', 'PlainDoe': '189350494328586240', 'Zerefsis': '215506389353758720', 'Tympest': '292615553942683648', 'leafa1244': '187764065131560960', 'Tatumi': '394763425777057794', 'Firis': '323444581033050113', 'Ciaosuh': '218659635513524224'}
    
id_name = {'333666': 'zeta','720352409817186345':'LaVolpe', '433367046248595466': 'Atomsk', '245258944212238341': 'Bruno',\
          '359361962414440449': 'Cats On Mars', '328108124953247746': 'Leofarr', '346869109339717633': 'LoRDKYRaN',\
            '400768894521966604': 'luxury777', '222808023255613440': 'SolidD', '207924668844212225': 'Vent',\
            '234077877958606849': 'Ainthe', '563787164987686925': 'Angel', '139662285089013760': 'Apeks',\
             '281087273418752001': 'Ben', '120428736637173760': 'traffyboi',\
            '362102976581599241': 'CloudExt', '884080970666504202': 'Collin', '153660394349658112': 'Consutron',\
            '274133775917645824': 'Dan', '270699806949638144': 'Dante', '591897303573331978': 'Evian',\
            '244998176275300352': 'Glass', '315112026093649920': 'Gunther', '168124858113196032': 'Idk',\
            '202635850599759873': 'Ioni', '312642855330119681': 'Dostic', '162171044566794240': 'Eolf',\
            '207111511410212865': 'Moss', '211679799867998218': 'eph || booyah', '509805857425588224': 'Kenshin',\
            '223398953549299712': 'Levi', '139262103214227456': 'Link2D3atH', '201177323293114368': 'Mixer',\
            '250779681257684992': 'MoonMan', '314404530936610827': 'Yui', '553055447469522944': 'Odyn',\
            '274682038970482688': 'ReddlsRow', '130852537199886337': 'SenorTonto', '134863783444086784': 'Spike/Chitoge',\
            '176147192719998977': 'Tachii', '826618819191242792': 'Tedo',\
            '339045828276781056': 'Tydio', '396398521462554624': 'Foxcolt', '199916175776284674': 'Chuckno14',\
            '189088073689071617': 'AsaTyre', '497120107819040768': 'Moon', '579199616143327258': 'virant (Variant-1)',\
            '673517909125103619': 'WindaRB', '106850505631772672': 'Daedalus', '281088989610377216': 'latvice',\
            '500124144755671040': 'mUmU', '563082215198556211': 'zero00', '253994447782543361': 'maple',\
            '465942228791984149':'GonBu', '123456789': 'aile', '189350494328586240': 'PlainDoe', '215506389353758720': 'Zerefsis', '292615553942683648': 'Tympest','394763425777057794': 'Tatumi', '187764065131560960': 'leafa', '323444581033050113': 'Firis', '218659635513524224': 'Ciaosuh'}

AGE_members = {}
for x in id_name:
  AGE_members[x] = 0


def add_slime(member_id, number):
  if member_id in db:
    slime_count = db[member_id]
    slime_count += int(number)
    db[member_id] = slime_count
  else:
    db[member_id] = 1

        
def minus_slime(member_id):
  slime_count = db[member_id]
  slime_count -= 1
  db[member_id] = slime_count
    

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, \
                        activity = discord.Game('Counting slimes!'))
    print('Bot is ready.')



    
@client.listen('on_message') 
async def message(message):
    if message.author == client.user:
        return
    if message.channel.id == 887894832708730881:
     
        if ('<@&887894985398157363>') in message.content or ('<@&887915507804692511>') in message.content : 

          
           
                    if len(message.raw_mentions) != 0:
                        member_id = str(message.raw_mentions[0])
                        
                        
                        
                        add_slime(member_id,1)
                        await message.channel.send(f'Woah! It is a slime!  (ﾉ>ω<)ﾉ  Klee has counted {db[member_id]} slimes for {id_name[member_id]}!')
                            
                    elif (message.content.split()[1].lower() == 'me') or ('me' in message.content.split()[1].lower()):
                        member_id = str(message.author.id)
                        
                        add_slime(member_id,1)
                        
                        await message.channel.send(f'Woah! It is a slime!  (ﾉ>ω<)ﾉ  Klee has counted {db[member_id]} slimes for {id_name[member_id]}!')
                        
                    else:
                        name_mentioned = message.content.split()[1]
                        
                        member_id = 0
                        
                        if name_mentioned.lower() == 'dan':
                            member_id = str(name_id['Dan'])
                        elif name_mentioned.lower() == 'moon':
                            member_id = str(name_id['Moon'])
                        else:
                            for x in name_id:
                                if name_mentioned.lower() in x.lower():
                                    member_id = str(name_id[x])
                                
                        if member_id == 0:
                            await message.channel.send('Uh, Klee does not know this name, and therefore cannot add this slime to anyone...')
                            return
                                
                        add_slime(member_id,1)

                    
                        await message.channel.send(f'Woah! It is a slime!  (ﾉ>ω<)ﾉ  Klee has counted {db[member_id]} slimes for {id_name[member_id]}!')



@client.command()
async def doubleping(ctx, *, member):
    if ctx.channel.id == 887894832708730881 or ctx.channel.id == 887967982356148254:

        if (member.lower() == 'me') or ('me' in member.lower()):
            member_id = str(ctx.message.author.id)
                
            minus_slime(member_id)
            
        else: 
            name_mentioned = member
                        
            member_id = 0
                        
            if name_mentioned.lower() == 'dan':
                member_id = str(name_id['Dan'])
            elif name_mentioned.lower() == 'moon':
                member_id = str(name_id['Moon'])
            else:
                for x in name_id:
                    if name_mentioned.lower() in x.lower():
                        member_id = str(name_id[x])
                                
            if member_id == 0:
                await ctx.send('Uh, Klee does not know this name, and therefore cannot subtract this slime from anyone...')
                return
                        
            minus_slime(member_id)


            
            
        await ctx.send(f'Klee has subtracted a slime from {id_name[member_id]}! The number of slimes {id_name[member_id]} has summoned has gone from {int(db[member_id])+1} to {db[member_id]}')
        return
    
    
    
def is_it_me(ctx): #custom check
    return ctx.author.id == 253994447782543361
#whether the author's id is the same as the specified user's id
    
def two_people(ctx): #custom check
  if ctx.author.id == 315112026093649920:
    return True
  elif ctx.author.id == 253994447782543361:
    return True



@client.command()
async def total(ctx):
  if ctx.channel.id == 887894832708730881 or ctx.channel.id == 887967982356148254:

    member_count = db.keys()
    total = 0
    for member_id in member_count:
        slime_count = db[member_id]
        total += slime_count

    await ctx.send(f'For the current season, Ultra has {len(id_name)} members with 3 Altras, and we have summoned {total} slimes so far! Dear RNG God, please help us summon more slime! ٩(๑•̀ω•́๑)۶')
    
def multiple_max(dictionary):
    max_key = max(dictionary, key=dictionary.get)
    first = [max_key]
    
    for x in dictionary:
        if x != max_key:
            if dictionary[x] == dictionary[max_key]:
                first += [x]
    return first
    
@client.command()
@commands.check(two_people)
async def first(ctx): #change to AGE_members
    #age_members = {'maple': 4,'kenshin': 16,'gunther':5,'moon':16,'asa':5} #AGE_members is id to slime count
  if ctx.channel.id == 887894832708730881 or ctx.channel.id == 887967982356148254:

    member_count = db.keys()
    dictionary = {}
    for member_id in member_count:
      dictionary[member_id] = db[member_id]

    copy = dict(dictionary)
    
    first = multiple_max(copy)
    
    copy1 = dict(dictionary)
    for x in copy1:
        for y in first:
            if x == y:
                del copy[x]
                
    second = multiple_max(copy)
    
    copy2 = dict(copy1)
    for x in copy2:
        for y in second:
            if x == y:
                del copy[x]
                
    third = multiple_max(copy)
    
    first_name= []
    for x in first:
        first_name += [id_name[x]]
        
    second_name= []
    for y in second:
        second_name += [id_name[y]]
        
    third_name= []
    for z in third:
        third_name += [id_name[z]]
                
    await ctx.send(f'The current first is {first_name} with {db[x]} slimes! Second is {second_name} with {db[y]} slimes, and third is {third_name} with {db[z]} slimes! They are the best! ⁽⁽٩(๑˃̶͈̀ ᗨ ˂̶͈́)۶⁾⁾')
                       
@client.command()
@commands.check(two_people)
async def member_total(ctx, user_id):
  if ctx.channel.id == 887894832708730881 or ctx.channel.id == 887967982356148254:
    target = await client.fetch_user(user_id)
    message = {}

    
    member_count = db.keys()
    for x in AGE_members:
      for y in member_count:
        if x == y:
          AGE_members[x] = db[y]

    for x in AGE_members:
      message[id_name[x]] = AGE_members[x]

    await target.send(f'{message}')
        
@client.command()
async def sself(ctx):
  if ctx.channel.id == 887894832708730881 or ctx.channel.id == 887967982356148254:
    self_member_id = str(ctx.author.id)
    await ctx.send(f'Klee knows that you have summoned {db[self_member_id]} slimes so far this season! You are the best!')


@client.command()
async def daily(ctx):
    if ctx.channel.id == 887894832708730881:
        current = datetime.datetime.utcnow()
        
        hour_ago = datetime.timedelta(hours=24)
        
        hour = current - hour_ago
        
        counter = 0
        
        async for message in ctx.channel.history(limit=300, after=hour, before=current):
            if ('<@&887894985398157363>') in message.content or ('<@&887915507804692511>') in message.content :
                counter += 1
        await ctx.send(f'Klee has counted hand by hand, in the past 24 hours, we have summoned {counter} slimes! ٩(๑❛ᴗ❛๑)۶ ')
        
        
@client.command()
async def add(ctx, number, *, username):
  if ctx.channel.id == 887894832708730881 or ctx.channel.id == 887967982356148254:
    member = username.strip()

    member_count = db.keys()
    dictionary = {}
    for member_id in member_count:
      dictionary[member_id] = db[member_id]

    if (member.lower() == 'me') or ('me' in member.lower()):
          member_id = str(ctx.message.author.id)

          if member_id in member_count:
                original = db[member_id]
                add_slime(member_id, number)
          else:
            original = 0
            db[member_id] = 1
    else:
                                  name_mentioned = member
                                  if name_mentioned.lower() == 'dan':
                                            member_id = str(name_id['Dan'])
                                  elif name_mentioned.lower() == 'moon':
                                            member_id = str(name_id['Moon'])
                                  else:
                                      for x in name_id:
                                        if str(name_mentioned.lower()) in x.lower() or str(name_mentioned.lower()) == x.lower():
                                                member_id = str(name_id[x])

                                  if member_id in member_count:
                                    original = db[member_id]
                                    add_slime(member_id, number)

                                  else:
                                    original = 0
                                    db[member_id] = 1
    await ctx.send(f'Klee has added a slime to {id_name[member_id]}! The number of slimes {id_name[member_id]} has summoned has gone from {original} to {db[member_id]}')


@client.event
async def on_command_error(ctx,error):
    if ctx.channel.id == 887894832708730881:
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Klee does not know this command... ヾ(⌒(_´･ㅅ･`)_ ')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Klee does not know this name... ヾ(⌒(_´･ㅅ･`)_ ')

@client.command()
async def gif(ctx):
    if ctx.channel.id == 887894832708730881:
        embed = discord.Embed(title='Channel not for talking', color=discord.Colour.blue())
        embed.set_image(url="https://c.tenor.com/EwX63Uf2_x0AAAAC/sml-jackie-chu.gif")
        await ctx.send(embed=embed)

@client.command()
@commands.check(two_people)
async def clear(ctx):
  if ctx.channel.id == 887894832708730881 or ctx.channel.id == 887967982356148254:
    member_count = db.keys()
    for member_id in member_count:
      db[member_id] = 0
    await ctx.send('slime record cleared')

keep_alive()

client.run(os.getenv('TOKEN'))
