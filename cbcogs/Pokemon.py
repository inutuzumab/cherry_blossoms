import discord, random, os, json
from aiohttp import request
from discord.ext import commands
from discord import Member

class Pokemon(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Pokémon functions are ready to use.')

#catch... API
    @commands.command(aliases = ('pokemon', 'Pokemon', 'Catch'))
    @commands.cooldown(1, 5, type = commands.BucketType.user)
    async def catch(self, ctx):

        id = random.randint(1, 893)
        joel_check = random.randint(1, 2000)
        shiny_check = random.randint(1,20)
        joel = '**ROKDACLOK**'
        URL = (f"https://pokeapi.co/api/v2/pokemon/{id}/")
        member = ctx.message.author
        trainer = str(ctx.author.id)
        member_mention = member.mention
        pokemon_species = "Species"

        with open("F:\A_PROGRAMMING\A_VSC\Python\cherry blossoms\pokemon_PC.json", "r") as f:
            trainers = json.load(f)
            if trainer not in trainers:
                trainers[trainer] = {}
            if pokemon_species not in trainers[trainer]:
                trainers[trainer][pokemon_species] = {}

        if joel_check == 1:
            with open("F:\A_PROGRAMMING\A_VSC\Python\cherry blossoms\pokemon_PC.json", "w") as f:
                if "Pokédex entries" not in trainers[trainer]:
                    trainers[trainer]["Pokédex entries"] = 0
                if "ROKDACLOK" not in trainers[trainer][pokemon_species]:
                    trainers[trainer][pokemon_species]["ROKDACLOK"] = 1
                    trainers[trainer]["Pokédex entries"] += 1
                elif "ROKDACLOK" in trainers[trainer][pokemon_species]:
                    trainers[trainer]["ROKDACLOK"] += 1
                f.write(json.dumps(trainers, indent=5))
            embeds = discord.Embed(title = f'Congratulations! 🎉', description = (f"{member_mention}, you've caught a wild {joel}!"), colour = 0x3498db)
            embeds.set_image(url = f"https://i.ibb.co/3mXHTK1/joel-final-product.gif")
            await ctx.send(embed = embeds)

#rolling pokemon
        else:
            async with request("GET", URL, headers = {}) as response:
                if response.status == 200:
                    data = await response.json()
                    pokemon = str(data["name"])
#pokemon checks
                    if "-male" in pokemon:
                        pokemon2 = pokemon.replace('-male', '')
                    elif "-female" in pokemon:
                        pokemon2 = pokemon.replace('-female', '-f')
                    elif "tapu-" in pokemon:
                        pokemon2 = pokemon.replace('tapu-', 'tapu')
                    elif "-midday" in pokemon:
                        pokemon2 = pokemon.replace("-midday", "")
                    elif "red-striped" in pokemon:
                        pokemon2 = pokemon.replace("-red-striped", "")
                    elif "blue-striped" in pokemon:
                        pokemon2 = pokemon.replace("-blue-striped", "-bluestriped")
                    elif "-incarnate" in pokemon:
                        pokemon2 = pokemon.replace("-incarnate", "")
                    else:
                        pokemon2 = pokemon
#storage for pokemon
                    with open("F:\A_PROGRAMMING\A_VSC\Python\cherry blossoms\pokemon_PC.json", "w") as f:
                        if "Pokédex entries" not in trainers[trainer]:
                            trainers[trainer]["Pokédex entries"] = 0
                        if pokemon.capitalize() not in trainers[trainer][pokemon_species]:
                            trainers[trainer][pokemon_species][pokemon.capitalize()] = 1
                            trainers[trainer]["Pokédex entries"] += 1
                        elif pokemon.capitalize() in trainers[trainer][pokemon_species]:
                            trainers[trainer][pokemon_species][pokemon.capitalize()] += 1
                        f.write(json.dumps(trainers, indent=5))
                else:
                    await ctx.send(f'API returned a {response.status} status')
            
#registering pokemon            
            if shiny_check == 1:
                caught_pokemon = f'**_shiny {pokemon.capitalize()}_**'
                embed = discord.Embed(title = f'Congratulations! 🎉', description = (f"{member_mention}, you've caught a wild {caught_pokemon}!"), colour = 0xf1c40f)
                embed.set_image(url = f"http://play.pokemonshowdown.com/sprites/ani-shiny/{pokemon2}.gif")
                await ctx.send(embed = embed)
            else:
                caught_pokemon = f'**_{pokemon.capitalize()}_**'
                embed = discord.Embed(title = f'Congratulations! 🎉', description = (f"{member_mention}, you've caught a wild {caught_pokemon}!"), colour = 0xff6347)
                embed.set_image(url = f"http://play.pokemonshowdown.com/sprites/ani/{pokemon2}.gif")
                await ctx.send(embed = embed)


#open pc
    @commands.command()
    async def pcbox(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        dd = member.name
        trainer = str(member.id)
        trainer_specific = str(member.id)
        pokemon_species = "Species"
        with open("F:\A_PROGRAMMING\A_VSC\Python\cherry blossoms\pokemon_PC.json", "r") as f:
            trainers = json.load(f)
        if trainer not in trainers:
            embed = discord.Embed(title = f"Opening {dd}'s PC...", description = f"Trainer {member.mention} has not caught any Pokémon yet... :((")
            await ctx.send(embed = embed)
        else:
            with open("F:\A_PROGRAMMING\A_VSC\Python\cherry blossoms\pokemon_PC.json", "r") as f:
                trainers = json.load(f)
                embed = discord.Embed(title = f"Opening {dd}'s PC...", description = f"__{trainers[trainer_specific]['Pokédex entries']}/894__ Pokémon:")
                for x in trainers[trainer][pokemon_species]:
                    if 'Shiny' not in x:
                        embed.add_field(name = f"{x}", value = f"caught: {trainers[trainer][pokemon_species][x]}", inline = False)
                await ctx.send(embed = embed)

#stats
    @commands.command()
    async def stats(self, ctx, pokemon):
        pokemon_species = str(pokemon)
        name = "hmm"
        URL = (f"https://pokeapi.co/api/v2/pokemon/{name}/")


def setup(client):
    client.add_cog(Pokemon(client))
