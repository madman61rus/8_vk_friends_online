import vk

APP_ID = 5808833  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    '''Функция ввода логина пользователя'''
    login = input('Введите логин в ВК ')
    return login


def get_user_password():
    '''Функция ввода пароля пользователя'''
    password = input('Введите пароль в ВК ')
    return password


def get_online_friends(login, password):
    '''Функция для получения пользователей и фильтрации тех, которые онлайн'''

    session = vk.AuthSession(
         app_id=APP_ID,
         user_login=login,
         user_password=password,
     )
    api = vk.API(session)
    users = api.friends.get(fields='nickname,online')
    users_online =list(filter(lambda user: user['online'] == 1, users))
    return users_online


def output_friends_to_console(friends_online):
    '''Функция для вывода пользователей онлайн в консоль'''
    print('Сейчас в ВК онлайн : ')
    for friend in friends_online:
        print (friend['first_name'],friend['last_name'])

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
