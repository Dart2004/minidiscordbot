import discord
import discord.ext.commands
import keep_alive
import asyncio
import requests
import random
import asyncio
from translate.translate import Translator
disabled={}
premium =[]
restore_roles = {}
bot_token = 'ODI3MTkwODg1MjgwMjUxOTQ3.YGXbiw.RvIlmiSUxdqxeiFIakbUvevrdjU'
embed_color = 424122
client = discord.ext.commands.Bot(command_prefix = '!', help_command=None, activity = discord.Game('!help'))
premium_client = discord.ext.commands.Bot(command_prefix = 'premium!', help_command = None)
moderation_client = discord.ext.commands.Bot(command_prefix = 'moderation!', help_command = None)
memes_client = discord.ext.commands.Bot(command_prefix = 'memes!', help_command = None)
translator_client = discord.ext.commands.Bot(command_prefix = 'translator!', help_command = None)
search_client = discord.ext.commands.Bot(command_prefix = 'search!', help_command = None)
music_client = discord.ext.commands.Bot(command_prefix = 'music!', help_command = None)
trivia_client = discord.ext.commands.Bot(command_prefix = 'trivia!', help_command = None)
economy_client = discord.ext.commands.Bot(command_prefix = 'economy!', help_command = None)
welcomer_client = discord.ext.commands.Bot(command_prefix = 'welcomer!', help_command = None)
invites_client = discord.ext.commands.Bot(command_prefix = 'invites!', help_command = None)
giveaways_client =  discord.ext.commands.Bot(command_prefix = 'giveaways!', help_command = None)
autoroles_client = discord.ext.commands.Bot(command_prefix = 'autoroles!', help_command = None)
reactionroles_client = discord.ext.commands.Bot(command_prefix = 'reactionroles!', help_command = None)
logs_client = discord.ext.commands.Bot(command_prefix = 'logs!', help_command = None)
levels_client = discord.ext.commands.Bot(command_prefix = 'levels!', help_command = None)
finder_client = discord.ext.commands.Bot(command_prefix = 'finder!', help_command = None)
nitro_client = discord.ext.commands.Bot(command_prefix = 'nitro!', help_command = None)
news_client = discord.ext.commands.Bot(command_prefix = 'news!', help_command = None)
follower_client = discord.ext.commands.Bot(command_prefix = 'follower!', help_command = None)
antibotverification_client = discord.ext.commands.Bot(command_prefix = 'antibotverification!', help_command = None)
antispam_client = discord.ext.commands.Bot(command_prefix = 'antispam!', help_command = None)
antiswear_client = discord.ext.commands.Bot(command_prefix = 'antiswear!', help_command = None)
setup_client = discord.ext.commands.Bot(command_prefix = 'setup!', help_command = None)
serverbackups_client = discord.ext.commands.Bot(command_prefix = 'serverbackups!', help_command = None)
customcommands_client = discord.ext.commands.Bot(command_prefix = 'customcommands!', help_command = None)
warns_client = discord.ext.commands.Bot(command_prefix = 'warns!', help_command = None)
serverstats_client = discord.ext.commands.Bot(command_prefix = 'serverstats!', help_command = None)



def create_disabled_embed(name):
  return discord.Embed(title='Mini '+name,color=embed_color,description=name+' disabled')

@client.command(name = 'help')
async def help_command(ctx):
  embed = discord.Embed(title='Mini help', color = embed_color)
  try:
    if 'moderation' in disabled[ctx.guild.id]:
      pass
    else:
      embed.add_field(name = 'Mini Moderation', value='A minified Moderation bot.\n```moderation!help```')
  except:
    embed.add_field(name = 'Mini Moderation', value='A minified Moderation bot.\n```moderation!help```')
  try:
    if 'moderation' in disabled[ctx.guild.id]:
      pass
    else:
      embed.add_field(name = 'Mini Memes', value='A minified Memes bot.\n```memes!help```')
  except:
    embed.add_field(name = 'Mini Memes', value='A minified Memes bot.\n```memes!help```')
  try:
    if 'moderation' in disabled[ctx.guild.id]:
      pass
    else:
      embed.add_field(name = 'Mini Translator', value='A minified Translator bot.\n```translator!help```')
  except:
    embed.add_field(name = 'Mini Translator', value='A minified Translator bot.\n```translator!help```')
  
  await ctx.send(embed = embed)

@premium_client.command(name = 'help')
async def premium_help_command(ctx):
  embed= discord.Embed(title='Premium',description='Message Dart2.0#0027 for Premium.', color=embed_color)
  await ctx.send(embed = embed)

@moderation_client.command(name = 'help')
async def moderation_help_command(ctx):
  embed= discord.Embed(title='Mini Moderation', color=embed_color)
  embed.add_field(name = 'Mute', value='moderation!mute ```@user``` ```reason```')
  embed.add_field(name='Unmute', value='moderation!unmute```@user``` ```reason```')
  embed.add_field(name = 'Kick', value='moderation!kick ```@user``` ```reason```')
  embed.add_field(name = 'Ban', value='moderation!ban ```@user``` ```reason```')
  embed.add_field(name='Softban', value='moderation!softban ```@user``` ```reason```')
  await ctx.send(embed = embed)

@moderation_client.command(name='unmute')
async def moderation_unmute_command(ctx,user:discord.Member,*,reason):
  if user == ctx.author:
    await ctx.send(embed=discord.Embed(title='Mini Moderation',description='You can\'t unmute yourself',color=embed_color))
    return
  if not ctx.author.guild_permissions.manage_roles:
    await ctx.send(embed=discord.Embed(title='Mini Moderation',description='You don\'t have manage_roles permissions.',color=embed_color))
  else:
    try:
      for role in user.guild.roles:
        if role.name == 'Muted':
          await user.remove_roles(role)
        else:
          try:
            if role.id in restore_roles[str(user.id)+str(user.guild.id)]:
              await user.add_roles(role)
          except:
            pass
      try:
        await user.send(embed=discord.Embed(title='Unmuted in '+ctx.guild.name,description='Reason: '+reason))
      except:
        pass
      await ctx.send(embed=discord.Embed(title='Mini Moderation',description='Unmuted '+str(user)+'.\nReason: '+reason))
    except Exception as es:
      await ctx.send(embed=discord.Embed(title='Mini Moderation',description='Unmute failed\nReason: Bot missing permissions'))

@moderation_client.command(name='fastmute')
async def moderation_fastmute_command(ctx,user:discord.Member,*,reason):
  if user == ctx.author:
    await ctx.send(embed=discord.Embed(title='Mini Moderation',description='You can\'t fastmute yourself',color=embed_color))
    return
  if not ctx.author.guild_permissions.manage_roles:
    await ctx.send(embed=discord.Embed(title='Mini Moderation',description='You don\'t have manage_roles permissions.',color=embed_color))
  else:
    try:
      restore_roles[str(user.id)+str(user.guild.id)] = []
      for role in user.guild.roles:
        if role.name == 'Muted':
          await user.add_roles(role)
        else:
          try:
            if role in user.roles:
              restore_roles[str(user.id)+str(user.guild.id)].append(role.id)
              await user.remove_roles(role)
          except:
            pass
      if len(user.roles) == 1 or len(user.roles) == 0:
        await client.http.create_role(ctx.guild.id,name='Muted',permissions=0)
      for role in user.guild.roles:
        if role.name == 'Muted':
          await user.add_roles(role)
      try:
        await user.send(embed=discord.Embed(title='Muted in '+ctx.guild.name,description='Reason: '+reason))
      except:
        pass
      await ctx.send(embed=discord.Embed(title='Mini Moderation',description='Muted '+str(user)+'.\nReason: '+reason))
      await asyncio.sleep(60)
      if not ctx.author.guild_permissions.manage_roles:
        await ctx.send(embed=discord.Embed(title='Mini Moderation',description='You don\'t have manage_roles permissions.',color=embed_color))
      else:
        try:
          for role in user.guild.roles:
            if role.name == 'Muted':
              await user.remove_roles(role)
            else:
              try:
                if role.id in restore_roles[str(user.id)+str(user.guild.id)]:
                  await user.add_roles(role)
              except:
                pass
          try:
            await user.send(embed=discord.Embed(title='Unmuted in '+ctx.guild.name,description='Reason: '+reason))
          except:
            pass
          await ctx.send(embed=discord.Embed(title='Mini Moderation',description='Unmuted '+str(user)+'.\nReason: '+reason))
        except Exception as es:
          await ctx.send(embed=discord.Embed(title='Mini Moderation',description='Unmute failed\nReason: Bot missing permissions'))
    except Exception as es:
      await ctx.send(embed=discord.Embed(title='Mini Moderation',description='Mute failed\nReason: Bot missing permissions'))

@moderation_client.command(name='mute')
async def moderation_mute_command(ctx,user:discord.Member,*,reason):
  if user == ctx.author:
    await ctx.send(embed=discord.Embed(title='Mini Moderation',description='You can\'t mute yourself',color=embed_color))
    return
  if not ctx.author.guild_permissions.manage_roles:
    await ctx.send(embed=discord.Embed(title='Mini Moderation',description='You don\'t have manage_roles permissions.',color=embed_color))
  else:
    try:
      restore_roles[str(user.id)+str(user.guild.id)] = []
      for role in user.guild.roles:
        if role.name == 'Muted':
          await user.add_roles(role)
        else:
          try:
            if role in user.roles:
              restore_roles[str(user.id)+str(user.guild.id)].append(role.id)
              await user.remove_roles(role)
          except:
            pass
      if len(user.roles) == 1 or len(user.roles) == 0:
        await client.http.create_role(ctx.guild.id,name='Muted',permissions=0)
      for role in user.guild.roles:
        if role.name == 'Muted':
          await user.add_roles(role)
      try:
        await user.send(embed=discord.Embed(title='Muted in '+ctx.guild.name,description='Reason: '+reason))
      except:
        pass
      await ctx.send(embed=discord.Embed(title='Mini Moderation',description='Muted '+str(user)+'.\nReason: '+reason))
    except Exception as es:
      await ctx.send(embed=discord.Embed(title='Mini Moderation',description='Mute failed\nReason: Bot missing permissions'))

@moderation_client.command(name='softban')
async def moderation_softban_command(ctx, user:discord.Member, *, reason):
  if user == ctx.author:
    await ctx.send(embed=discord.Embed(title='Mini Moderation',description='You can\'t softban yourself',color=embed_color))
    return
  if not ctx.author.guild_permissions.ban_members:
    await ctx.send(embed=discord.Embed(title='Mini Moderation',description='You don\'t have softban_members permissions.',color=embed_color))
  else:
    try:
      await user.ban()
      await user.unban()
      try:
        await user.send(embed=discord.Embed(title='Softbanned in '+ctx.guild.name,description='Reason: '+reason))
      except:
        pass
      await ctx.send(embed=discord.Embed(title='Mini Moderation',description='Softbanned '+str(user)+'.\nReason: '+reason))
    except:
      await ctx.send(embed=discord.Embed(title='Mini Moderation',description='Softban failed\nReason: Bot missing permissions'))

@moderation_client.command(name = 'kick')
async def moderation_kick_command(ctx, user:discord.Member, *, reason):
  if user == ctx.author:
    await ctx.send(embed=discord.Embed(title='Mini Moderation',description='You kick mute yourself',color=embed_color))
    return
  if not ctx.author.guild_permissions.kick_members:
    await ctx.send(embed=discord.Embed(title='Mini Moderation',description='You don\'t have kick_members permissions.',color=embed_color))
  else:
    try:
      await user.kick()
      try:
        await user.send(embed=discord.Embed(title='Kicked in '+ctx.guild.name,description='Reason: '+reason))
      except:
        pass
      await ctx.send(embed=discord.Embed(title='Mini Moderation',description='Kicked '+str(user)+'.\nReason: '+reason))
    except:
      await ctx.send(embed=discord.Embed(title='Mini Moderation',description='Kick failed\nReason: Bot missing permissions'))

@moderation_client.command(name = 'ban')
async def moderation_ban_command(ctx, user:discord.Member, *, reason):
  if user == ctx.author:
    await ctx.send(embed=discord.Embed(title='Mini Moderation',description='You can\'t ban yourself',color=embed_color))
    return
  if not ctx.author.guild_permissions.ban_members:
    await ctx.send(embed=discord.Embed(title='Mini Moderation',description='You don\'t have ban_members permissions.',color=embed_color))
  else:
    try:
      await user.ban()
      try:
        await user.send(embed=discord.Embed(title='Banned in '+ctx.guild.name,description='Reason: '+reason))
      except:
        pass
      await ctx.send(embed=discord.Embed(title='Mini Moderation',description='Banned '+str(user)+'.\nReason: '+reason))
    except:
      await ctx.send(embed=discord.Embed(title='Mini Moderation',description='Ban failed\nReason: Bot missing permissions'))

@memes_client.command(name = 'help')
async def memes_help_command(ctx):
  embed= discord.Embed(title='Mini Memes',description='Feature coming soon', color=embed_color)
  embed.add_field(name='Random',value='memes!random')
  embed.add_field(name='Search',value='memes!search')
  await ctx.send(embed = embed)

@memes_client.command(name = 'random')
async def memes_random_command(ctx):
  meme = requests.get('https://meme-api.herokuapp.com/gimme/dankmemes').json()
  embed=discord.Embed(title='Mini Memes',color=embed_color,description=meme['title'])
  embed.set_footer(text='Random Meme')
  embed.set_image(url=meme['preview'][len(meme['preview'])-1])
  await ctx.send(embed=embed)

@memes_client.command(name='search')
async def memes_search_command(ctx,*,query):
  queryx = query.replace(' ','%20')
  embed=discord.Embed(title='Mini Memes',color=embed_color,description=query)
  embed.set_footer(text='Search Meme')
  embed.set_image(url='https://th.bing.com/th/id/abc/?q=meme-'+queryx+str(random.randint(0,20)))
  await ctx.send(embed=embed)

@translator_client.command(name = 'help')
async def translator_help_command(ctx):
  if ctx.guild.id in blocked['translator']:
    await ctx.send(embed=create_disabled_embed('Translator'))
  embed= discord.Embed(title='Mini Translator',color=embed_color)
  embed.add_field(name='Translate',value='translator!translate ```language``` ```message```')
  await ctx.send(embed = embed)

@translator_client.command(name = 'translate')
async def translator_translate_command(ctx, language, *, message):
  if ctx.guild.id in blocked['translator'] or ctx.guild.id in blocked['translator.translate']:
    await ctx.send(embed=create_disabled_embed('Translator: Translate'))
  translator = Translator(to_lang = language)
  if translator.translate(message) == translator.translate(message).upper():
    await ctx.send(embed = discord.Embed(title='Mini Translator', color=embed_color, description='Please choose a valid language code.'))
    return
  embed=discord.Embed(title='Mini Translator',color=embed_color)
  embed.add_field(name='Message',value=message)
  embed.add_field(name='Translated',value=translator.translate(message))
  await ctx.send(embed = embed)




keep_alive.keep_alive()
loop = asyncio.get_event_loop()
loop.create_task(client.start(bot_token))
loop.create_task(moderation_client.start(bot_token))
loop.create_task(memes_client.start(bot_token))
loop.create_task(translator_client.start(bot_token))
loop.run_forever()
