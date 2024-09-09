import time


class User:

    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}'


class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.current_user: User | None = None
        self.videos: list[Video] = []
        self.users: list[User] = []

    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if nickname == user.nickname:
                print('Данное имя пользователя уже занято выберите другое ')
                return self.current_user
        user = User(nickname, password, age)
        self.users.append(user)
        self.current_user = user
        print(f'Вы успешно создали и вошли в аккаунт {nickname}')

    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if nickname == user.nickname:
                if hash(password) == user.password:
                    self.current_user = user
                    print('Всё отлично! ')
                else:
                    print('Пароль неверный! ')
                return
        print('Аккаунт не найден. ')

    def log_out(self):
        self.current_user = None

    def add(self, *args: Video):
        self.videos.extend(args)

    def get_videos(self, string):
        return [video.title
                for video in self.videos
                if string.lower() in video.title.lower()]

    def watch_video(self, title_v):
        if self.current_user is not None:
            for video in self.videos:
                if video.title == title_v:
                    if video.adult_mode:
                        if self.current_user.age > 17:
                            for i in range(video.time_now + 1, video.duration + 1, 1):
                                time.sleep(1)
                                print(i)
                            print('Конец')
                        else:
                            print('Вам нет 18 лет, покиньте страницу')
                    elif not video.adult_mode:
                        for i in range(video.time_now + 1, video.duration + 1, 1):
                            print(f'{i}')
                            time.sleep(1)
        else:
            print('Войдите в аккаунт чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 20)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
