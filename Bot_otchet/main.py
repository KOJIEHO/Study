import asyncio
from WASDE import get_info_WASDE
from AMIS import get_info_AMIS
from IGC import get_info_IGC


async def get_info():
    while True:
        get_info_WASDE()
        get_info_AMIS()
        get_info_IGC()
        print('__________________________________________________________________')
        await asyncio.sleep(10) # 0,5 суток - 43200


if __name__ == '__main__':
    asyncio.run(get_info())
    bot.polling(none_stop=True)


