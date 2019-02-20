from pyrogram import Client

app = Client("694466049:AAFx8Ln9OmlfcX2dTjHuTnaznm2iAGqz9Lc")

@app.on_message()
def my_handler(client, message):
	if ("#Важно" in message.text or "#важно" in message.text):
		app.send_message("hatersgonahate", message.text)

app.run()