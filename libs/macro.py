import discord


class Macro:
    '''the BEST macro class :D'''
    async def WOW_message(title=None, thumb=None, *args):
        """USING ARGUMENTS:
            MAKE A DICT WITH 'title', 'desc', 'thumb'
            FOR EACH ITEM IN *ARGS
            """
            embed = discord.Embed(
                title=title,
                type='rich',
                color=discord.Color.orange()
                )
            for arg in args:
                embed.add_field(name=arg.get('title'), value=arg.get('value'))
            if not thumb:
                return embed
            embed.set_thumbnail(url=thumb)
            return embed
    @staticmethod
    async def msg(desc=None, title=None, color:discord.Color=None, thumb:str=None):
        embed = discord.Embed(
            type='rich',
            description=desc,
            title=title,
            color=color
        )
        if not thumb:
            return embed
        embed.set_thumbnail(url=thumb)
        return embed
    @classmethod
    async def img(cls, image:str, desc:str=None, title:str=None):
        message = await cls.message(desc=desc, title=title)
        message.set_image(url=image)
        return message
    @classmethod
    async def error(cls, desc):
        return await cls.message(desc=desc, thumb='https://images.emojiterra.com/twitter/v11/512px/274c.png')

err, error = Macro.error, Macro.error
send, msg = Macro.message, Macro.message
img, pic = Macro.img, Macro.img
            
                
