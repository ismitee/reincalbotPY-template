# 🚀 Discord Bot Template - Hybrid Commands Ready!

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Discord.py](https://img.shields.io/badge/discord.py-2.3%2B-yellow)](https://discordpy.readthedocs.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

**Supercharge your Discord server with this ready-to-go bot template!** Supports both classic prefix commands (`p!`) and modern slash commands (`/`) out of the box. Extend with cogs, customize effortlessly, and deploy in minutes.

![Bot Demo](https://dc.missuo.ru/file/1491465390428127525) <!-- Replace with your GIF/screenshot -->

## ✨ Features
- **Hybrid Commands**: Prefix (`p!ping`) + Slash (`/ping`) – Best of both worlds!
- **Cog System**: Auto-loads from `cogs/` (prefix) and `slash_cogs/` (slash).
- **Production-Ready**:
  - Slash command auto-sync on startup.
  - Custom status/activity.
  - Env-based token for security.
  - Full intents (messages + more).
- **Minimal Dependencies**: discord.py 2.3+, python-dotenv.
- **Example Commands**: Ping latency & hello – ready to expand!

## ⚡ Quick Start (2 Minutes)
1. **Clone/Setup**:
   ```
   git clone <https://github.com/Calrexon/reincalbotPY-template>  # Or just use these files!
   cd reincalbotPY-template
   ```

2. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Create `.env`** (Get token from [Discord Developer Portal](https://discord.com/developers/applications)):
   ```
   BOT_TOKEN=your_bot_token_here
   ```

4. **Run the Bot**:
   ```
   python bot.py
   ```
   Output:
   ```
   YourBot#1234 has logged in!
   Loaded cogs: 2
   Synced 2 slash command(s)
   ```

5. **Invite Bot**: Use [OAuth2 URL Generator](https://discord.com/developers/applications > Your App > OAuth2 > bot scope + permissions).

## 📋 Commands Showcase
| Prefix | Slash | Description |
|--------|-------|-------------|
| `p!ping` | `/ping` | Check bot latency (e.g., Pong! 42 ms) |
| `p!hello` | `/hello` | Friendly greeting! |

**Pro Tip**: Slash commands appear instantly after sync – no restarts!

## 🛠️ Extending the Bot
1. **New Prefix Cog** (`cogs/mycommands.py`):
   ```python
   class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        """Ping latency command."""
        start_time = time.time()
        message = await ctx.send('Pong!')
        end_time = time.time()
        latency = round((end_time - start_time) * 1000)
        await message.edit(content=f'Pong! Latency: {latency} ms')


   async def setup(bot):
       await bot.add_cog(MyCommands(bot))
   ```
   Restart bot – auto-loaded! ✨

2. **New Slash Cog** (`slash_cogs/mycommands.py`): Similar, use `@app_commands.command()`.

3. **Customize**:
   - Change prefix: `command_prefix='!'`
   - Status: Edit `on_ready()` activity.
   - Intents: Add `intents.members = True`.

## 🐛 Troubleshooting
- **No slash commands?** Wait 1hr for Discord sync or re-sync in dev portal.
- **Token error?** Check `.env` (no quotes!).
- **Cogs not loading?** Ensure `setup(bot)` func exists.
- **Permissions**: Bot needs 'Send Messages', 'Use Slash Commands'.

## 🤝 Contributing
1. Fork & PR.
2. Add cogs/examples.
3. Star if helpful! ⭐

**Made with ❤️ by Reincal. Questions? go to discord.py docs or discord server!**

---

*Readme by BLACKBOXAI!* 
