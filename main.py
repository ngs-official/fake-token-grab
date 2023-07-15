
# Developed by J0HAN | v1.1 | This is a 100% fake token grabber by the way.

import base64, random, string, discord, re, asyncio

try:
    with open("config.txt") as file:
        bot_token = file.readline()
        prefix = file.readline()
except:
    print("\nUNABLE TO GET INFO FROM 'config.txt' FILE")

print("")
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("\nConnected to Discord!")
    print(f"Bot: {client.user}")
    print(f"Prefix: {prefix}")

@client.event
async def on_message(message):
    if message.content.startswith(f"{prefix}grab"):
        command = message.content.split(" ")
        # Checking if an user ID is inputted
        if len(command) > 1:
            # Checking if the user ID is more than or equal to 18 characters
            if len(command[1]) >= 18:
                try:
                    # Testing if user ID is a number
                    targetID = int(command[1])
                    pass_test = True
                except:
                    await message.reply("User IDs shouldn't contain any letters.")
                    pass_test = False

                if pass_test == True:
                    targetID = command[1]

                    try:
                        target = await client.fetch_user(targetID)
                        print(f"\nTarget User: {target}")

                        # Encoding into b64
                        userID_ascii = targetID.encode("ascii")
                        base64_bytes = base64.b64encode(userID_ascii)

                        # User ID into start of token
                        rtoken1 = base64_bytes.decode("ascii")
                        token1 = rtoken1.replace("==", "")

                        # Just random letters lol
                        token2 = "".join(random.choices(string.ascii_letters, k=5))
                        token3 = "".join(random.choices(string.ascii_letters, k=38))
                        target_ftoken = token1 + "." + token2 + "." + token3

                        print(f"User Token: {target_ftoken}")

                        # Embed
                        target_display = target.display_name
                        target_pfp = target.avatar
                        target_creationDate = target.created_at
                        target_dateCreated = str(target_creationDate).split(" ")
                        target_flags = target.public_flags.all()
                        if not str(target_flags) == "[]":
                            badges = 0
                            for flag in target_flags:
                                if badges > 0:
                                    target_badges = target_badges + ", " + (str(flag).replace("UserFlags.", "").replace("_", " ").title())
                                else:
                                    target_badges = str(flag).replace("UserFlags.", "").replace("_", " ").title()
                                badges += 1
                        else:
                            target_badges = "No badges to display."

                        tokenEmbed = discord.Embed(title="ACCOUNT FUCKED BY NAHU", description=
f"""▸ **💎 Display Name:**
{target_display}
▸ **📄 Username:**
{target}
▸ **📝 User ID:**
{targetID}
▸ **🛠️ Creation Date:**
{target_dateCreated[0]}
▸ **🏅 Badges:**
{target_badges}
▸ **👑 Token:**
{target_ftoken}"""
                        , colour=000000)
                        tokenEmbed.set_author(name=target, icon_url=target_pfp)
                        tokenEmbed.set_thumbnail(url=target_pfp)
                        tokenEmbed.set_footer(text="Developed by NAHU & JXX")
                        try:
                            loading = await message.reply(f"Grabbing token of {target}...")
                            await asyncio.sleep(1.5) # Delay time, set to 0 for instant
                            await loading.delete()
                            await message.channel.send(embed=tokenEmbed)
                        except:
                            print("\nUNABLE TO SEND EMBED, SENDING BACKUP")
                            await message.reply(f"### User Token:\n{target_ftoken}")
                    except:
                        await message.reply("Can't get information of the user.")
            else:
                await message.reply("That's an invalid user ID.")
        else:
            await message.reply("Please put an user ID.")

try:
    client.run(bot_token)
except:
    print("\nINVALID BOT TOKEN\n")
