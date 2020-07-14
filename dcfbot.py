import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord import utils
import requests
import io
import config
import os
#from PIL import Image, ImageFont,ImageDraw
PREFIX='.'
client = commands.Bot(command_prefix=PREFIX) 
client.remove_command('help')
POST_ID=732475275375411210
ROLES={
    '🍞':727096503012818974,
}
EXCROLES=()
MAX_ROLES_PER_USER=5
#check
bad_words = ['https://discord.gg/']
@client.event
async def on_ready():
    print("i am ok!")
#rolegiving!!!  
# template of the nested dict:
######################################################################
@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def report(ctx, member:discord.Member=None, *, arg=None):
    message = ctx.message
    channel = client.get_channel(732492737995079770)    
    if member == None:
        await ctx.send(embed=discord.Embed(description='Tag member!', color=discord.Color.red()))
    elif arg == None:
        await ctx.send(embed=discord.Embed(description='Whats the reason?', color=discord.Color.red()))
    else:
        emb = discord.Embed(title=f'We got a report for {member}', color=discord.Color.blue())
        emb.add_field(name='Report author:', value=f'*{ctx.author}*')
        emb.add_field(name='Reason:', value='*' +arg + '*')
        emb.add_field(name='Report ID:', value=f'{message.id}')
        await channel.send(embed=emb)
        await ctx.author.send('✅ Your report was send to staff!')

#########################################################3
@client.command()
@commands.has_permissions(administrator=True)
async def ping(ctx):
    await ctx.send("pong! i am working okay.")
#mute

@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member:discord.Member, reason:str=None,):
    mute_role=discord.utils.get(ctx.message.guild.roles, name="mute")
    member_r=discord.utils.get(member.guild.roles, name="Member")
    await member.add_roles(mute_role)
    await member.remove_roles(member_r)
    message = f"You have been muted from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.channel.send (f'{member} was muted for {reason}')
#unmute

@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx,member:discord.Member):
    mute_role=discord.utils.get(ctx.message.guild.roles, name="mute")
    member_r= discord.utils.get(member.guild.roles, name="Member")
    await member.remove_roles(mute_role)
    await member.add_roles(member_r)
    await ctx.channel.send(f"{member} is unmuted!")
'''
@client.event
async def on_member_join(member):
    member_r= discord.utils.get(member.guild.roles, name="Member")
    await member.add_roles(member_r)
    '''
#ban
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx,member:discord.Member,reason:str=None):
    if member == None or member == ctx.message.author:
        emb = discord.Embed(description=f':no_entry_sign: You cannot ban yourself!',colour=discord.Color.red())
        emb.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)
        return
    if reason == None:
        reason = "idk ask staff"
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    emb1 = discord.Embed(description=f':white_check_mark: {member} was banned!',colour=discord.Color.green())
    emb1.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar_url)
    await ctx.guild.ban(member, reason=reason)
    await ctx.send(embed=emb1)
    await member.send(message)
#kick
#emb = discord.Embed(description=f':white_check_mark: Cleared {amount} messages',colour=discord.Color.blue())
#emb.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar_url)
#await ctx.send(embed=emb)
@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx,member:discord.Member,reason=None):
    if member == None or member == ctx.message.author:
        emb = discord.Embed(description=f':no_entry_sign: You cannot kick yourself!',colour=discord.Color.red())
        emb.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)
        return
    if reason == None:
        reason = "idk ask staff"
    message = f"You have been kicked from {ctx.guild.name} for {reason}"
    emb1 = discord.Embed(description=f':white_check_mark: {member} was kicked!',colour=discord.Color.green())
    emb1.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar_url)
    #await ctx.guild.kick(member, reason=reason)
    await ctx.send(embed=emb1)
    await member.send(message)

#clear
@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx,amount = 5):
    emb = discord.Embed(description=f':white_check_mark: Cleared {amount} messages',colour=discord.Color.blue())
    emb.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar_url)
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(embed=emb)
#help
@client.command()
@commands.has_permissions(administrator=True)
async def help(ctx):
    emb = discord.Embed(title='List of commands:',colour=discord.Color.blue())
    emb.add_field(name='{}clear'.format(PREFIX), value='Clears messages. Usage: .clear ~amount~')
    emb.add_field(name='{}ban'.format(PREFIX), value='Use to ban someone. Usage: .ban ~user~')
    emb.add_field(name='{}kick'.format(PREFIX), value='Use to kick someone. Usage: .kick ~user~')
    emb.add_field(name='{}mute'.format(PREFIX), value='Use to mute someone. Usage: .mute ~user~')
    emb.add_field(name='{}unmute'.format(PREFIX), value='Use to mute someone. Usage: .unmute ~user~')
    emb.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar_url)
    await ctx.send(embed = emb)

#shit 
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def test(ctx):
    emb=discord.Embed(title='some shit', colour=discord.Color.blue())
    emb.set_author(name =client.user.name, icon_url=client.user.avatar_url)
    emb.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar_url)
    emb.set_thumbnail(url='https://i.ibb.co/7Qm0MLK/image.png')
    await ctx.send(embed=emb)
#rolegiving
@client.event
async def on_message(message):
    await client.process_commands(message)
    msg = message.content.lower() 
    if msg in bad_words:
        await message.delete()
        await message.author.send(f'{message.author.name}, dont send invite links! u will be banned!')    
'''
@client.command(aliases=['me'])
@commands.has_permissions(administrator=True)
async def card_user(ctx):
    await ctx.channel.purge(limit=1)
    img=Image.new('RGBA',(400,200),'#232529')
    url = str(ctx.author.avatar_url)[:-10]
    response =requests.get(url,stream=True)
    response-Image.open(io.BytesIO(response.content))
    response = response.convert('RGBA')
    response=response.resize((100,100), Image.ANTIALIAS)
    img.paste(response,(15,15,115,115))
    idraw = ImageDraw.Draw(img)
    name=ctx.author.name #name
    tag=ctx.author.discriminator #9610
    headline = ImageFont.truetype('arial.ttf', size =20)
    undertext = ImageFont.truetype('arial.ttf',size = 12)
    idraw.text((145,15),f'{name}#{tag}', font=headline)
    idraw.text((145,50),f'ID:{ctx.author.id}', font=undertext)
    img.save('user_card.png')
    await ctx.send(file=discord.File(fp='user_card.png'))
'''
token=os.environ.get('BOT_TOKEN')
