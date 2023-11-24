class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player_name, initial_score=0):
        if not self._find_player(player_name):
            new_player = Player(player_name, initial_score)
            self.players.append(new_player)
            print(f'Добавлен новый игрок {player_name}.')
        else:
            print(f'Игрок {player_name} уже существует.')

    def remove_player(self, player_name):
        player = self._find_player(player_name)
        if player:
            self.players.remove(player)
            print(f'Игрок {player_name} удален из игры.')
        else:
            print(f'Игрок {player_name} не найден. Удаление невозможно.')

    def determine_winner(self):
        if not self.players:
            print('Нет игроков. Невозможно определить победителя.')
            return None

        winner = max(self.players, key=lambda x: x.score)
        print(f'Победитель: {winner.name} с {winner.score} очками.')
        return winner

    def _find_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player
        return None

class Player:
    def __init__(self, name, initial_score):
        self.name = name
        self.score = initial_score

# Пример использования:

# Создаем объект игры
game = Game()

# Добавляем игроков
game.add_player("Alice", initial_score=100)
game.add_player("Bob", initial_score=80)

# Определяем победителя
winner = game.determine_winner()
