from proxygen import ProxyGen
from telethon import events, Button
from proxygen.plugins.proxy import k
from Configs import Config

btn =[
  [Button.inline("Https", data="https")],
  [Button.inline("Socks4", data="socks4"), Button.inline("Socks5", data="socks5")],
  [Button.url("My Source Code", "https://github.com/TgxBotz/ProxyGenBot")]
  ]

@ProxyGen.on(events.NewMessage(pattern="^[!?/]start$"))
async def start(event):

    Text = """
**Heya {}**
I am free proxygenbot which
can generate any type of proxies
for you!
__Click on the button below!__
""".format(event.sender.first_name)

    if event.is_group and event.chat_id != Config.LOGS_CHAT:
      await event.reply("**I dont work in groups!**\n__I am leaving this chat!__")
      await ProxyGen.delete_dialog(event.chat_id)
      return

    await ProxyGen.send_message(Config.LOGS_CHAT, f"Bot started by [{event.sender.first_name}](tg://user?id={event.sender_id}).")
    await event.reply(Text, buttons=[[Button.inline("Generate Proxies", data="proxy")]])

@ProxyGen.on(events.CallbackQuery(data="proxy"))
async def k(event):
    Text = """
**Heya {}
Choose the proxies you
want to generate:**
""".format(event.sender.first_name)
    await event.edit(Text, buttons=btn)
