from aiogram import types


async def help_command(message: types.Message):
    await message.answer('Привет 👋\n'
                         'Я помогу тебе вести журнал настроения.\n\n'
                         '/start – запустить бота\n'
                         '/help – показать справочное сообщение\n'
                         '/chart – построить график настроения\n'
                         '/names – изменить обращения\n'
                         '/questions – изменить вопросы')
