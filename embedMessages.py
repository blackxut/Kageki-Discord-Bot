import discord

def embed_info(interaction:discord.Integration,user:discord.Member) -> discord.Embed:

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