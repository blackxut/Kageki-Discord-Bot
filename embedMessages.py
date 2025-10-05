import discord

def embed_info(interaction:discord.Interaction,user:discord.Member) -> discord.Embed:

    # TODO : refactoring + checking if bot, if in guild
    
    title = user.global_name
    color = 12236510
    embedMessage = discord.Embed(title=title,color=color)

    thumbnail = user.display_avatar
    embedMessage.set_thumbnail(url=thumbnail)

    embedMessage.set_footer(text="made by Kageki#9156 - version 0.1")
    

    text =  "\n* **username** : `" + str(user.name) + "`" \
            "\n* **user_id** : `" + str(user.id) + "`" \
            "\n* **created_at** : `" + str(user.created_at.strftime("%Y-%m-%d %H:%M:%S")) + "`"
    
    embedMessage.add_field(name="\nInformations générales", value=text, inline=False)

    return embedMessage

def embed_leaderboard(users:list) -> discord.Embed:
    """
    schema of the users SQL request :
    (id,username,score) -> (0,'blackxut',183) 
    """

    title = "Leaderboard of the best users"
    color = 12236510
    embedMessage = discord.Embed(title=title,color=color)

    embedMessage.set_footer(text="made by Kageki#9156 - version 0.1")

    i = 0
    text = ""
    while i < len(users):
        
        if i == 0:
            emoji = ":first_place:"
        elif i == 1:
            emoji = ":second_place:"
        elif i == 2:
            emoji = ":third_place:"
        else:
            emoji = ":small_orange_diamond:"

        text += f"{emoji} **{users[i][0]}** - {users[i][1]} points\n"
        i+=1
    embedMessage.add_field(name="",value=text, inline=False)

    return embedMessage