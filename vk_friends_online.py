import vk
import getpass

APP_ID = 5808833  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    login = input('Введите логин в ВК ')
    return login


def get_user_password():
    password = getpass.getpass(prompt='Введите пароль в ВК ')
    return password


def get_online_friends(login, password):

    session = vk.AuthSession(
         app_id=APP_ID,
         user_login=login,
         user_password=password,
         scope='friends'
     )
    api = vk.API(session)
    users_online = api.friends.getOnline()
    if not users_online:
        return []
    else:
        get_users_info = api.users.get(user_ids=users_online)
        return get_users_info


def output_friends_to_console(friends_online):
    if friends_online:
        print('Сейчас в ВК онлайн : ')
        for friend in friends_online:
            print (friend['first_name'],friend['last_name'])
    else:
        print('Онлайн никого нет')

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
