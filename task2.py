list_players = ["Маша", "Петя", "Саша",
                "Оля", "Кирилл", "Коля"]



num_players = len(list_players)


if num_players % 2 == 0:

    team1 = list_players[:num_players // 2]
    team2 = list_players[num_players // 2:]


    print(team1)
    print(team2)
else:
    print("Невозможно разделить игроков на две равные команды, "
          "так как их количество нечетное.")


