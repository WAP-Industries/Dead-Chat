__import__("sys").dont_write_bytecode = True

from dotenv import load_dotenv
from os import environ
from bot import DeadChat

def main():
    load_dotenv()
    DeadChat.Guild = int(environ.get("GUILD"))
    DeadChat.Bot.run(environ.get("TOKEN"))

if __name__=="__main__":
    main()