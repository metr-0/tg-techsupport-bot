import motor.motor_asyncio
from bot import config

client = motor.motor_asyncio.AsyncIOMotorClient(
    config['mongodb']['host'],
    config['mongodb']['port']
)
database = client[config['mongodb']['database']]

users = database['users']
