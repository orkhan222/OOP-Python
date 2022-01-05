    # player1:
    #     id : 1
    #     name : Cristaino Ronaldo
    #     yearOfBirth : 1985
    #     nationality : Portugal
    #     current_team : Portugal
    #     history : Juventus,Real Madrid,Portugal
        
    #  player2:
    #     id : 2
    #     name : Lionel Messi
    #     yearOfBirth : 1987
    #     nationality : Argentina
    #     current_team : Barcelona
    #     history : PSJ,Barcelona,Argentina


players = {
    '1': 
        {
            'name': 'Cristaino Ronaldo', 'yearOfBirth': '1985', 'nationality': 'Portugal', 'current_team': 'Portugal', 'history': ['Juventus', 'Real Madrid', 'Portugal']},
    '2': 
        {
            'name': 'Lionel Messi', 'yearOfBirth': '1987', 'nationality': 'Argentina', 'current_team': 'Barcelona', 'history': ['PSJ', 'Barcelona', 'Argentina']}
        
}

id = input('oyuncu id: ')
name = input('name: ')
yearOfBirth = input('yearOfBirth: ')
nationality = input('nationality: ')
current_team = input('current_team: ')
history = input('history: ')



players.update({
    id: {
        'name' : name,
        'yearOfBirth' : yearOfBirth,
        'nationality' : nationality,
        'current_team' : current_team,
        'history' : history.split(',')
    }
    
})


# 2-ci id  e gore arama yapiniz.
id = input('aramak istediginiz oyuncu id: ')
player = players.get(id)
print(player)

# 3-cu id e gore bilgi kayit siliniz.
id = input('aramak istediginiz oyuncu id: ')
players.pop(id)
print(players)


print(players)
